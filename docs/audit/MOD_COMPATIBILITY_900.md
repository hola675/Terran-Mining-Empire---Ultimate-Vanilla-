# Compatibilidad estática con X4 9.00

**Revisión:** 2026-10-10. **Estado:** juego no ejecutado en esta auditoría; compatibilidad conjunta `NOT_TESTED`. [Solapamientos y selectores](data/overlaps.csv).

## Problemas comprobados

1. **XML no bien formado:** paquete Kill And Attack Notifications Extended, `md/kill_and_attack_notifications_extended.xml`, línea 667, columna 8. ElementTree informa `mismatched tag`; la lectura directa confirma un cierre de `do_if` discordante. SHA-256 del miembro: `ac3a0a6b6aaff2dd8344a39910893c87d0643d34cd819576d5da389d27b00189`. El paquete queda en cuarentena; no se editó el original ni se presentó un arreglo de terceros como release.
2. **Sustitución compartida de UI:** UIX y Star Command incluyen `ui/addons/ego_targetmonitor/targetmonitor.xpl` en catálogos `subst` con MD5 distintos. Star Command tiene varias copias en sus catálogos. Hay un riesgo concreto de selección/sobrescritura; falta determinar el payload efectivo y reproducir el fallo o la integración. No se declara incompatibilidad de toda la combinación por esta evidencia aislada.
3. **Alternativas con ID idéntico:** los siete IDs repetidos de [dependencias](MOD_DEPENDENCIES.md) deben tener un único proveedor seleccionado. La referencia UIX contiene además un `targetmonitor.xpl` loose cuyo hash difiere de su copia CAT, aunque su manifiesto coincida con el release. Leer el manifiesto no basta para elegir la fuente de instalación.

## Matriz de rutas compartidas

| Clase | Rutas | Acción |
|---|---:|---|
| `SAME_ID_ALTERNATIVES` | 81 | Separar releases, variantes y fuentes del mismo ID |
| `DIFF_OVERLAP_REVIEW` | 97 | Revisar operaciones, selectores, orden y coincidencias en XML fusionado |
| `SHARED_PATH_REVIEW` | 208 | Revisar mapas, librerías y assets; no deducir conflicto solo del nombre |
| `TEXT_IDS_REVIEW` | 17 | Comparar IDs de páginas/textos e idiomas; el mismo nombre de archivo no basta |
| `REPLACEMENT_REVIEW` | 1 | Resolver la sustitución de target monitor entre UIX y Star Command |

Total: 404 rutas, contando toda la biblioteca, incluidas fuentes. De ellas, 184 están también en el índice directo de catálogos actuales base/DLC. Las otras pueden ser adiciones o contenido compartido entre mods. No se simula la resolución efectiva de archivos ni se fusionan los diffs; el CSV conserva proveedor, ID, origen, modo CAT, hash y selectores para esa revisión posterior.

Ejemplos materiales: `aiscripts/order.trade.routine.xml` es parcheado por Emergent Missions, Trade Analytics, Logistics Guidance, Replicate Commanders Logic, Station Trader Multiorder, Subordinates Config Unlocker y KUDA. `aiscripts/trade.station.xml` añade Star Command y otros sistemas de reputación/analítica a la revisión. Alinear la selección con [SYSTEM_OWNERSHIP](SYSTEM_OWNERSHIP.md) antes de probar economías/órdenes conjuntas.

## Cambios del motor y falsos positivos

Egosoft documenta para 9.00 la reconversión de colisiones `.jcs`, cambios en equipos S/M, APIs retiradas, nuevos datos de recursos y cambios en acciones MD. También indica que la capa UI puede tener cambios no enumerados. [Breaking Changes oficial](https://wiki.egosoft.com/X4%20Foundations%20Wiki/Modding%20Support/Breaking%20Changes/).

El escaneo de once patrones retirados/deprecados dio una coincidencia: `event_area_discovered` en `md/kuertee_ssac.xml:737`, Social Standings And Citizenships. La comprobación directa la encontró dentro de un comentario XML. No se marca como código incompatible. Cero coincidencias adicionales en esta lista limitada **no** demuestra ausencia de otros cambios de 9.00.

No se comprobó la versión de las colisiones `.jcs`, ni sintaxis/semántica Lua, ni XPL compilado. El MD5 verificado de 24.703 entradas de los 46 pares CAT/DAT solo confirma que el payload coincide con el índice de su paquete. No sustituye la validación XSD, la firma de procedencia ni una ejecución en el juego.

## Gates de aceptación

Antes de integrar: XML bien formado → XSD pertinente → requisitos/IDs → payload y selectores contra baseline → carga aislada → UI/mapa → órdenes manuales y prioritarias → inventario/saldos → save/load → prueba conjunta y rollback. Guardar `PASS`, `FAIL`, `BLOCKED` o `NOT_TESTED` con hashes y logs del ensayo. El procedimiento está en [TEST_PROFILES](TEST_PROFILES.md) y el [plan QA](../plan/19_MATRIZ_QA_EVIDENCIAS.md).
