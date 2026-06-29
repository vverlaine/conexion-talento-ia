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

### Iteración 2 — consejo ✅ + aplicación ✅
- Veredicto: el andamiaje estratégico es sólido; quedaban **6 defectos reales** de cierre/cumplimiento/alcance.
- **Mejoras aplicadas (6):**
  1. *(alta)* **Tangible del viernes sin violar el Decreto 144:** un CV real anonimizado por correo → teaser
     branded esta semana en entorno con DPA; ATS + abogado al lunes; demo completa (20–30 CVs) dentro de F0. (§9, §10)
  2. *(alta)* **Guatemala** en la tabla de riesgos + transferencia SV–GT; taxonomía "se construye una vez, se despliega en SV y GT". (§8, §3)
  3. *(media)* **Tablero de línea base condicional** ("si el ATS lo permite") en el doc cliente. (§3 F0)
  4. *(media)* **Jerga de la Fase 1 → resultados de negocio** (RoPA-lite, golden set, ESCO, North Star, RACI traducidos). (§3 F1)
  5. *(media)* **Seguro del comprador:** los activos tangibles son tuyos aunque la Puerta 0 salga roja. (§5)
  6. *(media)* **Alivio operativo en 3 semanas** (temp redirigida a descargar operación) en el doc cliente. (§2)
- Reflejado en deck (riesgos+GT, próximos pasos legal-safe, seguro del comprador, demo con nota DPA) y propuesta interna §12.
- Verificado: §8 riesgos (glyph SV–GT corregido), §9 secuencia legal. **Estado: HECHO.**

### Iteración 3 — consejo ✅ + aplicación ✅
- Foco: afinar el **cierre comercial** del viernes. **7 mejoras** (4 altas, 3 medias).
  1. *(alta)* **ROI con el fee real:** pedir el *fee* HOY por WhatsApp; §9 "Cuándo"→HOY; §5 deja de ser marcador. (PDF §5/§9, deck ROI)
  2. *(alta)* **Reconciliar la cuenta:** temp (~$2.000) + F0 ($2.500) = $4.500 vs. el **5º reclutador (~$15k/año)** = el puente económico. (PDF §5, deck inversión)
  3. *(alta)* **2º tangible legal el viernes:** registro anti-duplicado en vivo (datos de ejemplo), además del CV. (PDF §10, deck pasos)
  4. *(alta)* **Ruta si la F0 sale roja + economía del primer cliente** (referencia+IP > margen, concentración, BATNA, bus factor). (interna §11.6 nueva)
  5. *(media)* **Autocanibalización de F1** (~$233/jornada): flag como **decisión comercial de Víctor** — subir F1 o acreditar 50% — sin tocar el 100% del doc cliente. (interna §11.4)
  6. *(media)* **Puerta 2 honesta con el *n*:** concordancia cualitativa caso-por-caso, no umbral estadístico. (PDF §3 F2)
  7. *(media)* **Licencia DPA visible:** nombrar herramienta/costo/pagador (~$30–60/usuario/mes). (PDF §3 F0)
- Punto ciego unánime de los revisores: **este es el primer cliente** → la referencia+IP vale más que el fee (capturado en §11.6).
- Verificado: §5 inversión (ambos callouts). **Estado: HECHO.**

### Iteración 4 — 🔄 consejo en curso
### Iteración 5 — ⏳ pendiente
### Iteración 4 — ⏳ pendiente
### Iteración 5 — ⏳ pendiente

---

*Cada iteración debería converger: rondas tardías deberían hallar menos/más pequeñas mejoras. Si una
ronda no encuentra nada significativo, se registra igual y se cuenta para el mínimo de 5.*
