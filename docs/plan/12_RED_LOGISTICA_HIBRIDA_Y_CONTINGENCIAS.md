# 12. Red minera híbrida y recuperación asistida

**Proyecto:** Terran Mining Empire — Ultimate Vanilla+  
**Revisión documental:** 2026-10-10  
**Horizonte técnico:** X4: Foundations 9.00  
**Estado:** especificación de diseño, salvo evidencias identificadas expresamente.

> Convención obligatoria: APROBADO = decisión de diseño; CANDIDATO = propuesta pendiente; VERIFICADO = evidencia ejecutada; BLOQUEADO = dependencia no resuelta. Ninguna regla APROBADA implica que haya código o una partida de X4 certificada.

## Decisiones V5.2 y V5.4
El abastecimiento de CIT-01 combina extracción directa desde Cuenca y acopio/redistribución mediante CMC-01. **La coordinación es asistida**, no autónoma. Liora investiga incidencias y propone usar inventario libre, una nave existente o ruta alternativa. Solo el juego ejecuta Mine for Commander, Trade for Commander u orden manual válida.

## Flujos
Directo: yacimiento Cuenca → Bolo subordinada a CIT-01 → CIT-01.
Territorial: yacimiento → Bolo subordinada a CMC-01 → almacén CMC-01 → Bolo distribuidora → CIT-01.
Contingencia: si HZ-04A está inoperativa, comprobar trayecto Cuenca → Fundacional → Horizonte por HZ-01 y HZ-02. Tener camino físico no garantiza elección de ruta por IA; documentar la ruta efectiva.

## Diagnóstico REC-54
1. Confirmar incidencia y datos recientes; una minera explorando por cambios 9.00 no implica avería.
2. Detectar órdenes prioritarias del jugador y **no tocarlas**.
3. Revisar bodega, equipo minero, oferta compra/venta, reglas, presupuesto, alcance, espacio y peligros.
4. Si CMC-01 dispone de stock P3 útil, proponer envío parcial y dejar intactas P1/P2.
5. Considerar ruta por Fundacional cuando ambas conexiones iniciales funcionan.
6. Solicitar compra externa o nueva nave solo tras justificar insuficiencia y financiación.
7. Verificar recepción y reconciliar todos los expedientes.

## Ejemplo aprobado de planificación
CMC-01: 6.000 silicio, P1 1.200, P2 2.500 = 2.300 libres. CIT-01 solicita 3.000; la propuesta puede despachar máximo 2.300 y dejar déficit 700. Con Bolo sólida de 880 u por carga se necesitan al menos tres cargas para el parcial. **Cifras ficticias de caso de ensayo**, no estado del juego.

## Concurrencia
La recuperación no abre una segunda solicitud completa si existe un contrato directo pendiente; cada recepción resta de la misma necesidad. El regreso de la Bolo directa no reabre automáticamente pedidos ya satisfechos. Un accidente no restaura naves ni inventario.

## Pruebas
Interrupción genuina, diagnóstico correcto, alternativa disponible, permiso, envío real, descarga, persistencia e idempotencia de SAVE/LOAD, respeto de P1/P2 y de órdenes prioritarias.
