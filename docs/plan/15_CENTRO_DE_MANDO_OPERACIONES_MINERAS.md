# 15. Centro de Mando y COM: diseño funcional

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## COM V5.5
El Centro de Operaciones Mineras es una sección del Centro de Mando. Interfaz propia de gestión, **no sustituto de IA de X4**. Seis vistas:
1. Resumen: flotas, demanda, riesgos y calidad de datos.
2. Flotas: nave real, capitán, comandante, orden, mercancía y cargo.
3. Estaciones: PAF-01, CMC-01, CIT-01, almacenaje/producción.
4. Reservas: P1/P2/P3 por ware y localización, tránsito y obra.
5. Incidencias: hipótesis, evidencia, severidad y recomendación.
6. Tesorería: liquidez real donde pueda conciliarse, compromisos y solicitudes.

## Ruta de producto
COM-01 observación sin acciones → COM-02 análisis y KPI → COM-03 recomendaciones de Liora/Iven/Darian → COM-04 aplicación guiada mediante menús vanilla y auditoría. Escritura de órdenes por scripts **fuera de V5.6/V5.7**.

## Experiencia del presidente
Cada aviso muestra: objeto afectado, hecho observado, confianza, consecuencias, alternativas y autorización requerida. Aprobación registrada no significa ejecución. Botón de consulta no debe abrir confirmación de gasto. Las propuestas obsoletas caducan cuando cambia nave, comandante, inventario, ruta o una orden prioritaria.

## Manejo de desconocidos
VERIFIED, DERIVED, STALE, UNKNOWN, UNSUPPORTED, MISSING_OBJECT, ERROR. No sustituir UNKNOWN por cero; no mostrar '3 naves' si son simuladas. En prototipos y screenshots señalar claramente datos DEMO.

## Compatibilidad
Evitar sustituir interfaces vanilla extensas y no añadir botones globales sin evaluar concurrencia UI de otros mods. Menús Lua registrados correctamente; separar persistencia MD del estado visual Lua. No consultar universo completo en bucle sin control de rendimiento.

## Política personal
Kopis y Kukri personales fuera del panel de activos corporativos salvo vinculación consentida, aunque puedan aparecer en otras vistas del juego.

## V5.7 — ratificación y criterios operativos (2026-10-10)

COM muestra una sola estación vinculada, fecha de lectura y calidad por campo; botón de refresco únicamente consulta. Estados VERIFIED, UNKNOWN, UNSUPPORTED, STALE y ERROR. La UI no muestra mock como dato real.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).
