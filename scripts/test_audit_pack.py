"""Focused checks for archive isolation, CAT boundaries and dependency evidence."""
import tempfile
import unittest
import zipfile
from pathlib import Path

from audit_pack import collisions, dependency_rows, parse_catalog, parse_unrar_listing, scan_archive


class AuditChecks(unittest.TestCase):
    def test_rar_listing_excludes_directories(self):
        listing = 'Name: mod/assets\nType: Directory\nName: mod/a file.xml\nType: File\nSize: 5\n'
        self.assertEqual(parse_unrar_listing(listing), [{"Name": "mod/a file.xml", "Type": "File", "Size": "5"}])

    def test_catalog_paths_with_spaces_and_offsets(self):
        rows = parse_catalog(b"ui/a file.lua 3 1 900150983cd24fb0d6963f7d28e17f72\nmd/b.xml 2 1 4124bc0a9335c27f086f24ba207a4912\n")
        self.assertEqual([(r["path"], r["offset"]) for r in rows], [("ui/a file.lua", 0), ("md/b.xml", 3)])

    def test_bad_catalog_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_catalog(b"file.xml 3 1 invalid\n")

    def test_no_installed_claim_for_download(self):
        packages = [{"path": "a.zip", "mods": [{"package": "a.zip", "root": "a", "attributes": {"id": "a", "version": "2"},
                    "dependencies": [{"id": "b", "version": "3"}, {"id": "alias_b", "optional": "true"}]},
                    {"package": "a.zip", "root": "b", "attributes": {"id": "b", "version": "4"}, "dependencies": []}]}]
        rows = dependency_rows(packages, {"installed": [], "game_version": "900"})
        self.assertEqual(rows[0]["state"], "NOMINAL_VERSION_OK")
        self.assertEqual(rows[1]["state"], "NOT_FOUND")
        self.assertEqual(rows[1]["optional"], "true")

    def test_minimum_base_version(self):
        packages = [{"path": "a.zip", "mods": [{"root": "a", "attributes": {"id": "a"},
                    "dependencies": [{"version": "901"}]}]}]
        self.assertEqual(dependency_rows(packages, {"installed": [], "game_version": "900"})[0]["state"], "BELOW_MINIMUM")

    def test_nested_manifests_and_catalog_fingerprint(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "mods.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("content.xml", '<content id="parent"/>')
                archive.writestr("child/content.xml", '<content id="child"/>')
                archive.writestr("child/ext_01.cat", "ui/a.lua 3 1 900150983cd24fb0d6963f7d28e17f72\n")
                archive.writestr("child/ext_01.dat", b"abc")
            result = scan_archive(path, Path(folder))
            self.assertEqual(result["status"], "READ")
            self.assertEqual(len(result["mods"]), 2)
            parent, child = result["mods"]
            self.assertEqual(parent["files"], [])
            self.assertEqual(child["files"][0]["integrity"], "MATCH")
            self.assertEqual(child["catalogs"][0]["status"], "VERIFIED_DAT")

    def test_truncated_dat_is_a_coverage_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "mod.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("content.xml", '<content id="a"/>')
                archive.writestr("ext_01.cat", "ui/a.lua 4 1 900150983cd24fb0d6963f7d28e17f72\n")
                archive.writestr("ext_01.dat", b"abc")
            result = scan_archive(path, Path(folder))
            self.assertEqual(result["mods"][0]["catalogs"][0]["status"], "ERROR")
            self.assertTrue(result["mods"][0]["limitations"])

    def test_same_path_is_not_automatically_incompatible(self):
        packages = [{"path": f"{i}.zip", "mods": [{"root": "m", "attributes": {"id": str(i)},
                    "files": [{"path": "md/base.xml", "kind": "xml_diff", "catalog_mode": "ext",
                               "actual_md5": str(i), "origin": "ext.cat", "operations": []}]}]} for i in (1, 2)]
        self.assertEqual(collisions(packages)[0]["risk"], "DIFF_OVERLAP_REVIEW")


if __name__ == "__main__":
    unittest.main()
