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

### Iteración 4 — consejo ✅ + aplicación ✅
- Foco: **mecánica del cierre** + auto-corrección de la iteración 3. **7 mejoras** (3 altas, 4 medias).
  1. *(alta)* **Instrumento de cierre:** nueva **§11 Orden de servicio (1 página, para firmar)** dentro del PDF — alcance, $2.500, 50% anticipo, garantía, validez. (PDF §11, deck pasos)
  2. *(alta)* **Placeholder + credibilidad/continuidad:** añadida nota de continuidad (no dependes de 1 persona) al doc cliente; **nombre de la firma → pendiente: Víctor elige entre 3 sugerencias** (decisión suya).
  3. *(alta)* **Reversión de riesgo:** garantía de devolución del anticipo si no ve valor. (PDF §5, deck inversión)
  4. *(media)* **Puerta 0 con vara de negocio** (candidato olvidado encontrado / terna en mitad de tiempo). (PDF §3)
  5. *(media)* **ROI sin tarea:** pre-llenado con supuesto conservador en vez de "manda el fee HOY" — **revierte un exceso de la iter. 3** (el consejo se auto-corrigió). (PDF §5/§9/§10, deck ROI)
  6. *(media)* **Plan B del tangible:** CV sintético si no llega el real; "tantos CVs como permita el export". (PDF §9/§10)
  7. *(media)* **Gantt honesto:** solape mínimo + apoyo puntual (no superhéroe en solitario). (PDF §4, deck gantt)
- **Auto-corrección sana:** el Forastero señaló que apilar callouts de precio "huele a defensa"; suavizado el de "manda el fee HOY".
- Verificado: §11 orden de servicio + §10. PDF 18 pp. **Estado: HECHO** (salvo el nombre de la firma).

### Iteración 5 — consejo ✅ + aplicación ✅ — **LOOP COMPLETO (5/5)**
- Foco: integridad económica y legal final. **8 mejoras** (5 altas, 3 medias).
  1. *(alta)* **Des-apilar el "put gratis":** quitada la devolución del anticipo; garantía atada a la **vara objetiva de Puerta 0**, no a "valor claro". (PDF §5/§11, interna §11.4) — *auto-corrige la iter. 4.*
  2. *(alta)* **Demanda-vs-oferta:** caveat honesto al ROI ("aplica solo si pierdes mandatos por velocidad") + la pregunta como **1ª del martes**. (PDF §5/§9)
  3. *(alta)* **Entorno DPA asignado a Víctor el lunes** (bloqueante del teaser legal). (interna §12)
  4. *(alta)* **Placeholders de la orden:** validez → "10 días hábiles"; **nombre de la firma sigue pendiente de tu elección.**
  5. *(alta)* **Consentimiento prospectivo de uso secundario desde la Fase 1** (irretroactable). (PDF §3 F1)
  6. *(media)* **Vara (a) de Puerta 0 condicionada al export**; (b) como criterio principal. (PDF §3)
  7. *(media)* **Renombrar Fase 0** → "Quick Wins + prueba de valor con tus datos" (valor del cliente, no "spike"). (PDF §3/§5/§11, deck)
  8. *(media)* **Encuadre de la demo:** las discrepancias IA-vs-tripa son el insumo que la Fase 1 codifica, no una ruptura. (PDF §10)
- Verificado: §5 garantía objetiva, §11 orden final. PDF 19 pp., deck 19 slides.

---

## ✅ LOOP COMPLETO — 5/5 iteraciones (no relanzar)

**Convergencia observada:** estructural (1) → cumplimiento/alcance (2) → cierre comercial (3) → mecánica de cierre (4) → integridad fina + auto-correcciones (5). Las rondas 4–5 empezaron a **corregir adiciones propias** (señal de rendimientos decrecientes). Recomendación: **parar el ciclo sintético aquí** y pasar a prueba con humano real (Virginia/un colega senior). Si la heartbeat programada se dispara, leer esto y **detenerse**.

**Único pendiente abierto:** el **nombre de la firma** (Víctor elige entre Cifra / Vértice / Praxis u otro) → reemplazar ‹TU CONSULTORA› en `Propuesta-Conexion-Talento.md`, `assets/render_pdf.py` (FIRM) y `assets/build_pptx.py` (FIRM), re-render.
### Iteración 4 — ⏳ pendiente
### Iteración 5 — ⏳ pendiente

---

*Cada iteración debería converger: rondas tardías deberían hallar menos/más pequeñas mejoras. Si una
ronda no encuentra nada significativo, se registra igual y se cuenta para el mínimo de 5.*
