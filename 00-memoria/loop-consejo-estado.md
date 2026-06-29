# Loop /consejo-llm — estado (≥5 iteraciones)

**Objetivo:** correr el Consejo LLM ≥5 veces sobre el proyecto. Cada ronda: si hay mejoras
**significativas** (no nitpicks), aplicarlas al repo; luego relanzar el consejo. Mínimo 5 iteraciones.

**Driver:** las rondas del consejo y los workflows de aplicación son trabajo de fondo rastreado por el
harness → me re-invocan al completarse. `ScheduleWakeup ~1800s` = red de seguridad por si algo se cuelga.

**Criterio de "significativo":** cambia el riesgo de cierre, la economía/pricing, el alcance entregable,
el cumplimiento legal, o la probabilidad de éxito del primer proyecto. Lo cosmético no cuenta.

---

## Bitácora del loop

### Iteración 1 — consejo inicial ✅ + aplicación ✅
- Consejo emitió veredicto → [`consejo-llm-01.md`](./consejo-llm-01.md). **Mejoras significativas: SÍ.**
- Cambios mayores: vender solo Fase 0 el viernes; roadmap $39k → horizonte/anexo; slide+sección ROI;
  "SÍ/retamos" → "Sí, y"; demo viva; "blindar tu legado"; blindajes internos (contrato/IP/legal/caja).
- Aplicado: deck reescrito (19 slides, `build_pptx.py` v2), PDF reescrito (17 pp., nuevo `render_pdf.py`),
  propuesta interna §11 blindajes. Red-team del workflow corrigió 1 defecto reintroducido (tono "una persona más").
- Verificado visualmente: portada PDF, §5 inversión, §2 "Sí, y", portada deck. **Estado: HECHO.**

### Iteración 2 — 🔄 consejo en curso (revisa el estado ya mejorado)
### Iteración 3 — ⏳ pendiente
### Iteración 4 — ⏳ pendiente
### Iteración 5 — ⏳ pendiente

---

*Cada iteración debería converger: rondas tardías deberían hallar menos/más pequeñas mejoras. Si una
ronda no encuentra nada significativo, se registra igual y se cuenta para el mínimo de 5.*
