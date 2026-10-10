# 06. Tesorería corporativa y contabilidad verificable

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Regla central
**Cartera personal y presupuesto empresarial son conceptos separados**, pero X4 tiene flujos nativos que pueden llegar a la cartera del jugador. La partición financiera virtual **no está resuelta técnicamente**; no publicar un saldo preciso de la compañía hasta certificar conciliación.

## Libros conceptuales
- Dinero real disponible: cartera nativa menos pertenencia personal y compromisos validados, más saldos de estaciones cuando corresponda y **sin contarlos dos veces**.
- Saldos asignados a estaciones: fondos operativos reales, pueden necesitarse para ofertas de comercio.
- Envolventes departamentales: límites internos, **no monedas adicionales**.
- FIE: Fondo Imperial de Emergencias, restringido a continuidad menor y excepciones según doctrina; no fuente ordinaria para minería, astilleros o puertas.
- Inventarios: activo no líquido; valor económico de mercancías propias no equivale a créditos disponibles.

## Reglas de conciliación
Una compra a NPC genera gasto externo real. Una venta a NPC genera ingreso externo solo tras observar cobro. Una transferencia entre estaciones propias cambia localización y eventualmente saldos internos, **no crea beneficio consolidado**. El costo de oportunidad de insumos fabricados internamente forma parte del análisis de inversión, pero no se registra como segundo desembolso.

## Política de autorizaciones
Toda inversión debe tener coste equipado/completo, proveedores reales, plan de financiación, impacto en P1/P2, capital libre, coste de oportunidad, riesgo y responsable. Compras de mineras M, Hokkaido L, almacenes, muelles L, defensas y obras de Horizonte requieren decisión presidencial salvo delegación probada.

## Ejemplo HZ-04A
600 sustrato × 8.280 + 1.200 carburo × 1.414 + 4.000 micromalla × 50 + 16.000 energía × 16 = **7.120.800 Cr de referencia de materiales**. Dos constructoras NPC a 50.000 Cr cada una: subtotal provisional **7.220.800 Cr**. No es oferta de mercado ni coste final; planos, transporte, seguridad y otras tarifas faltan. Estos precios son supuestos de planificación y deben contrastarse en la partida.

## QA financiero
No gastar dinero privado inadvertidamente; no duplicar las estaciones en el consolidado; controlar cobros y pagos efectivos; audit trail idempotente en guardar/cargar. Marcar FINANCE_PARTIAL hasta resolver la separación de cartera y cuentas.
