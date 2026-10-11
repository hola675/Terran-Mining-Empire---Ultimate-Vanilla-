# Entorno local de desarrollo para X4

**Actualizado:** 2026-10-10

## Estado preparado

- Juego detectado: X4: Foundations 9.00 en `D:\Games\X4 Foundations`.
- X4 Forge Studio: fuente extraída en `tools/X4_Forge-main`; dependencias instaladas con `npm ci` y compilación completada.
- `x4cat` 1.2.6: instalado con `uv` usando Python 3.13.
- Índice de X4: `workspace/x4cat-v900.db`; registra 461.598 archivos, 8.890 reglas de esquema y 2.333 propiedades de scripts.
- Esquemas: 42 archivos XSD extraídos en `workspace/x4-schemas`; Forge usa `libraries/md.xsd` y `libraries/common.xsd`.
- VS Code ya tiene X4CodeSense instalado; se puede configurar para leer directamente desde el directorio del juego.

Las rutas locales de herramientas, índice, esquemas, configuración y staging están bajo rutas ignoradas por Git. El destino de Forge es `workspace/deploy-staging`, aislado de la carpeta real `D:\Games\X4 Foundations\extensions`.

## Abrir Forge

Desde PowerShell, en la raíz del proyecto:

```powershell
Set-Location tools\X4_Forge-main
npm run dev
```

También se puede usar `restart-studio.bat` desde esa carpeta. La configuración local está en `tools/X4_Forge-main/config.json`.

## Consultar datos del juego

```powershell
x4cat --db workspace\x4cat-v900.db search "energy cells"
x4cat --db workspace\x4cat-v900.db inspect energycells
x4cat list "D:\Games\X4 Foundations" -g "libraries/*.xml"
```

Para reconstruir el índice después de actualizar el juego:

```powershell
x4cat index "D:\Games\X4 Foundations" -o workspace\x4cat-v900.db --refresh
```

## Alcance pendiente

La carpeta de trabajo `workspace/mods` existe y está configurada, pero todavía no contiene el código fuente del mod Terran Mining Empire. El repositorio disponible hasta ahora contiene principalmente paquetes de mods y referencias. Cuando se incorpore el código del mod, esa carpeta debe apuntar a su ubicación de trabajo; el staging puede seguir separado hasta que se decida probar el despliegue en el juego.

El X Catalog Tool oficial de Egosoft (versión 1.11) es otra opción para operar con archivos CAT/DAT, pero requiere registrar un juego X en una cuenta Egosoft. Para esta instalación, `x4cat` ya cubre lectura, extracción, empaquetado, comparación y búsqueda en los catálogos. Egosoft Blender Mod Tools 0.7.0 queda como opción si el mod necesita crear o convertir modelos 3D; no hace falta para scripts, XML y lógica de juego.

## Referencias

- [Egosoft: recursos oficiales de modding para X4](https://wiki.egosoft.com/X4%20Foundations%20Wiki/Modding%20Support/)
- [Egosoft: X Catalog Tool](https://wiki.egosoft.com/X4%20Foundations%20Wiki/Modding%20Support/X%20Catalog%20Tool/)
- [Egosoft: descargas y herramientas de X4](https://www.egosoft.com/download/x4/bonus_en.php)
- [X4 Forge](https://github.com/KennyG1990/X4_Forge)
- [x4cat](https://github.com/meethune/x4cat)
- [X4CodeSense en Open VSX](https://open-vsx.org/extension/X4DevTools/x4codesense)

## Enlace con la especificación V5.7 (2026-10-10)

La [documentación canónica de veinte temas](README.md) recoge las decisiones de Terran Mining Empire y el próximo prototipo **COM-01/V5.7**, que observará una estación real y su almacenamiento sin modificar economía u órdenes. Los recursos descritos arriba siguen siendo datos del entorno local documentado, no una certificación ejecutada desde GitHub. El código fuente propio y los ensayos en el motor siguen pendientes.

## Comprobación local del pack (2026-10-10)

La [auditoría técnica](audit/README.md) leyó los 113 archivos, incluidos RAR con UnRAR 7.01 instalado y 7Z con py7zr 1.1.3 aislado en `workspace/audit-pack-base/vendor`. No se ejecutaron los programas de herramientas descargados. Forge conserva `node_modules` y `dist`; su compilación no se repitió. La CLI x4cat respondió a la consulta de ayuda, sin reconstruir el índice.

El archivo `version.dat` declara `900` y `X4.exe` informa versión 9.0.0.0. El log existente del 2026-10-09 identifica build **611726** y registra un prototipo TME con errores de `TME_Kernel`; ese antecedente no localiza su fuente actual ni acredita V5.7. En las carpetas inspeccionadas del juego y del perfil hay siete DLC con manifiesto `900`, sin mods comunitarios presentes. El perfil mantiene entradas antiguas de SW Interworlds/Friendly Fire Tweaks y `uisafemode=false`; falta registrar la lista cargada en una nueva ejecución.

El SQLite tiene 461.598 filas `game_files`, 8.890 filas `schema_groups` y 2.333 `script_properties`. Sus nueve registros `cat_files` apuntan únicamente a `01.cat`–`09.cat` del juego base. No usar ese índice como prueba de cobertura de DLC: la auditoría leyó además los índices de catálogos de los siete DLC, 30 catálogos en total con el juego base. Las consultas de recursos terranos requieren incluir explícitamente ese ámbito. Los detalles y hashes se conservan en [summary.json](audit/data/summary.json).
