# 11. Minería, flotas M, pilotos y especialización

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Modelo V5.1–V5.2
Dos líneas diferenciadas de **mineral** y **silicio**, más función de distribución de carga sólida cuando exista la nave. Las Bolos del organigrama representan funciones, no un listado de activos confirmados.

Bolo (Mineral) candidata: 8.800 m³ sólidos; Bolo (Gas): 10.000 m³ de gases; Baldric: 10.700 m³ de contenedores; Hokkaido Mineral L: 51.300 m³ sólida, condicionada a infraestructura y equipamiento L. Todas las cifras y precios deben verificarse contra el juego instalado antes de inversiones.

## Identidades
TME-MIN-001 fue la primera Bolo prevista; TME-LOG-001 es una función de distribución candidata (minera sólida, no transporte genérico). TME-CM-MIN-002 para especialidad silicio cuando se adquiera/redistribuya una segunda unidad. Solo registrar un objeto si el motor realmente lo contiene. Kopis privada y Kukri de Darian fuera de inventario corporativo por defecto.

## Asignaciones vanilla candidatas
- Mine for Commander → CIT-01 para minería directa de silicio/mineral en Cuenca con descarga industrial.
- Mine for Commander → CMC-01 para acopio territorial.
- Trade for Commander → CIT-01 o CMC-01 para distribución de sólidos **con una minera capaz de llevar sólidos**, según prueba de ofertas.
- Limitar mercancías de cada subordinado a mineral o silicio si el control de 9.00 existe y funciona en ese contexto.

Las asignaciones precisas, el alcance del administrador, habilidad del piloto y navegación por una puerta creada por el mod **son hipótesis pendientes de certificación**, no promesas.

## Capacidad por recurso
Piloto CIT-01: mineral 4.000 u/h (40.000 m³/h), silicio 6.600 (66.000 m³/h); aproximadamente cinco cargas de Bolo para mineral y ocho para silicio si se separan mercancías. Una nave no puede ser simultáneamente extractora completa y distribuidora completa. Caudal = carga media × 60 / tiempo completo de ciclo (minutos de juego).

## Personal
Cada capitán y administrador es un NPC real con habilidades y moral observadas. No otorgar ascensos, estrellas, salarios o permisos mágicos. Registrar IDs persistentes, subordinación, orden y últimos eventos. Ante destrucción: pérdida real y archivado de expediente.

## Inversión
Reorganización primero, compras después de medir cuello de botella, tiempo y capacidad; comprar nueva Bolo solo con precio equipado, tripulación y aprobación de Presidencia.
