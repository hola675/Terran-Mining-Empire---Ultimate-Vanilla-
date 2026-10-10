# 18. V5.7: primer observador de estación real y almacén

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Decisión presidencial
**Opción A V5.7:** primera lectura real de una estación existente, su administrador y sus existencias sólidas, antes de observar toda la flota. La prueba puede utilizar una estación de propiedad legítima en sector vanilla, sin esperar a CMC-01, CIT-01 o HZ-04A.

## Alcance de primer vertical slice
Comprobar handshake Lua↔MD; seleccionar/bindear una estación real; observar referencia, nombre, sector, propietario y manager; leer si está disponible: capacidad sólida, espacio utilizado, mineral y silicio; abrir/cerrar un menú de solo lectura y conservar asociación tras SAVE/LOAD. Si una propiedad no tiene método comprobado, UNSUPPORTED en lugar de número ficticio.

## Protocolo de prueba
**Gate A — Preparación:** registrar versión 9.00, DLC activos, lista de mods del entorno de prueba, hash/versión del mod, ID de guardado y copia previa. Disponer de estación existente con administrador real y almacenamiento sólido; no regalarla ni crearla para cumplir la prueba. Si el save no tiene estación propia, usar una partida de ensayo en la que se adquiera/construya legítimamente o marcar BLOCKED.

**Gate B — Descubrimiento API:** consultar fuentes locales de X4 con x4cat y esquemas XSD. Identificar expresiones MD / llamadas Lua concretas para estación, sector, manager, tipo de almacenamiento, cargo actual y capacidad. Documentar archivo vanilla o XSD, firma, tipos y versión. No escribir código de producción basándose en sintaxis supuesta.

**Gate C — Comunicación:** petición Lua con request_id → evento MD → validar estación → escribir snapshot en blackboard → raise_lua_event → Lua lee y comprueba request_id. Dos peticiones seguidas no deben cruzar respuestas. Eventos con namespace único.

**Gate D — Datos reales:** comparar el inventario mostrado por COM con Logical Station Overview del juego en instante controlado. Probar estación con silicio positivo, luego lectura legítima de cambio de stock; diferenciar 0, UNKNOWN y ERROR. No alterar wares desde scripts de prueba. Si no es seguro manipular stock de partida, esperar una entrega natural o usar save de ensayo.

**Gate E — Persistencia:** renombrar estación y comprobar continuidad de corporate_id; guardar/cargar y resolver referencia; destruir/vender una estación solo en save descartable de pruebas si se justifica, comprobando MISSING_OBJECT y sin reconstrucción.

**Gate F — Vanilla+:** inspeccionar logs y diff de comportamiento: ninguna orden minera/comercial alterada, ningún crédito o ware creado, ninguna modificación de manager o NPC. UI se abre/cierra sin romper mapa ni campañas.

## Evidencia mínima
captura vanilla antes/después, captura COM con estado de calidad, IDs/logs de solicitud y respuesta, versión/commit, XML lint/XSD, save de ensayo y lista de pruebas. Cada caso: PASS/FAIL/BLOCKED/NOT_TESTED con timestamp e incidencia reproducible.

## Dependencias
Extensión fuente propia aún inexistente en el main consultado. Local x4cat/XSD preparado según docs/ENTORNO_DESARROLLO.md; **no ejecutado remotamente**. HZ-04A no bloquea V5.7, porque el primer observador utiliza una estación real en cualquier lugar compatible.

## Resultado y siguiente fase
Se puede marcar COM57_STATION_PASS solamente tras comparar lecturas reales y persistencia. Después añadir una Bolo real/capitán, luego varias estaciones, y solo más tarde contabilidad de reservas y recomendaciones.

## V5.7 — ratificación y criterios operativos (2026-10-10)

Opción A ratificada: estación real propia, administrador y almacén sólido. Pruebas necesarias: inventario positivo, cero real, cambio natural, renombrado, dos solicitudes consecutivas, SAVE/LOAD, referencia ausente y regresión de órdenes/créditos.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).
