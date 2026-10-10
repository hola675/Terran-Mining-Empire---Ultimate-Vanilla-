# Perfiles de pruebas

**Revisión:** 2026-10-10. **Estado:** protocolos preparados; perfiles no creados ni activados. No se han modificado carpetas de extensiones, configuración ni saves.

| Perfil | Componentes admitidos | Objeto y salida mínima |
|---|---|---|
| `X4-VANILLA-900` | Juego 9.00 y DLC declarados; sin mods comunitarios | Baseline de carga, UI, estación, inventario y órdenes |
| `TME-CORE-DEV` | Baseline + futura fuente TME + dependencias justificadas | Gates Lua/MD, lectura, comparación vanilla y persistencia V5.7 |
| `TME-INTEGRATION` | Core probado + un complemento seleccionado por incremento | Diferencia respecto al control y pruebas conjuntas de su dominio |
| `TME-LAB` | Una hipótesis: puertas, gobernadores, AI o rescate | Save descartable separado, requisitos y rollback propios |

`TME-LAB` es una familia de ensayos: no activar todos los experimentos simultáneamente. Registrar subcaso, por ejemplo `TME-LAB-GATES-01`, y su lista exacta. Un nombre de perfil escrito en un documento no constituye un gestor de extensiones ni aísla automáticamente el directorio del juego.

## Preparación del control

La inspección local encontró siete DLC en las dos ubicaciones revisadas (juego y perfil de usuario): Split Vendetta, Cradle of Humanity, Tides of Avarice, Kingdom End, Timelines, Hyperion Pack y Envoy Pack. Todos declaran versión `900` y `enabled="1"`. No hay mod comunitario con `content.xml` en esos directorios, pero se debe confirmar la lista cargada dentro del juego.

El perfil de usuario conserva `SW Interworlds` habilitado y Friendly Fire Tweaks deshabilitado; ninguna de esas extensiones apareció instalada. `uisafemode=false` es el estado observado, no una recomendación de cambiarlo. Registrar el modo UI para cada ensayo y elegirlo conforme a la implementación y requisitos concretos; no comparar pruebas con configuración diferente sin anotarlo.

El log existente comenzó el 2026-10-09 y registra 9.00 (611726), archivos de TME y siete errores de `TME_Kernel`. Es historial, no el resultado de esta auditoría. Copiarlo/preservarlo al preparar un ensayo nuevo; no mezclar sus fallos con logs del nuevo build.

## Registro obligatorio de cada ensayo

- ID de ensayo/perfil, fecha y versión/build que muestra esa ejecución.
- DLC y IDs efectivamente cargados; versiones de release/internas; SHA-256 de cada paquete y fuente TME.
- Modo UI, lista de proveedores elegidos y orden/dependencias verificadas.
- Save de entrada de prueba y copia anterior; estación realmente obtenida y su administrador/almacenamiento.
- Precondición, acción concreta, resultado esperado, resultado observado y estado `PASS/FAIL/BLOCKED/NOT_TESTED`.
- Log nuevo, capturas vanilla/COM, request IDs, saldos/wares/órdenes antes/después y procedimiento de reversión.

## Casos mínimos

| Caso | Qué debe demostrar | Estado de esta auditoría |
|---|---|---|
| BASE-01 | Carga del control y lista efectiva de DLC; UI y manager normales | NOT_TESTED |
| CORE-01 | Dos peticiones Lua/MD sin cruzar respuestas; lectura real comparada con UI | NOT_TESTED |
| CORE-02 | Renombrado y save/load mantienen identidad; no duplican datos/acciones | NOT_TESTED |
| CORE-03 | Cero cambios en órdenes, créditos, NPC o inventario por el observador | NOT_TESTED |
| INT-01 | Complemento aislado y después junto a core, sin regresión del dominio | NOT_TESTED |
| LAB-GATE-01 | Solo construcción con materiales/constructoras; ambos extremos y persistencia | BLOCKED: laboratorio aún no preparado |
| LAB-PFR-01 | Requisitos completos; autoridad/órdenes y cuentas sin duplicación | BLOCKED: Conversation Pagination no disponible localmente |
| LAB-CREW-01 | Identidad y rescate sin duplicación; un sistema por ensayo | NOT_TESTED |

La sustitución UIX/Star Command requiere comparar el payload efectivo del target monitor y su comportamiento, además de la lista de archivos. El fallo XML en cuarentena se resuelve con un artefacto corregido antes de probarlo en el motor.

## Ensayos de las dos incorporaciones

| Caso | Control y acción | Estado |
|---|---|---|
| LAB-SETS-01 | Con Print Extension List 1.01: función inicialmente apagada, crear/aplicar conjuntos y verificar lista tras reinicio; repetir con y sin UIX | NOT_TESTED |
| LAB-SETS-02 | Saves descartables: distinguir manuales por conjunto; comprobar visibilidad de slots 11–20 con/sin UIX, desactivación y reversión | NOT_TESTED |
| LAB-SUPPORT-PATCH-01 | Reproducir primero un fallo con soporte 1.95; repetir exactamente el caso con parche 1.97, registrando payload efectivo, nuevos logs y regresiones UI/MD/hotkeys/save-load | NOT_TESTED |

Según el README local, el gestor aplica conjuntos al reiniciar, mantiene el gestor y Print Extension List habilitados y solo separa saves manuales; quicksaves, autosaves y saves online siguen compartidos. Retirar UIX oculta los slots manuales 11–20 sin borrar sus archivos. Estas condiciones impiden tratar los conjuntos como aislamiento completo de los laboratorios. No ejecutar opciones de borrar saves durante una prueba de aislamiento.

Los procedimientos de runtime y evidencias siguen el [documento 18](../plan/18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y el [documento 19](../plan/19_MATRIZ_QA_EVIDENCIAS.md). Retirar una extensión que creó objetos persistentes no es un rollback demostrado: usar el save anterior al ensayo cuando corresponda y comprobar la reversión.
