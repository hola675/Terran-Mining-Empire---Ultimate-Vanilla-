# Responsabilidad de sistemas y permisos

**Revisión:** 2026-10-10. **Estado:** contrato de diseño candidato que concreta los invariantes ya aprobados. No implementa automatización ni concede permisos de escritura nuevos.

| Sistema | Responsable de ejecutar | TME V5.7 | Capas externas que deben aislarse |
|---|---|---|---|
| Minería, producción y comercio ordinario | Motor X4 / manager vanilla | Observar | Mods de AI, órdenes comerciales y economy overhauls |
| Órdenes manuales/prioritarias | Jugador y motor | Respetar, sin restaurar colas | Mimic, Replicate, GS Fleet Trade, Multiorder, KUDA |
| Construcción y financiación | Jugador / mecanismos nativos | Leer estado si hay API validada | Planificadores, procurement y gobernadores |
| Existencias físicas | Inventario del motor | Snapshot informativo | Transferencias repetidas y reservas con promesa de bloqueo |
| Tesorería | Saldos reales del juego | Registro propio conciliable | Watchdog, procurement, PFR y economía civil |
| Gobernanza | Presidente; delegación aprobada | Recomendaciones futuras | Player Feudal Realm y Star Command como sistemas alternativos |
| Menús/callbacks | Estrategia de UI elegida | Menú propio de lectura | UIX y sustituciones `subst` de otros mods |
| Personajes y rescate | Entidades reales y diseño de campaña | Sin crear ni reemplazar NPC | Living Crew, Escape Pod, Rescue Rangers |
| Territorios y puertas | Motor + adaptador propio autorizado | Fuera del observador | Gate API e Inix en laboratorio |

## Matriz mínima de decisiones

| Acción | Operación vanilla existente | Director/Consejo TME | Autorización presidencial |
|---|---|---|---|
| Leer estación, manager o ware | Permanece en el motor | Puede proponer/consultar tras validar API | Alcance de lectura V5.7 ya aprobado |
| Publicar snapshot o expediente propio | Sin mutar operación vanilla | Admitido en namespace propio | Contrato V5.7; persistencia por verificar |
| Recomendar presupuesto, compra o ruta | El jugador decide | Propuesta identificada, aún sin executor | Necesaria antes de cualquier aplicación futura |
| Comprar nave/módulo, transferir ware/créditos | Mecanismo legítimo original | Prohibido en V5.7 | API, alcance y permiso específico posteriores |
| Cambiar orden o subordinación | Control del jugador | Prohibido en V5.7 | Nunca desplazar prioridad/manual por defecto |
| Cambiar propietario/puerta/NPC | Fuera del observador | Prohibido en V5.7 | Laboratorio, decisión técnica y QA separados |

Referencia de autoridad: [gobernanza](../plan/05_GOBERNANZA_NPC_PERMISOS.md), [tesorería](../plan/06_TESORERIA_Y_CONTABILIDAD.md), [arquitectura](../plan/16_ARQUITECTURA_LUA_MD_Y_CODIGO.md). La autonomía vanilla existente no se convierte en una nueva autorización TME; los cambios siguen fuera del primer prototipo.

## Contratos que faltan para un executor futuro

Solicitud con ID, objeto y estado observado → propuesta → autorización con alcance/presupuesto/caducidad → aplicación por mecanismo vanilla → verificación y conciliación. Al guardar/cargar, una autorización no debe ejecutar de nuevo una compra o entrega ya aplicada. Si el objeto desaparece o una orden manual cambia el contexto, revalidar o cancelar; no reconstruir objetos ni restaurar órdenes automáticamente.

Para cada dominio seleccionado, registrar un responsable de escritura y sus APIs; dos mods que controlan ese dominio requieren una decisión explícita de integración. Esta tabla sirve para rechazar combinaciones no justificadas, no para certificar que dos diffs compatibles sintácticamente respetan la autoridad presidencial.
