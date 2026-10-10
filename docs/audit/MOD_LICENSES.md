# Procedencia, licencias y redistribución

**Revisión:** 2026-10-10. **Estado global:** `NOT_CLEARED`. [Registro de los 110 paquetes](data/license_packages.csv), [documentos/fingerprints dentro de extensiones](data/licenses.csv) y [autor declarado por manifiesto](data/extensions.csv).

Se encontraron documentos de tipo LICENSE/licence/permissions/README en 55 paquetes. Eso no significa 55 licencias favorables: un README puede carecer de permiso y un archivo puede estar en la raíz de una colección, fuera de la extensión concreta. Se preservan ruta y SHA-256, sin republicar código, assets ni textos de licencia de terceros. Los hashes identifican la copia, no prueban su descarga desde un autor autenticado.

## Comprobaciones prioritarias

| Componente | Evidencia leída | Conclusión acotada / acción |
|---|---|---|
| Mod Support APIs | El release local contiene `readme.txt`; la colección fuente `x4-projects-master/LICENSE` contiene MIT | La licencia del repositorio no se deduce del nombre del ZIP; verificar alcance de componentes/bibliotecas del artefacto final |
| UI Extensions | La ficha del autor limita la subida a otros sitios y concede determinados usos/modificaciones con atribución | Mantener descarga externa autorizada; aclarar cualquier distribución del pack con sus binarios |
| Gate Manage API | `LICENSE` Apache 2.0 dentro del DAT; mismo SHA-256 en la referencia fuente; la ficha Nexus tiene restricciones de publicación | Registrar las dos fuentes y aclarar su alcance; no tratar las restricciones de Nexus como descripción completa del código fuente |
| Inix | Ficha del autor con restricciones de subida, modificación y uso de assets | Referencia/laboratorio; no incluir ni adaptar archivos para publicar sin resolver permisos |
| Station Budget Watchdog | `x4-foundations-station-budget-watchdog-main/LICENSE` tiene texto MIT; el release local no incorpora esa misma evidencia en su raíz | Confirmar qué fuente corresponde al release y conservar avisos aplicables si se reutiliza |
| Player Feudal Realm y demás paquetes | Declaraciones de autor/metadatos y documentos del CSV | Permisos individuales pendientes; ausencia de licencia legible no se transforma en autorización |
| Recursos del juego/DLC | Catálogos instalados de Egosoft | Dependencia externa; no incorporar archivos del juego a la distribución propia |

En Mod Support APIs hay una discrepancia documental relevante: los campos de permisos de Nexus muestran restricciones, pero la nota expresa del autor remite a la licencia MIT de GitHub. [Ficha de SirNukes](https://www.nexusmods.com/x4foundations/mods/503), [licencia del repositorio](https://github.com/bvbohnen/x4-projects/blob/master/LICENSE). Debe resolverse el alcance por artefacto y componente; el informe inicial no justifica describir toda la API como no redistribuible.

La licencia Apache localizada para Gate Manage API tiene SHA-256 `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4`. Las condiciones de publicación de la ficha son una evidencia separada. [Ficha de Gate Manage API](https://www.nexusmods.com/x4foundations/mods/1856). Para UIX e Inix se revisaron sus fichas propias: [UI Extensions](https://www.nexusmods.com/x4foundations/mods/552), [Inix](https://www.nexusmods.com/x4foundations/mods/2319).

## Registro para cerrar un permiso

Cada componente seleccionado necesita: autor/procedencia y URL concreta, revisión/commit o release, SHA-256 del paquete y de los documentos, licencia aplicable al código y a cada asset de tercero, avisos que deben conservarse, alcance de modificación/redistribución, distribución comercial si procede y evidencia de permiso adicional cuando sea necesaria. Registrar por separado los componentes de un ZIP que agrupa varias extensiones.

El registro actual pone todos los paquetes en `NOT_CLEARED`; no se han solicitado permisos a autores. Los marcadores automáticos MIT/Apache/GPL/restricciones solo ayudan a localizar documentos para revisión. No se atribuye una licencia al paquete entero por detectar esas palabras en un README.

Política candidata del pack: publicar fuente TME y referencias a descargas oficiales como opción inicial; incorporar material de terceros solo después de cerrar este registro. Estudiar funcionamiento no implica autorización para copiar implementación, textos narrativos, modelos o recursos.
