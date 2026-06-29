# Diagnóstico de Situación Actual
### Conexión Talento — Proyecto "Conexión Talento IA" | Fase de Descubrimiento

---

## 0. Cómo leer este documento

Este es un documento de **diagnóstico**, no de propuesta. Su objetivo es establecer una línea de verdad —defendible y sin complacencia— sobre el estado actual de Conexión Talento en sus dimensiones de proceso, datos, tecnología, métricas y personas; mapear el proceso de reclutamiento de 8 pasos contra su "deber ser"; y emitir un veredicto fundamentado sobre Team Tailor.

Dos disciplinas atraviesan el documento:

1. **Honestidad sobre lo que sabemos vs. lo que suponemos.** Todo dato no confirmado por el cliente se marca con ⚠️ y se trata como *supuesto a validar*, no como hecho. Varios de estos supuestos son **bloqueantes**: condicionan el alcance, el riesgo legal y la viabilidad técnica. No se difieren como "preguntas abiertas"; se elevan como **precondiciones con dueño**.
2. **Separar el síntoma de la causa.** El cliente percibe el problema como "falta una persona" y la solución como "6 agentes de IA". El diagnóstico sostiene una tesis distinta y la defiende con evidencia.

---

## 1. Síntesis ejecutiva (BLUF)

> **Tesis central:** Conexión Talento no tiene un problema de tecnología ni de capacidad; tiene un problema de **disciplina de proceso**. Opera un proceso de 8 pasos ejecutado de cuatro maneras distintas por cuatro personas, sin estándar documentado, sin métricas instrumentadas y con un activo de datos (4.000 candidatos) que hoy es **potencial sin refinar, no "oro" líquido**. Automatizar este estado con IA no resolvería el problema: **escalaría la inconsistencia a velocidad de máquina** y erosionaría justo el "ojo clínico" y la "cercanía al candidato" que hacen premium a la firma.

**Los cinco hechos que definen el punto de partida:**

| # | Hallazgo | Implicación |
|---|----------|-------------|
| 1 | El cuello de botella real **no es el cribado de 200 CVs**, es el **intake** (pasos 1–2). Sin un *scorecard* calibrado, los 4 reclutadores aplican 4 criterios y la terna depende del juicio no escalable de Virginia. | "Garbage in, garbage out": acelerar el cribado sin estandarizar el origen produce malos *matches* más rápido. |
| 2 | La promesa de marca —"cercanía al candidato"— **contradice la realidad operativa**: atacan en LinkedIn por falta de seguimiento; el único contacto sistemático con el rechazado es un correo automático a 15 días. | El diferenciador que quieren *vender* es hoy su mayor **pasivo reputacional**. |
| 3 | "Cero métricas" es **parcialmente falso**. Team Tailor registra *timestamps* y etapas. Existe una línea base **recuperable** ⚠️ (sujeta a verificación de API/export y a la contaminación por uso inconsistente de etapas). El problema es de **lectura**, no de inexistencia. | La línea base es recuperable, pero **solo confiable en los extremos** (apertura→terna→cierre); los tiempos intermedios son ruido hasta estandarizar etapas. |
| 4 | Enviar el mismo candidato dos veces al mismo cliente **no es una anécdota**: es ausencia de *submission ownership* e historial. Es un fallo de control determinista, no un problema de IA. | Riesgo reputacional **ya materializado**; corregible con un registro simple, no con un modelo. |
| 5 | La base de 4.000 candidatos **no es "oro" todavía**. Sin clave de identidad única, sin taxonomía de *skills*, sin protocolo de vigencia. Estimación gruesa ⚠️: 30–50% podría no estar vigente. El número honesto es "candidatos vigentes y contactables", probablemente **1.500–2.500** ⚠️. | El "60% del valor" es potencial **condicionado** a una estructura de datos que aún no existe. |

**Madurez global:** Conexión Talento se sitúa en un **Nivel 1–2 de 5 ("Inicial / Reactivo")** en una escala de madurez digital. El conocimiento es tácito, los procesos son artesanales y el dato está sin gobernar. Esto **no es una crítica**: es típico de una PYME consultora exitosa cuyo valor reside en el criterio humano. El reto es industrializar el *back-office* sin commoditizar el *craft*.

---

## 2. Supuestos bloqueantes (precondiciones, no "preguntas abiertas")

La crítica adversarial es contundente en este punto y la incorporamos: **no se puede dimensionar ni prometer nada** mientras estos supuestos sigan abiertos. Cada uno tiene dueño y plazo.

| ID | Supuesto a validar ⚠️ | Por qué bloquea | Dueño / Cómo se cierra |
|----|----------------------|-----------------|------------------------|
| **B1** | **País exacto de operación** (y residencia de candidatos/clientes). | Define la ley de datos (Ley 8968 CR + PRODHAB · Ley 81 Panamá + ANTAI · Ley 787 Nicaragua · *habeas data* Guatemala), la viabilidad del benchmark salarial y la exposición a GDPR/EU AI Act si hay UE. | **Virginia — correo de 5 minutos. Cerrar HOY.** Es el dato más barato y más estructural del proyecto. |
| **B2** | **API / export / tier real de Team Tailor.** | Toda la estrategia de datos y la línea base retrospectiva cuelgan de esto. Si el plan limita llamadas o no permite export masivo, colapsa medio diagnóstico cuantitativo. | Consultor — verificación técnica directa en la cuenta. **No prometer ningún quick-win de datos hasta confirmarlo.** |
| **B3** | **Existencia de un *golden set*** (historial recuperable de quién entró a terna vs. no). | Sin él no se puede calibrar ni evaluar un *ranker* contra el criterio de Virginia. Con "cero documentación", **probablemente no existe** y construirlo consume el recurso más escaso (tiempo de Virginia). | Consultor + Virginia — auditoría del ATS. Tratar como **esfuerzo no trivial**, no como insumo dado. |
| **B4** | **Origen y consentimiento de los 4.000** (aplicación voluntaria vs. *sourcing*/scraping de LinkedIn). | Cambia por completo la base legal para reutilizar/monetizar y el % realmente vigente. | Muestreo de vigencia + revisión de términos de aplicación actuales. |
| **B5** | **Modelo de honorarios y volumen** (fee por colocación, mandatos/mes, colocaciones/año ⚠️ est. 20–60). | Define la economía unitaria, el ROI y la **validez estadística** de toda métrica de embudo (a este volumen, NPS y auditorías de sesgo tienen *n* insuficiente). | Virginia — primera pregunta de scoping. |

> **Regla de gobierno:** ninguna afirmación cuantitativa de este diagnóstico se eleva a "hecho" hasta cerrar B1–B5. Lo que sigue se construye sobre lo observable y marca explícitamente lo supuesto.

---

## 3. Diagnóstico de madurez por dimensión

Escala: **1 Inicial · 2 Reactivo · 3 Definido · 4 Gestionado · 5 Optimizado.**

| Dimensión | Nivel actual | Evidencia (estado "es") | "Deber ser" mínimo viable (Nivel 3) | Brecha clave |
|-----------|:---:|-------------|------------------------|--------------|
| **Procesos** | **1 → 2** | Un proceso de 8 pasos, 4 ejecuciones distintas. Cero documentación. Único activo semi-estándar: el "prompt" de CV de Virginia (no versionado, vive en su cuenta). | SOP por paso con dueño (RACI), SLA, entradas/salidas y *scorecard* de intake. Estándar como **propiedad de la firma**, no de personas. | No se sabe aún si las 4 formas difieren por **criterio** (qué evalúan) o por **formato** (cómo registran). **Resolverlo es prerrequisito del scoping.** ⚠️ |
| **Datos** | **1** | 4.000 registros sin clave única, sin taxonomía, sin etiquetas, sin protocolo de vigencia. Duplicados confirmados (caso del candidato reenviado). No saben cuántos vigentes. | Modelo canónico (Candidato/Aplicación/Vacante/Cliente/Skill/Evento), resolución de identidad, *score* de vigencia, taxonomía (base ESCO + overlay local ⚠️ esfuerzo de curaduría real). | El dato es hoy **pasivo legal y operativo**, no activo. El "60% del valor" está sin materializar. |
| **Tecnología** | **2** | ATS Team Tailor en uso real (integración LinkedIn, psicométricas, rechazos automáticos). Funciones de IA **pagadas y no usadas**. ChatGPT de consumo con PII de candidatos (**brecha activa**). | Explotar lo ya pagado antes de construir. Capa de orquestación determinista sobre API. Cortar PII en ChatGPT de consumo (Enterprise/API con no-entrenamiento + DPA). | Sub-utilización, no carencia. El problema es de **adopción y configuración**, no de falta de herramientas. |
| **Métricas** | **1** | "No métricas" declarado. Sin KPIs de industria. Sin línea base. Sin seguimiento del plan a 90 días (que ya entregan y es, sin saberlo, su *quality-of-hire*). | Árbol de ~10 KPIs con North Star (*fill rate* dentro de SLA + colocaciones/reclutador). Captura forward + reconstrucción retrospectiva con *caveats*. | Los datos **existen** en el ATS pero no se leen. Brecha de **instrumentación y lectura**, no de generación. |
| **Personas** | **2** | 4 reclutadores + 1 temporal. Conocimiento tácito concentrado en Virginia ("ojo clínico") y Lili (operación). Lili a 7am–7pm: punto único de falla **y *flight risk*** no gestionado. | Dueño de proceso nombrado; conocimiento extraído y documentado; rol de "Embajador de Marca / Candidate Experience" que redefine la persona extra de *backfill* a capacidad. | Dependencia crítica de 2 personas. Si Lili renuncia por *burnout* antes de extraer su conocimiento, se pierden operación, memoria y *sponsor* de golpe. |

**Lectura transversal:** la firma es fuerte donde reside su valor (criterio humano, relación) y débil donde se industrializa el valor (proceso, dato, medición). El proyecto debe **estandarizar sin piedad el back-office** (cribado, etiquetado, formateo, registro) y **preservar el juicio humano** en terna, negociación y relación con el candidato. Sobre-estandarizar el diferenciador lo destruye.

---

## 4. Mapa del proceso de reclutamiento: "es actual" vs. "deber ser"

> **Nota de método:** este mapa documenta el flujo declarado. La distinción **criterio vs. formato** en las 4 variantes (paso 4 sobre todo) **no está resuelta** y debe levantarse mediante *shadowing* de una vacante real antes de diseñar el "deber ser" definitivo. Lo que sigue es el armazón, no el SOP final.

| # | Paso | Estado actual ("es") | Deber ser ("debe") | Dueño | Brecha / Riesgo |
|---|------|---------------------|-------------------|-------|-----------------|
| **1** | **Perfilamiento** | Tácito, depende del reclutador. Sin captura estructurada del contexto. | *Kickoff* estructurado **con el cliente**: contexto, 3–5 competencias críticas, definición de éxito a 90 días. | Reclutador (consultivo) | **Cuello de botella real.** Sin esto, ningún paso posterior tiene criterio. |
| **2** | **Redacción de perfil de puesto** | Variable, no calibrada de forma consistente al tamaño/contexto de la empresa. | Plantilla única calibrable. *Must-have* vs. *nice-to-have* con **pesos**. | Reclutador | Sin pesos explícitos, el cribado es subjetivo aguas abajo. |
| **3** | **Sourcing / búsquedas** | Manual; búsquedas + preguntas para revelar perfil real (artesanal, no documentado). | Búsqueda booleana estándar + uso de la base interna como **primera fuente** (hoy no se mide *internal-fill*). | Reclutador | Único paso genuinamente "agéntico" (decisiones iterativas). Se sub-explota la base. |
| **4** | **Cribado de ~200 CVs** (puntuar → top 10 → terna) | **4 personas, 4 criterios.** Rúbrica tácita en el "ojo clínico" de Virginia. Mayor consumo de horas. | *Scorecard* explícito y ponderado + *golden set* de referencia. Cribado asistido **con humano validando**. | Reclutador + dueño de estándar | **Keystone de la estandarización.** Documentar la rúbrica es ~80% del valor de la fase de estándares. |
| **5** | **Pre-screening telefónico** ("a veces grabado" → IA) | Sin banco de preguntas ligado al *scorecard*. Grabación inconsistente, **sin consentimiento documentado** ⚠️. | Entrevista **estructurada** (predice desempeño ~2x mejor) con guion STAR por competencia + consentimiento de grabación. | Reclutador | Sin estructura, la IA de transcripción aporta **ruido, no señal**. Riesgo legal de grabación. |
| **6** | **Terna** | Depende del juicio de Virginia; sin *quality gate* uniforme. | Terna = exactamente 3 finalistas validados contra *scorecard*. **Gate anti-duplicado obligatorio**. | Virginia / reclutador | *Craft* a preservar. Pero requiere verificación determinista previa al envío. |
| **7** | **Negociación / cierre con cliente** (plan de desarrollo a 90 días) | Se entrega como "valor"; **no se instrumenta** ni se recupera el dato a 90 días. | Clausular la **devolución del dato de retención/desempeño a 90 días** = KPI de *quality-of-hire* + gancho de cross-sell. | Virginia | *Craft* a preservar. Se está regalando la métrica más vendible de todas. |
| **8** | **Formateo de CV con branding** | "Prompt" de Virginia en ChatGPT de consumo. **Único proceso semi-estándar**, no versionado, con **PII en herramienta de consumo (brecha activa)**. | Plantilla determinista (el layout no lo decide el LLM) + extracción a esquema fijo. Versionado y propiedad de la firma. Entorno con no-entrenamiento + DPA. | Dueño de estándar | **Candidato natural al primer quick-win** de bajo esfuerzo y alta visibilidad. |

### 4.1 Los "6 agentes": reencuadre honesto

El cliente visualiza 6 agentes de IA. El diagnóstico técnico es inequívoco: **de los 6, solo 1 (Sourcer) es verdaderamente agéntico.** Los otros 5 son *prompt-chains*/herramientas con salida estructurada y *routing* determinista.

| "Agente" que visualiza el cliente | Qué es en realidad | Veredicto de secuencia |
|-----------------------------------|--------------------|------------------------|
| 1. Perfilador | Herramienta de plantillas + RAG sobre fuentes curadas | Requiere biblioteca de competencias/salarios **verificable**; cifras salariales **nunca** generadas por LLM. |
| 2. Redactor | Plantilla con LLM normalizador | Depende del SOP del paso 2. |
| 3. Sourcer | **Único agéntico** (búsqueda iterativa) | Aspiracional; depende de base estructurada. |
| 4. Screener/Ranker | Scorer contra rúbrica + *ranking* | El de **mayor palanca**, pero exige *golden set* y des-identificación de PII. Humano valida top 10. |
| 5. Entrevistador pre-screening | ASR (comprar) + resumen estructurado | Requiere consentimiento + entrevista estructurada previa. |
| 6. Generador de CV | Extracción a esquema + plantilla determinista | **Quick-win** de menor riesgo. |

> **Conclusión:** no se construyen 6 agentes en paralelo. Se construyen **3 herramientas deterministas confiables** (CV, dedup, cribado asistido) con humano-en-el-loop, **sobre proceso ya estandarizado**, y se reserva la autonomía agéntica solo donde aporta. El guardarraíl del cliente —"la IA no opina fuera de scope"— es correcto y debe materializarse **como código** (salida forzada por esquema), no como instrucción de *prompt*.

### 4.2 Corrección crítica al guardarraíl de auto-rechazo

El guardarraíl propuesto por el cliente —*rank* 30+ = **rechazo cordial automático**— es el **mayor pasivo legal y reputacional del diseño**. En una empresa a la que **ya atacan en LinkedIn** por falta de seguimiento, dejar que la IA rechace sin aprobación humana amplifica el problema y constituye **decisión automatizada** (intervención humana exigible si hay exposición UE; *profiling*). **Recomendación firme: el rechazo es *human-in-the-loop* obligatorio** —o como mínimo, *batch* revisado antes de enviar—. Esto, además de cumplir, **protege el diferenciador de cercanía**.

---

## 5. Evaluación de Team Tailor

### 5.1 Qué hace bien (y ya se paga)

- **Integración con LinkedIn** (link de aplicación) operativa.
- **Envío automático de pruebas psicométricas** funcionando.
- **Correos automáticos de rechazo** (a 15 días) — funcionan, aunque su *timing* y tono son parte del problema de experiencia.
- **Registro silencioso de eventos** (*timestamps*, movimientos de etapa) sobre ~4.000 candidatos → **línea base histórica latente**.
- **DPA y funciones de cumplimiento integradas** como procesador de datos: relevante, porque migrar a sistema propio **trasladaría a una PYME de 10 personas** toda la responsabilidad de seguridad, notificación de brechas y atención de derechos ARCO.
- **Funciones de IA incluidas** en el plan ⚠️ (alcance a confirmar) — **pagadas y no usadas**.

### 5.2 Qué no hace bien (o no se está usando)

- **Sub-utilización severa:** las funciones de IA pagadas no se usan; trabajo manual pese a herramientas disponibles.
- **Etapas usadas de forma inconsistente** (4 personas) → contamina los tiempos intermedios del embudo.
- **Sin custom fields/tags estructurados** que hagan la base buscable por *skill*.
- **Sin gate anti-duplicado** nativo aprovechado → permitió el reenvío del mismo candidato.

### 5.3 Decisión: ¿augmentar o reemplazar?

> **Veredicto: AUGMENTAR. No migrar — todavía y probablemente no.** La disposición de Virginia a dejar el ATS es comprensible pero **resuelve el problema equivocado**: migrar 4.000 registros sin taxonomía ni protocolo solo replicaría el desorden en un sistema nuevo y más caro, y pondría en riesgo la operación que genera el **63% de los ingresos**.

**Criterios de decisión (a evaluar con datos, no por impulso):**

| Criterio | Umbral que justificaría **augmentar** (default) | Umbral que justificaría **reemplazar** |
|----------|------------------------------------------------|----------------------------------------|
| **API / export** (B2) | API REST con export másivo disponible en el tier actual → se extrae y enriquece **por encima** sin migrar. | Sin export másivo / *rate-limit* prohibitivo que impida explotar el dato. |
| **Funciones de IA pagadas** | Cubren matching/screening/ASR con calidad aceptable → exprimir antes de construir. | No existen o son inservibles para el caso. |
| **Costo total de propiedad** | TCO de quedarse < TCO de construir+operar+asumir compliance. | Costo de quedarse demostrablemente superior **con caso de negocio**. |
| **Riesgo de seguridad/compliance** | Mantener el DPA y los controles de TT reduce exposición de la PYME. | Solo si se cuenta con controles propios equivalentes. |
| **Volumen** ⚠️ (20–60 colocaciones/año) | A este volumen, **construir custom probablemente da ROI negativo por años**. Favorece *buy*. | Solo si el volumen escala materialmente. |

> **Declaración de integridad (incorporada de la crítica adversarial):** existe un **conflicto de interés estructural** —nuestro ingreso crece cuanto más custom se construya—. La recomendación honesta para el primer proyecto es **exprimir lo que Team Tailor ya cobra y comprar *add-ons* antes de construir infraestructura propia**. Lo declaramos explícitamente. La decisión augmentar-vs-reemplazar se toma en una fase posterior, **con datos de B2 y B5**, no en este diagnóstico.

---

## 6. Riesgos del estado actual (priorizados)

| Severidad | Riesgo | Naturaleza | Mitigación inmediata |
|:---:|--------|-----------|----------------------|
| 🔴 **Crítico** | **Brecha activa de PII**: CVs de candidatos en ChatGPT de consumo. | Legal / hoy | Cortar uso; migrar a entorno con no-entrenamiento + DPA. Costo casi nulo. |
| 🔴 **Crítico** | **Reenvío de candidato al mismo cliente** ya materializado. | Reputacional / operativo | Registro de presentaciones (candidato × cliente × fecha) + regla de no-reenvío. Determinista, días. |
| 🔴 **Crítico** | ***Flight risk* de Lili** (7am–7pm, punto único de falla, *sponsor* de adopción). | Humano / continuidad | Aliviar **antes** de pedirle documentar; extraer su conocimiento en las primeras 2–3 semanas; enmarcar la temporal como **seguro anti-fuga**. |
| 🟠 **Alto** | **Benchmark de compensaciones** que el cliente quiere vender ya. | Legal (antitrust/datos) | **Congelar la venta.** Re-identificable aun agregado en mercado pequeño; posible violación de NDAs. Camino positivo: alianza con proveedor licenciado o producto futuro con consentimiento granular. |
| 🟠 **Alto** | **Daño reputacional en LinkedIn** por mala experiencia de candidato. | Reputacional | SLA de comunicación + plantillas. **Arreglar el SLA antes de lanzar CSAT** (encuestar a candidatos ya enojados provoca más backlash). |
| 🟠 **Alto** | **Sesgo algorítmico** si se cribara sobre datos históricos con PII (foto, edad, estado civil comunes en CVs de la región). | Legal-laboral / ético | Des-identificación antes del scoring; auditoría de impacto desigual antes de producción. |
| 🟡 **Medio** | **Sobrevaloración del activo de datos** (supuesto del "60%"). | Estratégico | Auditoría de vigencia **antes** de invertir en enriquecer. |
| 🟡 **Medio** | **Continuidad operativa**: el 63% de ingresos debe seguir fluyendo durante la transformación. | Negocio | Guardarraíl: ninguna intervención toca un mandato en vuelo. |

---

## 7. Tensiones entre dimensiones y ruta crítica

La crítica adversarial señaló con razón que las distintas perspectivas **se contradicen en la secuencia** y nadie lo reconcilia. Lo hacemos aquí explícitamente:

- **Datos** quiere extraer/parsear en paralelo temprano.
- **Procesos** quiere documentar primero ("no automatizar el desorden").
- **Métricas** necesita etapas estandarizadas antes de medir el embudo.

**Reconciliación — una sola ruta crítica:**

```
B1 país (HOY) ─┐
B2 API TT ─────┼──► [Spike de factibilidad técnica+legal, 1 sem]
B3 golden set ─┤        │
B4 consent. ───┘        ▼
                 Estandarizar etapas + scorecard de intake (proceso)
                        │
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
   Línea base       Quick-wins      Auditoría de
   (extremos)       deterministas   vigencia base
   con caveats      (dedup, CV)     (radiografía real)
          └─────────────┼──────────────┘
                        ▼
        Solo entonces: enriquecimiento de datos + IA asistida
```

**Dependencia circular que hay que romper (señalada por la crítica):** para estandarizar etapas hay que **liberar a Lili**; para liberarla ayuda la IA de cribado; para la IA de cribado hace falta el *golden set*; el *golden set* requiere tiempo de Virginia (el recurso más escaso y resistente por identidad).

> **Cómo se rompe:** la asistente temporal **descarga la operación de Lili** (su pedido real) para liberar 4–6 h/semana de tiempo protegido de Lili y Virginia destinado a *co-diseñar* el estándar y etiquetar el *golden set*. **No** se usa la temporal para "hacer data" mientras Lili sigue ahogada —eso quemaría a la *champion* en el mes 2.

---

## 8. Qué NO concluye este diagnóstico (límites de honestidad)

Para no caer en el mismo error que señalamos al cliente —prometer sobre supuestos frágiles—, declaramos los límites:

- **No afirmamos** que la línea base esté lista "en 2 semanas": depende de B2 y los tiempos intermedios estarán contaminados hasta estandarizar etapas. Solo los **extremos** serán confiables.
- **No afirmamos** que parsear 4.000 CVs sea trivial: el cómputo cuesta ⚠️ ~US$40–150, pero el **QA, la des-identificación, la dedup y el mapeo a taxonomía son semanas de trabajo calificado**, no centavos.
- **No afirmamos** el ahorro de "10–15 h/semana de Lili": es estimación hasta hacer un *time-tracking* ligero de 2 semanas. El ROI "IA vs. contratar" se construye **contra el costo de build**, no solo contra el costo de la temporal.
- **No afirmamos** que la base valga "60%": es marketing interno hasta que la auditoría de vigencia (B4) lo confirme o lo desmienta con datos.
- **No tratamos** el benchmark de compensaciones como línea de ingreso real: puede estar **legalmente muerto de origen** según B1/B4.

---

## 9. Conclusión del diagnóstico

Conexión Talento es una firma **valiosa y bien posicionada** cuyo problema no es la ausencia de tecnología, sino la **ausencia de disciplina de proceso, medición y gobierno del dato**. El estado actual es coherente con una PYME exitosa que creció sobre talento artesanal; el reto —y la oportunidad— es **industrializar el back-office sin matar el craft que la hace premium**.

El camino correcto está claro y va **a contracorriente del impulso inicial del cliente** (6 agentes, "mismo día", vender el benchmark, salir del ATS, contratar una persona más):

1. **Cerrar los 5 supuestos bloqueantes** (empezando por el país, hoy).
2. **Estandarizar, digitalizar y documentar** antes de automatizar.
3. **Recuperar la línea base** y empezar a medir lo que sí se controla (*time-to-submit*, *fill rate* dentro de SLA, *internal-fill*), no lo ajeno ("mismo día").
4. **Augmentar Team Tailor**, no reemplazarlo, hasta tener datos.
5. **Reparar la experiencia del candidato** —la "cercanía" prometida— como proceso verificable, no como eslogan.

> **La afirmación más defendible de todo el diagnóstico:** el primer entregable de valor para Conexión Talento **no tiene una sola línea de código**. Es un *scorecard* de intake, un SLA de comunicación al candidato y un registro anti-duplicado —artesanía de proceso que ningún competidor con IA puede copiar sin el criterio humano detrás—. Si un humano nuevo no puede seguir el SOP, la IA tampoco.

---
*Documento de diagnóstico — Fase de Descubrimiento. Las cifras marcadas ⚠️ son supuestos a validar y no deben citarse como hechos confirmados del cliente hasta cerrar las precondiciones B1–B5.*
