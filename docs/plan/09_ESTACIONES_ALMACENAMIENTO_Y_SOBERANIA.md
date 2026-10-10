# 09. Estaciones, almacenes físicos y ampliaciones

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Inventario arquitectónico de estaciones
**PAF-01 (Fundacional):** primer centro de acopio, muelle Terran 4M10S Luxury Dock Area, almacenamiento sólido S de 100.000 m³ y administrador NPC. Inicialmente sin contenedores; no asumir que puede almacenar sustrato/carburo/micromalla.

**CMC-01 (Cuenca):** muelle 4M10S, almacenamiento sólido S y administrador; acopio territorial de mineral/silicio. Añadir módulo administrativo terrano al mismo complejo solo cuando exista plano, materiales y autorización, y verificar propiedad nativa del sector.

**CAG-01 → CIT-01 (Horizonte):** comenzar con muelle 4M10S y líquido S (100.000 m³ nominales) para gas. **No crear una segunda estación**: evolucionar la existente a CIT-01 incorporando sólidos, contenedores y módulos productivos. La identidad de objeto debe mantenerse.

## Tipos de carga
Sólidos (mineral, silicio), líquidos (gases), contenedores (componentes terranos y células energéticas). No utilizar Baldric contenedores para mineral, ni Bolo sólida para gases, ni asumir que toda nave puede transportar cualquier carga.

## Almacenes y disparadores
- S sólidos: 100.000 m³ nominales.
- M sólidos: +500.000 m³ nominales; receta candidata 24 sustrato, 50 carburo, 178 energía = 272.268 Cr de valor a precios de planificación.
- M líquidos: 500.000 m³ nominales como candidato si las entregas de gas saturan capacidad.
- Contenedores S para CIT-01; una ampliación de contenedores en PAF-01 solo si Fundacional demuestra demanda regular.
- Muelles L antes de usar Hokkaido L con CIT-01; muelle M no equivale a atraque L.

La decisión debe surgir de datos: stock saturado, rechazos a descarga, colas repetidas, objetivos P1+P2 superiores a capacidad y demanda de producción. No ampliar automáticamente por estética o fórmulas de hora completa.

## Construcción
Cada módulo debe consumirse mediante el sistema normal, con planos desbloqueados, material y constructora en condiciones válidas. En presupuestos separar coste de mercancías, planos, contratación, equipamiento y cambios de estaciones.
