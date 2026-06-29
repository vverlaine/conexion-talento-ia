# Mapa de oportunidades — Conexión Talento

**Proyecto:** Conexión Talento · Reclutamiento & Selección (63% de ingresos)
**Documento:** Memoria del proyecto — Mapa de oportunidades (valor vs esfuerzo)
**Estado:** Borrador para discusión interna y base de la propuesta · v1
**Advertencia de datos:** Este mapa se construye **exclusivamente** sobre el diagnóstico disponible. Todo número económico, de volumen o de tiempo está marcado como **⚠️ supuesto a validar** porque el cliente aún no ha entregado fee por colocación, volumen de mandatos/mes ni país de operación. **Ninguna oportunidad P0 se promete en firme hasta cerrar el Spike de Factibilidad (Fase 0).**

---

## 1. Cómo leer este mapa (y qué corrige respecto del análisis inicial)

El análisis de las 8 lentes converge en una tesis correcta y la firmamos: **la disciplina de proceso —no la IA— es el diferenciador, y se construye primero**. Pero como documento de decisión, este mapa corrige cinco distorsiones que un mapa de oportunidades ingenuo arrastraría:

1. **La base de 4000 NO es "oro" todavía.** Es oro sin refinar e ilíquido. Su valor está condicionado, no realizado. Lo desarrollamos sin complacencia en §3.1.
2. **"Mismo día" es marketing, no KPI.** Separamos lo que el cliente controla (entrega de terna) de lo que no controla (cierre). Ver §3.2.
3. **El benchmark de compensaciones puede estar legalmente muerto de origen.** Lo tratamos como oportunidad **condicionada**, con bandera legal explícita y un camino positivo, no como línea de ingreso confirmada. Ver §3.3.
4. **Las etiquetas "esfuerzo bajo" son por tarea; el agregado es un programa de meses.** Por eso el mapa incluye una columna de dependencia y una sección de economía y capacidad (§5–§6) que el análisis original omitió.
5. **Varias oportunidades P0 cuelgan de supuestos no verificados** (API de Team Tailor, existencia de un golden set, país, consentimiento). Los convertimos de "preguntas abiertas" a **precondiciones bloqueantes con dueño** (§7).

**Convención de fases:**

| Fase | Nombre | Naturaleza |
|---|---|---|
| **Fase 0** | Spike de factibilidad + quick wins | Apaga supuestos frágiles; entrega 2 quick wins visibles. Precio "sí fácil". |
| **Fase 1** | Estandarizar → documentar → medir | El valor real. SOPs, scorecards, líneas base, gobernanza de datos. |
| **Fase 2** | IA asistida sobre proceso estandarizado | Solo lo que pasó el gate "Listo para IA". Human-in-the-loop. |
| **Fase 3** | Monetización del activo | Base como producto, mercado interno, benchmark (condicionado a base legal). |

---

## 2. Matriz valor vs esfuerzo

> Eje de valor = impacto en ingresos, riesgo evitado o credibilidad del primer proyecto. Eje de esfuerzo = costo + tiempo + dependencia técnica/legal **agregados** (no por tarea aislada).

```
   ALTO   │  [Q1] HACER YA                 │  [Q2] APUESTAS ESTRATÉGICAS
   VALOR  │  • Dedup / historial          │  • Estructurar la base (taxonomía+vigencia)
          │    candidato-cliente          │  • Screener/Ranker asistido (golden set)
          │  • SOP de cribado + scorecard │  • Mercado interno / portal candidato
          │  • Plantilla CV con branding  │  • Línea base forward + stage-gates
          │  • SLA candidate experience   │
          │  • Apagar PII en ChatGPT      │
          │  • Línea base retrospectiva*  │
   ───────┼───────────────────────────────┼──────────────────────────────────────
          │  [Q3] RELLENO / EVITAR        │  [Q4] CONDICIONADAS / CUIDADO
   BAJO   │  • Migrar del ATS "ya"        │  • Benchmark de compensaciones ⚠️LEGAL
   VALOR  │    (sin estructura) → NO      │  • Cross-sell capacitaciones ⚠️LEGAL
          │  • 6 agentes autónomos        │  • Sourcer agéntico
          │    en paralelo → NO           │  • Entrevistador (ASR) pre-screen
          │                               │
          └───────────────────────────────┴──────────────────────────────────────
              BAJO ESFUERZO                    ALTO ESFUERZO
```

*Línea base retrospectiva: alto valor pero su esfuerzo y viabilidad dependen de la API de Team Tailor (no verificada) y de etapas históricas inconsistentes. Por eso vive en Q1 **solo si** el Spike de Fase 0 la confirma; de lo contrario migra a Q2.

**Lectura ejecutiva:** la firma debe vivir en Q1 durante los primeros 60 días. Q2 es el land-and-expand. Q4 son oportunidades reales pero con riesgo legal que **no deben tocar el camino crítico de la propuesta del viernes**. Q3 son trampas que el cliente pidió (salir del ATS, los 6 agentes) y que rechazamos con argumento.

---

## 3. Las cinco tesis de valor desarrolladas

### 3.1 El "oro": la base de 4000 candidatos

**Tesis del cliente:** la base vale ~60% del valor.
**Nuestra tesis corregida:** la base es **oro sin refinar, ilíquido y en decadencia**. Su valor es *potencial condicionado*, no realizado. Hoy es tanto activo como pasivo.

Por qué no es oro todavía:

- **Sin clave de identidad única ni deduplicación.** Es lo que produjo el incidente de mandar el mismo candidato dos veces al mismo cliente — un riesgo reputacional ya materializado.
- **Sin taxonomía de skills/sectores.** No es buscable por competencia; cuatro personas etiquetan (cuando etiquetan) de cuatro formas.
- **Sin protocolo de vigencia.** Estimación de industria: **30–50% de la base podría estar vencida** (cambio de empleo, contacto muerto, >18 meses sin actividad). **⚠️ Supuesto a validar con muestreo.** El número honesto no es "4000 candidatos", es "candidatos vigentes y contactables por sector/skill", probablemente **1.500–2.500 ⚠️**.
- **Sin base legal trazable para uso secundario.** Parte pudo ser sourced de LinkedIn sin consentimiento de monetización (ver §3.3 y §7).

**El dato técnico que cambia el encuadre:** 4000 registros **no son big data** — caben en una tabla Postgres de pocos MB. El problema nunca fue el tamaño. Y el costo de *cómputo* de parsear los 4000 CVs con un LLM es marginal (**~US$40–150 una sola vez ⚠️**). **El costo real no es el cómputo: es el QA (muestreo humano 5–10% = 200–400 revisiones), la deduplicación, el manejo de PDFs escaneados con foto/multi-idioma y el mapeo a una taxonomía.** Eso son semanas de trabajo calificado, no centavos. Quien lea solo el titular de "$150" subestima el activo por un orden de magnitud.

**Secuencia correcta para refinar el oro (no negociable):**
> identidad única → deduplicación + timeline candidato-cliente → score de vigencia → taxonomía (ESCO + overlay local) → *recién entonces* embeddings / búsqueda semántica.

Saltar a la búsqueda vectorial "sexy" sobre una base sucia es ponerle un motor de Fórmula 1 a un carro sin ruedas: devuelve basura con alta confianza.

**Valor estimado:** el mayor del portafolio si se materializa — habilita velocidad (internal-fill), cross-sell y benchmark. Pero **el valor llega en Fase 1–3, no antes**. Comunicarlo así protege la credibilidad.
**Qué se necesita:** modelo de datos canónico, pipeline de extracción/parsing con validación, taxonomía ESCO + 15–30 sectores locales curados, score de vigencia, gobernanza de consentimiento.
**Fase:** auditoría de vigencia y dedup en **Fase 0** (radiografía honesta); estructuración y enriquecimiento en **Fase 1**; búsqueda semántica y productos en **Fase 2–3**.

> **Decisión de encuadre:** no migrar del ATS para explotar la base. Se extrae por API y se enriquece en una capa propia **por encima** de Team Tailor. Abandonar el ATS ahora es resolver el problema equivocado y arriesgar el 63% de los ingresos.

---

### 3.2 La velocidad: "5 días → mismo día"

**Tesis del cliente:** pasar de 5 días al mismo día.
**Nuestra tesis corregida:** "mismo día" es una promesa que mezcla dos métricas distintas y vende un número que el cliente **no controla**.

| Métrica | ¿La controla Conexión Talento? | Promesa correcta |
|---|---|---|
| **Time-to-submit** (entrega de terna) | **Sí** | Meta agresiva: de 5 días → **48–72 h ⚠️** |
| **Time-to-fill** (cierre/contratación) | **No** — depende de la decisión del cliente y el preaviso del candidato | Se reporta, **no se promete** |
| **"Mismo día"** | Solo para *hits pre-matcheados* de la base interna ya enriquecida | Reservado a Fase 3, y aun así como excepción, no como SLA |

**Recomendación dura:** **enterrar "mismo día" como promesa**, no reprogramarlo a Fase 3. Vender cualquier versión a una CEO enamorada del concepto siembra una decepción diferida. Lo que la firma posee y debe liderar es **time-to-submit, fill rate dentro de SLA e internal-fill rate** (% de procesos servidos desde la base vs sourcing fresco). Cada colocación servida desde la base recorta días de sourcing — ahí vive la velocidad real, y depende 100% de §3.1.

**Valor estimado:** alto y defendible una vez que hay línea base. Reducir time-to-submit es el ROI más vendible de Fase 1–2.
**Qué se necesita:** línea base honesta (§4), stage-gates estandarizados, base enriquecida para el internal-fill.
**Fase:** baseline en **Fase 0–1**; mejora de time-to-submit vía IA asistida en **Fase 2**; internal-fill como palanca en **Fase 3**.

---

### 3.3 El benchmark de compensaciones — **⚠️ BANDERA LEGAL EXPLÍCITA**

**Tesis del cliente:** vender un benchmark de compensaciones y beneficios construido con los datos de la base.
**Nuestra postura:** es la mayor oportunidad de monetización **y el mayor riesgo del encargo**. Se **congela como producto vendible** hasta cerrar la capa legal. Lanzarlo crudo no es un activo: es una factura legal con tono de autoridad.

**Por qué la bandera (sin rodeos):**

1. **Derecho de competencia / antitrust.** El intercambio de datos de compensación entre empresas es materia sensible. Vender datos salariales agregados puede constituir facilitación de coordinación de precios laborales.
2. **Confidencialidad contractual.** Esos datos provienen de negociaciones con clientes, probablemente cubiertas por NDA. Venderlos puede violar contratos con los **mismos clientes que pagan el 63% de los ingresos** → litigio con la cuenta que te da de comer.
3. **Re-identificación en mercado pequeño.** En Centroamérica, "el salario del CFO de la empresa X" es re-identificable **aun agregado**. *Anonimizado ≠ libre de usar.*
4. **Limitación de finalidad y consentimiento.** Datos recolectados para reclutamiento no pueden reutilizarse para un producto comercial sin base legal/consentimiento separado.
5. **Alucinación.** Si las cifras las genera un LLM sin fuente licenciada, son inventadas con autoridad. **Prohibido exponer números generados por el modelo.**

**Camino positivo (no solo "no"):**
- Validación legal **por país** antes de prometer nada (precondición de Fase 0).
- Diseño con **k-anonimato** (N mínimo de empresas/registros por celda rol×sector×país), fuentes lícitas, consentimiento granular opt-in, nota metodológica.
- Alternativa de menor riesgo: **alianza con un proveedor licenciado de comp-data** (revender/curar) en lugar de construir el dataset desde los candidatos.

**Valor estimado:** potencialmente una nueva línea de ingreso. **⚠️ Pero puede ser inviable de origen** en este mercado; no se cuantifica hasta el dictamen legal.
**Qué se necesita:** dictamen legal local, base de consentimiento, umbrales de anonimización, cobertura/representatividad mínima (métrica que hoy no existe).
**Fase:** **Fase 3, estrictamente condicionada.** **No aparece como compromiso en la propuesta del viernes.**

---

### 3.4 Cross-sell de capacitaciones a la base

**Tesis del cliente:** vender capacitaciones a los ~4000 candidatos.
**Nuestra postura:** oportunidad real de ingreso recurrente, pero con **la misma bandera de limitación de finalidad** que el benchmark, y con un riesgo reputacional propio.

- Datos recolectados para reclutamiento **no** pueden reutilizarse para marketing de capacitaciones sin **consentimiento separado** o interés legítimo documentado + opt-out funcional.
- Es exactamente el vector que ya les genera ataques en LinkedIn: a candidatos ghosteados, recibir ofertas comerciales amplifica el daño. **Reparar la experiencia (§3.5) es precondición de monetizar la relación.**

**Camino correcto:** opt-in granular (casilla separada "deseo recibir ofertas de capacitación") en el aviso de privacidad del formulario de aplicación, gestión de preferencias, segmentación por skill (que depende de §3.1).

**Valor estimado:** medio-alto como ingreso recurrente de bajo costo marginal **⚠️ (sin volumen no se dimensiona)**.
**Qué se necesita:** base enriquecida y segmentada (§3.1), consentimiento granular, SLA de experiencia reparado.
**Fase:** **Fase 3**, después de gobernanza de datos (Fase 1) y reparación de experiencia.

---

### 3.5 Candidate experience como diferenciador

**Tesis del cliente:** "cercanía al candidato" como diferenciador; pedir un reclutador extra.
**Nuestra tesis:** hoy "cercanía al candidato" es un **eslogan que no cumplen** y su **mayor pasivo reputacional** — los atacan en LinkedIn por falta de seguimiento, y el único contacto sistemático con el rechazado es un correo automático a 15 días. **El diferenciador que quieren vender es hoy su mayor herida.** Esta es, probablemente, la oportunidad de mejor relación valor/esfuerzo del mapa.

**Reencuadres clave:**

- **La persona extra que pide Lili no es backfill operativo: es un Embajador de Marca / Candidate Experience.** Un rol que la IA *no puede* hacer (seguimiento humano, cierre del loop, curaduría de relación). Esto convierte la petición de "una persona más" de amenaza ("la IA me reemplaza") en aspiración, y resuelve el dolor reputacional. El guardarraíl del cliente —"la IA no opina ni decide"— deja de venderse como restricción técnica y se vuelve **el mensaje central de adopción: "tú decides, la IA pre-ordena"**.
- **Secuencia crítica (corrección a la crítica adversarial):** **reparar el SLA de comunicación ANTES de lanzar la encuesta CSAT.** Encuestar a candidatos ya enojados ("me ignoraron y ahora me preguntan cómo me sentí") provoca *más* backlash. Primero el kit de comunicación, después la medición.
- **Human-in-the-loop obligatorio en rechazos.** Eliminar el auto-rechazo por IA en rank 30+ como decisión final: en una empresa ya criticada en LinkedIn, automatizar el rechazo amplifica el daño y expone a sesgo no auditable. Un humano valida antes de comunicar.

**Valor estimado:** alto en riesgo reputacional evitado + soporte directo al precio premium "clase mundial". Bajo esfuerzo.
**Qué se necesita:** SLA de contacto (acuse 48 h, actualización de estado, rechazo personalizado con feedback), plantillas, job description del rol embajador, HITL en rechazos.
**Fase:** kit + job description en **Fase 0** (munición para la reunión Virginia–Lili); CSAT y medición en **Fase 1**; portal de auto-actualización (mercado interno) en **Fase 3**.

---

## 4. Catálogo de oportunidades

> Valor y esfuerzo = agregados. "Dep." = dependencia bloqueante. Valores económicos marcados ⚠️ por falta de fee/volumen.

### Quadrante 1 — Hacer ya (Fase 0)

| # | Oportunidad | Valor estimado | Qué se necesita | Dep. | Fase |
|---|---|---|---|---|---|
| Q1.1 | **Dedup + historial candidato-cliente** (regla de no-reenvío + alerta de duplicado) | Cierra un riesgo reputacional **ya materializado**; embrión del mercado interno. Lleva incidentes de duplicado a ~0 | Check determinista (SQL/API o incluso hoja + regla obligatoria antes de enviar terna). **No es IA** | API TT (o export manual) | 0 |
| Q1.2 | **SOP de cribado + scorecard de 1 página** (extraer el "ojo clínico" de Virginia a rúbrica ponderada) | Estandariza el paso de mayor dolor; **de-riskea** el futuro ranker; mejora calidad de terna de inmediato | Shadowing de los 4 reclutadores sobre 1 vacante real; rúbrica con pesos y anclas; golden set embrionario | Tiempo de Virginia | 0→1 |
| Q1.3 | **Plantilla/SOP de CV con branding** (formalizar el prompt de Virginia como activo de la firma) | Resuelve "4 personas, 4 CVs"; quick win visible para la CEO; base del agente Generador | Plantilla determinista (layout fijo) + LLM solo normaliza/redacta; versionado y ownership | — | 0 |
| Q1.4 | **Kit de candidate experience** (SLA + plantillas + HITL en rechazos) | Detiene el sangrado reputacional en LinkedIn; materializa "cercanía"; protege el precio premium | SLA de contacto, plantillas, job description del embajador, regla de revisión humana | — | 0 |
| Q1.5 | **Cortar PII en ChatGPT de consumo** (brecha activa hoy) | Cierra exposición legal inmediata; credibilidad; costo casi nulo | Migrar el prompt a entorno con no-entrenamiento + DPA | País/legal | 0 |
| Q1.6 | **Activar la IA que Team Tailor YA cobra** | Valor "gratis"; evita construir lo que ya pagan | Auditoría de funciones del plan contratado (matching, ASR, rechazos) | Tier TT | 0 |
| Q1.7 | **Línea base retrospectiva** (process mining del event log de TT) | Convierte "cero métricas" en datos en semanas; ancla metas a datos | Export/API del audit log; validación por muestreo; **reportar solo extremos confiables** (apertura→terna→cierre) con caveats | **API TT (no verificada)** | 0→1 |

### Quadrante 2 — Apuestas estratégicas (Fase 1–2)

| # | Oportunidad | Valor estimado | Qué se necesita | Dep. | Fase |
|---|---|---|---|---|---|
| Q2.1 | **Estructurar la base** (modelo canónico + parsing + taxonomía ESCO + overlay local + score de vigencia + entity resolution) | El "60% del valor" del cliente, **condicionado**. Habilita búsqueda por skill, internal-fill, cross-sell | Pipeline de extracción/QA, ESCO + 15–30 sectores CA, golden record, gobernanza | Q1.7, base legal, vigencia real | 1 |
| Q2.2 | **Línea base forward + stage-gates estandarizados** (6–8 etapas únicas + 6–8 campos obligatorios al intake) | Sin esto, toda métrica de funnel es basura. Prerrequisito de la analítica y de los kickers de éxito | Definición de etapas, campos obligatorios en TT, adopción de los 4 | Co-diseño con equipo | 1 |
| Q2.3 | **Plantilla de intake/kickoff + scorecard por familia de puesto** | El cuello de botella REAL es el intake, no el cribado. Garbage in, garbage out | 3–5 familias de puesto priorizadas; guía estructurada con must-have/nice-to-have/pesos | — | 1 |
| Q2.4 | **Screener/Ranker asistido** (puntúa contra scorecard, HITL, des-identificación PII, eval de sesgo) | Reduce horas de cribado; acelera time-to-submit **sin escalar inconsistencia** | Golden set etiquetado por Virginia; rúbrica; auditoría de sesgo; gate "Listo para IA" | Q1.2, Q2.1, golden set | 2 |
| Q2.5 | **Búsqueda semántica sobre base enriquecida** (pgvector + filtros) | Habilita internal-fill y el "mismo día" de hits pre-matcheados | Base ya deduplicada/taxonomizada/vigente | Q2.1 | 2 |

### Quadrante 4 — Condicionadas / cuidado (Fase 3)

| # | Oportunidad | Valor estimado | Qué se necesita | Dep. | Fase |
|---|---|---|---|---|---|
| Q4.1 | **Mercado interno / portal de auto-actualización del candidato** | Refresca vigencia sin trabajo manual; mejora experiencia; resuelve el ghosting | Consentimiento y gobernanza resueltos; UX | Q2.1, legal | 3 |
| Q4.2 | **Cross-sell de capacitaciones** ⚠️ | Ingreso recurrente de bajo costo marginal ⚠️ | Opt-in granular, segmentación, experiencia reparada | Legal, Q2.1, §3.5 | 3 |
| Q4.3 | **Benchmark de compensaciones** ⚠️**LEGAL** | Potencial nueva línea — **o inviable de origen** | Dictamen legal, k-anonimato, fuentes lícitas, cobertura mínima | **Dictamen legal por país** | 3 |
| Q4.4 | **Sourcer agéntico + Entrevistador (ASR)** | Aceleración incremental; el único agente verdaderamente agéntico es el Sourcer | Base estructurada, guardarraíles validados, consentimiento de grabación | Q2.1, Q2.4 | 3 |

### Quadrante 3 — Lo que NO es oportunidad todavía (rechazar con argumento)

- **Migrar del ATS "ya".** Migrar 4000 registros sin taxonomía replica el desorden en un sistema más caro y traslada a una PYME de 10 personas la responsabilidad de seguridad/brechas/derechos ARCO que hoy delega en Team Tailor. **Primero exprimir TT por API; decidir con datos, no con entusiasmo.**
- **Construir los 6 agentes autónomos en paralelo.** 5 de los 6 no son agentes: son herramientas con salida estructurada. Seis agentes autónomos en un equipo de 10 sin procesos ni métricas es ingobernable. Empezar con **3 herramientas deterministas + 1 orquestador con HITL**.
- **Automatizar antes de estandarizar.** Automatizar el desorden lo escala a velocidad de máquina y destruye el "ojo clínico" que los hace premium.

---

## 5. Economía y asequibilidad — el chequeo que faltaba

> La crítica adversarial señaló, con razón, que un mapa de oportunidades sin economía es "un menú sin precios". No tenemos los datos para cerrarlo, pero **sí** para exponer la tensión honestamente.

- **Ancla del cliente:** ~3 meses de una asistente temporal ≈ **US$1.5k–2.7k ⚠️**. Si la propuesta compite contra ese número, nos posicionamos como mano de obra sustituible.
- **Costo agregado del roadmap completo** (parsing + taxonomía + entity resolution + auditoría de sesgo + abogado local + DPAs + SOPs + tableros + agentes): fácilmente **un programa de varios meses de trabajo senior = decenas de miles de US$ ⚠️**. **Es muy probable que el roadmap completo exceda lo que esta PYME puede o quiere financiar.**
- **Conflicto de interés que declaramos:** nuestro ingreso crece cuanto más custom se construya. La recomendación honesta —**maximizar la IA que Team Tailor ya cobra y comprar add-ons antes de construir infraestructura propia**— es justo la que encoge nuestro encargo. La integridad en el primer proyecto vale más que el tamaño del contrato.

**Plantilla de economía unitaria (para enchufar el número en la reunión):**
> Payback por fase = (fee por colocación **⚠️** × colocaciones incrementales por mayor velocidad/internal-fill **⚠️**) − costo del sistema.

**Cuadro de alternativas a vencer** (para que la propuesta sea irrebatible, no solo buena):

| Opción | Costo | Activo resultante |
|---|---|---|
| No hacer nada | $0 | Sigue el caos; crece el pasivo reputacional |
| Solo la temporal (3 meses) | ~$1.5–2.7k ⚠️ | Capacidad lineal que desaparece; cero capacidad instalada |
| Firma grande | Alto ⚠️ | Deck genérico, poco a la medida de boutique |
| **Nosotros (fixed-fee por fase)** | Fase 0 "sí fácil"; resto modular | **Estándar + documentación + métricas + activos que quedan y componen** |

---

## 6. Capacidad de entrega — quién cocina

> Omisión grave del análisis original. El líder (Víctor) es experto en data/IA pero **explícitamente no en RRHH ni en compliance**. Este mapa exige ingeniería de datos, ML, derecho de protección de datos/antitrust, diseño de proceso de selección y gestión del cambio.

- **In-house (data/IA):** dedup, extracción/parsing, taxonomía, métricas, agentes.
- **A subcontratar (declarado en la propuesta):** **asesoría legal de protección de datos local** (precondición del benchmark, cross-sell y de toda la capa de gobernanza) y **ASR de calidad para español regional** (comprar, no construir).
- **Co-autoría obligatoria con el cliente:** el "deber ser" del proceso debe co-diseñarse con **Lili** (cubre el gap de dominio HR) y la rúbrica de cribado con **Virginia** (su "ojo clínico" es el insumo, no algo que la IA amenaza).
- **Riesgo de personas clave a gestionar como activo del proyecto:**
  - **Lili (7am–7pm) es flight-risk, no solo "saturada".** Si renuncia por burnout antes de extraer su conocimiento, se pierden operación, memoria y sponsor de adopción de golpe. **El presupuesto de la temporal se reencuadra como seguro anti-fuga + alivio operativo real** (descargar la operación de Lili, su pedido literal), no como recurso de data. La extracción de su conocimiento se secuencia en las **primeras 2–3 semanas**.
  - **Continuidad operativa:** guardarraíl explícito de que **ninguna intervención toca un mandato en vuelo**. El 63% de ingresos debe seguir fluyendo durante la transformación.

---

## 7. Precondiciones bloqueantes (Fase 0 — Spike de factibilidad)

> Convertimos las "preguntas abiertas" repetidas en las 8 lentes en **precondiciones con dueño**. **Ningún P0 se promete en firme hasta cerrarlas.** Esto es lo que separa un deck de un resultado.

| # | Precondición | Por qué bloquea | Dueño / cómo se cierra |
|---|---|---|---|
| P-1 | **País de operación** | Define ley de datos, antitrust (benchmark), laboral, dimensionamiento legal de TODO | Email de 5 min a Virginia — **cerrar HOY** |
| P-2 | **API/export/tier real de Team Tailor** | De ella cuelgan Q1.1, Q1.7 y toda la estrategia de datos. Sin export masivo o con rate-limit, colapsa medio mapa | Spike técnico semana 1; plan B definido |
| P-3 | **¿Existe golden set?** (historial recuperable de quién entró a terna vs no) | El Screener (Q2.4) depende de él. Con cero documentación, podría haber que crearlo desde cero usando el tiempo más escaso (Virginia) | Auditoría del ATS; si no existe, financiar su construcción explícitamente |
| P-4 | **Vigencia real de la base** (muestreo) | Valida o desarma el "60% del valor". Dimensiona el esfuerzo a la base vigente, no a 4000 nominales | Muestreo de 200–300 registros en Fase 0 |
| P-5 | **Consentimiento y origen de los datos** | Habilita o bloquea benchmark, cross-sell y portal | Revisar términos de aplicación de TT + dictamen legal (P-1) |
| P-6 | **Fee por colocación + volumen de mandatos/mes** | Sin esto no hay ROI ni pricing defendibles | Primera pregunta de la reunión |
| P-7 | **Postura de seguridad de la propia consultora** | Al exportar PII a un almacén propio, la firma se vuelve sub-procesadora: cifrado, accesos, DPA cliente-consultora, borrado al cierre | Definir antes de tocar la base |

**Kill-criteria / go-no-go concretos (ejemplo a calibrar):**
- **Fase 0 exitosa** = (a) ≥X% de duplicados detectados, (b) plantilla de CV adoptada por los 4 reclutadores, (c) baseline de 3 KPIs entregada, (d) precondiciones P-1 a P-5 resueltas. **Si no se cumple, se detiene antes de Fase 1.**

---

## 8. Tensiones entre lentes — la ruta crítica acordada

> El análisis original dejó flotando una contradicción de secuencia. La resolvemos aquí en una sola cadena.

- **Lente de datos** quiere extraer/parsear en paralelo en Fase 1.
- **Lente de proceso** quiere documentar SOPs primero.
- **Lente de métricas** exige stage-gates estandarizados antes de medir limpio.

**Resolución (ruta crítica única):**

```
P-1..P-7 (Fase 0 spike)
   → Q1.1 dedup + Q1.3 CV + Q1.4 experiencia + Q1.7 baseline retrospectiva [quick wins paralelos, bajo riesgo]
   → Q2.2 stage-gates + Q1.2 scorecard [estandarizar: habilita medición forward Y datos limpios]
   → Q2.1 estructurar base [parsing/taxonomía sobre un modelo ya definido]
   → gate "Listo para IA"
   → Q2.4 Screener / Q2.5 búsqueda semántica
   → Fase 3 (monetización condicionada a legal)
```

**Romper el huevo-y-gallina (golden set ↔ liberar a Lili ↔ IA de cribado):** la temporal descarga la **operación** de Lili (no hace data), liberando 4–6 h/semana de Lili para co-diseño; Virginia aporta horas protegidas para el golden set en las primeras 2–3 semanas. Sin esas horas financiadas y agendadas, el ciclo no se rompe y el proyecto se estanca en piloto.

---

## 9. Síntesis para la decisión

1. **El primer entregable no es un agente: es un scorecard de intake y un SLA de comunicación al candidato.** Artesanía de proceso que ningún competidor con IA puede copiar sin el criterio humano detrás.
2. **La base de 4000 es oro condicionado, no realizado.** Se refina en una secuencia disciplinada y se explota *sobre* el ATS, no migrando.
3. **"Mismo día" se entierra; se vende time-to-submit, fill rate e internal-fill** — lo que el cliente realmente controla.
4. **Benchmark y cross-sell son Fase 3 condicionada a dictamen legal** y no tocan el camino crítico del viernes.
5. **Candidate experience es la oportunidad de mejor valor/esfuerzo** y reconvierte la petición de "una persona más" en un Embajador de Marca.
6. **Nada se promete en firme hasta el Spike de Factibilidad.** Es la diferencia entre un deck y un resultado.

> **Lo que honra la ambición de Virginia (el "sí" inspirador):** Conexión Talento *será* una máquina de clase mundial con cercanía real al candidato y, eventualmente, los agentes y la base como producto. Pero se construye en orden — disciplina antes que automatización — para que lo que la hace premium no se rompa en el camino.
