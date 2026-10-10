# V5.7 — Encargo de implementación para agente local

## Meta
Construir primer observador COM-01 para **una estación real** en X4 9.00, únicamente lectura, con persistencia de asociación y reproducción de QA. Seguir [20 capítulos](README.md), [entorno](ENTORNO_DESARROLLO.md) y [matriz ejecutable](V57_EJECUCION_Y_EVIDENCIAS.md).

## Trabajo permitido
- Revisar fuente e interfaces reales Lua/MD y APIs de inventario disponibles con x4cat/XSD.
- Crear extensión propia en directorio de trabajo separado; validar `content.xml`, `ui.xml` y namespace único de eventos.
- Vincular explícitamente estación propiedad jugador, validar objeto y resolver tras SAVE/LOAD.
- Leer nombre, sector, propietario, administrador, capacidad/ocupación sólidos y mineral/silicio cuando realmente soportado.
- Renderizar COM mínimo: estación, valores, unidades, fuente, antigüedad y calidad por campo; refrescar sin repetir handlers ni provocar tormenta de eventos.
- Capturar pruebas y publicar PR con logs, matrices, diferencias, rendimiento y rollback.

## Fuera de alcance
No modificar órdenes `Mine for Commander`, `Trade for Commander` o `Prospect`; no crear/donar estación, naves, recursos, dinero, territorios o puertas; no activar HZ, SIH, reservas, presupuestos, contratación ni misiones. No utilizar mocks como prueba del juego.

## Gates de entrega
G0 inventario de instalación y APIs reales; G1 validación estática; G2 handshake correlacionado; G3 comparación de estación/almacén con UI vanilla; G4 renombrado y persistencia; G5 regresión vanilla; G6 rendimiento y rollback. La falta de un gate se informa como FAIL/BLOCKED/NOT_TESTED, sin cerrar V5.7.

## Informe final obligatorio
Resumen en español con commit exacto, versión/build X4, DLC/mods, tabla COM57-01–15, fallos, logs/capturas, diferencias de órdenes y economía, verificación de SAVE/LOAD, rendimiento, rollback, bloqueos y siguiente paso. No declarar VERIFICADO antes de ejecutar en motor local.
