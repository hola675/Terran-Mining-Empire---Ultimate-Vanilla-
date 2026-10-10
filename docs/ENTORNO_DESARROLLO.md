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
