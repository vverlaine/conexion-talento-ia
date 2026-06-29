# Bitácora del proyecto — Conexión Talento

Registro vivo de sesiones, decisiones y pendientes. La entrada más reciente va arriba.

---

## Sesión 01 — 2026-06-29 — Descubrimiento y diagnóstico inicial

**Participaron:** Víctor (consultor). Fuente: transcripción de la llamada de descubrimiento con Virginia (CEO).

**Qué se hizo:**
- Se creó el repositorio de la memoria del proyecto (`conexion-talento-ia`).
- Se guardó la transcripción verbatim y la extracción de datos clave (`01-descubrimiento/`).
- Se ejecutó un análisis multi-experto (8 lentes + crítica adversarial + síntesis) que generó los
  documentos base de diagnóstico, dolores, oportunidades, solución, datos, riesgos, métricas, roadmap y propuesta.

**Decisiones tomadas:**
- **Tesis central:** *estandarizar y documentar antes de automatizar* + *activar el "oro" de la base de 4000 candidatos*.
- Estructura del engagement por **fases flexibles** (Fase 0 quick win → 1 procesos+datos → 2 IA asistida → 3 escala/monetización).
- Establecer **líneas base de métricas desde la semana 1** (el cliente hoy no mide nada).

**Hallazgos de investigación (deep-research, integrados):**
- **Jurisdicción confirmada:** El Salvador (primario) + Guatemala (secundario). **El Salvador YA tiene Ley de Protección de Datos Personales vigente (Decreto 144/2024)** → Conexión Talento es sujeto obligado hoy. Guatemala sin ley general aún.
- **Team Tailor:** base extraíble por **API REST (key Admin/Read)**; el "Co-pilot" de IA **no hace búsqueda semántica transversal** → estrategia **augmentar, no reemplazar**. *Descarga masiva de CVs por API NO confirmada — probar con cuenta real.*
- **Pricing:** fixed-fee por fase; arranque Fases 0–2 **~USD 13–33k** (alineado a benchmark LATAM USD 14–36k).
- **Benchmark IA-RRHH:** patrón replicable = cribado/matching semántico (Claude + RAG) con humano-en-el-bucle.
- Detalle y fuentes en [`99-research/`](../99-research/README.md). La **crítica adversarial interna** quedó en [`critica-adversarial.md`](./critica-adversarial.md).

**Reconciliación hecha:** propuesta actualizada con jurisdicción + hecho legal SV + **3 modelos de pricing con cifras**; `riesgos §5.1` corregido (el dato viejo "El Salvador laxo" era falso); README con carpetas marcadas completas.

**Banderas vivas (para no perder de vista):**
- ⚠️ Benchmark de compensaciones: solo lícito **anonimizado irreversible + agregado (k-anonimato)** y con **dictamen de abogado salvadoreño**. Congelado hasta entonces.
- ⚠️ No precipitar la salida de Team Tailor; augmentar por API primero.
- ⚠️ Riesgo de adopción: reclutadora que insiste en leer 200 CVs; cada quien con su método.
- ⚠️ Economía vs ancla del cliente (~USD 1.5–2.7k de la temporal): vender por fases autofinanciadas; declarar conflicto de interés build-vs-buy.

**Pendientes / próximos pasos:**
- [ ] Pedir a Virginia **acceso de solo-lectura / export de muestra de Team Tailor** → probar API + mini-demo de búsqueda semántica para el viernes.
- [ ] Conseguir **fee por colocación + volumen de mandatos/mes** (para el caso de ROI). Conversación del martes.
- [ ] Validar oficialmente **consentimiento de la base** y posible exposición UE.
- [ ] **Dictamen de abogado salvadoreño** antes de cualquier benchmark.
- [x] **Entregables del viernes producidos:** `Propuesta-Conexion-Talento.pdf` (16 pp., con portada, fases, esfuerzo, pricing) + `Presentacion-Conexion-Talento.pptx` (17 slides). Generadores en `04-propuesta/assets/` (regenerables).
- [ ] Pulir cifras de pricing con tarifa local + reemplazar ‹TU CONSULTORA› por el nombre/logo de la firma.
- [ ] (Opcional) Verificar visualmente las 17 slides en PowerPoint/Keynote antes de exponer.

---

## Sesión 01b — 2026-06-29 — Producción de entregables (PDF + PPT)

- Foco redirigido: **olvidar la reunión de Lili**; objetivo = proyecto completo por fases + PDF + PPT para Virginia el viernes.
- **Pricing concretado** (indicativo USD): F0 2.500 (acredita a F1) · F1 9.500 · F2 12.000 (modular) · F3 desde 15.000 / retainer 3.500/mes. Arranque F0+F1 ~12.000; programa 0–2 ~24.000.
- **Esfuerzo por fase** añadido (jornadas-persona): F0 8–12 · F1 20–30 · F2 25–35.
- Stack de generación: **pandoc + weasyprint** (PDF) y **python-pptx** (deck). Portada PDF verificada visualmente; portada PPTX verificada con QuickLook.
- Marca pendiente: el placeholder **‹TU CONSULTORA›** debe reemplazarse por el nombre/logo real (la firma aún no tiene nombre definido).

---

## Sesión 01d — 2026-06-29 — Loop del Consejo LLM (5 iteraciones) + reajustes

**Qué se hizo:** se corrió el Consejo LLM **5 veces** sobre el proyecto; cada ronda emitió un veredicto
estructurado y, cuando hubo mejoras significativas, se aplicaron al repo y se relanzó el consejo. Detalle
ronda por ronda en [`loop-consejo-estado.md`](./loop-consejo-estado.md).

**Resultado:** **34 mejoras aplicadas** en 5 rondas (commits `fe8542e`, `58a1d76`, `1574317`, `958ea73`, +iter5).
Arco de convergencia: estructural → cumplimiento → cierre comercial → mecánica de cierre → integridad fina.
Las rondas 4–5 empezaron a auto-corregir adiciones propias (rendimientos decrecientes) → **se paró en 5**.

**Cambios netos más importantes (acumulados):**
- El viernes vende **solo la Fase 0** ("Quick Wins + prueba de valor", US$2.500), con **orden de servicio
  firmable** (§11) y **garantía objetiva** atada a la vara de la Puerta 0 (no a "valor claro").
- **Tangible legal del viernes:** un CV anonimizado/sintético + registro anti-duplicado en vivo, en entorno
  con DPA — sin tocar el ATS ni violar el Decreto 144 (la demo completa va dentro de la Fase 0).
- **ROI honesto:** ejemplo con supuesto conservador + caveat **demanda-vs-oferta** (la 1ª pregunta del martes).
- Ancla económica: temp + F0 = $4.500 **vs. el 5º reclutador (~$15k/año)**.
- Guatemala en riesgos; consentimiento prospectivo desde F1; jerga traducida a resultados de negocio.
- Blindajes internos: contrato por hitos, IP/metodología, ruta si la F0 sale roja, autocanibalización de F1.

**Pendiente único:** **nombre de la firma** (Cifra / Vértice / Praxis u otro) para reemplazar ‹TU CONSULTORA›.

---

## Sesión 01c — 2026-06-29 — Estrés-test con Consejo LLM + reajuste de la propuesta

**Qué se hizo:** sometí el proyecto completo (propuesta, deck, pricing, roadmap) a un **Consejo LLM** de 5
asesores independientes + revisión entre pares + síntesis del presidente. Veredicto completo en
[`consejo-llm-01.md`](./consejo-llm-01.md).

**Hallazgos clave del consejo (los que dispararon cambios):**
- **Abismo del ancla sin cerrar:** Virginia ancla en ~US$2.000; se le presentaba $12k–$39k sin ROI en *sus* dólares.
- **"No" a casi todo lo que pidió** + IA en la semana 12+ → riesgo de rechazo o decepción. Falta una victoria visible YA.
- **API de Team Tailor sin verificar** = el riesgo que mata en silencio (toda la Fase 2 lo asume).
- **Tiempos irreales para 1 persona** (≈5–6 meses, no "F0–F2 seguidas").
- **Tono:** confianza ≠ humillación; reformular "retos" en clave **"sí, y"**.
- Punto ciego del Expansionista (IP/plataforma de $500k): visión correcta, *timing* equivocado para el viernes → va al **contrato, no al pitch**.

**Reajuste aplicado (cambios concretos):**
- **Deck + PDF reescritos** con arco "una victoria primero": la **Fase 0 ($2.500) es la decisión del viernes**; el roadmap completo pasa a **horizonte/anexo**, ya no es el pedido.
- Nuevo **slide + sección de ROI en dólares de Virginia** (fórmula + ejemplo marcador + dato que falta: su *fee*).
- **"SÍ/retamos" → "Sí, y"** (mismo fondo, tono de socio).
- Nuevos slides **"Empecemos por una victoria" (F0)** y **"Lo que te llevas en 3 semanas" (demo viva** con sus datos).
- "Documentar el ojo clínico" → **"blindar tu legado"**.
- Inversión **reanclada en F0**; paquetes $12k/$24k/$39k de-enfatizados.
- Propuesta interna: **contrato por hitos, cláusula de IP/reutilización de metodología, flujo de caja de Víctor, caveat legal de consentimiento, build-vs-buy.**

**Pendiente que sigue vivo:**
- [ ] **Lo primero (acción real):** pedir a Virginia acceso de lectura/export de Team Tailor y hacer un **export de prueba** (20–30 CVs de una vacante abierta) → confirma la Fase 2 y arma la **demo viva** del viernes.
- [ ] Ponerle **nombre a la firma** (reemplazar ‹TU CONSULTORA›).
- [ ] Calibrar el ROI con el *fee* por colocación real de Virginia.

---
