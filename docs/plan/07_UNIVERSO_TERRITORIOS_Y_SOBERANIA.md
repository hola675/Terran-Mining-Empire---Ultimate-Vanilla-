# 07. Universo, cuatro territorios y soberanía nativa

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Sectores propuestos
1. **Fundacional**: centro político/comercial con PAF-01; salida exterior hacia Neptuno.
2. **Cuenca Minera**: mineral/silicio, CMC-01 y reclamación territorial.
3. **Horizonte Industrial**: gases y CIT-01, núcleo fabril.
4. **Frontera Estratégica**: expansión y seguridad, pendiente de apertura.

## Siete conexiones finales bidireccionales
Externa Neptuno–Fundacional y seis internas (grafo completo de los cuatro sectores):
HZ-01 Fundacional–Cuenca, HZ-02 Fundacional–Horizonte, HZ-03 Fundacional–Frontera, HZ-04A Cuenca–Horizonte, HZ-04B Cuenca–Frontera, HZ-04C Horizonte–Frontera.

## Cambio de orden aprobado
**HZ-04A se adelanta a HZ-03**. El cuarto sector permanece previsto pero la prioridad siguiente es cerrar el corredor productivo Cuenca–Horizonte. Las puertas ya descritas no están implementadas; comprobar objetos y navegación mediante pruebas reales.

## Soberanía
Para Cuenca se eligió incorporar un centro administrativo terrano a la estación CMC-01, en lugar de un edificio separado. Referencia candidata: module_ter_def_claim_01, sujeto a validación contra catálogo local 9.00. Ser dueño de una estación o tener una bandera corporativa **no prueba** ser propietario nativo de un sector. Comprobar que el juego adjudica la propiedad tras construir el módulo válido.

Control de nuevas estaciones NPC, restricciones de paso y tránsito de otras facciones son tres problemas independientes. No borrar estaciones ajenas ni asumir que construir una puerta da control total sobre flotas de NPC.

## Diseño espacial
La ubicación de puertas requiere mapa, aproximaciones despejadas, orientación, ausencia de conflictos físicos, rutas IA y manuales seguras. No inventar coordenadas hasta tener geometría real. El extremo remoto de una puerta hacia sector inaccesible necesita mecanismo de obra legalmente abastecible; bloquear la activación mientras no se resuelva.

## V5.7 — opción A: aplicación al dominio

La estación del ensayo puede residir en un sector vanilla existente; no se crearán sectores ni puertas para certificar V5.7.

**Estado:** especificación, sin validación de motor. Referencias: [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [pruebas](19_MATRIZ_QA_EVIDENCIAS.md).

## Ratificación de arquitectura — facción del jugador (2026-10-10)

**Decisión definitiva:** Fundacional, Cuenca Minera, Horizonte Industrial y Frontera Estratégica son siempre territorio reservado exclusivamente a la facción del jugador/TME. Se descarta liberar su reclamación a NPC al completar los cuatro. El privilegio NO regala estaciones, evita ataques naturales ni implica propiedad nativa antes de construir módulo reclamante. La exclusividad permanente tras la destrucción de módulos requiere investigar un adaptador restringido a los cuatro sectores; todavía NO VERIFICADO. Fuera del núcleo, TME podrá proponer anexiones de sectores colindantes por conexiones activas, reclamados con mecánica nativa y costo real. Neptuno es el único vecino exterior inicial y pertenece a TER: la anexión pacífica exterior no está garantizada. [ADR-0001](../decisions/ADR-0001_FACCION_JUGADOR_SOBERANIA_Y_EXPANSION.md).
