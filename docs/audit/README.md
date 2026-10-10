# Auditoría técnica del pack base

**Inspección:** 2026-10-10. **Objetivo:** X4: Foundations 9.00. **Resultado:** auditoría estática completada; selección propuesta y compatibilidad en el motor pendientes.

Se inspeccionaron los **112 archivos locales**: 80 en `inputs/mods`, 20 en `inputs/reference/mods` y 12 en `inputs/reference/tools`. Los 102 ZIP, 6 7Z y 4 RAR pudieron leerse. Se calcularon SHA-256 de cada paquete, se leyeron 131 manifiestos de extensión (124 IDs distintos) y se verificaron 48 pares CAT/DAT con 24.739 entradas mediante los MD5 declarados por sus catálogos. Un ZIP puede contener muchas extensiones: `x4-projects-master.zip` contiene 29 manifiestos; no es un único mod instalable.

`READ` significa que se pudo inspeccionar el archivo; no certifica todos sus assets, instalación, ejecución, autenticidad de origen ni compatibilidad. Los hashes identifican esta copia local, sin comparación con hashes publicados por el autor. La inspección de herramientas se limita a su archivo, índice y documentos: no se ejecutaron los programas descargados.

## Hallazgos que cambian el informe inicial

| Prioridad | Evidencia | Consecuencia |
|---|---|---|
| P0 | Kill And Attack Notifications Extended: `md/kill_and_attack_notifications_extended.xml`, línea 667, cierre de etiqueta discordante | Cuarentena del artefacto; no instalar esta copia |
| P0 | Player Feudal Realm declara `ws_3722585376`, versión mínima `900`, obligatorio, sin proveedor local en la colección ni instalación inspeccionadas | Laboratorio de gobernadores bloqueado por Conversation Pagination API |
| P0 | UI Extensions y Star Command sustituyen `ui/addons/ego_targetmonitor/targetmonitor.xpl` con contenido diferente | Resolver la selección y sustitución de UI antes de probarlos juntos |
| P0 | Siete IDs tienen más de un paquete proveedor, incluidos dos Don't Ignore Blacklists distintos con ID `Dont_Ignore_blacklists` | Elegir una sola variante por ID; no copiar fuentes y releases simultáneamente |
| P1 | Ocho dependencias usan `minversion`, y dos relaciones tienen versiones no comparables como enteros | Preservar la declaración y verificar su interpretación por el motor |
| P1 | El perfil conserva SW Interworlds habilitado, sin carpeta presente; `uisafemode=false` | Preparar y registrar una línea base de pruebas; no declarar vanilla limpio |
| P1 | Log del 2026-10-09: X4 9.00 (611726), referencias a TME y siete errores de cue `TME_Kernel` | Existe antecedente de ejecución, pero no fuente actual localizada ni certificación V5.7 |
| P1 | El índice x4cat tiene nueve registros de catálogo, todos del juego base | Sus 461.598 archivos no prueban cobertura de los siete DLC |
| P2 | El ZIP local Claude Code Toolkit V3.2.0 contiene `KNOWLEDGEBASE.md` y fuentes `tools/x4validate/`, ausentes en las rutas usadas por los agentes actuales | Hay una vía de recuperación local que debe revisarse antes de buscar otra descarga; no se extrajo ni ejecutó |

Hay **404 rutas compartidas** entre proveedores; 184 aparecen en los catálogos actuales del juego/DLC. Su clasificación distingue 97 solapamientos de diffs, 81 alternativas del mismo ID, 208 rutas compartidas de otros tipos, 17 archivos de traducción y una ruta de sustitución UI entre IDs distintos. Esto no equivale a 404 incompatibilidades ni es una matriz de una instalación activa. Incluye las fuentes de referencia. La única coincidencia del escaneo con acciones/API retiradas de 9.00 (`event_area_discovered`) se revisó en el fuente: está comentada en `md/kuertee_ssac.xml:737` y **no demuestra uso incompatible**.

## Expedientes

La colección incluye las [dos descargas incorporadas desde `Downloads/new`](PACK_BASE_MANIFEST.md#incorporación-de-las-dos-descargas-nuevas): Extension Sets Manager 1.03 como candidato opcional y Sir Sector's Compatibility Patch 1.97 como laboratorio. Se preservaron los originales y se verificaron los hashes de las copias. Las [doce sustituciones del parche](data/compatibility_patch_overrides.csv) se compararon aparte contra soporte 1.95; el detector general no resuelve ese prefijo de extensión destino.

- [Selección y manifiesto del pack base](PACK_BASE_MANIFEST.md)
- [Dependencias, IDs y orden de carga](MOD_DEPENDENCIES.md)
- [Compatibilidad y solapamientos en 9.00](MOD_COMPATIBILITY_900.md)
- [Procedencia, licencias y distribución](MOD_LICENSES.md)
- [Capacidades vanilla y alcance propio](VANILLA_CAPABILITIES.md)
- [Responsabilidad y permisos de cada sistema](SYSTEM_OWNERSHIP.md)
- [Perfiles y pruebas reproducibles](TEST_PROFILES.md)
- [Preguntas abiertas y criterios de cierre](RESEARCH_GAPS.md)

## Evidencias y repetición

La carpeta [data](data/) publica solo metadatos, rutas y fingerprints: inventario de 112 paquetes, 131 manifiestos, 201 relaciones declaradas, solapamientos con selectores, selección propuesta y registro documental de licencias para todos los paquetes. [summary.json](data/summary.json) conserva fecha UTC, hash del script, estado del entorno y hashes de los 30 catálogos del juego/DLC consultados. Se excluyeron sus catálogos de firmas `_sig`. Se identificaron 513.274 rutas virtuales únicas en ese ámbito, sin leer ni verificar los DAT del juego. Ese número no es comparable directamente con el índice que cubre solo el juego base.

El informe detallado local `workspace/audit-pack-base/audit.json` conserva las operaciones XML por archivo, los MD5 comprobados y la cobertura de catálogos. No se incorpora completo a Git por su tamaño; puede regenerarse con las mismas entradas. Los paquetes originales y las dependencias del lector siguen ignorados por Git.

Desde la raíz, en PowerShell, con Python 3.14 (versión usada en esta inspección) y UnRAR instalado en `C:\Program Files\WinRAR\UnRAR.exe` o disponible como `unrar` en PATH:

```powershell
python -m pip install --target workspace/audit-pack-base/vendor py7zr==1.1.3
python scripts/audit_pack.py --vendor workspace/audit-pack-base/vendor --game 'D:\Games\X4 Foundations' --profile 'C:\Users\Admin\Documents\Egosoft\X4\6144'
python scripts/test_audit_pack.py
```

`--root`, `--output`, `--game` y `--profile` permiten usar otras rutas. Seleccionar explícitamente el perfil correcto. Los ocho checks sintéticos verifican límites de CAT/DAT, hashes, manifiestos anidados, mínimos, aliases ausentes, exclusión de directorios RAR y que compartir un diff no se convierta automáticamente en incompatibilidad. No son pruebas del juego. La biblioteca py7zr se instaló únicamente en el área local de auditoría; no se descargaron mods adicionales.

Para actualizar la evidencia versionada tras revisar un nuevo resultado:

```powershell
Copy-Item -LiteralPath workspace/audit-pack-base/packages.csv, workspace/audit-pack-base/extensions.csv, workspace/audit-pack-base/dependencies.csv, workspace/audit-pack-base/overlaps.csv, workspace/audit-pack-base/licenses.csv, workspace/audit-pack-base/license_packages.csv, workspace/audit-pack-base/selection.csv, workspace/audit-pack-base/summary.json -Destination docs/audit/data
```

## Límites de la conclusión

Las herramientas MCP del grafo no estuvieron disponibles: no se obtuvo generación ni cobertura del grafo. Se usó lectura directa de archivos en el ámbito documentado. No se lanzaron X4 ni los mods, no se inspeccionaron saves, no se alteraron perfiles/extensiones y no se aplicaron diffs a un universo fusionado. El escáner no interpreta XPath, precedencia entre loose/CAT, variantes por versión, aliases equivalentes, ciclos de carga ni callbacks Lua; el bytecode XPL queda opaco. Los marcadores de licencia son pistas documentales, no una autorización de redistribución. Cualquier caso fuera de estas comprobaciones sigue `NOT_TESTED` o `NOT_CLEARED`.

**Siguiente trabajo:** preparar `X4-VANILLA-900`, elegir la estrategia mínima de UI para V5.7 y ejecutar los gates del [documento 18](../plan/18_V57_ESTACION_REAL_ALMACENAMIENTO.md). La auditoría no cambia la prioridad presidencial de observar una estación real.
