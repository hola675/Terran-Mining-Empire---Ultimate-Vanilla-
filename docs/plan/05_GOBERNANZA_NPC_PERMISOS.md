# 05. Consejo ejecutivo, NPC reales y delegaciones

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Principio
La corporación es un sistema administrativo; la nave o estación sigue teniendo los comandantes que reconoce X4. Nunca confundir un 'director territorial' (rol del mod) con el NPC administrador de estación que gobierna subordinados vanilla.

## Cadena de autoridad
Presidente → Consejo (Liora logística, Iven industria, Darian seguridad) → directores territoriales → administradores de estación → capitanes y tripulaciones NPC. Cada nivel requiere existencia del personaje y vínculo verificable. Si falta un personaje, el rol está VACANTE: no inventar biografía u órdenes en su nombre.

## Permisos
| Operación | Consejo | Presidente |
|---|---|---|
| Leer estados y generar diagnóstico | Permitido | Permitido |
| Recomendar cambio de ruta o comandante | Permitido | Permitido |
| Ajustes menores dentro de delegación verificada | Solo tras certificar API | Decide delegación |
| Interrumpir una orden prioritaria | No | Acción manual |
| Comprar nave, módulo, estación o puerta | Solicitar presupuesto | Autorizar |
| Usar mercancía P1 para destino diferente | Solicitar excepción | Autorizar |
| Usar FIE | Solo política limitada | Aprobar excepción |
| Cambiar relaciones/facciones | Ninguna atribución implícita | Según progreso legítimo |

## Expedientes
Toda propuesta tiene ID, autor, origen, evidencia, activo afectado, riesgo, importe, permiso necesario, estado y resultado. 'Aprobado' no significa 'aplicado'. Si la orden vanilla cambia manualmente, actualizar propuesta; jamás restaurarla en silencio.

## Persistencia personal
Guardar IDs reales de NPC, nave y puesto; el nombre visible puede cambiar. Ante venta, destrucción, despido o falta de acceso, marcar MISSING_OBJECT y detener recomendaciones. Darian/Kukri y Kopis personal fuera de compras corporativas, salvo incorporación explícita y verificable.

## Garantía
No simular nóminas periódicas ni niveles de habilidad que X4 no cobre/otorgue. Evaluar salarios o carreras solo si una mecánica concreta existe o se implementa de forma explícita y balanceada.

## V5.7 — opción A: aplicación al dominio

Leer únicamente el administrador real. Una referencia ausente no permite crear, reasignar ni ascender NPC.

**Estado:** especificación, sin validación de motor. Referencias: [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [pruebas](19_MATRIZ_QA_EVIDENCIAS.md).

## Ratificación de arquitectura — facción del jugador (2026-10-10)

**Facción única:** Darian, Liora, Iven, Consejo y directores son cargos dentro de las propiedades del jugador. Operan con asignaciones, gerentes y comandantes vanilla cuando existan autorizaciones y métodos comprobados; no se crean facciones subordinadas, ni un NPC se convierte en dueño de propiedades corporativas. Las decisiones presidenciales prevalecen. Ver [ADR-0001](../decisions/ADR-0001_FACCION_JUGADOR_SOBERANIA_Y_EXPANSION.md).
