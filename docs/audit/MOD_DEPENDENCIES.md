# Dependencias, IDs y carga

**Revisión:** 2026-10-10. **Evidencia exhaustiva de declaraciones leídas:** [dependencies.csv](data/dependencies.csv), 201 relaciones de 131 manifiestos. El ámbito incluye fuentes de referencia y plantillas; no es una lista de requisitos de TME.

Se resuelve por ID exacto de `content.xml`, preservando versión y opcionalidad; no por nombre de carpeta o número de Nexus. Los DLC locales documentan que una dependencia opcional establece orden cuando existe y no causa error por faltar. Las dependencias se cargan antes del consumidor. [Anatomía de una extensión, por el autor de Gate Manage API](https://chemodun.github.io/x4/modding-support/anatomy-of-an-extension/).

## Cadena del laboratorio de puertas

| Consumidor | Proveedor | Declaración interna | Resultado local |
|---|---|---|---|
| Gate Manage API `102` | X4 | mínimo `760` | Juego `900`, mínimo nominal satisfecho |
| Gate Manage API `102` | `ws_2042901274` | obligatorio, mínimo `193` | Mod Support APIs `195` descargado; no instalado |
| Inix `401` | `ws_3588643062` | obligatorio, mínimo `102` | Gate Manage API `102` descargado |
| Inix `401` | `ws_2042901274` | obligatorio, mínimo `195` | Mod Support APIs `195` descargado |
| Inix `401` | `kuerteeUIExtensionsAndHUD` | opcional, sin mínimo | Variante Nexus/local encontrada |
| Inix `401` | `ws_3477279743` | opcional, sin mínimo | Variante Workshop no encontrada por ID exacto |

El orden parcial resultante es soporte → Gate Manage API → Inix, y UIX antes de Inix por la declaración opcional que corresponda. La descripción del autor exige UIX funcional aunque el manifiesto declare sus dos variantes como opcionales: evaluar esa condición como **alternativa entre proveedores**, no como dos descargas simultáneas. [Requisitos de Inix](https://www.nexusmods.com/x4foundations/mods/2319). El mínimo público de Gate Manage API es soporte 1.93. [Ficha del autor](https://www.nexusmods.com/x4foundations/mods/1856).

## Gobernadores y otras dependencias ausentes

Player Feudal Realm declara X4 `900`, soporte `195` obligatorio, `ws_3722585376` versión `900` obligatorio y UIX local opcional. No hay proveedor de `ws_3722585376` en los paquetes/manifiestos y directorios de instalación inspeccionados. Su documentación lo identifica como Conversation Pagination API. [Requisitos de Player Feudal Realm](https://www.nexusmods.com/x4foundations/mods/2214). Si se decide probarlo, confirmar procedencia y variante de [Conversation Pagination](https://www.nexusmods.com/x4foundations/mods/2216?tab=files); no se descargó en esta sesión.

El otro requisito obligatorio sin proveedor es `MeJ_Disable_Encounters`, requerido por `sn_script_profiler` dentro de `x4-projects-master.zip`. No bloquea UIX, soporte ni V5.7: no instalar las 29 extensiones de esa colección por usar una sola API.

Las siete relaciones opcionales no resueltas son: `JP_ScriptLibrary` y `JP_AnotherExplorer` de la variante AnotherExplorer de Don't Ignore Blacklists; `ws_3477279743` de Inix y Map Sidebar Organizer; `GalaxyTraderMK3` y `kuerteeFriendlyFireTweaks` de Star Command; y `sn_mod_support_apis` del parche de soporte (su alias `ws_2042901274` sí está presente). Las entradas antiguas de `content.xml` del perfil no son proveedores instalados.

## Dependencias de las dos incorporaciones

Extension Sets Manager `103` declara X4 mínimo `800` y Print Extension List `ws_3770927339` mínimo `100`, obligatorio. El juego local `900` y la descarga de Print Extension List `101` satisfacen nominalmente esos mínimos; no se comprobó carga. Su README indica que UIX dejó de ser obligatorio en 1.03.

El parche `sn_mod_support_apis_patch` versión `197` declara X4 mínimo `300` y dos variantes opcionales de soporte, ambas mínimo `195`: `ws_2042901274`, presente en la colección, y `sn_mod_support_apis`, sin proveedor por ID exacto. El README exige Mod Support APIs activo. Por tanto, el requisito funcional es disponer de soporte, aunque ambos alias estén marcados opcionales; no instalar dos proveedores de la API. El README describe soporte para 7.00–9.00+, mientras el manifiesto permite desde `300`: conservar la discrepancia y probar en 9.00, sin inferir compatibilidad con 3.00.

Los dos ZIP no proporcionan `ws_3722585376`; el laboratorio PFR continúa bloqueado.

## Calidad de los metadatos

| Resultado del escáner | Relaciones | Interpretación |
|---|---:|---|
| `NOMINAL_VERSION_OK` | 182 | Existe proveedor descargado o DLC instalado con entero suficiente; no prueba carga |
| `NOT_FOUND` | 9 | Dos obligatorias y siete opcionales, dentro del ámbito inspeccionado |
| `UNVERIFIED_ATTRIBUTE` | 8 | Usan `minversion`; semántica del motor no verificada, conservada en atributos originales |
| `UNKNOWN_VERSION` | 2 | Mínimo `9.00` de Ship Variation Expansion y proveedor `1.6` de Service Crew Repairs para Star Command |

No se convierte automáticamente `9.00` en `900`, ni `1.6` en `160`. También aparece `version="4.0"` en SpaceCamouflage; no se detectó una relación que lo requiera, pero su formato debe verificarse antes de instalar. Las declaraciones originales están en la columna `declared_attributes`.

## Un solo proveedor por ID

IDs repetidos entre releases/fuentes: `Dont_Ignore_blacklists`, `ws_3588643062`, `ws_3750545906`, `DeadAirAITweaks_kuerteeAttackAITweaks`, `kuerteeUIExtensionsAndHUD`, `ws_2042901274` y `vas_station_budget_watchdog`. Hotkey API tiene `80009` en el release y `80006` en la referencia. Los dos Don't Ignore Blacklists son variantes diferentes. Aunque varios `content.xml` sean idénticos, sus payloads pueden diferir: no certifican equivalencia binaria.

Para un perfil elegido, reconstruir el grafo de **solo sus componentes**, comprobar ciclos y requisitos por runtime además de manifiestos, y conservar la lista cargada del juego. La tabla actual no implementa un ordenador de instalación ni garantiza el orden total entre mods sin relación declarada.
