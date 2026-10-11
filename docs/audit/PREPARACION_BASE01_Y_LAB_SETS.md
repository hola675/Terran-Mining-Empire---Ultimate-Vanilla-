# Preparación local de BASE-01 y laboratorio de conjuntos

**Fecha:** 2026-10-10. **Estado:** preparación en disco verificada; ejecución X4 `NOT_TESTED`.

## BASE-01

El perfil inspeccionado es `C:\Users\Admin\Documents\Egosoft\X4\6144`. Se copiaron sus ocho archivos, 45.660.548 bytes, y se verificó cada SHA-256 contra el original. Se preservaron configuración, estado UI y log histórico; no hay carpeta `save` bajo ese perfil. Esta constatación no descarta partidas en otra ubicación.

| Artefacto local, ignorado por Git | Contenido |
|---|---|
| `workspace/labs/BASE-01-20261010/original-profile/` | Respaldo íntegro del perfil inspeccionado |
| `workspace/labs/BASE-01-20261010/preparation.json` | Inventario, hashes de respaldo y DLC, límites y estado runtime vacío |
| `workspace/labs/BASE-01-20261010/candidate-profile/config.xml` | Copia sin cambios de la configuración original, incluido el modo UI |
| `workspace/labs/BASE-01-20261010/candidate-profile/content.xml` | Siete IDs DLC habilitados; SW Interworlds y Friendly Fire Tweaks deshabilitados |

Los manifiestos instalados declaran `900`: `ego_dlc_boron`, `ego_dlc_mini_01`, `ego_dlc_mini_02`, `ego_dlc_pirate`, `ego_dlc_split`, `ego_dlc_terran`, `ego_dlc_timelines`. La configuración candidata no está activa y sus flags no prueban qué cargó el motor. Una carpeta de staging tampoco aísla las partidas automáticamente.

Para ejecutar el control:

1. Cerrar X4 y comprobar el perfil que realmente utiliza. Si cambia o aparece una partida, crear y verificar un respaldo nuevo antes de modificarlo. Preservar también cualquier ubicación externa de saves que se use.
2. Aplicar la configuración candidata al perfil de ensayo elegido y confirmar que las carpetas de extensiones correspondientes solo contienen los siete DLC. Mantener la misma configuración UI al comparar ensayos.
3. Iniciar X4 9.00 y registrar build, lista de extensiones efectivamente cargadas y un log nuevo. La baseline estricta no incluye Print Extension List ni Extension Sets Manager.
4. Comparar UI vanilla y estado normal de una estación existente. No cargar una partida estable con dependencias ausentes. Registrar `PASS/FAIL/BLOCKED`, evidencias y reversión; no sustituirlas por el inventario en disco.

## LAB-SETS-01/02

Se preparó `workspace/labs/LAB-SETS-01-20261010/extensions/` con copias de los ZIP ya auditados de **Print Extension List 1.01** y **Extension Sets Manager 1.03**. `preparation.json` conserva SHA-256 de paquetes y archivos extraídos, los dos manifiestos y `installed_in_game=false`. No se copiaron a las extensiones del juego ni del perfil activo.

Después de BASE-01, usar un entorno de ensayo con saves descartables y copia externa. Estos casos siguen `NOT_TESTED`:

| Caso | Acción y evidencia requerida |
|---|---|
| Inicio | Solo los siete DLC + los dos mods del laboratorio; lista real en un log nuevo; función del gestor inicialmente apagada |
| Cambio de conjunto | Capturar Default, crear otro conjunto, aplicar y reiniciar; comprobar lista real después del reinicio |
| Guardados manuales | Activar guardados individuales, crear un save manual en cada conjunto y comprobar visibilidad y recuperación al cambiar/reiniciar |
| Autosaves/quicksaves | Comprobar que siguen compartidos; no emplear Continue como prueba de aislamiento de un conjunto nuevo |
| Desactivación | Apagar la función del gestor, comprobar recuperación del pool compartido y reactivación; no borrar conjuntos con eliminación de saves |
| UIX opcional | Ensayo separado con y sin UIX para slots 11–20; no está incluido en este staging |
| Reversión | Retirar los mods del ensayo y restaurar perfil y save anteriores; comparar hashes y nueva lista cargada |

El autor documenta reinicio obligatorio, guardados manuales por conjunto y autoguardados/quicksaves compartidos. [Documentación de Extension Sets Manager](https://www.nexusmods.com/x4foundations/mods/2401). Esas reglas justifican el protocolo, pero no equivalen a resultados de estas pruebas.

## Puerta para V5.7

No se encontró una partida de estación bajo el perfil inspeccionado. Falta identificar una partida de ensayo con estación propia, administrador y almacenamiento sólido obtenidos legítimamente. BASE-01 y el descubrimiento de firmas en fuentes/XSD vigentes deben preceder al prototipo Lua/MD del [documento 18](../plan/18_V57_ESTACION_REAL_ALMACENAMIENTO.md).

El usuario confirmó que no hay partida de ensayo y pidió posponer su creación. BASE-01 y las pruebas que requieren saves, incluidos LAB-SETS-02 y COM57, quedan pospuestos; el staging se conserva para retomarlos.

La PR #3 conserva su rama independiente y no se ha fusionado. Esta preparación no recupera su fuente ni implementa el observador; COM57 continúa `NOT_TESTED`. Conversation Pagination y LAB-SETS no son requisitos del núcleo.
