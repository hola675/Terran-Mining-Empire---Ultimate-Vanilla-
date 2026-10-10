# Selección del pack base

**Revisión:** 2026-10-10. **Estado:** CANDIDATO; no congelado. **Evidencia:** [110 paquetes con SHA-256](data/packages.csv) y [selección completa](data/selection.csv).

La selección es una propuesta conservadora de investigación, no una autorización para instalar o redistribuir. `inputs/mods` contiene descargas y no define el pack. Ningún mod comunitario queda establecido como requisito obligatorio de V5.7 en esta auditoría. La arquitectura aprobada del [documento 16](../plan/16_ARQUITECTURA_LUA_MD_Y_CODIGO.md) requiere primero demostrar el observador propio.

| Capa | Componentes propuestos | Estado y condición |
|---|---|---|
| Juego | X4 9.00; DLC terrano para contenidos de origen terrano | Presencia en disco verificada; activación runtime pendiente |
| Fuente TME | Extensión propia, COM de solo lectura | Fuente actual del mod pendiente; el script de auditoría no es el mod |
| Dependencias técnicas condicionales | UI Extensions 9.0.0.16; Mod Support APIs 1.95 | Incluir solamente si la estrategia de UI/puente las necesita y supera QA |
| Diagnóstico opcional | Print Extension List 1.01 | Evaluar en perfil de pruebas; no convertirlo en dependencia del jugador |
| Complementos | Visuales, contenido y UI seleccionados individualmente | Doce candidatos; cambios de modelos/estaciones requieren revisar balance y 9.00 |
| Laboratorios | Puertas, gobernadores, IA, rescate y economía civil | Ocho paquetes; nunca forman parte del perfil estable por estar descargados |
| Biblioteca | Fuentes, logística, órdenes, formación, pinturas y ejemplos | Conservar para estudiar; integración requiere una decisión posterior |

## Clasificación de los 110 archivos

| Rol propuesto | Archivos | Significado |
|---|---:|---|
| `CONDITIONAL_CORE` | 2 | APIs candidatas, con dependencia justificada y QA pendientes |
| `OPTIONAL_CANDIDATE` | 12 | Posible complemento tras aceptación individual |
| `LAB` | 8 | Experimentos aislados |
| `REFERENCE` | 75 | 55 descargas y 20 archivos de referencia de mods |
| `TOOL_REFERENCE` | 12 | Recursos de desarrollo, no mods del pack |
| `QUARANTINE` | 1 | Kill And Attack Notifications Extended: XML inválido |
| **Total** | **110** | Todos incluidos en `selection.csv` |

La clasificación del script usa rutas/nombres y el fallo XML observado. Es una propuesta revisable, no un análisis semántico completo de los 110 programas. No se asigna `OBSOLETE` por antigüedad ni `INCOMPATIBLE` por un solapamiento. La cuarentena afecta exactamente al SHA-256 `51d8be7651c7ac251e5ed88020ffc228b84ee30c792a7b6f46a9c4b54a50a800`.

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

El release humano y el entero del manifiesto pueden diferir. Un manifiesto `900` no identifica por sí solo la revisión 9.0.0.16. Fijar ambos campos junto con el hash del archivo y el hash de `content.xml`, disponibles en [extensions.csv](data/extensions.csv).

## Condición de congelación

Para cada componente elegido: un único proveedor/ID, hash de release, procedencia confirmada, dependencias transitivas resueltas en ese perfil, permiso de distribución aclarado, diffs y sustituciones revisados, pruebas de carga/UI/economía/save-load y rollback documentado. La combinación completa necesita su propia prueba además de los PASS individuales. Hasta entonces el campo `decision` permanece `CANDIDATE`.

Distribución propuesta: fuente propia TME y manifiesto de dependencias con enlaces autorizados; los binarios de terceros no se incluyen automáticamente. El mecanismo técnico de instalación tampoco queda implementado por esta documentación.
