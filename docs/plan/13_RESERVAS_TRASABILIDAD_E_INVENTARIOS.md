# 13. Reservas P1/P2/P3 y trazabilidad física

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Política aprobada V4.6
Reservas híbridas por ubicación física: minerales prioritariamente en Cuenca; gases/productos terminados en CIT-01; Fundacional almacena sólidos y coordina comercio. La reserva financiera no traslada mercancía; solo un cargamento real y descarga la cambia de ubicación. Los insumos de construcción tienen su propio almacén de obra separado del operacional.

## Categorías
P1 compromiso firme de proyecto autorizado, no comerciable hasta liberación formal. P2 buffer de continuidad productiva, ajustable con criterio y delegación. P3 excedente libre, vendible o despachable. Previsiones de extracción no son inventario. Una reserva P1 asociada a un contrato no se resta dos veces.

## Identidad de reserva
reserve_id, ware, owner_corporation, physical_location_ref, quantity_units, priority, purpose, project_id, created_at_game_time, status, source_snapshot, policy_revision. No confiar en nombre de estación como referencia primaria.

## Estados de mercancías
En estación A; cargada en nave; en tránsito; descargada en estación B/almacén de construcción; consumida; destruida; o cantidad desconocida. Una unidad solo pertenece a **un único contenedor físico a la vez**. Si cambia la situación y no hay datos de calidad suficiente, bloquear conclusiones.

## Invariantes
free = max(0, observed_stock - unique_protected_commitments) por mercancía y ubicación. Si compromisos superan stock, reportar reserva no cubierta (no truncar silenciosamente la deuda contractual). Verificar físicamente cantidades antes de ofertas y después de entregas; la regla vanilla por sí sola no impone un candado transaccional perfecto.

## Cobertura P2
Meta orientativa = consumo observado × horas de cobertura deseadas, sujeto a almacenamiento y prioridades aprobados. Diferenciar cobertura objetivo, cobertura realmente disponible y faltante. Un objetivo no es una existencia.

## Pruebas
Venta manual durante reserva, dos solicitudes simultáneas, pérdida de nave cargada, consumo en obra, carga/descarga parcial, falla en guardado, borrado de proyecto, saldo interno sin beneficio externo, vuelta atrás sin mercancía ficticia.
