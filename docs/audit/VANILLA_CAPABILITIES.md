# Capacidades vanilla y desarrollo propio

**Revisión:** 2026-10-10. **Objeto:** delimitar el alcance; no certificar APIs ni sustituir [los principios Vanilla+](../plan/02_VISION_Y_REGLAS_VANILLA_PLUS.md).

El manual oficial describe managers que coordinan minería/comercio y asignación de almacenamiento, con presupuestos, ofertas y controles en Logical Station Overview. [Station Building And Management](https://wiki.egosoft.com/X4%20Foundations%20Wiki/Manual%20and%20Guides/X4%3A%20Foundations%20Manual/Station%20Building%20And%20Management/?language=en). El anuncio 9.00 confirma órdenes prioritarias y un sistema de recursos mineros localizado y dinámico. [Lanzamiento de Empire Update](https://www.egosoft.com/news/archive/2026June_en.php). Estas fuentes describen capacidades del juego, no un PASS del prototipo TME.

| Necesidad | Responsabilidad vanilla | Aportación propia prevista | Investigación necesaria |
|---|---|---|---|
| Minería y comercio de estación | Manager, subordinación, órdenes, ofertas | Observar cuellos de botella y recomendar | Comparar station/UI y datos accesibles; no reemplazar AI |
| Almacenamiento | Existencias y capacidad reales | Snapshot COM con calidad/fecha/origen | Firmas exactas para sólido, mineral y silicio; V5.7 |
| Prioridad del jugador | Órdenes prioritarias nativas 9.00 | Respetarlas en toda recomendación/automatización futura | Detectar estado sin sobrescribir colas |
| Construcción | Plan, constructoras, build storage y materiales | Expedientes, fases y conciliación SIH | Cotejar eventos y referencias persistentes |
| Presupuesto | Saldos y presupuesto de estación | Contabilidad corporativa y autorizaciones | Conciliar, sin crear ni duplicar créditos |
| Soberanía | Reclamación que reconoce el motor | Reglas de los cuatro territorios TME | Mecanismo acotado contra reclamación NPC |
| Progreso y personajes | Objetos/NPC y acontecimientos reales | Consejo, campaña y continuidad narrativa | Identidad de Darian/Liora/Iven y save/load |
| Red de puertas | Mapas y estructuras del juego | Proyecto Horizonte con obras verificables | Adaptador, materiales y persistencia; laboratorio separado |
| Mando corporativo | Propiedad y controles originales | COM, recomendaciones y registro de decisiones | Aportar información sin crear otra autoridad de órdenes |

La propiedad de sector se debe contrastar con las reglas nativas, no con un banner o una cuenta de módulos supuesta. [Sector Ownership oficial](https://wiki.egosoft.com/X4%20Foundations%20Wiki/Manual%20and%20Guides/Objects%20in%20the%20Game%20Universe/Systems%2C%20Sectors%20and%20Zones/Sector%20Ownership/?language=en).

## Qué demuestran las referencias

Logistics Guidance, Station Trader Multiorder, GS Fleet Trade y otros modifican/proponen mecanismos próximos al dominio logístico; conservarlos para comparar con el comportamiento del juego antes de integrar. El nombre interno de Prospect Missions es **Prospect Missions Tweak**: no basta para inferir que introduce una función nueva ausente en vanilla. La comparación concreta con Prospect del juego queda abierta; el changelog completo del foro no pudo leerse por su control de acceso automatizado.

El autor de Inix documenta dos modos: colocación instantánea predeterminada y construcción con recursos/constructoras. Para Horizonte solo estudiar el segundo en un save separado. [Modo de construcción de Inix](https://www.nexusmods.com/x4foundations/mods/2319). Que el laboratorio tenga ese mecanismo no aprueba copiarlo ni certificar su ajuste a nuestros costes.

## Contrato de V5.7

La extensión propia debe limitarse a leer una estación real, manager y almacenamiento; conservar la asociación y distinguir cero, desconocido, error y no soportado. Toda firma Lua/MD requiere cotejo con XSD/fuente vanilla y ensayo. El índice local de 461.598 archivos registra solo nueve catálogos base: las consultas de IDs/recetas terranas también necesitan los catálogos de Cradle of Humanity. La documentación de almacenamiento no demuestra un bloqueo físico de reservas ni un sistema contable implementado.

Aceptar el siguiente incremento solo tras cumplir los [gates de estación real](../plan/18_V57_ESTACION_REAL_ALMACENAMIENTO.md). No hace falta añadir gobernadores, puertas, rescate, economía civil ni reemplazos de minería para ejecutar ese primer ensayo.
