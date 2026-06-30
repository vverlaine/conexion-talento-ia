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

## Primera tanda ✅ — 5/5 iteraciones

**Convergencia:** estructural (1) → cumplimiento/alcance (2) → cierre comercial (3) → mecánica de cierre (4) → integridad fina + auto-correcciones (5). Las rondas 4–5 empezaron a **corregir adiciones propias** (rendimientos decrecientes).

**Único pendiente abierto:** el **nombre de la firma** (Cifra / Vértice / Praxis u otro) → reemplazar ‹TU CONSULTORA› en `Propuesta-Conexion-Talento.md`, `assets/render_pdf.py` (FIRM) y `assets/build_pptx.py` (FIRM), re-render.

---

## Segunda tanda (6–10) — el usuario relanzó el loop

**Ajuste:** umbral ALTO. El consejo ahora (a) vigila el **bloat** y vale recortes tanto como adiciones,
(b) evita oscilaciones/re-edits, (c) ignora el nombre de la firma (pendiente del usuario), (d) prefiere
**retos profundos** (¿la tesis es correcta? ¿la razón más fuerte para un NO? ¿el BATNA?), (e) **sesga hacia
haySignificativas=false** — concluir "ya está listo" es un resultado válido.

### Iteración 6 — consejo ✅ + aplicación ✅ (umbral alto funcionó)
- **Solo 3 mejoras** (2 altas, 1 media) — sustantivas, sin nitpicks. El umbral alto evitó el relleno.
  1. *(alta)* **Auditoría exprés de Team Tailor** sobre una vacante viva en semana 1 = **alivio inmediato con mano de Víctor** (no de la temporal) → desarma la objeción del CFO "¿qué hace tu $2.500 esta semana?". Estaba solo como nota filosófica; ahora es entregable. (PDF §3 F0, deck slide 8)
  2. *(alta)* **Protocolo de la garantía objetiva:** la prueba (b) "mitad de tiempo" era etiqueta sin método. Definido baseline + reloj de pared + misma vacante/pool, **aislado de la temporal** (que contaminaba el test "proceso, no manos"). (PDF Puerta 0/§5/§11)
  3. *(media)* **"Competidor" en sentido estrecho** en la cláusula de IP — si no, casi cualquier boutique CA sería "competidora" y la cláusula quedaba hueca. (interna §11.2)
- Choque no resuelto (registrado, no aplicado): el Pensador quiere recortar a un 2º doc el horizonte; el Forastero-como-Virginia "ya firmo". Tratado como criterio, no defecto.
- Verificado: §3 Fase 0 (auditoría + protocolo). **Estado: HECHO.**

### Iteración 7 — consejo ✅ + aplicación ✅ — **CONVERGENCIA**
- Veredicto: **"el proyecto está listo para imprimirse"**; el mayor riesgo ya no es el documento sino seguir puliendo en vez de cerrar. Alertó *groupthink*. Solo 3 retoques (2 medias, 1 baja), todos aplicados:
  - "el martes" colgado → "nuestra primera sesión" (PDF + deck); capacidad ociosa **reordena** el programa (no solo apaga el ROI); **Plan B comercial** si la Puerta 0 sale roja (interna §11.6).

---

## Intermedio — Reescritura a lenguaje ejecutivo (pedido del usuario)
Todo el proyecto comunicado en lenguaje de negocio: 16 docs (workflow + verificación), doc cliente y deck
(~95 términos traducidos), preservando cifras/⚠️/fuentes. Commit `8359672`. El consejo ahora también
verifica claridad y que la traducción no perdió nada.

### Iteración 8 — consejo ✅ + aplicación ✅ (umbral alto cazó un defecto fuerte)
- **Hallazgo unánime de los 5 revisores:** la **garantía estaba amañada** ("seguro de cartón") — la prueba (b) comparaba contra un baseline **declarado** ("~5 días") → siempre pasa. + contradicción interna (la línea 110 prometía medir, la 119 declaraba). **5 mejoras:**
  1. *(alta)* **Garantía des-amañada:** baseline **medido en la semana 1**, no declarado (§3) + espejo en §11.
  2. *(media)* **Confesar el costo en horas** de Virginia/Lili en F1 (~4–6h/sem) → por eso la temporal descarga primero. (§3 F1)
  3. *(media)* **Team Tailor = Riesgo #1 consolidado:** las 3 dependencias (prueba a, adelanto CV real, tablero) nombradas como un solo punto de falla gestionado. (§8)
  4. *(media)* **Desacoplar el pedido del CV real** del documento (acción interna lunes; el sintético es el plan primario). (interna §11.6)
  5. *(baja → recorte)* **Bloat:** quitada la repetición "es lo único que decides hoy" (§5). Alinea con el pedido de claridad.
- Patrón raíz que el consejo nombró: el doc diseñaba sus propios criterios para "siempre ganar" — grieta de credibilidad, ya cerrada.
- Verificado: §8 riesgo #1, §3 garantía medida. PDF 19 pp. **Estado: HECHO.**

### Iteración 9 — consejo ✅ + aplicación ✅
- Siguió afilando la garantía: 2 confounders más allá del baseline — **efecto-repetición** (la 2ª terna corre más rápido porque ya conoces a esos candidatos) y **vacante limpia disponible**. + Fase 0 sobre-suscrita. **4 mejoras:**
  1. *(alta)* **Protocolo de garantía único** (anexo de 1 pág firmable): baseline medido + sin efecto-repetición (lo corre quien no armó la base / grupo distinto) + vacante nombrada con plan B. (§3, §11)
  2. *(alta)* **Fase 0 reconciliada:** 8–12 → **10–14 jornadas** (alcance real ~8 frentes); registrado interno que es **tarifa de adquisición, no margen**. (§3, deck, interna §11.4)
  3. *(media)* **Capturar el activo real:** fila para asegurar testimonio + permiso de marca al cumplirse la Puerta 0. (interna §11.6)
  4. *(baja)* Baseline declarado que sobrevivía en la tabla de métricas §6 → "a medir en sem. 1".
- Meta-mensaje del consejo (3er consenso unánime): **"dejen de pulir; el riesgo es no cerrar el viernes."** PDF 20 pp.

### Iteración 10 — consejo ✅ + aplicación ✅ — **CIERRE DE LA TANDA (10/10)**
- **Bug de honestidad real** (coronado unánime, verificable en 10s): la tabla "El horizonte completo" mostraba la **suma bruta** ($12k/$24k/$39k), **borrando el crédito del 100%** prometido 4 veces. **5 mejoras (1 alta, 2 medias, 2 bajas):**
  1. *(alta)* **Tabla neteada:** Sistema $12k→**~$9.500**, $24k→**~$21.500**, $39k→**~$36.500**, con nota del crédito. (§5 + deck + nota interna ligada a la decisión de precio L302)
  2. *(media)* **Nombrar la palanca de F0** que da el "mitad de tiempo": los activos de F0 (plantilla, cribado v0, anti-dup), no la rúbrica de F1 → resuelve la contradicción "(b) no depende de extracción". (§3)
  3. *(media)* **Acotar el n=1:** 1–2 vacantes = señal direccional validada por criterio, no prueba estadística; vacante de control de dificultad equivalente. (§3)
  4. *(baja)* **Descartada** — añadir lectura de mandatos enfriados a F0 contradice la reconciliación de sobre-suscripción de la iter. 9.
  5. *(baja)* Recorte del protocolo: mantenido tight, no inflado (sin crear anexo aparte).

---

## ✅ SEGUNDA/TERCERA TANDA COMPLETA — 10/10 iteraciones totales

**Valor real de las rondas 6–10 (umbral alto):** lejos de ser relleno, cazaron defectos de **cierre y credibilidad** que las 5 primeras no vieron: la **garantía amañada** (3 confounders, blindada en un protocolo serio) y el **bug aritmético del crédito del 100%**. Ambos eran del tipo "un CFO lo ve en 10 segundos" — sangraban el mayor activo de Víctor, la honestidad.

**Convergencia final:** el consejo declara el documento **imprimible**; su 3er consenso, repetido en cada ronda 7–10, es *"dejen de pulir; el riesgo dominante ya no es el texto sino no cerrar el viernes"*. Las últimas mejoras empiezan a oscilar (instrumentar más vs recortar más) → **señal clara de parar.**

## ✅ LOOP CERRADO POR EL USUARIO — decisiones tomadas

- **Loop:** cerrado tras 10 rondas (el usuario eligió "cerrar"). **No relanzar.** Si una heartbeat se dispara, leer esto y detenerse.
- **Marca:** la firma se llama **Vértice** · Data, IA & Transformación Digital. Aplicada en PDF (portada/pie/cierre/orden de servicio), deck y `FIRM` de ambos generadores.
- **Precio:** **crédito parcial 50%** (F1 se queda en US$9.500). Todas las menciones "100% acreditable" → "50%"; netos del horizonte recalculados (Sistema ~$10.750, Sistema+IA ~$22.750, Completo desde ~$37.750). Registrado en `propuesta-comercial.md` §11.4.

**Entregables finales:** PDF 20 pp. + deck 19 slides, en lenguaje ejecutivo, con marca Vértice, garantía blindada, tabla de inversión correcta. Listos para el viernes.
### Iteración 10 — ⏳ pendiente
### Iteración 8 — ⏳ pendiente
### Iteración 9 — ⏳ pendiente
### Iteración 10 — ⏳ pendiente
### Iteración 4 — ⏳ pendiente
### Iteración 5 — ⏳ pendiente

---

*Cada iteración debería converger: rondas tardías deberían hallar menos/más pequeñas mejoras. Si una
ronda no encuentra nada significativo, se registra igual y se cuenta para el mínimo de 5.*
