# 20. Roadmap integrado, riesgos y decisiones aprobadas

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Roadmap vigente
| Etapa | Contenido | Estado |
|---|---|---|
| V3–V4.3 | Fundación, sectores, CIT-01, producto sustrato | Diseño aprobado; juego sin certificar |
| V4.6 | Reservas híbridas P1/P2/P3 | Diseño aprobado |
| V4.7 | SIH entregas escalonadas | Diseño aprobado |
| V4.8 | Prioridad HZ-04A sobre HZ-03 | Diseño aprobado |
| V4.9 | Construcción equilibrada de ambos extremos | Diseño aprobado |
| V5.0–V5.1 | Optimización industrial y Bolos especializadas | Diseño aprobado |
| V5.2 | Sistema minero híbrido | Diseño aprobado |
| V5.3 | Primero certificar minería directa CIT-01 | Procedimiento aprobado |
| V5.4 | Recuperación logística asistida / CMC-01 | Diseño aprobado |
| V5.5 | COM con seis vistas | Diseño funcional aprobado |
| V5.6 | Lua/MD solo lectura | Arquitectura aprobada |
| **V5.7** | **Primer objeto real: estación y almacenamiento** | **Próximo vertical slice, NO IMPLEMENTADO** |
| Posterior | Bolo/NPC, COM análisis, autorizaciones, HZ-04A y HZ-03 | Condicionado a QA |

## Bloqueos críticos
B1 código propio aún ausente; B2 ruta Lua↔MD y API de inventarios no validada; B3 separación financiera jugador/empresa no certificada; B4 módulos y recetas necesitan confirmar IDs 9.00; B5 creación/pareja de puertas requiere adaptador propio; B6 HZ-01 y HZ-02 son prerequisitos físicos de HZ-04A; B7 incompatibilidad potencial con mods de referencia; B8 contabilidad save/load sin duplicaciones; B9 historial de 20 misiones no detallado íntegramente.

## Orden de trabajo recomendado
Primero documentar y certificar lectura estación vanilla en entorno local; después lectura de Bolo y piloto; después COM multisector y reservas, sin conceder permisos de escritura. Paralelamente, en rama aislada, prototipar puertas y estaciones de los sectores; nunca declarar corredor operativo por solo existir en un mapa de diseño.

## Gestión de decisiones
No preguntar de nuevo decisiones A/B/C ya resueltas. Si aparece una discrepancia entre documentos previos y la última decisión presidencial explícita, preservar el historial y marcar la corrección. Datos de fichas y mod IDs son CANDIDATO hasta verificación x4cat/XSD. No elevar a 'VERIFICADO' un cálculo de plan ni una fuente web sin una prueba ejecutada.

## Criterio de entrega a agentes
Una tarea de implementación debe citar objetivo, alcance, precondiciones, invariantes Vanilla+, archivos admitidos, contratos de datos, tests, logs y rollback. Pedir commit/PR y resumen español con evidencias, no mera afirmación de éxito.

## V5.7 — ratificación y criterios operativos (2026-10-10)

V5.7 permanece en especificación hasta STATION_PASS real. Después observar Bolo/piloto, múltiples estaciones y solo luego reservas y autorizaciones. No iniciar HZ-04A para resolver bloqueos de lectura COM.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).
