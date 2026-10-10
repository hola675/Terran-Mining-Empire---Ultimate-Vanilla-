# ADR-0001 — Facción del jugador y soberanía territorial

**Fecha de decisión:** 2026-10-10  
**Estado:** APROBADO (diseño), implementación NO VERIFICADA  
**Alcance:** Terran Mining Empire — Ultimate Vanilla+, X4: Foundations 9.00

## Decisión presidencial ratificada
1. **Una sola facción operativa:** la facción **nativa del jugador** de X4. «Terran Mining Empire» es la identidad corporativa y narrativa de esa misma facción; **NO** introducir una facción NPC TME separada, vasalla, aliada ni subsidiaria.
2. **Propiedad directa:** todas las naves, estaciones, módulos y reclamaciones adquiridos jugando seguirán perteneciendo a la facción del jugador en el motor. La clasificación «patrimonio personal / corporativo» es contable/organizativa dentro de TME, **no** una transferencia de owner/faction.
3. **Gobierno corporativo:** Presidencia, Consejo, Darian, Liora, Iven y directores territoriales actúan como roles, autorizaciones, expedientes y propuestas; la ejecución usa administradores, capitanes, órdenes, asignaciones, presupuestos de estación y flotas **vanilla** donde existan APIs comprobadas. No asignar a un NPC el control real de toda la facción ni reemplazar la IA global del juego.
4. **Núcleo inalienable de cuatro sectores:** Fundacional, Cuenca Minera, Horizonte Industrial y Frontera Estratégica siguen **reservados exclusivamente a Terran Mining Empire durante toda la partida**. **Se revoca y descarta** la propuesta anterior de «fin de exclusividad» al completar cuatro sectores. No incorporar colonización o reclamación NPC sobre esos cuatro. Esta regla no implica bloqueo comercial general, inmunidad de naves/estaciones, desaparición de enemigos ni invasiones programadas.
5. **Expansión exterior:** se permite intentar **anexar sectores colindantes** con territorio del jugador por conexiones de tránsito efectivamente activas, manteniendo propiedad vanilla y coste real. La contigüidad es condición de la **expansión corporativa guiada por TME**, no una prohibición artificial de las acciones manuales del jugador fuera de dicha interfaz.
6. **Sin guerras provocadas por hitos:** obtener los cuatro sectores no inicia automáticamente una invasión, guerra, cambio diplomático ni evento de ataque. La anexión pacífica de un sector neutral requiere los módulos de reclamación reales. La conquista de sector ajeno sigue las condiciones nativas de titularidad/disputa; TME no elimina módulos de otras facciones ni regala propiedad por pulsar un botón.
7. **Prioridad intacta:** V5.7 sigue siendo solo lectura de una estación real y almacén, sin cambios a órdenes, economía, propietario, facciones o soberanía.

## Contexto técnico comprobado (documental, no ensayo X4 local)
- La documentación oficial de X Community Wiki describe órdenes, comportamientos y asignaciones para unidades propiedad del jugador: https://wiki.egosoft.com/X4%20Foundations%20Wiki/Manual%20and%20Guides/Objects%20in%20the%20Game%20Universe/Orders%2C%20Behaviours%20and%20Assignments/
- La misma wiki describe administradores de estaciones, gestión de almacenamiento, comercio y fondos: https://wiki.egosoft.com/X4%20Foundations%20Wiki/Manual%20and%20Guides/X4%3A%20Foundations%20Manual/Station%20Building%20And%20Management/
- La propiedad de sector depende de módulos reclamantes del juego. La disputa y el cambio de titularidad no se resuelven contando quién tiene más módulos: https://wiki.egosoft.com/X4%20Foundations%20Wiki/Manual%20and%20Guides/Objects%20in%20the%20Game%20Universe/Systems%2C%20Sectors%20and%20Zones/Sector%20Ownership/
- Egosoft anunció mejoras de IA, órdenes prioritarias y gestión de imperios en 9.00: https://www.egosoft.com/news/archive/2026June_en.php

## Distinciones técnicas obligatorias
- **Reservado** ≠ **reclamado en motor**. Antes de construir un módulo administrativo válido, no decir que el juego ha adjudicado efectivamente el sector al jugador. No inventar soberanía con un simple tag TME.
- **Exclusividad permanente** del núcleo ≠ soberanía vanilla totalmente intocable: si se destruyen todos los módulos reclamantes vanilla, la propiedad puede cambiar o quedar sin dueño. Para cumplir la exclusividad total hará falta **excepción mod limitada a los cuatro sectores**, que impida/neutralice técnicamente la reclamación NPC sin afectar a otros sectores. Diseño de adaptador pendiente: investigar si restricciones de creación/construcción bastan y qué ocurre tras destrucción, SAVE/LOAD y DLC/mods; no asumir APIs disponibles ni modificar/modificar mediante spawns destructivos otras estaciones.
- **Colindancia** para TME se define como una conexión de salto/acelerador transitable y aprobada en el grafo activo. Vanilla no requiere necesariamente contigüidad para que el jugador construya o reclame; la UI corporativa no bloqueará directamente acciones vanilla.
- **Solo Neptuno conecta al exterior** en el grafo actualmente aprobado de los cuatro sectores, y es territorio del Protectorado Terrano. No prometer anexión exterior pacífica inmediata si el único vecino externo pertenece a otra facción. Para una expansión pacífica se necesita un neutral adyacente accesible, cambiar estrategia diplomática/geográfica o investigar nuevas conexiones físicas con costes reales y QA.
- **No forzar hostilidades:** el juego podrá tener peligros y ataques naturales; el mod no fabricará ataques como castigo por poseer cuatro sectores.

## Arquitectura lógica acordada
~~~text
Facción nativa del jugador (único propietario técnico)
  ├── Patrimonio personal del fundador (clasificación TME)
  ├── Activos corporativos TME (clasificación TME)
  │    ├── Flotas y sus comandantes vanilla
  │    ├── Estaciones, gerentes, fondos y comercios vanilla
  │    ├── Consejo / directores / permisos (metadatos y propuestas)
  │    └── Centro de Mando Imperial (lectura primero)
  ├── Cuatro sectores fundacionales exclusivos (protección TME específica)
  └── Sectores exteriores anexados mediante reclamación nativa
~~~

## Decisiones descartadas explícitamente
- No facción TME independiente, NPC subordinada o vasallaje como eje de arquitectura.
- No migración de owner de naves/estaciones del jugador a una segunda facción.
- No desbloqueo de vulnerabilidad de reclamación NPC sobre los cuatro sectores al completar la campaña.
- No invasión, guerra o reequilibrio de relaciones automático por consolidación del imperio.

## Pruebas de aceptación futuras
| Caso | Resultado requerido | Estado |
|---|---|---|
| FAC-01 | La nave/estación TME conserva owner nativo del jugador tras clasificación económica | NOT_TESTED |
| FAC-02 | Orden manual del jugador prevalece sobre propuestas de director TME | NOT_TESTED |
| FAC-03 | IA vanilla minería/comercio/defensa continúa operativa sin override | NOT_TESTED |
| TER-01 | La reclamación nativa del núcleo usa centro administrativo real | NOT_TESTED |
| TER-02 | Ninguna facción NPC puede reclamar permanentemente los cuatro sectores | NOT_TESTED |
| TER-03 | Destrucción de módulos, renombrado y SAVE/LOAD no crean reclamos falsos | NOT_TESTED |
| TER-04 | Sector exterior neutral adyacente puede reclamarse legalmente con recursos reales | NOT_TESTED |
| TER-05 | Sector exterior reclamado por NPC exige resolver disputa vanilla; sin anexión gratis | NOT_TESTED |
| TER-06 | Culminar cuatro sectores no dispara guerra, incursiones o cambios diplomáticos scripted | NOT_TESTED |

**Nota de verdad:** este ADR sustituye las propuestas del informe exploratorio de facción híbrida y exclusividad temporal. Las referencias citadas son guías y anuncios, no una certificación del adaptador de protección de sectores en una partida X4 9.00.
