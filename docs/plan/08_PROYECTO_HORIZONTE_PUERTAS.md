# 08. Proyecto Horizonte: puertas, obras y corredor HZ-04A

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Propósito
Construir nuevas puertas bidireccionales como inversiones físicas propias: materiales, transporte, almacenamiento de construcción, constructoras, créditos reales, examen del objeto final y persistencia. Las puertas **no son módulos de estación vanilla**; crear/convertir objetos dinámicos necesita prototipo MD y adaptador de puertas.

## Primeras obras
HZ-01 abre Fundacional–Cuenca (siete hitos narrativos integrados en la campaña). HZ-02 enlaza Fundacional–Horizonte. HZ-04A, ahora prioritaria, enlazará Cuenca–Horizonte. Si los dos primeros accesos no existen y no funcionan, HZ-04A está BLOQUEADA para ejecución.

## Receta piloto HZ-04A: dos extremos
| Material | Total | Cuenca | Horizonte | Volumen total |
|---|---:|---:|---:|---:|
| Sustrato | 600 | 300 | 300 | 30.000 m³ |
| Carburo | 1.200 | 600 | 600 | 24.000 m³ |
| Micromalla | 4.000 | 2.000 | 2.000 | 4.000 m³ |
| Energía | 16.000 | 8.000 | 8.000 | 16.000 m³ |
Total mercancías 74.000 m³ y **7.120.800 Cr** de valor orientativo con precios adoptados. No es receta oficial de Egosoft ni autorización presupuestaria final.

## Construcción equilibrada
Dos emplazamientos HZ-04A-CM y HZ-04A-HI, cada uno con almacenamiento temporal y constructora compatible. Cuatro remesas por extremo, alternando CM-R01, HI-R01 … CM-R04, HI-R04. Cada remesa: 75 sustrato, 150 carburo, 500 micromalla y 2.000 energía = 9.250 m³, 890.100 Cr de valor de planificación. Una Baldric de 10.700 m³ es candidata a transportar esas remesas, si está adquirida y equipada; 8 viajes cargados de referencia, **no 8 naves**.

## Gates de obra y activación
Validar fondos y reservas, dos almacenes de construcción, materiales efectivamente entregados, constructora real por obra, consumo una sola vez, ID de ambos objetos finales, enlace bidireccional, navegación manual e IA, retorno, guardar/cargar y recuperación de fallos parciales. No enlazar prematuramente ni generar una segunda puerta al reintentar tras un crash.

## Precedentes y propiedad intelectual
Inix Gate Network Control y Gate Manage API son precedentes externos a estudiar, **no dependencias instaladas/avaladas ni código reutilizable automáticamente**. Comprobar licencia, compatibilidad y alternativas en X4 9.00 antes de adoptar adaptador.

## V5.7 — opción A: aplicación al dominio

HZ-04A, construcción de puertas y Proyecto Horizonte no bloquean la lectura de estación. No activar conexiones ni modificar universo durante las pruebas COM57.

**Estado:** especificación, aún sin pruebas X4 ejecutadas. Aplicar [protocolo V5.7](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [matriz COM57](19_MATRIZ_QA_EVIDENCIAS.md).

## Ratificación de arquitectura — facción del jugador (2026-10-10)

Las siete conexiones previstas de los cuatro sectores no cambian. Construir una puerta NO transfiere propiedad territorial ni inicia hostilidades. El núcleo sigue reservado exclusivamente al jugador durante toda la partida. La apertura de rutas exteriores para expansión solo podrá proponerse con financiación, ingeniería y comprobación de rutas reales; tampoco se inventarán conexiones gratuitas a sectores neutrales. [ADR-0001](../decisions/ADR-0001_FACCION_JUGADOR_SOBERANIA_Y_EXPANSION.md).
