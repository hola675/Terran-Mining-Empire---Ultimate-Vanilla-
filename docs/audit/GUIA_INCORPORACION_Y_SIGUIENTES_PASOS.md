# Incorporación de complementos y próximas instrucciones — 2026-10-10

**Estado:** guía operativa y decisiones de selección, **no** instalación en X4 ni nueva certificación runtime.  
**Ámbito:** X4: Foundations 9.00, Terran Mining Empire — Ultimate Vanilla+.

## Estado real de los complementos mencionados

| Componente | Autor / origen público | Release | ID técnico / evidencia | Estado |
|---|---|---|---|---|
| **Extension Sets Manager** | ChemODun; [Nexus 2401](https://www.nexusmods.com/x4foundations/mods/2401) | **1.03** (01-10-2026) | `ws_3806682809`, versión manifiesto `103` | **YA INCORPORADO AL INVENTARIO LOCAL** de 112; archivo en `inputs/mods` (ignorado por Git), con SHA-256 documentado |
| **Sir Sector's Mod Support Compatibility Patch** | [Nexus 2373](https://www.nexusmods.com/x4foundations/mods/2373) | **1.97** | `sn_mod_support_apis_patch`, versión manifiesto `197` | **YA INCORPORADO AL INVENTARIO LOCAL** de 112; laboratorio aislado, no perfil base |
| **Conversation Pagination API** | mantxiasdasdasd; [Nexus 2216](https://www.nexusmods.com/x4foundations/mods/2216) | **9.0**, según página pública 08-07-2026 | **ID esperado** `ws_3722585376` y mínimo `900` según dependencia de Player Feudal Realm. Falta verificar contra su propio ZIP `content.xml`. | **PENDIENTE DE ADQUIRIR Y AUDITAR**: no aparece en las 112 descargas inventariadas |

**Aclaración:** el conjunto anterior contenía 110 paquetes; una revisión más reciente de `main` ya incorporó al inventario **Extension Sets Manager 1.03 + Compatibility Patch 1.97**, llegando a **112**. No duplicar ni recontar esos dos paquetes como adquisiciones nuevas. Conversation Pagination sigue ausente y bloquea el laboratorio PFR, pero **NO** bloquea V5.7.

## Licencias y distribución

Las páginas Nexus de **Conversation Pagination API** y **Extension Sets Manager** restringen volver a subir sus archivos a otros sitios y exigen consentimiento previo para modificar/reutilizar assets. Por tanto:
- Conservar **solo** enlaces oficiales, versiones, IDs esperados, hashes y documentación en Git; **no** incorporar ZIP, CAT, DAT, Lua, XML o assets de estos autores al repositorio público sin permiso verificable.
- El auditor local `inputs/mods` está excluido mediante `.gitignore`; una copia adquirida legítimamente puede residir allí para uso local y análisis.
- No declarar permisos `CLEARED` ni añadir los complementos al instalador distribuible sin evidencia de licencia por artefacto. El parche de soporte también permanece `NOT_CLEARED`.

## Adquisición pendiente: Conversation Pagination API

1. Abrir la [descarga oficial Nexus 2216](https://www.nexusmods.com/x4foundations/mods/2216?tab=files), obtener el archivo **9.0** con la cuenta del usuario y preservar el nombre y original; no descargar desde mirrors sin procedencia.
2. Guardar **una sola copia** bajo `inputs/mods/` (el usuario/agente local puede copiar desde `C:\Users\Admin\Downloads\new`). No crear duplicados para un ID existente.
3. Registrar nombre, fecha, URL, SHA-256, tamaño y licencia; inspeccionar `content.xml` del ZIP para confirmar **ID, versión interna, dependencias, enabled/save**. No inferir el ID únicamente a partir del nombre o número Nexus.
4. Ejecutar `scripts/audit_pack.py` y `scripts/test_audit_pack.py` desde la raíz, con el entorno y dependencias documentados en [README de auditoría](README.md). La fuente de verdad de paquetes será **el resultado real regenerado**, no sumar uno manualmente a 112.
5. Regenerar los CSV/JSON de `docs/audit/data/` únicamente a partir de la inspección; actualizar `PACK_BASE_MANIFEST.md`, `MOD_DEPENDENCIES.md`, `MOD_LICENSES.md` y `RESEARCH_GAPS.md` con **nuevas evidencias**, sin modificar registros históricos a ciegas.
6. Solo después considerar `LAB-PFR-01` con el ID real cargado en el juego. No instalar PFR ni modificar una partida estable durante la adquisición.

Comandos orientativos desde PowerShell; **no** descargan, instalan ni modifican el juego:

```powershell
# Usar el nombre de ZIP descargado legítimamente desde Nexus; no adivinarlo.
Get-FileHash -Algorithm SHA256 -LiteralPath 'C:\Users\Admin\Downloads\new\ARCHIVO_CONVERSATION_PAGINATION.zip'
# Desde la raíz del repositorio, en el entorno preparado (Python/py7zr/UnRAR):
python scripts/audit_pack.py --vendor workspace/audit-pack-base/vendor --game 'D:\Games\X4 Foundations' --profile 'C:\Users\Admin\Documents\Egosoft\X4\6144'
python scripts/test_audit_pack.py
```

**No ejecutar el auditor contra un paquete recién descargado si aún no se ha copiado a `inputs/mods` y verificado; no publicar el ZIP en Git.**

## Extension Sets Manager 1.03: uso y límites

- Su release ya está registrado en `PACK_BASE_MANIFEST.md` y `summary.json`. Mantener candidato **OPTIONAL_CANDIDATE**, no dependencia obligatoria de TME ni de V5.7.
- Requiere **Print Extension List** `ws_3770927339`, versión mínima interna `100`; ya existe una descarga local de la versión interna `101`, aunque **no** hay prueba runtime.
- **UI Extensions deja de ser obligatorio en 1.03**; esta modificación del 01-10-2026 invalida la dependencia que se publicaba para 1.01.
- Los conjuntos **solo cambian las extensiones al reiniciar**. Sus guardados separados aplican **a guardados manuales**, **no** a quicksaves, autosaves ni guardados online.
- Si se desactiva UIX, los slots manuales **11–20 pueden desaparecer de los menús**, pero sus archivos no se borran; reaparecen al reactivarlo.
- Cada prueba debe conservar copia externa de saves. El gestor **no sustituye** una baseline sin mods ni prueba por sí solo aislamiento de perfiles.
- Para `LAB-SETS-01`: instalar solo Print Extension List + Extension Sets Manager en un entorno de ensayo controlado, probar creación/cambio de conjunto, reinicio y lectura de lista real. Para `LAB-SETS-02`: ensayar save manual propio, cambio de perfil y recuperación, nunca borrar un set con opción de eliminar saves.

Referencia: [documentación y changelog del autor](https://www.nexusmods.com/x4foundations/mods/2401).

## Compatibilidad Patch 1.97: regla de activación

- Ya documentado con 12 sustituciones `subst_01` hacia rutas de Mod Support APIs 1.95; **no** es reemplazo total de SirNukes ni solución para Conversation Pagination.
- **NO activar por defecto**: primero reproducir un defecto real con Mod Support APIs sin parche, luego ensayo `LAB-SUPPORT-PATCH-01` sobre save descartable, con logs antes/después y regresiones UI/MD/hotkeys.
- No activar simultáneamente con otras modificaciones amplias de UI/IA sin una matriz de compatibilidad aplicable a la selección exacta.

## Orden de trabajo y puertas de calidad

1. **BASE-01:** guardar backup del perfil y saves; registrar lista runtime real de juego + siete DLC. Revisar `SW Interworlds` residual en `content.xml` de perfil y `uisafemode=false` sin alterar valores sin evidencia.
2. **PACK-01:** congelar solo un **perfil mínimo** para el observador TME: X4 + DLC + futura extensión propia; otras APIs solo si una prueba demuestra que son necesarias. Elegir un proveedor por ID.
3. **SOURCE-01:** localizar/aislar los siete errores históricos de `TME_Kernel` del log 2026-10-09. No confundir logs viejos con un build V5.7 nuevo.
4. **INDEX-01:** indexar y consultar explícitamente catálogos de `ego_dlc_terran`; el índice x4cat histórico contenía solo nueve catálogos base.
5. **COM57:** implementar y probar **únicamente lectura** de estación propia y almacenamiento, handshake Lua/MD, identidad, SAVE/LOAD y cero cambios a órdenes/economía. Ejecutar COM57-01…15 con evidencia real.
6. **LAB-SETS:** si conviene para los perfiles, probar Extension Sets Manager 1.03 con sus precauciones, fuera de baseline estricta.
7. **LAB-PFR:** adquirir Conversation Pagination API y resolver sus dependencias antes de estudiar gobernadores; sin imponerlos al Centro de Mando.
8. **LAB-SUPPORT-PATCH:** investigar el parche solo cuando exista reproducción de fallo.
9. **INTEGRATION:** integrar una modificación por incremento y comparar contra base, con rollback y licencias individuales aclaradas.
10. **DOCS/GIT:** la rama de la PR #3 de V5.7 diverge de `main` tras la auditoría; reconciliar en una PR específica posterior **sin merge automático**, conservando los ADR y las evidencias.

**Estados iniciales:** BASE-01, PACK-01, LAB-SETS-01/02, COM57 = `NOT_TESTED`; LAB-PFR-01 = `BLOCKED` hasta adquirir y comprobar la API; LAB-SUPPORT-PATCH-01 = `NOT_TESTED`. Los **8 tests sintéticos** del auditor no equivalen a QA de X4.
