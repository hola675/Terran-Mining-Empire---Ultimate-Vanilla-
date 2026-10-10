# Terran Mining Empire — Ultimate Vanilla+

**Proyecto de una experiencia corporativa terrana Vanilla+ para X4: Foundations 9.00.** Desde una pequeña explotación minera hasta un imperio industrial y territorial, con créditos, naves, NPC, mercancías, estaciones y construcciones realmente obtenidos en el juego.

## Estado del proyecto

El repositorio recoge el entorno de investigación y la **especificación consolidada de 20 documentos**. No se ha publicado aún código propio del mod ni existe certificación in-game del Centro de Operaciones, la campaña o las puertas de Proyecto Horizonte. No utilizar documentos de planificación como evidencia de implementación.

[**Leer los 20 documentos del proyecto**](docs/README.md)

## Decisión inmediata: V5.7

Priorizar **la observación de una estación existente y de su almacenamiento** con un prototipo Lua/Mission Director de solo lectura. El ciclo: carga extensión → puente Lua/MD → vincular estación real → observar inventario/manager → comparar con UI vanilla → guardar/cargar → certificar. Esta prueba **no necesita que HZ-04A ya esté construida**.

## Reglas indeclinables

Sin dinero, naves, NPC, materiales o investigación regalados; sin alterar el PHQ y tramas originales; sin forzar comandos a mineras; sin contabilizar transferencias entre estaciones propias como beneficio externo; sin declarar PASS sin pruebas del motor X4 9.00; sin dependencias de mods comunitarios no autorizadas.

## Estado local declarado

La guía [Entorno de desarrollo](docs/ENTORNO_DESARROLLO.md) describe X4 9.00, X4 Forge, x4cat, XSD e índice locales. [Inventario del repositorio](docs/INVENTARIO_REPOSITORIO.md) describe descargas y archivos locales, muchos ignorados por Git. Esta actualización no ha ejecutado ni modificado ese entorno.

## Implementación futura

La fuente propia, cuando se apruebe e implemente, se organizará de forma independiente a referencias y staging. Seguir el plan técnico [documento 16](docs/plan/16_ARQUITECTURA_LUA_MD_Y_CODIGO.md) y pruebas [documento 18](docs/plan/18_V57_ESTACION_REAL_ALMACENAMIENTO.md), con criterios [documento 19](docs/plan/19_MATRIZ_QA_EVIDENCIAS.md).
