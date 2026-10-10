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
