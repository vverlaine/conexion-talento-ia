# Arquitectura de la Solución
## Conexión Talento — Sistema de Reclutamiento Asistido por IA

> **Documento de diseño.** Describe la arquitectura objetivo del sistema, sus componentes de IA, los guardarraíles y el nivel de autonomía de cada uno. Es un documento técnico-funcional; el cronograma, el precio y el plan de recursos viven en los entregables de *Roadmap por Fases* y *Propuesta Comercial*. Todo supuesto no confirmado por el cliente se marca con ⚠️ y se lista en §10 como precondición bloqueante.

---

## 1. Principios de diseño (las cinco reglas que gobiernan toda decisión)

La arquitectura no parte de la tecnología, parte de cinco principios que resuelven las tensiones detectadas en el análisis. Cuando dos opciones técnicas compiten, gana la que respeta estos principios.

1. **El proceso antes que el modelo.** Ningún componente de IA se construye sobre una etapa que no tenga su estándar documentado, su rúbrica explícita y su línea base. La IA digitaliza un SOP; sin SOP no hay especificación que programar. *Esto materializa el gate "Listo para IA".*
2. **Humano en el lazo donde se decide sobre personas.** La IA pre-ordena, evidencia y redacta; el reclutador decide. Toda comunicación adversa a un candidato (rechazo) pasa por revisión humana. No es una concesión de cumplimiento: es el diferenciador de "cercanía" convertido en arquitectura.
3. **Determinismo donde se pueda, IA solo donde aporte.** La deduplicación, el enrutamiento por umbrales y el maquetado del CV son reglas, no LLM. Reservar el modelo para lo que ningún `if` resuelve: lectura, extracción, normalización y resumen.
4. **Comprar antes que construir** (a escala boutique, ~20-60 colocaciones/año ⚠️, construir infraestructura propia rara vez se paga). Primero exprimir lo que Team Tailor **ya cobra**; construir a medida solo donde el ROI lo justifique con datos. *Declaramos el conflicto de interés: nuestro ingreso crece cuanto más construimos a medida; por eso esta regla está escrita como principio, no como excepción.*
5. **El dato nunca lo inventa el modelo.** Cifras de salario, competencias y experiencia se citan a su fuente (CV, encuesta licenciada, ATS). Un LLM jamás expone un número que no pueda trazar. Prohíbe la alucinación con autoridad.

---

## 2. Reencuadre honesto: no son "6 agentes autónomos"

El cliente visualiza seis agentes de IA. **Es un encuadre solución-primero que debemos retar con rigor, no comprar.** De los seis componentes, solo uno (el Sourcer) es verdaderamente *agéntico* —es decir, decide iterativamente sus propias acciones. Los otros cinco son **herramientas con salida estructurada y enrutamiento determinista**: leen, extraen, puntúan o redactan contra un esquema fijo y devuelven el control al humano.

Esta distinción no es semántica: cambia el costo, el riesgo de gobernanza y el nivel de autonomía. Vender "seis agentes autónomos" en un equipo de 10 personas, sin métricas ni procesos documentados, infla complejidad y crea un sistema ingobernable. La arquitectura correcta para la fase temprana es:

> **3 herramientas deterministas confiables + 1 orquestador con reglas + 1 capa de IA asistida** — y la autonomía agéntica reservada para cuando el proceso esté probado.

Mantenemos el nombre "agente" en la conversación con el cliente por continuidad con su visión, pero la **ficha técnica de cada uno declara su verdadera naturaleza y su nivel real de autonomía** (§3).

---

## 3. Los seis componentes de IA

Cada componente se describe con su función, entradas, salidas, guardarraíles, nivel de autonomía y —crítico— **qué se entrega en modo copiloto (asistido) vs. autónomo**. La columna de autonomía usa una escala de tres niveles:

- **N1 – Copiloto sugiere:** la IA produce un borrador/ranking; el humano edita y aprueba todo antes de cualquier acción externa.
- **N2 – Copiloto con excepción:** la IA actúa dentro de un rango pre-aprobado; el humano revisa por muestreo o solo las excepciones.
- **N3 – Autónomo acotado:** la IA ejecuta sin revisión por instancia, con logging y auditoría posterior. **Ningún componente que decida sobre una persona o se comunique con un candidato/cliente alcanza N3.**

### 3.1 Cuadro maestro de componentes

| # | Componente (visión cliente) | Naturaleza real | Función | Autonomía objetivo | Fase |
|---|---|---|---|---|---|
| 1 | **Perfilador** | Herramienta RAG + plantilla | Genera borrador de competencias, preguntas y rango salarial **citado a fuente** | N1 | 2 |
| 2 | **Redactor de perfil** | Herramienta (prompt-chain) | Redacta perfil de puesto calibrado al tamaño/contexto de la empresa | N1 | 2 |
| 3 | **Sourcer** | Agente (el único genuino) | Itera búsquedas booleanas + genera preguntas para revelar el perfil real | N2 | 3 |
| 4 | **Screener / Ranker** | Herramienta de scoring + routing determinista | Lee ~200 CVs, puntúa contra rúbrica, rankea, propone top 10 | N1 → N2 (solo rangos medios) | 2 |
| 5 | **Entrevistador pre-screening** | Buy (ASR) + herramienta de resumen | Transcribe, resume por esquema, detecta competencias con cita, sugiere preguntas | N1 | 2 |
| 6 | **Generador de CV con branding** | Herramienta (extracción a esquema + plantilla determinista) | Normaliza CV y produce documento con branding de la firma | N2 | 0–1 (quick win) |

> **Componente "cero" implícito y crítico:** el **check de deduplicación candidato-cliente** (§3.7). No es IA, no estaba en la lista de seis del cliente, y es el de mayor relación impacto/esfuerzo. Resuelve el riesgo reputacional ya materializado ("mandé el mismo candidato dos veces").

A continuación, la ficha de cada uno.

---

### 3.2 Agente 1 — Perfilador

| Atributo | Detalle |
|---|---|
| **Función** | Producir un borrador estructurado de competencias críticas, banco de preguntas y referencia salarial de mercado para un puesto/sector. |
| **Entradas** | Sector, puesto, seniority, contexto del intake (§4); biblioteca curada de competencias; **fuente salarial licenciada o dataset propio agregado con N mínimo** ⚠️. |
| **Salidas** | JSON estructurado: 3-5 competencias, banco de preguntas conductuales (STAR) por competencia, rango salarial **con fuente y fecha citadas**. |
| **Guardarraíles** | (1) **Prohibido exponer cifras salariales generadas por el modelo** — solo datos con fuente verificable o el campo va vacío con la nota "sin dato confiable". (2) No opina fuera del catálogo de competencias curado. (3) Toda salida es borrador editable. |
| **Autonomía** | **N1 – Copiloto sugiere.** El reclutador valida y ajusta antes de usar. |
| **Copiloto vs. autónomo** | **Solo copiloto, indefinidamente.** El benchmark salarial vendible es Fase 3 condicionado a base legal (ver *Documento de Datos y Legal*); aquí solo se consume internamente y citado. |

---

### 3.3 Agente 2 — Redactor de perfil de puesto

| Atributo | Detalle |
|---|---|
| **Función** | Redactar el perfil de puesto a partir del intake, calibrado al tamaño y contexto de la empresa-cliente. |
| **Entradas** | Plantilla de intake/scorecard completada (§4); plantilla única de perfil de puesto de la firma. |
| **Salidas** | Borrador de perfil de puesto en la plantilla estándar, con must-have/nice-to-have y definición de éxito a 90 días. |
| **Guardarraíles** | Estructura fija por plantilla (el LLM redacta, no inventa requisitos); no agrega competencias fuera del scorecard. |
| **Autonomía** | **N1 – Copiloto sugiere.** |
| **Copiloto vs. autónomo** | Copiloto. Es el paso 2 del proceso; depende 100% de que el intake (paso 1) esté estandarizado. |

---

### 3.4 Agente 3 — Sourcer *(el único verdaderamente agéntico)*

| Atributo | Detalle |
|---|---|
| **Función** | Iterar búsquedas (booleanas y semánticas sobre la base ya enriquecida) y generar preguntas para revelar el perfil real del candidato. |
| **Entradas** | Scorecard; base de talento enriquecida y vigente (precondición: §3.8 estructurada); fuentes externas (LinkedIn ⚠️ según términos). |
| **Salidas** | Conjunto de candidatos vigentes con justificación de match; preguntas de revelación de perfil. |
| **Guardarraíles** | Solo busca sobre candidatos **vigentes y con consentimiento válido**; no contacta de forma autónoma; presenta resultados al reclutador. |
| **Autonomía** | **N2 – Copiloto con excepción** (itera búsquedas solo; el contacto siempre es humano). |
| **Copiloto vs. autónomo** | **Aspiracional, Fase 3.** Depende de que la base esté estructurada, deduplicada y con score de vigencia. Sin eso, devuelve basura con confianza. No se promete en fase temprana. |

---

### 3.5 Agente 4 — Screener / Ranker *(el de mayor palanca y mayor riesgo)*

Es el corazón del valor (el paso 4 concentra el grueso del trabajo manual) **y** el de mayor riesgo legal-reputacional (cribado automatizado = decisión sobre personas, sesgo a escala de 200 CVs/proceso).

| Atributo | Detalle |
|---|---|
| **Función** | Leer ~200 CVs, puntuar cada uno contra la rúbrica del scorecard, rankear y proponer top 10. |
| **Entradas** | CVs (texto extraído); **rúbrica de scoring ponderada construida CON Virginia**; golden set de ternas históricas como referencia ⚠️ (ver §10). |
| **Pipeline** | (1) **Des-identificación de PII** (eliminar foto, edad, estado civil, nacionalidad, nombre como features) → (2) extracción de evidencia contra cada criterio → (3) score **con justificación citada textualmente al CV** (sin inventar) → (4) ranking. |
| **Salidas** | Ranking con score por criterio + cita de evidencia; los tres tramos del semáforo de orquestación (§5). |
| **Guardarraíles** | (1) **El ranking NUNCA es decisión final automática.** (2) **Des-identificación obligatoria antes del scoring** (equidad + defendibilidad). (3) Justificación trazable al CV; cero inferencias no soportadas. (4) **Auditoría de sesgo antes de producción** (selection rate por género/edad; exclusión de proxies prohibidos). (5) Logging de cada decisión. |
| **Autonomía** | **N1 en top 10 y terna** (el humano aprueba). **N2 solo en el tramo 30+** para *preparar* (no enviar) lotes de rechazo. |
| **Copiloto vs. autónomo** | **Copiloto siempre en lo que toca a una persona.** Se mide la concordancia con el "ojo clínico" de Virginia ("coincidió en X de 10") para construir confianza por evidencia. La rúbrica gana al modelo; el humano gana a la rúbrica mientras se calibra. |

---

### 3.6 Agente 5 — Entrevistador de pre-screening

| Atributo | Detalle |
|---|---|
| **Función** | Escuchar/transcribir la llamada de pre-screen, resumir por esquema, detectar competencias con evidencia y sugerir preguntas de seguimiento. |
| **Entradas** | Audio de la llamada **con consentimiento explícito de grabación**; guía de entrevista estructurada ligada al scorecard. |
| **Salidas** | Transcripción + resumen estructurado: competencias detectadas **con cita textual**, banderas, preguntas sugeridas. |
| **Guardarraíles** | (1) **Consentimiento de grabación al inicio de cada llamada** (guion obligatorio). (2) La IA **no concluye aptitud** — detecta y resume; el reclutador evalúa. (3) Retención de audios/transcripciones definida; la voz puede ser dato biométrico. |
| **Autonomía** | **N1 – Copiloto sugiere.** |
| **Copiloto vs. autónomo** | Copiloto. ASR se **compra** (no se construye), con calidad para español regional. |

---

### 3.7 Agente 6 — Generador de CV con branding *(el quick win visible)*

| Atributo | Detalle |
|---|---|
| **Función** | Tomar un CV crudo y producir el documento estandarizado con el branding de la firma, idéntico sin importar cuál de los 4 reclutadores lo opere. |
| **Entradas** | CV crudo (PDF/texto); el "prompt" de Virginia **formalizado, versionado y propiedad de la firma**; plantilla de branding determinista. |
| **Salidas** | CV con branding. **El LLM solo extrae a un esquema fijo y redacta el resumen; el maquetado es plantilla determinista, no lo decide el modelo** (elimina variabilidad). |
| **Guardarraíles** | No decide nada sobre la persona (riesgo bajo); estructura forzada por esquema; no inventa experiencia. |
| **Autonomía** | **N2 – Copiloto con excepción** (genera el documento; el reclutador revisa antes de enviar al cliente). |
| **Copiloto vs. autónomo** | Quick win de **semana 1-2**. Entregable visible que demuestra el método sin riesgo. **Precondición de cumplimiento:** cortar la inyección de PII de candidatos en ChatGPT de consumo y migrar a API/Enterprise con no-entrenamiento y DPA firmado (brecha activa hoy). |

---

### 3.8 Componente 0 — Check de deduplicación candidato-cliente *(no es IA, es el más rentable)*

| Atributo | Detalle |
|---|---|
| **Función** | Antes de enviar una terna, verificar si el candidato ya fue presentado a ese cliente (y detectar declaraciones falsas de participación previa). |
| **Entradas** | Historial candidato × cliente × fecha (derivado del ATS vía API ⚠️ o, en su defecto, hoja de cálculo / campo del ATS). |
| **Salidas** | Alerta de duplicado + línea de tiempo del candidato. |
| **Tecnología** | **Resolución de identidad determinista** (email/teléfono/cédula) + fuzzy match de nombre. **SQL/API + regla, cero LLM** (meterle IA introduciría falsos negativos). |
| **Autonomía** | **N2 – alerta dura** (bloquea el envío hasta confirmación humana). |
| **Nota** | Es el embrión del "mercado interno"/historial. **No convertirlo en lista negra compartida ni en exclusión automática:** informa al reclutador, no decide. |

---

## 4. Precondición transversal: el intake estandarizado

Ningún componente tiene criterio que aplicar sin esto. El **cuello de botella real no es el cribado, es el intake** (pasos 1-2). El artefacto que alimenta a *todos* los agentes es la **plantilla de intake + scorecard de 1 página por vacante**: contexto de la empresa, 3-5 competencias críticas, must-have vs. nice-to-have con pesos, señales de descarte, rango salarial y definición de éxito a 90 días.

```
                 ┌──────────────────────────────────────┐
                 │  SCORECARD / INTAKE (1 página)        │
                 │  (artefacto humano, paso 1-2)         │
                 └──────────────────────────────────────┘
                        │ alimenta a TODOS los componentes
   ┌───────────┬────────┼────────┬───────────┬───────────┐
   ▼           ▼        ▼         ▼           ▼           ▼
Perfilador  Redactor  Sourcer  Screener  Entrevistador  GenCV
```

---

## 5. Patrón de orquestación

El cliente definió los umbrales correctos; la arquitectura los **convierte en código determinista** (no en instrucción de prompt, que el modelo podría ignorar) y **corrige el punto ciego legal del auto-rechazo**.

```
        Screener/Ranker puntúa 200 CVs contra el scorecard
                              │
                   ┌──────────┴──────────┐
                   ▼                      ▼
          Des-identificación PII   Logging + justificación citada
                   │
                   ▼
         ┌─────────────────────────────────────────────┐
         │   ENRUTADOR DETERMINISTA (reglas, no IA)     │
         └─────────────────────────────────────────────┘
            │                  │                    │
        TOP 10            POSICIÓN 10-20         POSICIÓN 30+
            │                  │                    │
            ▼                  ▼                    ▼
   Reclutador valida   "Proceso sigue        Rechazo cordial
   → LLAMADA           abierto"              → ⚠️ REVISIÓN
   (N1: humano         (en espera,           HUMANA EN LOTE
    aprueba)           sin acción adversa)   antes de enviar
                                             (N2, nunca N3)
```

**Corrección crítica frente al diseño original del cliente:** el auto-rechazo en posición 30+ **no se envía de forma autónoma**. Es el mayor pasivo legal/reputacional del diseño —en una empresa a la que *ya* atacan en LinkedIn por falta de seguimiento— y constituye **decisión automatizada** (relevante si hay exposición a UE: GDPR Art. 22 / EU AI Act, cribado = alto riesgo). El rechazo se prepara en lote, lo revisa un humano y se envía con plantilla **personalizada** (no el correo automático genérico a 15 días). Esto protege simultáneamente el cumplimiento y el diferenciador de "cercanía".

---

## 6. Decisiones Build vs. Buy por componente

Sesgo explícito hacia **Buy/Activar** a escala boutique. Construir a medida solo donde no existe alternativa comprable que respete los guardarraíles.

| Componente | Decisión | Justificación |
|---|---|---|
| **Funciones de IA del ATS** (matching, screening, ASR de psicométricas) | **ACTIVAR** lo ya pagado | Team Tailor "tiene IA que no saben usar". Auditar y activar antes de comprar/construir nada. Valor inmediato a costo cero. |
| **Parsing de CV** | **Buy** (API LLM) | Extracción a esquema con modelo comercial; cómputo marginal (~US$0.01-0.03/CV ⚠️). *El costo real no es el cómputo: es el QA, la dedup y el mapeo a taxonomía.* |
| **ASR (transcripción pre-screen)** | **Buy** | Comprar ASR de calidad para español regional. Construir transcripción no aporta diferenciación. |
| **Modelos de lenguaje** | **Buy** (API) | Familia Claude vía API (ver §8). Nunca entrenar modelos propios. |
| **Taxonomía de skills** | **Buy/Adoptar** (ESCO) + overlay local | ESCO es gratuita y multilingüe (ES). *No es "gratis": curar el overlay de 15-30 sectores centroamericanos y normalizar texto libre es trabajo real.* |
| **Base de datos vectorial** | **Buy gestionada** (pgvector) | No construir infraestructura. Y **solo en Fase 2+**, sobre base ya limpia. |
| **Check de deduplicación** | **Build ligero** (SQL/regla) | Trivial y sin alternativa exacta comprable; horas de trabajo. |
| **Generador de CV con branding** | **Build ligero** (extracción + plantilla) | El branding es propio; el esfuerzo es formalizar el prompt existente. |
| **Rúbrica de scoring / golden set** | **Build con el cliente** | Es el "ojo clínico" de Virginia; nadie lo vende. Artefacto humano-céntrico, no de software. |
| **Almacén propio de datos** | **Diferir** | Solo si el caso de negocio lo justifica tras el spike de factibilidad. No migrar por impulso. |
| **Benchmark de compensaciones** | **NO construir aún** | Bandera legal (antitrust/datos) + alucinación. Camino positivo: alianza con proveedor licenciado o producto futuro con consentimiento granular. |

---

## 7. Rol de Team Tailor

**Postura: augmentar, no reemplazar.** Team Tailor es el sistema de registro y el procesador con DPA y funciones de cumplimiento ya integradas. Migrar 4.000 registros sin taxonomía replicaría el desorden en un sistema más caro, trasladaría a una PYME de 10 personas toda la responsabilidad de seguridad/brechas/derechos ARCO, y arriesgaría la operación que genera el 63% de los ingresos.

| Función | Quién la cumple en la arquitectura objetivo |
|---|---|
| Sistema de registro (candidatos, vacantes, aplicaciones, etapas) | **Team Tailor** (permanece) |
| Integración LinkedIn, envío de psicométricas, correos | **Team Tailor** (activar y afinar lo existente) |
| Stage-gates estandarizados (prerrequisito de métricas) | **Team Tailor** (configurar 6-8 etapas únicas) |
| Capa de orquestación, scoring, dedup, enriquecimiento | **Capa propia delgada vía API** ⚠️, *por encima* del ATS |
| Línea base de métricas | **Process mining sobre el event log del ATS** ⚠️ |

> **Supuesto bloqueante ⚠️:** toda la capa propia depende de que **el tier contratado de Team Tailor exponga API REST de lectura/escritura y export masivo sin rate-limit prohibitivo.** No verificado. Es la dependencia más load-bearing del diseño. **Plan B si falla:** operar la capa de dedup/scoring sobre exports manuales periódicos + maximizar las funciones nativas del ATS. La decisión "dejar Team Tailor sí/no" se pospone hasta tener evidencia de límites de API y un caso de negocio con datos.

---

## 8. Stack tecnológico recomendado (alto nivel)

| Capa | Recomendación | Nota |
|---|---|---|
| **Modelos LLM** | Familia **Claude vía API** ⚠️ *(validar IDs y precios vigentes contra la documentación oficial al momento de construir)*. Tier de **razonamiento** para Screener/Ranker y resumen de entrevista (donde se requiere fidelidad y trazabilidad); tier **rápido/económico** para parsing masivo de CVs y normalización. Configuración con **salida estructurada forzada por esquema** (function calling) para que la IA no pueda "opinar fuera de scope". | Sin no-entrenamiento + DPA, no se procesa PII. |
| **Parsing de CV** | LLM → JSON estricto (experiencia, skills, sector, ubicación, idiomas, educación, pretensión salarial) + **capa de validación** (detección de inconsistencias + muestreo humano 5-10%). | Nunca tratar el dato parseado como verdad sin trazar al CV fuente. |
| **Búsqueda / RAG** | **Híbrida**: filtros estructurados (sector, skill ESCO, vigencia, ubicación) + similitud semántica (embeddings en **pgvector**). | **Última milla, no la primera.** Orden obligatorio: identidad → estructura → frescura → taxonomía → *recién entonces* embeddings. RAG sobre la base sucia de hoy devuelve basura con confianza. |
| **Almacén** | Postgres + almacenamiento de objetos para PDFs. | Solo si se justifica; cifrado, control de acceso, DPA cliente-consultora, borrado al cierre. |
| **Taxonomía** | ESCO (esqueleto) + overlay local 15-30 sectores. | Normaliza el texto libre de "4 personas, 4 criterios". |
| **Des-identificación** | Capa de PII-stripping previa al scoring. | Equidad + defendibilidad. |
| **Integración** | API de Team Tailor ⚠️; sincronización incremental. | Capa propia portable por diseño. |

---

## 9. Diagrama textual del flujo end-to-end

```
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 1-2  INTAKE + SCORECARD (humano, consultivo)                      │
│   Reclutador + cliente → scorecard 1 pág.  ──►  Redactor (N1) borrador │
│   de perfil de puesto                                                  │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 3  SOURCING                                                       │
│   Sourcer (N2, Fase 3) busca sobre BASE ENRIQUECIDA + fuentes externas │
│   ── hoy: búsqueda manual / por skill sobre piloto de base estructurada│
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
        ┌───────────────── CHECK DEDUP (no IA, N2) ─────────────────┐
        │  ¿candidato ya presentado a este cliente?  → ALERTA DURA  │
        └───────────────────────────┬──────────────────────────────┘
                                     ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 4  CRIBADO                                                        │
│   CVs ─► PARSING (LLM→JSON) ─► DES-IDENTIFICACIÓN PII ─►               │
│   SCREENER/RANKER (N1) puntúa vs. rúbrica, cita evidencia ─►           │
│   ENRUTADOR DETERMINISTA:                                             │
│       top10 → llamada (humano aprueba)                                │
│       10-20 → en espera, sin acción adversa                          │
│       30+   → rechazo en LOTE con REVISIÓN HUMANA (jamás auto-envío)  │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 5  PRE-SCREENING                                                  │
│   Consentimiento de grabación ─► ASR (buy) ─► RESUMEN ESTRUCTURADO     │
│   (N1): competencias con cita, banderas, preguntas. Humano evalúa.    │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 6-7  TERNA + CIERRE (humano: "ojo clínico", negociación, craft)   │
│   ── ZONA SIN AUTOMATIZAR: aquí vive el diferenciador.                │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 8  CV CON BRANDING                                                │
│   GENERADOR (N2): extrae a esquema + plantilla determinista. Humano    │
│   revisa antes de enviar.                                             │
└──────────────────────────────────────────────────────────────────────┘

  ◄── Transversal: línea base de métricas (process mining ATS) +
      logging de toda decisión de IA + SLA de comunicación al candidato
```

---

## 10. Honestidad sobre fases: copiloto vs. autónomo

| Hoy entregamos (copiloto, asistido) | NO entregamos autónomo (y por qué) |
|---|---|
| CV con branding estandarizado (N2) | Nada que decida sobre una persona corre sin humano |
| Check de dedup con alerta dura (N2) | El rechazo nunca se auto-envía (sesgo no auditable + daño reputacional) |
| Screener/Ranker que pre-ordena, humano aprueba (N1) | El ranking nunca es decisión final automática |
| Resumen de pre-screen con cita (N1) | La IA no concluye aptitud |
| Perfilador/Redactor que borronean (N1) | Cifras salariales generadas por el modelo (alucinación) |

**La verdad para el cliente:** en el horizonte de este proyecto, **el sistema es un copiloto, no un piloto automático.** La autonomía real (Sourcer agéntico, monetización de la base, benchmark) es land-and-expand, depende de la base estructurada y de cerrar banderas legales, y **no se promete en fase temprana.** Esto no es una limitación a disculpar: es la decisión correcta. En una boutique que vive del "ojo clínico" y la cercanía, automatizar el juicio destruiría justo lo que la hace premium. La IA acelera de 5 días a horas **sin escalar la inconsistencia**; el "mismo día" solo aplica a coincidencias pre-matcheadas de la base interna, no como KPI estrella.

---

## 11. Precondiciones bloqueantes (apagar antes de comprometer arquitectura)

Estos supuestos load-bearing sostienen todo lo anterior. Se resuelven en un **spike de factibilidad técnica y legal de ~1 semana antes de fijar alcance**, no como "preguntas abiertas" que flotan:

| # | Supuesto ⚠️ | Si falla… | Dueño / acción |
|---|---|---|---|
| 1 | **País: El Salvador + Guatemala ✅** (confirmado). Falta validar consentimiento de la base y posible exposición UE | Define scoping legal (Decreto 144/2024 SV vigente) y viabilidad del benchmark | Validar consentimiento/registro con Virginia |
| 2 | **API/export/tier de Team Tailor** | Colapsa dedup automático, extracción, baseline retrospectiva | Verificar tier real + plan B (exports manuales) |
| 3 | **Existencia de golden set** (historial de ternas recuperable) | El Screener no replica el "ojo clínico"; construirlo exige tiempo escaso de Virginia | Muestrear historial; si no existe, financiar su construcción explícitamente |
| 4 | **Vigencia y consentimiento de la base de 4.000** | El "60% del valor" se sobrevalora; riesgo regulatorio | Auditoría de vigencia (muestreo) antes de invertir en enriquecer |
| 5 | **Brecha activa: PII en ChatGPT de consumo** | Transferencia de datos / posible entrenamiento | Cortar y migrar a API/Enterprise con no-entrenamiento + DPA — **inmediato** |
| 6 | **Rol de la consultora como sub-procesadora de PII** | Nuevo vector de brecha al exportar los 4.000 | Definir dónde viven los datos, cifrado, DPA cliente-consultora, borrado al cierre |

> **Sin el spike, no se promete ningún quick win P0.** Es la diferencia entre un *deck* de arquitectura y una arquitectura que se sostiene en el primer proyecto —que es existencial para la firma.
