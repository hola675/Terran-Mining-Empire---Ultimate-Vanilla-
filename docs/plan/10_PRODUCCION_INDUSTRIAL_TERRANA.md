# 10. Industria terrana y balance de CIT-01

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Estrategia aprobada
CIT-01 es la evolución de CAG-01, no estación duplicada. Añadir micromalla, solar, carburo y sustrato por etapas. Todos los módulos, planos e insumos serán reales. Recetas/IDs se basan en los diseños y fichas usadas previamente, **requieren comparación con el catálogo de la instalación 9.00 antes de implementarse**.

## Recetas de referencia
| Línea | Ciclo | Entradas por ciclo | Salida |
|---|---|---|---|
| Micromalla metálica | 3 min | 50 mineral, 130 helio, 50 energía | 190 micromalla |
| Carburo de silicio | 5 min | 300 silicio, 400 metano, 2 micromalla, 200 energía | 48 carburo |
| Sustrato computrónico | 10 min | 3.000 mineral, 3.000 silicio, 2.000 hidrógeno, 4.000 energía | 98 sustrato |
| Solar terrano | 1 min | Generación sujeta a radiación y juego | referencia 50 energía/min a 100 % |

## Capacidades nominales
A producción continua de micromalla: 1.000 mineral + 2.600 helio + 1.000 energía → 3.800 micromalla por hora. Carburo: 3.600 silicio + 4.800 metano + 24 micromalla + 2.400 energía → 576 carburo/h.

Sustrato a seis ciclos por hora: 18.000 mineral + 18.000 silicio + 12.000 hidrógeno + 24.000 energía → 588 sustrato/h. Estos son valores nominales a 100 % bajo supuestos de recetas; la partida puede variar por bonus, empleados, radiación y otros factores.

## Escenario piloto de consolidación
**Un ciclo de sustrato/h en promedio**, otras dos líneas nominales. Insumos de todos los procesos: mineral 4.000 u/h; silicio 6.600; helio 2.600; metano 4.800; hidrógeno 2.000; energía 7.400. Son 106.000 m³/h de sólidos y 56.400 m³/h de gases con volúmenes aprobados de las mercancías. No existe en vanilla una orden garantizada de 'un ciclo por hora'; el ritmo se obtiene mediante abastecimiento e historial observado.

## Energía
Con dos solares al 100 % nominal: 6.000 celdas/h. El piloto gasta 7.400: déficit teórico 1.400/h que debe compensarse con compra, más paneles aprobados, stock o reducción de ritmo. No asumir 100 % real en todo sector.

## Prueba obligatoria
Producir primer lote real de sustrato, ver su ingreso de inventario y consumo de entradas, conciliar 98 unidades nominales con posibles modificaciones efectivas. No fabricar wares para comprobar UI.

## V5.7 — opción A: aplicación al dominio

No derivar rendimientos de fábrica de un snapshot de almacenamiento. CIT-01 continúa pendiente; ninguna receta, ciclo o mercancía se modifica.

**Estado:** especificación, aún sin pruebas X4 ejecutadas. Aplicar [protocolo V5.7](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [matriz COM57](19_MATRIZ_QA_EVIDENCIAS.md).
