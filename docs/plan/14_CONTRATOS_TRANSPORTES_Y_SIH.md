# 14. Contratos, entregas y SIH de Proyecto Horizonte

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## SIH — Sistema Imperial de Suministros de Horizonte
Submódulo del COM. Ingeniería (Iven) define receta y estado de obra; Liora encuentra stock P3 o reserva P1 válida y propone despacho; Darian evalúa riesgo; Presidente autoriza inversión; transportista vanilla realiza carga/viaje/descarga; Tesorería concilia valor y pagos externos.

## Entregas escalonadas V4.7
El destino debe existir y ser alcanzable, el contrato debe identificar el origen físico y el almacén de obra correcto, y la carga solo puede salir cuando exista nave compatible. Para HZ-04A construir equilibradamente los dos extremos con cuatro remesas de referencia por lado; ningún porcentaje de material recibido implica mismo porcentaje de construcción terminada.

## Contrato mínimo
contract_id estable; project_id; terminal_id; ware_id; origin_object_ref; target_buildstorage_ref; requested_units; reserved_units; loaded_units; delivered_units; consumed_units; ship_ref; order_ref si es legible; money_commitment; authorizer; status; revision; evidence.

## Estados
PROPOSED → AUTHORIZED → RESERVED → ORDER_OBSERVED → LOADED → IN_TRANSIT → DELIVERED_VERIFIED → RECONCILED → CLOSED; también BLOCKED, CANCELLED y LOSS. Las transiciones solo ocurren por observaciones confiables. Tras guardar/cargar no volver a emitir un despacho confirmado.

## Diferencia operativa
Almacén ordinario de estación mantiene recursos de operación. Almacén de construcción mantiene materiales de un plan de obra; no asumir que dejar 600 sustratos en CIT-01 ya abastece una puerta. Las obras de puertas son personalizadas: su integración con construcción nativa requiere prototipo.

## Precedentes
X4 Mission Director/UI; Gate Manage API y mods de puertas como referencias externas sujetas a licencia y validación. No imponer dependencias externas sin aprobación. Si obra consume un material, registrar consumo real y no duplicar salidas.

## Incidencias
Ruta inaccesible; mercancía reservada a otro proyecto; precio no compatible; constructora ausente; bodega incompatible; daño; salvado a mitad de viaje; evento repetido; endpoint remoto inaccesible. Fallo parcial de puerta debe generar BLOCKED, no recreaciones automáticas.
