"""Read local X4 archives without installing them; write reproducible audit evidence.

ZIP: standard library. RAR: UnRAR. 7Z: optional py7zr (--vendor).
Outputs contain metadata and fingerprints, never third-party source or assets.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import os
import shutil
import sqlite3
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import xml.etree.ElementTree as ET

GAME_DIRS = {"aiscripts", "md", "ui", "libraries", "maps", "assets", "t", "index", "extensions"}
TEXT_LIMIT = 8 * 1024 * 1024
UNRAR = shutil.which("unrar") or str(Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "WinRAR/UnRAR.exe")
REMOVED_900 = {
    "event_area_discovered": r"<event_area_discovered\b",
    "get_highest_resource_yield": r"<get_highest_resource_yield\b",
    "find_asteroid_in_cluster": r"<find_asteroid_in_cluster\b",
    "find_recyclable_in_cluster": r"<find_recyclable_in_cluster\b",
    "resourceprobe.currentbestyield": r"\bcurrentbestyield\b",
    "resourceprobe.maxyield": r"\bmaxyield\b",
    "sector.averagemaxyield": r"\baveragemaxyield\b",
    "galaxy.yieldthresholds": r"\byieldthresholds\b",
    "object.efficiencyupgrades": r"\befficiencyupgrades\.",
    "GetEfficiencyUpgrades": r"\bGetEfficiencyUpgrades\s*\(",
    "ship.isexceedingmadscore": r"\bisexceedingmadscore\b",
}


def norm(name):
    return name.replace("\\", "/").removeprefix("./").rstrip("/")


def digest_file(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def local_tag(tag):
    return tag.rsplit("}", 1)[-1]


def parse_catalog(data):
    """Parse text CAT paths (including spaces); DAT offsets are cumulative bytes."""
    result, offset = [], 0
    for number, line in enumerate(data.decode("utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"(.+) (\d+) (\d+) ([0-9a-fA-F]{32})", line)
        if not match:
            raise ValueError(f"CAT line {number} is not a supported entry")
        path, size, stamp, md5 = match.groups()
        size = int(size)
        result.append({"path": norm(path), "size": size, "offset": offset,
                       "timestamp": int(stamp), "declared_md5": md5.lower()})
        offset += size
    return result


def wanted_text(name):
    path = PurePosixPath(name)
    return (path.suffix.lower() in {".xml", ".lua", ".xpl"}
            or re.search(r"license|licence|permissions|readme", path.name, re.I))


def parse_unrar_listing(text):
    """Technical listings distinguish files from directories (bare listings do not)."""
    entries, current = [], {}
    for line in text.splitlines():
        if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)
        if key == "Name":
            if current:
                entries.append(current)
            current = {"Name": value}
        elif current and key in {"Type", "Size"}:
            current[key] = value
    if current:
        entries.append(current)
    return [entry for entry in entries if entry.get("Type") == "File"]


class Archive:
    def __init__(self, path):
        self.path, self.z, self.sizes, self.cache = path, None, {}, {}
        if path.suffix.lower() == ".zip":
            self.z = zipfile.ZipFile(path)
            self.original = {norm(i.filename): i.filename for i in self.z.infolist() if not i.is_dir()}
            self.sizes = {norm(i.filename): i.file_size for i in self.z.infolist() if not i.is_dir()}
        elif path.suffix.lower() == ".7z":
            import py7zr
            with py7zr.SevenZipFile(path) as archive:
                entries = [e for e in archive.list() if not e.is_directory]
                self.original = {norm(e.filename): e.filename for e in entries}
                self.sizes = {norm(e.filename): e.uncompressed for e in entries}
            # Memory extraction only; never materialize third-party paths on disk.
            from py7zr.io import BytesIOFactory
            targets = [original for name, original in self.original.items()
                       if wanted_text(name) or name.lower().endswith((".cat", ".dat"))]
            factory = BytesIOFactory(limit=256 * 1024 * 1024)
            with py7zr.SevenZipFile(path) as archive:
                archive.extract(targets=targets, factory=factory)
            for name, original in self.original.items():
                if original in factory.products:
                    product = factory.get(original)
                    product.seek(0)
                    self.cache[name] = product.read()
                    if len(self.cache[name]) != self.sizes[name]:
                        raise ValueError(f"Truncated 7Z member: {name}")
        else:
            result = subprocess.run([UNRAR, "lt", "-c-", "-p-", str(path)], capture_output=True, check=True, timeout=30)
            entries = parse_unrar_listing(result.stdout.decode("utf-8", errors="replace"))
            if any("\ufffd" in e["Name"] for e in entries):
                raise ValueError("UnRAR filename encoding is not UTF-8; manual reader configuration required")
            self.original = {norm(e["Name"]): e["Name"] for e in entries}
            self.sizes = {norm(e["Name"]): int(e["Size"]) for e in entries}

    def read(self, name):
        if self.z:
            return self.z.read(self.original[name])
        if name in self.cache:
            return self.cache[name]
        # Windows bsdtar 3.5.2 can hang reading RAR members; use the installed UnRAR.
        member = self.original[name].replace("/", "\\") if sys.platform == "win32" else self.original[name]
        return subprocess.run([UNRAR, "p", "-inul", "-p-", str(self.path), member],
                              capture_output=True, check=True, timeout=60).stdout

    def stream(self, name):
        return self.z.open(self.original[name]) if self.z else io.BytesIO(self.read(name))

    def close(self):
        if self.z:
            self.z.close()


def text_evidence(data, mod, file, documents):
    """Record XML operations and search hits; no execution or XSD/PATCH PASS."""
    if len(data) > TEXT_LIMIT:
        mod["limitations"].append(f"Text above {TEXT_LIMIT} bytes: {file['path']}")
        return
    text = data.decode("utf-8-sig", errors="replace")
    if "\x00" in text:
        file["kind"] = "binary_or_compiled"
        return
    if file["path"].lower().endswith(".xml"):
        try:
            root = ET.fromstring(data)
            file["xml_root"] = local_tag(root.tag)
            file["kind"] = "xml_diff" if file["xml_root"] == "diff" else "xml_full"
            file["operations"] = [{"op": local_tag(e.tag), "sel": e.get("sel", "")}
                                  for e in root if e.get("sel") is not None] if file["kind"] == "xml_diff" else []
        except (ET.ParseError, ValueError) as error:
            file["kind"] = "xml_parse_error"
            file["error"] = str(error)
    # Comments/strings can match: every hit requires manual review.
    for label, pattern in REMOVED_900.items():
        for match in re.finditer(pattern, text):
            mod["breaking_900_hits"].append({"path": file["path"], "token": label,
                                            "line": text.count("\n", 0, match.start()) + 1})
    if re.search(r"license|licence|permissions|readme", PurePosixPath(file["path"]).name, re.I):
        labels = []
        for label, pattern in {
            "Apache-2.0 marker": r"Apache License[\s\S]{0,100}Version 2\.0",
            "MIT marker": r"Permission is hereby granted, free of charge",
            "GPL marker": r"GNU GENERAL PUBLIC LICENSE",
            "custom restriction marker": r"permission.*(?:author|upload|redistribut)|do not (?:upload|redistribut)|not allowed",
        }.items():
            if re.search(pattern, text, re.I):
                labels.append(label)
        documents.append({"package": mod["package"], "root": mod["root"],
                          "path": file["path"], "sha256": file["sha256"],
                          "markers": labels, "redistribution": "NOT_REVIEWED"})


def scan_archive(path, base):
    package = {"path": path.relative_to(base).as_posix(), "bytes": path.stat().st_size,
               "sha256": digest_file(path), "format": path.suffix[1:].upper(),
               "status": "READ", "limitations": [], "mods": [], "documents": []}
    archive = None
    try:
        archive = Archive(path)
        package["member_count"] = len(archive.original)
        roots = sorted({n.rsplit("/", 1)[0] if "/" in n else "" for n in archive.original
                        if PurePosixPath(n).name.lower() == "content.xml"})
        # Deepest root owns nested content, preventing source collections being merged.
        for root in roots:
            content = f"{root}/content.xml" if root else "content.xml"
            raw = archive.read(content)
            node = ET.fromstring(raw)
            if local_tag(node.tag) != "content":
                continue
            mod = {"package": package["path"], "root": root, "content_sha256": hashlib.sha256(raw).hexdigest(),
                   "attributes": {k: v for k, v in node.attrib.items() if k != "description"},
                   "dependencies": [dict(e.attrib) for e in node if local_tag(e.tag) == "dependency"],
                   "files": [], "catalogs": [], "breaking_900_hits": [], "limitations": []}
            package["mods"].append(mod)
            prefix = root + "/" if root else ""
            members = [n for n in archive.original if n.startswith(prefix)
                       and not any(n.startswith(r + "/") for r in roots if r != root and r.startswith(prefix))]
            catalogs = [n for n in members if n.lower().endswith(".cat")]
            catalog_pairs = set()
            for catalog in catalogs:
                record = {"member": catalog, "status": "VERIFIED_DAT", "entries": 0}
                mod["catalogs"].append(record)
                try:
                    entries = parse_catalog(archive.read(catalog))
                    record["entries"] = len(entries)
                    dat = catalog[:-4] + ".dat"
                    catalog_pairs.update({catalog, dat})
                    with archive.stream(dat) as stream:
                        for entry in entries:
                            remaining, buffer = entry["size"], bytearray()
                            fingerprint = hashlib.md5()
                            keep = wanted_text(entry["path"]) and remaining <= TEXT_LIMIT
                            while remaining:
                                chunk = stream.read(min(remaining, 1024 * 1024))
                                if not chunk:
                                    raise ValueError(f"DAT ends early at {entry['path']}")
                                fingerprint.update(chunk)
                                if keep:
                                    buffer.extend(chunk)
                                remaining -= len(chunk)
                            file = {**entry, "origin": catalog, "kind": "asset",
                                    "catalog_mode": "subst" if PurePosixPath(catalog).name.lower().startswith("subst") else "ext",
                                    "actual_md5": fingerprint.hexdigest()}
                            file["integrity"] = "MATCH" if file["actual_md5"] == entry["declared_md5"] else "MISMATCH"
                            if file["integrity"] != "MATCH":
                                record["status"] = "MD5_MISMATCH"
                            mod["files"].append(file)
                            if keep:
                                file["sha256"] = hashlib.sha256(buffer).hexdigest()
                                text_evidence(bytes(buffer), mod, file, package["documents"])
                        if stream.read(1):
                            record["status"] = "TRAILING_DAT_BYTES"
                except Exception as error:
                    record["status"] = "ERROR"
                    record["error"] = str(error)
                    mod["limitations"].append(f"CAT/DAT: {catalog}: {error}")
            for member in members:
                relative = member[len(prefix):]
                if member in catalog_pairs or relative == "content.xml":
                    continue
                if not (relative.split("/")[0].lower() in GAME_DIRS or relative.lower() == "ui.xml" or wanted_text(relative)):
                    continue
                file = {"path": relative, "origin": member, "kind": "asset", "catalog_mode": "loose"}
                mod["files"].append(file)
                if wanted_text(relative):
                    if archive.sizes.get(member, 0) > TEXT_LIMIT:
                        mod["limitations"].append(f"Loose text too large: {member}")
                        continue
                    data = archive.read(member)
                    file["size"] = len(data)
                    file["sha256"] = hashlib.sha256(data).hexdigest()
                    file["actual_md5"] = hashlib.md5(data).hexdigest()
                    text_evidence(data, mod, file, package["documents"])
            # Root docs for source repositories may sit above src/content.xml.
        package["archive_documents"] = []
        for name in archive.original:
            if re.search(r"license|licence|permissions|readme", PurePosixPath(name).name, re.I) and archive.sizes.get(name, 0) <= TEXT_LIMIT:
                data = archive.read(name)
                package["archive_documents"].append({"path": name, "sha256": hashlib.sha256(data).hexdigest()})
    except Exception as error:
        package["status"] = "ERROR"
        package["limitations"].append(str(error))
    finally:
        if archive:
            archive.close()
    return package


def environment(game, profile, base):
    result = {"game_directory": str(game), "profile_directory": str(profile),
              "game_version": None, "installed": [], "profile_overrides": [], "limitations": []}
    version = game / "version.dat"
    if version.exists():
        result["game_version"] = version.read_text().strip()
        result["version_sha256"] = digest_file(version)
    for folder in (game / "extensions", profile / "extensions"):
        if folder.exists():
            for path in sorted(folder.glob("*/content.xml")):
                node = ET.parse(path).getroot()
                result["installed"].append({"location": str(path), "sha256": digest_file(path),
                                             "attributes": {k: v for k, v in node.attrib.items() if k != "description"},
                                             "dependencies": [dict(e.attrib) for e in node if local_tag(e.tag) == "dependency"]})
    content = profile / "content.xml"
    if content.exists():
        result["profile_overrides"] = [dict(e.attrib) for e in ET.parse(content).getroot() if local_tag(e.tag) == "extension"]
        result["profile_content_sha256"] = digest_file(content)
    config = profile / "config.xml"
    if config.exists():
        result["uisafemode"] = ET.parse(config).getroot().findtext("uisafemode")
    log = profile / "debuglog.txt"
    if log.exists():
        text = log.read_text(encoding="utf-8", errors="replace")
        result["historical_log"] = {
            "path": str(log), "sha256": digest_file(log),
            "started": next((line for line in text.splitlines() if line.startswith("Logfile started")), None),
            "builds": sorted(set(re.findall(r"\b9\.00 \((\d+)\)", text))),
            "tme_mentioned": "terran_mining_empire" in text or "TME_Kernel" in text,
            "tme_kernel_errors": len(re.findall(r"Error in MD cue md\.TME_Kernel", text)),
            "status": "HISTORICAL_ONLY",
        }
    result["limitations"].append("No game launched; no save inspected; enabled in content.xml is not runtime confirmation.")
    database = base / "workspace/x4cat-v900.db"
    if database.exists():
        with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as connection:
            tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
            result["index_tables"] = tables
            result["index_counts"] = {table: connection.execute('SELECT count(*) FROM "' + table.replace('"', '""') + '"').fetchone()[0]
                                      for table in tables if not table.startswith("sqlite_") and "fts" not in table}
    return result


def baseline_catalogs(game):
    paths, catalogs, errors = set(), [], []
    locations = [(p, "") for p in sorted(game.glob("*.cat")) if not p.stem.endswith("_sig")]
    locations += [(p, "extensions/" + p.parent.name + "/")
                  for p in sorted((game / "extensions").glob("*/*.cat")) if not p.stem.endswith("_sig")]
    for path, prefix in locations:
        try:
            entries = parse_catalog(path.read_bytes())
            paths.update((prefix + e["path"]).lower() for e in entries)
            catalogs.append({"path": str(path), "sha256": digest_file(path), "entries": len(entries)})
        except Exception as error:
            errors.append({"path": str(path), "error": str(error)})
    return paths, {"catalogs": catalogs, "errors": errors, "unique_virtual_paths": len(paths),
                   "limitation": "Catalog paths only, no load-order merge, vanilla XML selector simulation, signatures or DAT hash verification."}


def dependency_rows(packages, env):
    providers = defaultdict(list)
    for package in packages:
        for mod in package["mods"]:
            if mod["attributes"].get("id"):
                providers[mod["attributes"]["id"]].append(mod)
    installed = {item["attributes"]["id"]: item for item in env["installed"]}
    rows = []
    for package in packages:
        for mod in package["mods"]:
            for dep in mod["dependencies"]:
                target = dep.get("id", "")
                available = providers.get(target, [])
                candidates = [m["attributes"].get("version", "") for m in available]
                if target in installed:
                    candidates.append(installed[target]["attributes"].get("version", ""))
                if not target:
                    candidates = [env.get("game_version") or ""]
                minimum = dep.get("version", "0")
                comparable = [int(v) for v in candidates if v.isdigit()]
                note = ""
                if "minversion" in dep:
                    note = "minversion is preserved as declared; engine semantics not verified"
                if not candidates:
                    state = "NOT_FOUND"
                elif "minversion" in dep:
                    state = "UNVERIFIED_ATTRIBUTE"
                elif not minimum.isdigit() or not comparable:
                    state = "UNKNOWN_VERSION"
                elif max(comparable) < int(minimum):
                    state = "BELOW_MINIMUM"
                else:
                    state = "NOMINAL_VERSION_OK"
                rows.append({"package": package["path"], "extension": mod["attributes"].get("id", ""),
                             "root": mod["root"], "dependency": target or "X4_BASE_GAME",
                             "minimum": minimum, "optional": dep.get("optional", "false"), "state": state,
                             "declared_attributes": json.dumps(dep, ensure_ascii=False, sort_keys=True), "note": note,
                             "providers": " | ".join(m["package"] + "::" + m["root"] for m in available),
                             "available_versions": " | ".join(candidates)})
    return rows


def collisions(packages):
    targets = defaultdict(list)
    for package in packages:
        for mod in package["mods"]:
            key = package["path"] + "::" + mod["root"]
            for file in mod["files"]:
                path = norm(file["path"]).lower()
                if path.split("/")[0] not in GAME_DIRS:
                    continue
                targets[path].append({"provider": key, "id": mod["attributes"].get("id", ""),
                                      "kind": file["kind"], "mode": file["catalog_mode"],
                                      "hash": file.get("actual_md5", ""), "origin": file["origin"],
                                      "operations": file.get("operations", [])})
    result = []
    for path, entries in sorted(targets.items()):
        if len({e["provider"] for e in entries}) < 2:
            continue
        hashes = {e["hash"] for e in entries if e["hash"]}
        if len({e["id"] for e in entries}) == 1:
            risk = "SAME_ID_ALTERNATIVES"
        elif len(hashes) == 1 and all(e["hash"] for e in entries):
            risk = "IDENTICAL_CONTENT"
        elif all(e["kind"] == "xml_diff" for e in entries):
            risk = "DIFF_OVERLAP_REVIEW"
        elif any(e["mode"] == "subst" for e in entries) or path.endswith((".lua", ".xpl")):
            risk = "REPLACEMENT_REVIEW"
        elif path.startswith("t/"):
            risk = "TEXT_IDS_REVIEW"
        else:
            risk = "SHARED_PATH_REVIEW"
        result.append({"path": path, "risk": risk, "entries": entries})
    return result


def classify(package):
    """Conservative proposal, never authorization or compatibility certification."""
    name = package["path"].lower()
    if "/reference/tools/" in name:
        return "TOOL_REFERENCE", "Development resource; not an extension selection"
    if "/reference/mods/" in name:
        return "REFERENCE", "Source/example collection; do not install as a bundle"
    if any(f["kind"] == "xml_parse_error" for m in package["mods"] for f in m["files"]):
        return "QUARANTINE", "XML not well-formed; requires corrected upstream artifact"
    if "sir sector's mod support compatibility patch" in name:
        return "LAB", "Replaces Mod Support APIs files; evaluate only against a reproduced failure and an unpatched control"
    if "extension_sets_manager_" in name:
        return "OPTIONAL_CANDIDATE", "Optional profile manager; requires Print Extension List and save-isolation QA"
    if any(s in name for s in ["ui extensions 552", "sn_mod_support_apis_v"]):
        return "CONDITIONAL_CORE", "Only if the chosen TME UI implementation requires it; QA pending"
    if any(s in name for s in ["gate_manage", "inix gate", "player feudal", "kuda_ai", "escape pod", "living crew", "rescuerangers", "civilian economy"]):
        return "LAB", "Isolated evaluation of gameplay/authority/persistence changes"
    if any(s in name for s in ["textures", "more rooms", "ship variation", "terran station modules", "teladi kea", "antigone griffon", "dock_queue", "print_extension", "enhanced info", "station_production_overview", "all_ships_with_filters", "arck shipyard"]):
        return "OPTIONAL_CANDIDATE", "Individual content/UI candidate; Vanilla+ and QA review pending"
    return "REFERENCE", "Study first; no evidence justifies adding this to the base pack"


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("workspace/audit-pack-base"))
    parser.add_argument("--game", type=Path, default=Path("D:/Games/X4 Foundations"))
    parser.add_argument("--profile", type=Path, default=Path.home() / "Documents/Egosoft/X4/6144")
    parser.add_argument("--vendor", type=Path, help="Optional directory containing py7zr")
    args = parser.parse_args()
    if args.vendor:
        sys.path.insert(0, str(args.vendor.resolve()))
    base, out = args.root.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    packages = []
    paths = sorted(p for p in (base / "inputs").rglob("*") if p.suffix.lower() in {".zip", ".rar", ".7z"} and p.is_file())
    for i, path in enumerate(paths, 1):
        package = scan_archive(path, base)
        packages.append(package)
        print(f"{i}/{len(paths)} {package['status']} {path.name}", flush=True)
    env = environment(args.game, args.profile, base)
    deps, overlaps = dependency_rows(packages, env), collisions(packages)
    vanilla_paths, baseline = baseline_catalogs(args.game)
    for overlap in overlaps:
        overlap["in_baseline_catalogs"] = overlap["path"] in vanilla_paths
    mods = [mod for package in packages for mod in package["mods"]]
    summary = {"archives": len(packages), "archive_formats": dict(Counter(p["format"] for p in packages)),
               "archive_status": dict(Counter(p["status"] for p in packages)), "extension_manifests": len(mods),
               "distinct_extension_ids": len({m["attributes"].get("id") for m in mods}),
               "catalog_status": dict(Counter(c["status"] for m in mods for c in m["catalogs"])),
               "catalog_entries": sum(c["entries"] for m in mods for c in m["catalogs"]),
               "xml_parse_errors": sum(f["kind"] == "xml_parse_error" for m in mods for f in m["files"]),
               "dependency_states": dict(Counter(d["state"] for d in deps)),
               "overlap_risks": dict(Counter(c["risk"] for c in overlaps)),
               "breaking_900_hits": sum(len(m["breaking_900_hits"]) for m in mods),
               "proposed_roles": dict(Counter(classify(p)[0] for p in packages))}
    result = {"schema_version": 1, "generated_utc": datetime.now(timezone.utc).isoformat(),
              "script_sha256": digest_file(Path(__file__)), "summary": summary, "environment": env,
              "packages": packages, "dependencies": deps, "overlaps": overlaps, "baseline": baseline}
    (out / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(out / "packages.csv", [{**p, "extension_manifests": len(p["mods"]),
                                     "limitations": " | ".join(p["limitations"])} for p in packages],
              ["path", "format", "bytes", "sha256", "member_count", "extension_manifests", "status", "limitations"])
    write_csv(out / "extensions.csv", [{"package": m["package"], "root": m["root"], **m["attributes"],
                                       "content_sha256": m["content_sha256"], "files": len(m["files"]),
                                       "limitations": " | ".join(m["limitations"])} for m in mods],
              ["package", "root", "id", "name", "author", "version", "date", "enabled", "save", "content_sha256", "files", "limitations"])
    write_csv(out / "dependencies.csv", deps,
              ["package", "extension", "root", "dependency", "minimum", "optional", "state", "available_versions", "providers", "declared_attributes", "note"])
    write_csv(out / "overlaps.csv", [{"path": c["path"], "risk": c["risk"], "in_baseline_catalogs": c["in_baseline_catalogs"], "provider": e["provider"],
                                    **{k: e[k] for k in ["id", "kind", "mode", "hash", "origin"]},
                                    "selectors": " | ".join(o["op"] + ":" + o["sel"] for o in e["operations"])}
                                   for c in overlaps for e in c["entries"]],
              ["path", "risk", "in_baseline_catalogs", "provider", "id", "kind", "mode", "hash", "origin", "selectors"])
    write_csv(out / "licenses.csv", [d for p in packages for d in p["documents"]],
              ["package", "root", "path", "sha256", "markers", "redistribution"])
    write_csv(out / "selection.csv", [{"package": p["path"], "sha256": p["sha256"],
                                      "role": classify(p)[0], "reason": classify(p)[1],
                                      "decision": "CANDIDATE", "in_game": "NOT_TESTED", "redistribution": "NOT_CLEARED"} for p in packages],
              ["package", "sha256", "role", "reason", "decision", "in_game", "redistribution"])
    write_csv(out / "license_packages.csv", [{"package": p["path"], "sha256": p["sha256"],
                         "archive_documents": " | ".join(d["path"] for d in p.get("archive_documents", [])),
                         "catalog_documents": " | ".join(d["root"] + "::" + d["path"] for d in p["documents"]),
                         "redistribution": "NOT_CLEARED"} for p in packages],
              ["package", "sha256", "archive_documents", "catalog_documents", "redistribution"])
    (out / "summary.json").write_text(json.dumps({"schema_version": result["schema_version"],
                              "generated_utc": result["generated_utc"], "script_sha256": result["script_sha256"],
                              "summary": summary, "environment": env, "baseline": baseline}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
