# 19. Plan de QA, evidencias, compatibilidad y rollback

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Niveles de validación
- STATIC_PASS: XML bien formado, XSD, metadatos, paths y scripts presentes.
- BRIDGE_PASS: Lua y MD intercambian un dato real, correlacionado.
- STATION_PASS: estación real, administrador/inventario mostrados correctamente.
- PERSISTENCE_PASS: SAVE/LOAD, IDs y eventos idempotentes.
- VANILLA_PASS: ninguna regresión en órdenes, recursos, NPC, dinero y menús.
- NOT_TESTED/BLOCKED si no existe entorno o evidencia. **Nunca sustituir por estimación.**

## Matriz inmediata
| ID | Prueba | Evidencia |
|---|---|---|
| COM57-01 | Contenido de extensión y ui.xml válido | lint/XSD |
| COM57-02 | Carga en X4 9.00 | log y pantalla |
| COM57-03 | Handshake request/response | IDs, log, snapshot |
| COM57-04 | Estación existente y propia | ID, captura vanilla |
| COM57-05 | Manager y sector | lectura vs UI |
| COM57-06 | Almacenamiento sólido capacidad/uso | lectura vs UI |
| COM57-07 | Silicio y mineral, 0 vs UNKNOWN | muestra controlada |
| COM57-08 | Cambio de inventario real | dos snapshots y evento |
| COM57-09 | Renombrado | mismo object_ref |
| COM57-10 | SAVE/LOAD | mismo corporate_id sin duplicación |
| COM57-11 | Objeto destruido/ausente | MISSING_OBJECT seguro |
| COM57-12 | Ninguna orden ni economía alterada | pruebas de regresión |
| COM57-13 | Menú accesible y estable | vídeo/capturas |
| COM57-14 | Compatibilidad y rollback | smoke y reactivación |
| COM57-15 | Rendimiento base | tiempo de consulta medido |

## Alcance global posterior
Probar HZ-01/HZ-02/HZ-04A, pasaje manual/IA, construcción física, acopio, trade entre estaciones, flotas, seguridad, reservas, tesorería y veinte misiones. Cada bloque tiene estados independientes. No ocultar fallos COM con PASS de un sistema no relacionado.

## Evidencia estructurada
Guardar reportes con fecha, versión de juego, DLC, mods activos, commit exacto, save usado, caso, prerequisitos, acciones, observación, logs y prueba visual. No incluir contraseñas ni datos personales del equipo. Los paths locales de evidencia permanecen ignorados y no se suben al repo por defecto.

## Rollback
Validar restauración del save; registrar si quitar una extensión deja referencias pendientes. En COM-01 solo lectura se espera reversibilidad elevada, pero debe demostrarse. Mods de puertas pueden requerir desinstalación controlada y no son parte del primer prototipo.

## V5.7 — ratificación y criterios operativos (2026-10-10)

Los 15 casos COM57 siguen NOT_TESTED hasta contar con ejecución y pruebas reales. Cada PASS requiere versión X4/DLC, save, hash extensión, request_id, capturas vanilla/COM, logs, resultados y rollback verificable.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).

Extensión futura (sin mezclar con COM57): FAC-01 titularidad player en activos clasificados; FAC-02 prioridad de orden manual; FAC-03 funcionamiento de IA vanilla; TER-01 módulo reclamante nativo; TER-02 exclusividad NPC de los cuatro sectores; TER-03 pérdida/destrucción/SAVE/LOAD; TER-04 anexión sector neutral colindante con recursos; TER-05 disputa NPC sin anexión gratuita; TER-06 culminación de los cuatro sin hostilidad programada. Todos `NOT_TESTED`. Detalle y criterios en [ADR-0001](../decisions/ADR-0001_FACCION_JUGADOR_SOBERANIA_Y_EXPANSION.md).
