# 01. Contexto maestro y estado del proyecto

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Propósito y fuente de verdad
Este documento es el punto de entrada para agentes, autores y revisores. Se conserva la identidad Terran Mining Empire — Ultimate Vanilla+, una campaña corporativa terrana original sobre X4 9.00 que utiliza las mecánicas del juego como fuente de verdad. El imperio empieza pequeño, sin recursos gratuitos; crece mediante minería, contratos, industria, logística, defensa y colonización.

## Estado documental comprobado
La rama main consultada el 10-10-2026 contenía dos documentos: docs/ENTORNO_DESARROLLO.md y docs/INVENTARIO_REPOSITORIO.md. Este último es un inventario histórico de la carpeta local; incluye recursos ignorados por Git que no deben tratarse como publicados en remoto. No hay fuente propia del mod registrada en el árbol remoto inspeccionado. Los veinte documentos aquí reunidos forman una **nueva especificación** y no acreditan que el sistema esté programado.

El entorno local, de acuerdo con ENTORNO_DESARROLLO.md, dispone de X4 9.00, X4 Forge Studio, x4cat 1.2.6, índice local, XSD y X4CodeSense. Son datos declarados en el documento; este trabajo remoto no ha accedido ni ejecutado ese equipo.

## Decisiones más recientes, de mayor prioridad
- V4.6: reservas físicas híbridas, P1/P2/P3 protegidas por ubicación.
- V4.7: entregas escalonadas de Proyecto Horizonte con reserva en origen.
- V4.8: HZ-04A (Cuenca–Horizonte) se adelanta a HZ-03.
- V4.9: dos terminales con obras equilibradas, remesas alternas.
- V5.0–5.4: operación minera M especializada, extracción directa y acopio/distribución con contingencia asistida.
- V5.5: Centro de Operaciones Mineras (COM), interfaz de mando y auditoría.
- V5.6: primer prototipo Lua/MD estrictamente de solo lectura.
- **V5.7: primer objeto a observar es una estación real y su inventario**. No se debe esperar a construir HZ-04A para probar este observador.

## Conjunto de documentos
La carpeta docs/plan contiene exactamente veinte documentos numerados. El índice de docs/README.md enlaza cada área. Los documentos 18 y 19 contienen el procedimiento de ejecución y pruebas inmediato.

## Política de verdad
Fuente nativa: el juego determina créditos, naves, NPC, almacenes, órdenes, relaciones y progreso constructivo. La capa TME solo declara pertenencias corporativas, reservas, compromisos y recomendaciones comprobables. Nunca convertir una intención o una simulación en existencias ni marcar pruebas PASS sin logs/capturas/guardados. Cuando un dato no es legible, reportar UNKNOWN o UNSUPPORTED, no cero.

## Fuentes
Decisiones dialogadas V3–V5.7; materiales aportados por el usuario (Reorientar desarrollo del mod, Integrar juego DLC y mods); docs/ENTORNO_DESARROLLO.md; docs/INVENTARIO_REPOSITORIO.md. Los materiales preliminares aportados contienen propuestas anteriores: ante divergencia prevalece la última decisión presidencial explícita.

## Aplicación V5.7 — opción A (2026-10-10)

Decisión vigente: opción A, leer una estación propia real y almacenamiento, antes de cualquier Bolo. El commit inicial `b1a3e344` contiene especificaciones, no código ni ensayos de motor. Separar APROBADO, VERIFICADO y NOT_TESTED en toda comunicación.

**Evidencias:** se evaluará conforme a [V5.7](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA COM57](19_MATRIZ_QA_EVIDENCIAS.md); esta actualización es documental, no una prueba superada.

## Ratificación de arquitectura — facción del jugador (2026-10-10)

**Política de facción ratificada (ADR-0001):** Terran Mining Empire es la propia facción nativa del jugador, sin segunda facción NPC. Los cuatro sectores fundacionales mantienen exclusividad permanente; la expansión corporativa guiada considera sectores exteriores colindantes. La finalización de los cuatro sectores no genera guerra ni desbloquea reclamaciones NPC. Véase [ADR-0001](../decisions/ADR-0001_FACCION_JUGADOR_SOBERANIA_Y_EXPANSION.md).
