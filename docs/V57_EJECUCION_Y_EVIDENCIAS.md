# V5.7 — Procedimiento reproducible y registro de evidencias

**Decisión:** opción A — observar estación real y almacenamiento. **Estado:** DOCUMENTADO, NO TESTEADO en X4. **Base:** X4 Foundations 9.00. No modificar órdenes, economía, mercancías, NPC ni tramas vanilla.

## Preflight
1. Registrar fecha, versión/build X4, DLC, mods activos, rama/commit, hash extensión, versión de x4cat/XSD/Forge, save elegido y hash de respaldo.
2. Confirmar instalación y herramientas según [entorno](ENTORNO_DESARROLLO.md), sin asumir que el equipo sigue idéntico. No ejecutar desde GitHub el motor local.
3. Seleccionar estación real ya adquirida/construida legítimamente en partida descartable, con administrador y almacén sólido; documentar su identidad, propietario, sector y la Logical Station Overview. Si no existe, BLOCKED, nunca generar estación por script.
4. Buscar firmas **exactas** de acceso y comunicación Lua/MD en catálogos 9.00 y XSD; adjuntar ruta de fuente y fragmento. API no verificada = UNSUPPORTED, nunca pseudo-API inventada.

## Contrato de observación
El contrato lógico `tme.com.station-snapshot.v1` del capítulo 17 sigue siendo un ejemplo de diseño. Cada campo debe registrar `value`, `quality`, `source`, unidades y `game_time` cuando proceda. Correlacionar `request_id`, `snapshot_id`, `session_generation` y `revision`. Los identificadores internos del motor solo se persisten si su validez y resolución tras LOAD han sido confirmadas; el nombre visible no es clave primaria.

## Secuencia reproducible
1. Smoke de extensión: esquema XML, carga, apertura/cierre de COM (COM57-01/02/13).
2. Ejecutar handshake dos veces, comprobar respuestas correlacionadas y no obsoletas (COM57-03).
3. Capturar identidad, propietario, sector, administrador de la estación en juego y COM (COM57-04/05).
4. Comparar capacidad/ocupado de sólido y ore/silicon con UI vanilla en ventana controlada, distinguiendo 0/UNKNOWN/UNSUPPORTED (COM57-06/07).
5. Observar una entrega o retiro **natural** mediante mecánica vanilla y repetir lectura (COM57-08); no escribir mercancías con script.
6. Renombrar la estación mediante el juego: mantener identidad corporativa y referencia resoluble (COM57-09).
7. SAVE/LOAD sobre copia, reabrir y comprobar identidad, snapshots y ausencia de duplicados (COM57-10).
8. Probar objeto ausente en partida descartable cuando sea seguro: MISSING_OBJECT sin recrearlo (COM57-11).
9. Comparar ordenes, créditos, carga, propiedad, manager y progreso de misiones antes/después; diferenciar evolución natural (COM57-12).
10. Ejecutar prueba de latencia y memoria, desactivar/revertir extensión, restaurar copia y verificar sin regresiones (COM57-14/15).

## Matriz inicial (sin pruebas ejecutadas)
| Caso | Estado | Evidencia |
|---|---|---|
| COM57-01 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-02 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-03 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-04 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-05 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-06 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-07 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-08 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-09 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-10 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-11 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-12 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-13 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-14 | NOT_TESTED | Pendiente de log, captura y save de ensayo |
| COM57-15 | NOT_TESTED | Pendiente de log, captura y save de ensayo |

## Política de resultados
PASS solo cuando exista evidencia ejecutada. FAIL con pasos reproducibles y referencia de log. BLOCKED ante API/entorno/estación no disponible. NOT_TESTED si aún no se ha intentado. Si manager/capacidad/stock no están soportados, conservar UNSUPPORTED y no dar STATION_PASS por una UI bonita. Nunca subir saves privados, rutas sensibles o secretos.
