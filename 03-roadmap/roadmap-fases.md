# Roadmap por Fases — Conexión Talento
### Programa de estandarización, datos e IA asistida para Reclutamiento y Selección
*Documento de decisión | Borrador para revisión del viernes | Versión 1.0*

---

## Cómo leer este documento

Este roadmap traduce el diagnóstico de las 8 lentes expertas en una **secuencia accionable y financiable**. Tres decisiones de diseño lo gobiernan, y son la respuesta directa a la crítica adversarial:

1. **Secuencia única, no fases en paralelo.** Existe una sola ruta crítica que reconcilia la tensión entre las lentes (datos quiere extraer/parsear ya; proceso quiere documentar primero; métricas exige etapas estandarizadas antes de medir). El orden acordado es: **estandarizar criterios → documentar → instrumentar → recién entonces extraer/automatizar.** No se automatiza ninguna etapa sin su estándar documentado y su línea base. Esto es un *gate* contractual, no una buena intención.
2. **Precondiciones bloqueantes con dueño y fecha**, no "preguntas abiertas". Cuatro supuestos sostienen todo el programa (país, API de Team Tailor, consentimiento de origen, existencia de *golden set*). Se cierran en un **Spike de Factibilidad pagado de 1 semana** ANTES de comprometer alcance o precio de las fases siguientes.
3. **Camino por defecto = "suficientemente bueno con lo que ya se paga"** (BUY/activar Team Tailor + SOPs livianos), y *build* a medida **solo** si el volumen y la economía lo justifican con datos. Declaramos abiertamente nuestro conflicto de interés: construir infraestructura nos conviene a nosotros; recomendar exprimir lo ya pagado conviene al cliente. Elegimos lo segundo como postura por defecto.

> ⚠️ **Supuestos a validar marcados así en todo el documento.** Cifras de duración, costo y ahorro son rangos ilustrativos hasta cerrar el Spike de Factibilidad y obtener el *fee* por colocación y el volumen mensual de mandatos.

---

## Tabla resumen del roadmap

| Fase | Nombre | Objetivo en una línea | Duración | Hito de salida (go/no-go cuantificado) |
|---|---|---|---|---|
| **0.0** | **Spike de Factibilidad** (técnico + legal) | Apagar los 4 supuestos que sostienen todo lo demás | **1 sem** (dentro de Fase 0) | API/export de TT confirmados · país + base legal confirmados · muestra de vigencia de la base · ¿existe *golden set*? |
| **0** | **Quick win + Diagnóstico** | Credibilidad temprana visible + foto honesta del "es actual" | **2–3 sem** | ⭐ Plantilla CV adoptada por los 4 + dedup operando + baseline retrospectiva de 3 KPIs (extremos) entregada |
| **1** | **Estandarizar, documentar e instrumentar** | Convertir el "ojo clínico" tácito en estándar medible y datos en estructura | **4–6 sem** | Scorecard + SOP del cribado vivos · stage-gates únicos en TT · diccionario de datos · líneas base forward capturándose |
| **2** | **IA asistida (copiloto)** | Acelerar el proceso YA estandarizado, con humano en el loop | **6–10 sem** | Screener/Ranker concuerda ≥X% con criterio de Virginia en 2 búsquedas reales · CV-tool en producción · 0 auto-rechazos |
| **3** | **Orquestación, escala y monetización** | Activo de datos vivo + nuevas líneas de ingreso, condicionadas a base legal | **Trimestral, modular** | Decisión ATS con datos · internal-fill ≥30–40% ⚠️ · benchmark solo con dictamen legal favorable |

**Duración total estimada del núcleo (Fases 0–2): ~3–5 meses.** Fase 3 es *land-and-expand* opcional, modular y autofinanciada por el valor demostrado en fases previas.

---

## Principios rectores (la ruta crítica resuelta)

```
Spike factibilidad ─► Reparar comunicación al candidato ─► Estandarizar CRITERIOS (scorecard/rúbrica)
        │                                                          │
        └─► dedup + CV branding (quick wins)        ─► Stage-gates únicos en TT ─► Líneas base forward
                                                                   │
                                              Extraer/estructurar base ─► IA copiloto (HITL) ─► Escala/monetización
```

**Reglas no negociables del programa:**
- **Ninguna intervención toca un mandato en vuelo.** El 63% de los ingresos sigue fluyendo intacto durante la transformación. *Ring-fence* operativo explícito.
- **Reparar antes de medir.** El SLA de comunicación al candidato se arregla ANTES de lanzar cualquier CSAT. Encuestar a candidatos ya *ghosteados* sin haber cerrado el loop genera **más** *backlash* en LinkedIn, no menos.
- **Human-in-the-loop obligatorio** en todo rechazo y en la terna. La IA pre-ordena; el humano decide. El auto-rechazo a "rank 30+" se elimina como decisión final automática.
- **El presupuesto de la temporal (3 meses) descarga la OPERACIÓN de Lili** (su pedido real, su seguro anti-fuga), **no** se quema en tareas de datos para las que no está calificada. La estructuración de datos la ejecutamos nosotros.

---

## Precondiciones bloqueantes globales (cerrar HOY)

| # | Precondición | Por qué bloquea | Dueño | Fecha límite |
|---|---|---|---|---|
| P1 | **País exacto de operación + residencia de candidatos/clientes** | Define ley de datos (Ley 8968 CR / Ley 81 PA / Ley 787 NI / habeas data GT), registro ante regulador, viabilidad del benchmark y exposición UE (GDPR Art. 22 / AI Act) | Virginia (email de 5 min) | **Lunes** |
| P2 | **Tier de Team Tailor: ¿API REST + export masivo + custom fields + límites?** | Sostiene extracción, baseline retrospectiva, dedup y RAG. Sin esto, medio Fase 0–1 colapsa | Consultoría + admin TT del cliente | Spike sem. 1 |
| P3 | **Origen y consentimiento de los 4000** (¿aplicaron vs *sourced* de LinkedIn?) | Define qué usos secundarios (benchmark, cross-sell) son legales | Virginia + revisión legal local | Spike sem. 1 |
| P4 | **¿Existe historial recuperable de "quién entró a terna vs no"?** (*golden set*) | Sin él, calibrar el Screener obliga a Virginia a re-etiquetar cientos de CVs — esfuerzo mayor no financiado | Lili/Virginia | Spike sem. 1 |

> **Colisión de calendario — atención.** La reunión Virginia–Lili es el **martes**; la propuesta es el **viernes**. Los artefactos de adopción para esa reunión (descripción del rol "Embajador de Marca", "día de Lili antes/después", mapa de proceso co-autorable) deben estar listos el **lunes**. El martes es el verdadero primer hito político del proyecto.

---

## FASE 0 — Quick win + Diagnóstico ⭐

**Duración:** 2–3 semanas (incluye el Spike de Factibilidad en la semana 1).
**Objetivo:** ganar credibilidad con un entregable **visible y táctil** en días, mientras se levanta la foto honesta del "es actual" y se apagan los supuestos frágiles. Es nuestro costo de adquisición: precio deliberadamente digerible (⚠️ orden de ~1–1.5 meses de la temporal) a cambio de derechos de caso de referencia y referidos.

### 0.0 — Spike de Factibilidad (semana 1, pagado)
Cierra P2, P3, P4 y valida P1. Entregable: memo de 2 páginas que confirma o reconfigura el alcance de las fases siguientes. **Sin esto no prometemos ningún P0.**

### Entregables concretos

| Entregable | Descripción | ¿Quick win? |
|---|---|---|
| **⭐ Plantilla/SOP de CV con branding v1** | Formalizar el *prompt* de Virginia como activo de la firma: esquema fijo (extracción a JSON validado) + plantilla determinista (el LLM normaliza/redacta, NO maqueta). Versionado, con *ownership* de la firma. Adoptado por los 4 reclutadores | **SÍ — visible** |
| **⭐ Dedup / registro de presentaciones candidato-cliente** | Check determinista (no IA): SQL/API o, si P2 falla, hoja estructurada + regla obligatoria antes de enviar terna. Alerta de duplicado. Cierra el riesgo reputacional ya materializado | **SÍ — emocional** |
| **Cortar la inyección de PII en ChatGPT de consumo** | Migrar el *prompt* a entorno con no-entrenamiento + DPA. Cierra una brecha legal **activa hoy**, costo casi nulo | **SÍ — riesgo** |
| **Kit de candidate experience v0** | SLA mínimo de comunicación (acuse 48h, rechazo personalizado) + plantillas. **Se despliega ANTES de medir CSAT** | SÍ — reputación |
| **Baseline retrospectiva (extremos)** | *Process mining* del *event log* de TT: time-to-submit y time-to-fill por mandato + nº reenvíos. Reportar p50/p90, **solo extremos confiables**, con *caveats* explícitos por etapas inconsistentes | SÍ — datos |
| **Diagnóstico "es actual" del cribado** | *Shadowing* de 45 min a los 4 reclutadores sobre 1 vacante real (swimlane/SIPOC del paso 4). Determinar si las 4 formas difieren por **criterio** o solo por **formato** | — |
| **Mapa de actores nominal + auto-registro de horas** | Postura de cada uno (Manuel incluido), palanca de conversión; 1 semana de registro de horas en cribado = el "antes" cuantificado | — |
| **Kit para la reunión del martes** | Descripción del rol *Embajador de Marca*, "día de Lili antes/después", mapa de proceso co-autorable | — (entregar **lunes**) |

### Precondiciones
- Acceso a Team Tailor (lectura) y al *prompt* de Virginia. Sponsor (Virginia) compromete su adopción pública primero.
- País confirmado (P1) para el corte de PII y el aviso de privacidad.

### Dependencias
- El Spike (0.0) precede a cualquier promesa de extracción. La baseline retrospectiva **depende de P2**; si la API/export no existen, se degrada a muestreo manual y se comunica como tal.

### Métrica de éxito (go/no-go a Fase 1)
**Fase 0 exitosa = (a) plantilla CV adoptada por los 4 reclutadores + (b) dedup operando con ≥1 duplicado real detectado/prevenido + (c) baseline de 3 KPIs de extremos entregada + (d) brecha de ChatGPT cerrada.** Si no se cumple (a)+(b), **paramos antes de Fase 1.**

---

## FASE 1 — Estandarizar, documentar e instrumentar

**Duración:** 4–6 semanas.
**Objetivo:** convertir el conocimiento tácito (el "ojo clínico" de Virginia) en un **estándar explícito, medible y replicable**, y poner la base de datos en estructura. Esta es la fase de mayor valor real y el activo que ningún competidor con IA puede copiar sin la artesanía detrás. **El entregable más valioso de los primeros 60 días no tiene una sola línea de código.**

### Entregables concretos

| Entregable | Descripción |
|---|---|
| **Scorecard de intake + SOP del cribado con rúbrica ponderada** | Co-diseñado en *workshop* con los 4 (ownership = adopción). Criterios, pesos, must-have/nice-to-have, anclas de evaluación, banderas de descarte, definición de éxito a 90 días. Es el "deber ser" del paso 1–2 y 4 |
| **Stage-gates únicos en Team Tailor** | 6–8 etapas con criterios de entrada/salida (p.ej. terna = exactamente 3 finalistas validados), forzadas para los 4. **Prerrequisito duro** de toda métrica de *funnel* forward |
| **Captura de líneas base forward** | 6–8 campos obligatorios al abrir mandato (fecha apertura, rango salarial, hiring manager, familia de rol, fuente, fecha terna, fecha oferta aceptada) |
| **Árbol de métricas en 1 página** | North Star: *fill rate* dentro de SLA + colocaciones/reclutador. Ramas: velocidad, calidad, experiencia, activo/base, riesgo. CSAT de 1 pregunta (1–5), reportando siempre el *n*; NPS solo con n≥30. ⚠️ time-to-fill se reporta, **no** se promete (no lo controlan) |
| **Diccionario de datos + taxonomía (ESCO + overlay local)** | Vocabulario estándar ANTES de enriquecer: skills, sectores, estados de ciclo de vida (vigente/en proceso/no vigente/no contactar). ESCO como esqueleto + overlay curado de 15–30 títulos centroamericanos. ⚠️ La curaduría local NO es gratis: es trabajo real |
| **Capa de extracción vía API sobre TT (NO migrar)** | Postgres + object storage para CVs. Sincronización incremental. **Solo si P2 lo permite.** Decisión de salir del ATS se pospone a Fase 3 |
| **Marco de gobernanza de datos (RoPA-lite)** | Inventario de tratamiento, base legal por finalidad, retención/purga, aviso de privacidad en el punto de aplicación, consentimiento granular (reclutamiento / capacitación / estudios de comp). **DPA cliente–consultora**: al exportar PII nos volvemos sub-procesadores; cifrado, control de accesos, borrado al cierre |
| **Gate "Listo para IA" (checklist 1 pág.)** | Artefacto que cada SOP debe aprobar antes de construir su agente: I/O documentado, rúbrica explícita, datos estructurados, excepciones/escalamiento, métrica + baseline, *golden set*, guardarraíles de lo que NO debe hacer |

### Precondiciones
- Fase 0 superada. **Tiempo protegido de Lili (4–6 h/sem) para co-diseño**, financiado descargando su operación con la temporal. Disposición de Virginia a documentar su criterio (retar este punto explícitamente).
- País y base legal confirmados (P1, P3) para gobernanza y extracción.

### Dependencias
- El diccionario de datos precede a cualquier enriquecimiento. Los stage-gates preceden a las métricas forward limpias. La gobernanza precede a tocar la base.

### Métrica de éxito (go/no-go a Fase 2)
Scorecard + SOP del cribado **en uso** por los 4 · stage-gates únicos aplicándose en ≥90% de mandatos nuevos · diccionario de datos v1 aprobado · líneas base forward capturándose · gate "Listo para IA" aprobado para el paso 4. **Si el SOP no se adopta, no se construye el agente.**

---

## FASE 2 — IA asistida (copiloto, human-in-the-loop)

**Duración:** 6–10 semanas, **modular por agente**.
**Objetivo:** acelerar el proceso **ya estandarizado** sin escalar la inconsistencia. **No** se construyen los "6 agentes": de ellos, 5 son herramientas con salida estructurada y solo 1 (Sourcer) es agéntico. Se pilotan **1–2** donde el ROI es claro y el riesgo bajo.

### Reencuadre técnico
Reframe de "6 agentes" → **3 herramientas deterministas + 1 orquestador con routing determinista y HITL.** Los guardarraíles del cliente (top10=llamada · 10-20=abierto · 30+=rechazo cordial) se materializan **como código** (structured output, allowlist por paso), no como instrucción de *prompt*. La IA no puede "opinar fuera de scope" porque la arquitectura no se lo permite. **Este guardarraíl es el mejor mensaje de adopción: "tú decides, la IA pre-ordena".**

### Entregables concretos

| Entregable | Descripción |
|---|---|
| **CV-tool con branding productizada** | Extracción a esquema + plantilla determinista. Riesgo nulo (no decide sobre personas), entregable visible. Evolución directa del quick win de Fase 0 |
| **Screener/Ranker asistido** | Pipeline: **des-identificar PII** (foto/edad/estado civil/origen) → extraer evidencia contra el scorecard → score con cita textual al CV (sin inventar) → ranking. Construido **CON** Virginia sobre su rúbrica + *golden set*. La IA pre-ordena; **humano aprueba top10 y terna** |
| **Piloto de concordancia (HITL)** | En 1–2 búsquedas reales: IA rankea, reclutador valida independiente; se mide "la IA coincidió en X de 10". Confianza por evidencia, no por fe. Protocolo: gana el humano, se ajusta la rúbrica |
| **Auditoría de sesgo del Screener** | Selection rate por género/edad; exclusión explícita de variables proxy prohibidas; documentación del resultado **antes** de producción |
| **Entrevistador pre-screening (ASR comprado, no construido)** | Consentimiento de grabación → transcripción → resumen estructurado por esquema (competencias con cita, banderas, preguntas de seguimiento). La IA no concluye aptitud |

### Precondiciones (gate "Listo para IA" aprobado)
- Scorecard + rúbrica + *golden set* existentes y validados por Virginia (P4). Stage-gates y línea base de Fase 1 operando. DPAs con proveedores de IA/ASR firmados. HITL obligatorio configurado.

### Dependencias
- **Dependencia circular a romper (explícita):** liberar a Lili requiere IA de cribado → que requiere *golden set* → que requiere tiempo de Virginia. **Se rompe** descargando la operación de Lili con la temporal (Fase 0–1) y **extrayendo el conocimiento de Virginia en las primeras 2–3 semanas** (mitigación de *flight risk*), no al final.

### Métrica de éxito (go/no-go a Fase 3)
Concordancia IA–criterio de Virginia ≥ **X%** ⚠️ (umbral a fijar con ella sobre el *golden set*) en 2 búsquedas reales · 0 rechazos automáticos sin revisión humana · auditoría de sesgo sin disparidad material · reducción medible de time-to-submit vs baseline (meta: 5 días → **48–72 h**, **no** "mismo día"). **Si la IA no replica el criterio que el cliente reconoce como propio, no escala.**

---

## FASE 3 — Orquestación, escala y monetización (land-and-expand)

**Duración:** trimestral, modular, **autofinanciada** por el valor demostrado.
**Objetivo:** convertir la base en activo vivo y abrir nuevas líneas de ingreso, **estrictamente condicionadas a la base legal de Fase 1.** Aspiracional, no inmediata.

### Entregables concretos (todos opcionales, con gate propio)

| Entregable | Condición de activación |
|---|---|
| **Estructuración + enriquecimiento de la base** (parsing LLM a campos, entity resolution / *golden record*, score de vigencia, búsqueda híbrida pgvector) | Diccionario de datos y gobernanza de Fase 1 cerrados. ⚠️ El parsing cuesta centavos de cómputo pero **semanas de QA, dedup y mapeo** — no subestimar |
| **Portal de auto-actualización del candidato (mercado interno)** | Consentimiento resuelto. Refresca vigencia sin trabajo manual y resuelve el dolor de LinkedIn |
| **Decisión ATS: augmentar vs migrar** | Con datos reales de límites de API y costo. **NO antes.** Migrar sin estructura replica el desorden en sistema más caro y nos vuelve responsables de seguridad/brechas |
| **Sourcer agéntico** | Base estructurada + guardarraíles validados |
| **Benchmark de compensaciones** | ⚠️ **Solo con dictamen legal favorable.** Requiere: contratos que permitan reutilizar comp-data, k-anonimato (N mínimo por celda — en mercado pequeño el "CFO de empresa X" es re-identificable aun agregado), consentimiento granular. **Camino positivo alternativo:** alianza con proveedor licenciado de comp-data. Puede estar legalmente muerto de origen; no se ancla la propuesta en él |
| **Cross-sell de capacitaciones a la base** | Consentimiento separado opt-in. Reutilizar datos de reclutamiento para marketing sin base legal viola limitación de finalidad |

### Precondiciones
Base legal cerrada y trazada al origen · muestreo de vigencia que confirme que el activo justifica la inversión · economía unitaria positiva demostrada.

### Métrica de éxito
Internal-fill rate de baseline desconocido → **30–40% en 6–9 meses** ⚠️ · vigencia de la base ≥50% ⚠️ · nueva línea de ingreso lanzada **solo** si pasó el gate legal · decisión ATS tomada con caso de negocio cuantificado.

---

## Economía del programa y asequibilidad (lo que la crítica exigió)

> **Honestidad sobre el dinero, no un menú sin precios.**

- **Ancla de precio del cliente:** ~US$1.5k–2.7k (3 meses de temporal). Competir contra ese número nos posiciona como mano de obra. **Reencuadre:** "una temporal añade capacidad lineal por 3 meses y se va dejando el mismo desorden; nosotros instalamos estándar + datos + métricas que quedan y se componen."
- **Costo total all-in del *build* completo (Fases 0–3) excede con holgura el techo mental del cliente.** ⚠️ Por eso el **camino por defecto es BUY**: activar la IA que Team Tailor ya cobra + SOPs livianos + dedup en hoja/campo. El *build* a medida (pgvector, agentes custom, ASR) se reserva **solo** si el volumen (⚠️ ¿20–60 colocaciones/año?) y el *fee* por colocación lo justifican.
- **Plantilla de economía unitaria (lista para enchufar el número que falta):**
  `Payback por fase = (fee por colocación × colocaciones incrementales por mayor velocidad/internal-fill) − costo del sistema`
- **⚠️ Dato bloqueante para todo ROI:** *fee* por colocación + volumen de mandatos/mes. Primera pregunta de la reunión, no un detalle.
- **Validez estadística:** a 20–60 colocaciones/año, NPS, *accuracy* del ranker y auditoría de sesgo tienen *n* limitado. Reportar siempre conteos absolutos y *n*; no construir maquinaria de datos pesada para un dataset que no da significancia.

### Cuadro de alternativas (para pre-emptar lo que Virginia ya piensa)

| Opción | Costo | Activo resultante | Riesgo |
|---|---|---|---|
| No hacer nada | $0 | Sigue el caos, sigue el daño en LinkedIn, sigue el riesgo de reenvío | Erosión reputacional |
| Solo la temporal | ~$2.7k | Alivio 3 meses, **cero capacidad instalada**, dependencia vuelve en mes 4 | Dinero evaporado |
| Firma grande | $$$ | *Deck* genérico, sin cercanía al negocio | Caro, lento, sin *ownership* |
| **Nosotros (este roadmap)** | Por fase, *go/no-go* | Estándar + datos + métricas que quedan y se componen | Acotado por gates |

---

## Recursos y capacidad de entrega (ambos lados)

| Frente | Quién | Nota |
|---|---|---|
| Data/IA, arquitectura, métricas | Víctor (consultoría) | Núcleo de competencia |
| **Dominio RRHH / "deber ser"** | **Lili como co-autora obligatoria** | ⚠️ Víctor NO es de RRHH; el proceso diseñado sin Lili será rechazado por quienes lo ejecutan |
| **Legal / protección de datos / antitrust** | **Subcontratar abogado local** | Reconocemos no tener esta competencia in-house. Vincular antes de cualquier producto de datos |
| ASR español regional | Comprar, no construir | — |
| Operación de Lili (descarga) | Temporal (3 meses) | Su pedido real + seguro anti-fuga. NO hace tareas de datos |

> ⚠️ **Colisión de nombres a aclarar:** el consultor líder se llama Víctor y hay un reclutador "Víctor" en el cliente. Confirmar si son la misma persona (afecta gobernanza y conflicto de rol).

---

## Riesgos transversales y mitigaciones

| Riesgo | Severidad | Mitigación |
|---|---|---|
| **Fuga de Lili por burnout (7am-7pm)** — punto único de falla, champion y cuello de botella a la vez | **Crítica** | Descargar su operación en semana 1; extraer su conocimiento en sem. 2–3; enmarcar la temporal como seguro de retención |
| Automatizar el desorden (presión propia por entregar IA vistosa) | Alta | Gate "Listo para IA" no negociable; quick win es un SOP, no un agente |
| API/export de Team Tailor no disponible en el tier | Alta | Spike de Factibilidad lo cierra antes de prometer; plan B = muestreo manual comunicado como tal |
| *Golden set* inexistente | Alta | Confirmar en Spike; si no existe, financiar su creación explícitamente con tiempo de Virginia |
| Benchmark de comp = bomba legal (re-identificación, NDAs) | Alta | Fuera de ruta crítica; condicionado a dictamen; camino positivo vía proveedor licenciado |
| Primer proyecto fallido = **anti-referencia** existencial | Alta | Gates go/no-go y kill-criteria por fase; alcance quirúrgico; no sobre-prometer |
| Discriminación algorítmica a escala | Alta | Des-identificación + auditoría de sesgo antes de producción; HITL |
| Continuidad del 63% de ingresos durante la transformación | Media | Regla "ninguna intervención toca un mandato en vuelo" |
| Sobre-estandarizar el diferenciador (craft) | Media | Estandarizar el back-office; **preservar** juicio humano en terna, negociación y relación con el candidato |

---

## El reto a Virginia (con un SÍ, no un muro de NOs)

La propuesta dice "todavía no" a casi todo lo que ella amó: "mismo día", los 6 agentes, vender el benchmark, salir del ATS, la persona extra. Para que no se sienta sermoneada por un experto en datos sin credibilidad de dominio, el reencuadre es de **secuencia, no de negación**:

- *"Tu visión de clase mundial y cercanía es correcta. La estamos protegiendo: si automatizamos sobre el caos actual, escalamos la inconsistencia a velocidad de máquina y destruimos justo el 'ojo clínico' que te hace premium."*
- *"Tu diferenciador no será la IA — la disciplina de proceso lo será. La IA es la última milla, no la primera."*
- *"El pedido de Lili de 'una persona más' es la trampa elegante de no tocar el oficio: un quinto reclutador sin estándar solo añade una quinta forma de hacer las cosas. Le devolvemos sus 4 horas y la subimos de operativa a embajadora de marca."*
- *"El benchmark es tu mayor oportunidad Y tu mayor riesgo: lo construimos bien, no rápido — o con un socio que ya tiene la licencia."*

---

## Próximos pasos inmediatos

1. **Lunes:** Virginia confirma el país (P1) y entrega los artefactos para la reunión con Lili.
2. **Martes:** reunión Virginia–Lili — ganar a Lili como co-autora y embajadora (punto de fallo político, no logístico).
3. **Viernes:** presentar este roadmap + opciones de pricing por fase + **un teaser táctil** (un CV real reformateado con su branding + el concepto de dedup). Mostrar, no prometer.
4. **Arranque:** Spike de Factibilidad (1 semana) que apaga los 4 supuestos antes de comprometer alcance y precio de Fases 1–3.

> ⚠️ **Lista de datos a validar para cerrar cifras:** país; *fee* por colocación y modelo de cobro; volumen de mandatos/mes y colocaciones/año; tier y API de Team Tailor; % de la base vigente/con consentimiento; existencia de *golden set*; si el cliente devuelve retención a 90 días; presupuesto real más allá del techo mental de la temporal.
