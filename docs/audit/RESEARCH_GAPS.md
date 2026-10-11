# Preguntas pendientes y criterios de cierre

**Revisión:** 2026-10-10. Las decisiones de diseño ya aprobadas se conservan; estas preguntas buscan evidencia técnica y selección de componentes.

| ID / prioridad | Pregunta o bloqueo | Evidencia disponible | Criterio de cierre y siguiente acción |
|---|---|---|---|
| RG-01 / P0 | ¿Cuál es el pack estable mínimo? | Clasificación de 113 archivos y dos APIs condicionales | Elegir estrategia de UI V5.7; manifiesto por hash; QA individual y conjunto |
| RG-02 / P0 | ¿Qué variante se instala por ID? | Siete IDs repetidos; Don't Ignore Blacklists tiene variantes distintas | Seleccionar un proveedor; comparar payloads, no solo `content.xml` |
| RG-03 / P0 | ¿Cómo resolver target monitor de UIX/Star Command? | Misma ruta `subst`, contenido diferente | Elegir versión efectiva/adaptador autorizado y probar menús; Star Command sigue aislado |
| RG-04 / P0 | ¿Cómo corregir KAANE? | XML inválido `md/kill_and_attack_notifications_extended.xml:667` | Obtener/verificar release corregido; nuevo hash y parsing/XSD; conservar copia auditada |
| RG-05 / P0 | ¿Qué se puede redistribuir o adaptar? | Registro de todos los paquetes; documentos y fuentes prioritarias | Resolver licencia por componente/asset y discrepancias Nexus/fuente antes de publicar binarios |
| RG-06 / P1 | ¿Qué falta para el laboratorio PFR? | `ws_3722585376` versión `900` ya auditado; ausencia resuelta | Preparar laboratorio independiente y comprobar carga real y funcionamiento; `NOT_TESTED` |
| RG-07 / P1 | ¿Cómo interpreta X4 estos metadatos? | Ocho relaciones `minversion`; versiones decimales no comparables | Verificar documentación/lectura del motor sin normalización inventada |
| RG-08 / P1 | ¿Existe una baseline vanilla reproducible? | DLC presentes; overrides antiguos y UI safe mode desactivado | Ensayo BASE-01 con lista runtime y nuevo log, sin confundir historial |
| RG-09 / P1 | ¿Dónde está la fuente del prototipo TME histórico? | Log del 09/10 con build 611726 y fallos del kernel; fuente no localizada en repo/staging/directorios inspeccionados | Recuperar fuente/commit y reproducir fallos o desarrollar el spike aprobado; no certificar desde el log |
| RG-10 / P1 | ¿Cubre el índice las APIs y assets terranos? | 461.598 filas y nueve catálogos base; índice directo de 30 catálogos base/DLC | Consultar también DLC; validar firmas, IDs, recetas y esquemas por archivo vigente |
| RG-11 / P1 | ¿Qué garantiza exclusividad de cuatro sectores? | Diseño aprobado en capítulo 07 | Prototipo acotado sin sustituir política territorial global; IDs/recursos/puertas y reclamación reales |
| RG-12 / P1 | ¿Cómo conciliar tesorería, reservas y entregas? | Contratos conceptuales y ownership | Evidencias físicas y contables; save/load idempotente; cero créditos/wares duplicados |
| RG-13 / P1 | ¿Cuándo vence una autorización frente a orden manual? | Autoridad presidencial y prioridad vanilla definidas | API de detección y contrato de revalidación/cancelación; ningún executor en V5.7 |
| RG-14 / P2 | ¿Qué parte de Prospect/logística ya resuelve el juego? | Prospect Missions Tweak identificado; referencia oficial 9.00 | Comparación de comportamiento vanilla/mod; changelog del foro inaccesible al lector web de esta sesión |
| RG-15 / P2 | ¿Son actuales los modelos y sus `.jcs`? | Rutas inventariadas; cambios 9.00 publicados | Evidencia de conversión/versionado y ensayo de assets seleccionados; no inferir desde nombre 9.00 |
| RG-16 / P2 | ¿Qué herramienta está realmente lista para usar? | Forge tiene dependencias/dist; x4cat responde; otros paquetes solo inspeccionados | Smoke test aislado de SectorCreator/ModDoctor/XMLDiff según necesidad, sin ejecutarlos por existir |
| RG-17 / P2 | ¿Cómo recuperar automatización y referencias antiguas? | 24 `.pyc` sin fuentes x4pack; `KNOWLEDGEBASE.md` y fuentes de `tools/x4validate/` sí están dentro del ZIP local Claude Code Toolkit V3.2.0, pero no en las rutas actuales de los agentes | Evaluar esa recuperación y sus permisos sin sustituir nuestras instrucciones; x4pack requiere fuente legítima propia o retirada de la referencia |
| RG-18 / P2 | ¿Cómo completar campaña y continuidad de NPC? | Diseño de 20 misiones y personajes | IDs/diálogos/desbloqueos/errores/localización ES-EN y prueba de identidad sin duplicación |
| RG-19 / P1 | ¿Resuelve el parche de soporte un fallo real de este perfil? | Parche 1.97 incorporado; doce sustituciones diferentes del soporte 1.95; dos alias opcionales, uno presente | Reproducir con control sin parche y comparar LAB-SUPPORT-PATCH-01; verificar destino efectivo y licencia |
| RG-20 / P1 | ¿Aísla el gestor los ensayos lo suficiente? | Gestor 1.03 incorporado; requiere Print Extension List; el README mantiene quicksaves/autosaves compartidos | LAB-SETS-01/02, lista runtime tras reinicio y saves descartables; conservar copia externa anterior |

## Trabajo completado y alcance de los pendientes

Completado: hashes de los 113 archivos, lectura de los tres formatos, manifiestos/IDs/autores declarados, dependencias declaradas, verificación CAT/DAT comunitarios, XML bien formado, rutas/selectores compartidos, índices de catálogos vanilla/DLC, registro documental de licencias y clasificación propuesta. Los programas de herramientas, XSD completos, ejecución Lua/MD, mapas fusionados y casos del motor no están certificados.

Se consultaron fuentes públicas de Egosoft y autores para cambios, requisitos y permisos prioritarios. No se auditó la procedencia web ni todos los permisos/bugs públicos de los 113 archivos. La colección local y estos registros son una base de evidencia para cerrar esas preguntas, no una aprobación de instalación global.

El siguiente incremento sigue siendo V5.7: baseline, estrategia mínima de UI, descubrir firmas válidas y observar una estación real. Puertas, soberanía, gobernadores y rescate mantienen expedientes separados y no bloquean el observador salvo que se conviertan indebidamente en dependencias.
