# 17. Contratos de datos, IDs y persistencia

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Identidad
Usar dos capas: corporate_id permanente (ej. TME-CIT-01) y referencia de componente real validada (object_ref). El nombre visible puede cambiar sin romper la vinculación. Los nombres CMC-01 y CIT-01 **no significan que estén construidas**. La creación de relaciones empresa–objeto requiere selección explícita y verificación de propietario/clase.

## Snapshot conceptual v1
~~~json
{
  "schema": "tme.com.station-snapshot.v1",
  "revision": 1,
  "request_id": "example-only",
  "game_time": null,
  "quality": "UNKNOWN",
  "station": {
    "corporate_id": null,
    "object_ref": null,
    "exists": null,
    "owner_ref": null,
    "name": null,
    "manager_ref": null,
    "sector_ref": null
  },
  "storage": {
    "solid_capacity_m3": null,
    "solid_used_m3": null,
    "ore_units": null,
    "silicon_units": null
  },
  "errors": []
}
~~~
Es esquema lógico JSON para documentación/pruebas; no afirmar que sea formato blackboard nativo.

## Semántica de cantidades
null / UNKNOWN = dato no leído. 0 VERIFICADO = lectura fiable de cero. Separar ware units, metros cúbicos, tipo de almacenamiento, fecha/hora de juego y fuente. No mezclar capacidad total, cuota asignada a mercancía, capacidad utilizada y volumen libre.

## Versionado y correlación
Cada solicitud Lua lleva request_id, versión y generación de sesión. MD devuelve snapshot_id, revision, request_id y errores. Ignorar respuestas fuera de orden; validación de objetos previa a renderizar. Datos derivados necesitan enlazar revisiones de sus entradas. Evitar duplicar eventos al abrir/cerrar repetidamente el menú.

## Persistencia
Guardar enlaces aprobados y estado mínimo del registro en MD/blackboard. La caché Lua y snapshots temporales se pueden reconstruir. Si una referencia deja de resolver tras save/load: MISSING_OBJECT, sin crear el objeto ni reasignar identidades automáticamente.

## Concurrencia
Cambios manuales por usuario prevalecen. Los datos podrían cambiar entre lectura y presentación; marcar STALE y refrescar. Dos contratos no reservan simultáneamente mismas unidades. En V5.7 aún **no se escriben contratos de despacho ni reservas vanilla**.

## Privacidad y rendimiento
No registrar volúmenes masivos de universo ni snapshots completos cada segundo. Limitar observación a activos vinculados y muestreo de pruebas. Identificadores en logs deben servir a diagnóstico sin inventar nombres de NPC.

## V5.7 — ratificación y criterios operativos (2026-10-10)

El snapshot lógico no es formato blackboard certificado. Persistir identidad corporativa y resolver referencia real en save/load; descartar respuestas fuera de orden. MISSING_OBJECT prohíbe recrear entidad o vincular por nombre.

**Estado:** decisión documental aprobada; no confundir con prueba de juego. Consultar [protocolo](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA](19_MATRIZ_QA_EVIDENCIAS.md).
