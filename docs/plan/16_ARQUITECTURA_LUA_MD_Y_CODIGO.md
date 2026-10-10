# 16. Arquitectura técnica, Lua/MD y estructura de fuente

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Objetivo inmediato
Crear extensión única TME con módulo COM independiente; prototipo de **lectura** de estación real. No modificar aiscripts mineros ni reemplazar archivos de Egosoft para el primer alcance.

## Árbol propuesto, no creado
~~~
src/terran_mining_empire/
  content.xml
  ui.xml
  ui/tme_com_probe.lua
  ui/tme_com_bridge.lua
  ui/tme_com_menu.lua
  md/tme_com_probe.xml
  md/tme_com_registry.xml
  md/tme_com_observer.xml
  t/...
tests/com/
  contracts/
  acceptance/
~~~
El repositorio actual documenta workspace/mods y deploy-staging locales ignorados por Git; separar estos directorios de código fuente versionado. No copiar los ejemplos Lua/XML del chat anterior como código listo: sintaxis, tipos, métodos y atributos deben cotejarse con XSD/archivos vanilla 9.00.

## Canales reconocidos
- Lua → MD: AddUITriggeredEvent → event_ui_triggered.
- MD → Lua: raise_lua_event → RegisterEvent.
- Datos complejos: variables de blackboard asociadas a entidad y GetNPCBlackboard.
- Referencias de objetos cruzan frontera LuaID/64-bit y necesitan conversión.
- Estado Lua es reconstruible; variables MD persistentes pueden sobrevivir carga.
- Los eventos no transportan cualquier tabla. Namespaces TME_COM únicos para evitar colisiones globales.

Referencia: https://wiki.egosoft.com/X4%20Foundations%20Wiki/Modding%20Support/UI%20Modding%20support/Talking%20with%20MD%20and%20AI%20scripts/

## Seguridad
El único permiso de escritura inicial es para registro/snapshot propios del mod, no para datos operativos vanilla. Prohibidos create_order, set cargo, create ship, buy ware, add money, owner mutation, portal/gate mutation. No activar señales a pilotos.

## Pipeline técnico
Investigar APIs exactas en índice x4cat y XSD; generar scaffold mínimo; validar XML; comprobar carga; handshake evento–blackboard; leer estación real; comprobar manager/ware; guardar/cargar; menú simple; auditoría. No declarar acceso a APIs de inventario hasta ejecutar el spike.

## Riesgos
Fallos de FFI, eventos no registrados, diferencias boolean 0/1, LuaID sin conversión, propiedades de inventario no expuestas, snapshot obsoleto, distintos DLC y Protected UI Mode. Cada riesgo requiere prueba y degradación a UNKNOWN.

## V5.7 — ratificación y criterios operativos (2026-10-10)

Descubrir primero firmas reales de X4 9.00 en x4cat/XSD; instrumentar request_id, session_generation, respuesta MD y correlación, sin inventar APIs. Crear fuente aislada y staging, nunca cambiar scripts vanilla.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).
