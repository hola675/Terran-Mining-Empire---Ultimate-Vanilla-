# 02. Visión, principios y reglas Vanilla+

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Visión
Crear la experiencia de fundar y administrar una corporación minera de origen terrano que crece hasta convertirse en potencia industrial y territorial **mediante las mecánicas originales de X4**, coordinadas por una capa administrativa y narrativa propia. El jugador es presidente y fundador: conserva el poder de decidir expansión, inversiones, seguridad, operaciones extraordinarias y diplomacia.

## Invariantes no negociables
1. Ninguna nave, piloto, módulo, crédito, mercancía, tecnología o sector se regala por una misión administrativa o aparece para cumplir un organigrama.
2. No modificar las tramas vanilla de manera destructiva, ni duplicar el PHQ ni a Boso Ta. Usar los métodos legítimos de progreso e investigación.
3. El motor controla minería, comercio, construcción, producción y navegación; TME observa y recomienda. Toda automatización posterior requiere API validada y permiso explícito.
4. El progreso del mod se fundamenta en eventos reales, no en temporizadores artificiales que simulen prosperidad.
5. Las órdenes manuales/prioritarias del jugador prevalecen; nada las restablecerá a espaldas del presidente.
6. Una reserva contable no es un bloqueo técnico garantizado: comprobar ofertas vanilla, inventarios y contratos.
7. La condición 'propietario de sector' se obtiene solamente cuando el motor reconoce la reclamación nativa correspondiente; el banner corporativo no sustituye un centro administrativo.
8. Ninguna acción genera doble beneficio, doble inventario o dos entradas por guardar y cargar una misma entrega.
9. Los paquetes de mods de referencia no son dependencias instaladas ni autorizaciones para reutilizar código/assets.
10. Cambios seguros en saves, DLC y actualizaciones: adaptadores aislados, pruebas y rollback documentado.

## Filosofía de progresión
Fundación minera → consorcio industrial → corporación interterritorial → potencia defensiva → imperio autosostenido. Estas etapas son narrativa y metas, **no niveles que concedan recursos**.

## Límites del Centro de Mando
Permitido sin actuación sobre el juego: observar, analizar, redactar expedientes, detectar incertidumbre y registrar autorizaciones. No permitido en prototipos COM-01/V5.7: compras, movimiento de mercancías, ajustes de estaciones, órdenes a naves, NPC nuevos, modificación de reputación o saldos. Los controles futuros deberán ofrecer 'propuesto', 'autorizado', 'aplicado en vanilla' y 'verificado' como estados distintos.

## Condición de aceptación general
Instalación compatible, eventos y menús reversibles, ninguna regresión en economía, scripts, campañas y saves; documentación con evidencia real por cada PASS. Todo fallo no reproducible o acceso API ausente queda explícito como bloqueo.

## Aplicación V5.7 — opción A (2026-10-10)

V5.7 es solo observación: prohibido cambiar órdenes, inventarios, dinero, propiedad, gerentes, guiones de economía, relaciones o misiones. Datos no leídos = UNKNOWN y no cero; prohibidas cifras simuladas presentadas como reales. Exigir rollback validado.

**Evidencias:** se evaluará conforme a [V5.7](18_V57_ESTACION_REAL_ALMACENAMIENTO.md) y [QA COM57](19_MATRIZ_QA_EVIDENCIAS.md); esta actualización es documental, no una prueba superada.
