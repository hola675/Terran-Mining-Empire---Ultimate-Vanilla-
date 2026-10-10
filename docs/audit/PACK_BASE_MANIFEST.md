# Selección del pack base

**Revisión:** 2026-10-10. **Estado:** CANDIDATO; no congelado. **Evidencia:** [112 paquetes con SHA-256](data/packages.csv) y [selección completa](data/selection.csv).

La selección es una propuesta conservadora de investigación, no una autorización para instalar o redistribuir. `inputs/mods` contiene descargas y no define el pack. Ningún mod comunitario queda establecido como requisito obligatorio de V5.7 en esta auditoría. La arquitectura aprobada del [documento 16](../plan/16_ARQUITECTURA_LUA_MD_Y_CODIGO.md) requiere primero demostrar el observador propio.

| Capa | Componentes propuestos | Estado y condición |
|---|---|---|
| Juego | X4 9.00; DLC terrano para contenidos de origen terrano | Presencia en disco verificada; activación runtime pendiente |
| Fuente TME | Extensión propia, COM de solo lectura | Fuente actual del mod pendiente; el script de auditoría no es el mod |
| Dependencias técnicas condicionales | UI Extensions 9.0.0.16; Mod Support APIs 1.95 | Incluir solamente si la estrategia de UI/puente las necesita y supera QA |
| Diagnóstico opcional | Print Extension List 1.01 | Evaluar en perfil de pruebas; no convertirlo en dependencia del jugador |
| Complementos | Visuales, contenido y UI seleccionados individualmente | Trece candidatos; cambios de modelos/estaciones requieren revisar balance y 9.00 |
| Laboratorios | Puertas, gobernadores, IA, rescate y economía civil | Nueve paquetes; nunca forman parte del perfil estable por estar descargados |
| Biblioteca | Fuentes, logística, órdenes, formación, pinturas y ejemplos | Conservar para estudiar; integración requiere una decisión posterior |

## Clasificación de los 112 archivos

| Rol propuesto | Archivos | Significado |
|---|---:|---|
| `CONDITIONAL_CORE` | 2 | APIs candidatas, con dependencia justificada y QA pendientes |
| `OPTIONAL_CANDIDATE` | 13 | Posible complemento tras aceptación individual |
| `LAB` | 9 | Experimentos aislados |
| `REFERENCE` | 75 | 55 descargas y 20 archivos de referencia de mods |
| `TOOL_REFERENCE` | 12 | Recursos de desarrollo, no mods del pack |
| `QUARANTINE` | 1 | Kill And Attack Notifications Extended: XML inválido |
| **Total** | **112** | Todos incluidos en `selection.csv` |

La clasificación del script usa rutas/nombres y el fallo XML observado. Es una propuesta revisable, no un análisis semántico completo de los 112 programas. No se asigna `OBSOLETE` por antigüedad ni `INCOMPATIBLE` por un solapamiento. La cuarentena afecta exactamente al SHA-256 `51d8be7651c7ac251e5ed88020ffc228b84ee30c792a7b6f46a9c4b54a50a800`.

## Versiones e identidad que deben fijarse

| Producto | Release registrado en el archivo | `content.xml` ID | Versión interna |
|---|---|---|---|
| UI Extensions | 9.0.0.16 | `kuerteeUIExtensionsAndHUD` | `900` |
| Mod Support APIs | 1.95 | `ws_2042901274` | `195` |
| Gate Manage API | 1.02, aunque el nombre incluye `1.01.zip` | `ws_3588643062` | `102` |
| Inix Gate Network Control | 4.0.1 | `inix_gate_network_control` | `401` |
| Player Feudal Realm | v6 | `ws_3760859460` | `900` |
| Logistics Guidance | 1.04, archivo `Main File 1982` | `ws_3668059212` | `104` |
| Print Extension List | 1.01 | `ws_3770927339` | `101` |
| Extension Sets Manager | 1.03 | `ws_3806682809` | `103` |
| Sir Sector's Mod Support Compatibility Patch | 1.97 | `sn_mod_support_apis_patch` | `197` |

El release humano y el entero del manifiesto pueden diferir. Un manifiesto `900` no identifica por sí solo la revisión 9.0.0.16. Fijar ambos campos junto con el hash del archivo y el hash de `content.xml`, disponibles en [extensions.csv](data/extensions.csv).

## Incorporación de las dos descargas nuevas

El 2026-10-10 se copiaron los dos ZIP de `C:\Users\Admin\Downloads\new` a `inputs/mods`, conservando nombres y originales. Se verificó la igualdad SHA-256 entre origen y copia. No se instalaron en X4 ni se activaron perfiles.

| Archivo incorporado | SHA-256 | Selección propuesta |
|---|---|---|
| `extension_sets_manager_1.03.zip 2401 1.03 2026-10-01T11-27Z tIegefLnT.zip` | `746c4228b396c32f4313f9bd54ca67bcb363f7405145eca6c96e92b86c1aaeb8` | `OPTIONAL_CANDIDATE`: gestor de conjuntos de extensiones; requiere Print Extension List |
| `Sir Sector's Mod Support Compatibility Patch 2373 1.97 2026-10-06T08-21Z YwOaOVnm0.zip` | `3729e51d8e14f4a780a1f3e141bef4a12ec2c540006e8cef5afa864fcfd22463` | `LAB`: sustitución de archivos de soporte, solo tras reproducir un fallo con control sin parche |

El gestor no es un requisito del observador V5.7. El parche tiene ID propio y complementa una instalación de Mod Support APIs; no sustituye su paquete completo ni cubre Conversation Pagination. Sus declaraciones opcionales de alias no garantizan por sí solas la presencia de soporte. Véanse [dependencias](MOD_DEPENDENCIES.md), [sustituciones](MOD_COMPATIBILITY_900.md#parche-de-soporte-incorporado) y [ensayos específicos](TEST_PROFILES.md#ensayos-de-las-dos-incorporaciones).

## Condición de congelación

Para cada componente elegido: un único proveedor/ID, hash de release, procedencia confirmada, dependencias transitivas resueltas en ese perfil, permiso de distribución aclarado, diffs y sustituciones revisados, pruebas de carga/UI/economía/save-load y rollback documentado. La combinación completa necesita su propia prueba además de los PASS individuales. Hasta entonces el campo `decision` permanece `CANDIDATE`.

Distribución propuesta: fuente propia TME y manifiesto de dependencias con enlaces autorizados; los binarios de terceros no se incluyen automáticamente. El mecanismo técnico de instalación tampoco queda implementado por esta documentación.
