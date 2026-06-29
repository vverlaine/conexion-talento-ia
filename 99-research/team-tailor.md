# Team Tailor — capacidades, IA, datos e integraciones

> Brief de investigación para Conexión Talento. Fecha: 2026-06-29. Foco: viabilidad de extraer ~4.000 candidatos con sus CVs, evaluar la IA nativa y decidir entre **augmentar** o **reemplazar** el ATS.

---

## Resumen ejecutivo

- **La extracción completa de la base es viable vía API REST**, no por un botón de "Export CSV/todo". Teamtailor expone una API pública (formato JSON:API) con endpoints de candidatos; con una **API key de scope Admin + Read** se puede recorrer y descargar los ~4.000 candidatos, sus campos, respuestas, notas y la URL de su CV. Hay que **programar un script** (no es autoservicio de UI).
- **El límite de tasa es el principal cuello de botella, no un bloqueo**: ~**50 peticiones por cada 10 segundos** (~5/s); con manejo de paginación e `includes`, bajar 4.000 candidatos + adjuntos es cuestión de **horas, no días**. Recomiendan ~300 ms entre llamadas.
- **La IA nativa ("Co-pilot") es un asistente de redacción y screening por criterios, NO un buscador semántico de talento por skills**. Evalúa candidato-por-aplicación contra criterios (✓ / ✕ / – ) y resume CVs, pero **no rankea ni hace matching semántico transversal de toda la base**. Reseñas independientes confirman que el "smart search" es esencialmente **keyword matching**, sin fit-scores ni shortlists rankeadas por IA.
- **El Co-pilot es un add-on de pago** (potenciado por modelos GPT de OpenAI), activable por el Company Admin, y disponible en los **planes superiores** (Business/Pro/Enterprise), no en el plan de entrada.
- **Precios opacos y modelo por "job slots"** (no por usuario; usuarios ilimitados). Rango de mercado: **~US$2.750 hasta US$72.000+/año**, contrato medio **~US$16.500/año**, mínimo **12 meses** y escaladores anuales del 3-8%. Para una boutique como Conexión Talento, la franja baja-media es la realista.
- **Buen ecosistema de integraciones**: webhooks (eventos de candidato), Zapier/Make, LinkedIn (RSC), y un Marketplace con assessments psicométricos/técnicos (TestGorilla, AssessFirst, Codility, CodinGame, PerformanSe, JobMatch, etc.).
- **Recomendación: AUGMENTAR.** Mantener Teamtailor como **sistema de registro** (ATS, employer branding, pipeline, compliance) y **extraer la base a un motor propio de búsqueda semántica por skills** (embeddings + parsing de CVs). Es lo que el cliente realmente necesita y es justo donde Teamtailor es débil; reemplazar destruiría valor (employer branding, flujo, datos históricos) sin resolver el problema de búsqueda.

---

## Hallazgos detallados

### 1) Exportación / extracción de datos de candidatos

**Sí existe API REST pública y permite extraer la base.** Características confirmadas:

- **Especificación**: JSON:API (`application/vnd.api+json`). Endpoints sobre `https://api.teamtailor.com/v1/...` (stack EU/Irlanda). Hay stacks regionales: **NA** `api.na.teamtailor.com` (Oregon) y **AU** `api.au.teamtailor.com`. *Conviene verificar en qué stack está la cuenta de Conexión Talento.*
- **Autenticación**: token en header `Authorization: Token token=<API_KEY>` más header obligatorio `X-Api-Version`. La key se crea en **Settings → Integrations → API keys** (solo Company Admin). Las keys **no se editan**, solo se borran.
- **Scopes**: tres niveles de acceso (**Public / Internal / Admin**) × tres operaciones (**Read / Write / Read-Write**). **Los datos de candidatos están restringidos y requieren scope Admin.** Para una extracción de solo lectura, lo ideal es **Admin + Read**.
- **Endpoints de candidatos** (lectura):
  - `GET /v1/candidates` — lista paginada de candidatos.
  - `GET /v1/candidates/{id}` — candidato individual.
  - Relacionados: `job-applications`, `answers` (respuestas a preguntas), `notes`, `custom-field-values`, `jobs`. Permite reconstruir todo el contexto del candidato.
- **Filtros y orden**: la API soporta `filter` por email, departamento, rol, ubicaciones, regiones y fechas de creación/actualización, y `sort` por atributos. Útil para extracciones incrementales (solo lo cambiado desde la última corrida).
- **CV / resume**: el modelo de candidato incluye un atributo de **resume** (URL del archivo). En el flujo de *import* el CV se maneja como URL pública descargable; en lectura, el CV se obtiene siguiendo la URL del adjunto. **La descarga masiva de los PDFs/CVs es factible**, aunque la documentación pública no detalla exhaustivamente el endpoint de adjuntos — *punto a validar con la cuenta real y una key Admin.*
- **Formato**: la salida nativa es **JSON** (JSON:API). **No hay un "Export CSV de toda la base con CVs" en la UI**; el CSV se generaría del lado de Conexión Talento tras la extracción por API.
- **Límite de tasa**: **~50 req / 10 s** (~5/s); exceder devuelve **HTTP 429**. Recomendación oficial: ~300 ms entre llamadas. La librería Nango marca que **no trae paginación preconfigurada**, es decir, **el cursor/paginación JSON:API (`page[size]`, `page[number]`) hay que implementarlo a mano**.
- **Volumen 4.000 candidatos**: a ~5 req/s, listar con paginación (p. ej. 30/página) + traer relaciones e `includes` + descargar CVs es perfectamente abordable en una sola corrida de **pocas horas**. No hay un tope documentado que impida bajar la base completa.
- **Import (contexto)**: existe "Self-import via API" para *cargar* candidatos (crear candidato → custom fields → answers → notes; el CV se sube a un servidor público y se pasa la URL). **Es unidireccional (import)**; la "exportación" no es una función empaquetada, se hace leyendo los mismos endpoints.

> **Conclusión técnica:** extraer toda la base (datos + CVs) hacia un sistema propio **es técnicamente viable y soportado**, mediante scripting contra la API con key Admin/Read. No esperar un export de un clic.

### 2) Funciones de IA ("Co-pilot")

- **Motor**: potenciado por **modelos GPT de OpenAI** ("la misma tecnología que ChatGPT").
- **Catálogo de funciones** (agrupadas):
  - *Candidate insights*: **Ask Co-pilot**, **Candidate screening**, **Candidate suggestions**, **Resume summaries**, **Resume parser**.
  - *Interview prep*: sugerencias de skills/traits, sugerencias de preguntas para interview kits, preguntas de aplicación, **detección de discriminación/sesgo**.
  - *Meetings & feedback*: **meeting insights** (resúmenes/transcripciones), respuestas de interview kit, **borradores de email de rechazo**.
  - *Content*: borradores de descripción de puesto, asistente del editor, traducción de preguntas.
  - *Analytics*: constructor de bloques de gráficos.
- **Cómo funciona el screening**: evalúa cada candidato/aplicación contra **criterios definidos** usando resume, cover letter, respuestas a preguntas, comentarios, dirección, tags y custom fields (no privados). Devuelve **✓ (cumple) / ✕ (no cumple) / – (datos insuficientes)**. **Es evaluación por criterios, aplicación por aplicación**, no un ranking probabilístico global.
- **Disponibilidad**: **add-on** que un **Company Admin activa** en el "Add-on feature center". Según análisis de planes, **se incluye en los tramos Business/Pro/Enterprise, no en el de entrada**.

### 3) Planes y precios

- **Modelo**: por **job slots** (posiciones abiertas simultáneas), **no por asiento**; **usuarios ilimitados** y publicaciones ilimitadas en la mayoría de contratos.
- **Sin precios públicos** (solo cotización a medida; prueba de 14 días, sin tier gratuito).
- **Rango de mercado (datos de compradores)**: desde **~US$2.750/año (~US$229/mes)** en pequeño, **US$600-1.200/mes** en medio, hasta **US$72.000+/año** enterprise. **Contrato medio ~US$16.500-17.000/año.**
- **Diferencias por plan** (según análisis de mercado, *no oficial*): el **AI Co-pilot, SSO, nurture campaigns y SMS completo** aparecen en Business+; **CSM dedicado y capacidades avanzadas de API/data warehouse** se asocian a Enterprise.
- **Condiciones**: mínimo **12 meses**, sin mes-a-mes; **escaladores anuales 3-8%**; posibles fees de implementación (US$0-5.000+), overage de job slots y de SMS, integraciones premium con costo extra.

> ⚠️ La tabla de "qué plan incluye API" proviene de un blog de terceros (pin.com) y **debe confirmarse con un Account Executive**: hay evidencia de que **la creación de API keys está disponible para Company Admins** con independencia de un tier "Enterprise". No asumir que la API está bloqueada en planes bajos.

### 4) Integraciones relevantes

- **Webhooks nativos**: disparan eventos (p. ej. "Candidate Event") para enviar candidatos a sistemas HR, lanzar assessments, e-signing o background checks.
- **Zapier / Make**: conectores disponibles (incluido "Webhooks by Zapier"), permiten orquestar flujos sin código hacia cientos de apps.
- **LinkedIn**: integración **LinkedIn RSC (Recruiter System Connect)** y LinkedIn Ads vía Zapier.
- **Marketplace por categorías**: Assessments, CRM, E-signing, Employer Branding, HR Systems, Reference/Background Checking.
- **Assessments psicométricos/técnicos** (partners citados): **TestGorilla, AssessFirst, Codility, CodinGame, Talegent, PerformanSe, JobMatch, Pipplet, Astronaut, Evalart, Psigma**.

### 5) Limitaciones para búsqueda semántica por skills

Este es el punto crítico para el caso de Conexión Talento, y la evidencia es consistente:

- **No hay matching semántico nativo**: el screening/búsqueda de CVs se apoya en **keyword matching**, no en análisis semántico ni alineación de skills sofisticada.
- **Co-pilot ≠ motor de matching**: funciona como **asistente de redacción + screening por criterios**; **no rankea candidatos con fit-scores transparentes** ni genera **shortlists rankeadas por IA**. El shortlisting sigue siendo **manual**.
- **Competencias/skills** se almacenan como atributos del candidato y sirven de **filtro estructurado** (columna en la pestaña Candidates), pero eso es **filtrado exacto por etiqueta**, no búsqueda por similitud semántica ("encuéntrame perfiles parecidos a X aunque no usen las mismas palabras").
- **Fricciones reportadas**: ventana de previsualización de CV pequeña, datos del candidato fragmentados en múltiples lugares (notas, scores, mensajes, feedback), y analítica out-of-the-box limitada.

> En resumen: Teamtailor **no resuelve** "búsqueda semántica de los 4.000 candidatos por skills/seniority/idioma con ranking". Justo el corazón del proyecto.

---

## Qué significa para Conexión Talento

1. **El dato es recuperable y portable.** No hay lock-in duro: con una key Admin/Read se puede construir un **pipeline de extracción** (candidatos + relaciones + CVs) hacia un repositorio propio (data lake / Postgres + almacenamiento de objetos para los PDFs). Esto habilita el sistema de búsqueda propio sin pelear con la UI del ATS.
2. **El sistema de búsqueda semántica lo construimos nosotros, no lo compramos a Teamtailor.** Parsing de CVs → extracción estructurada de skills/experiencia → **embeddings + búsqueda vectorial** → ranking. Es exactamente la brecha de Teamtailor y el diferenciador de valor de nuestra propuesta.
3. **Diseñar para el rate limit desde el día 1.** 50 req/10s obliga a: extracción inicial *batch* + **sincronización incremental** vía `filter` por `updated-at` y/o **webhooks** para mantener el espejo actualizado casi en tiempo real sin reprocesar todo.
4. **Estandarización de datos = prerrequisito.** El screening de Co-pilot y nuestra búsqueda dependen de calidad/completitud de datos. Conviene **estandarizar custom fields, tags de skills y estructura de candidato en Teamtailor** (parte del encargo de "estructurar la base") para que tanto el ATS como el motor propio rindan.
5. **El Co-pilot puede convivir, no compite con nuestra solución.** Sirve para tareas operativas (resúmenes de CV, borradores, detección de sesgo, screening por criterios en una vacante puntual). Nuestro motor cubre lo que él no hace: **búsqueda transversal por similitud sobre toda la base**. Evaluar si el add-on justifica su costo según el plan contratado.
6. **Validaciones comerciales antes de la propuesta**: (a) confirmar **stack regional** de la cuenta (EU/NA/AU) — define el endpoint; (b) confirmar **scope de la API key actual** y si el plan vigente la incluye; (c) confirmar acceso a **descarga de CVs** vía API con la cuenta real; (d) pedir a Teamtailor el **detalle de qué incluye su plan** (Co-pilot, API, webhooks).
7. **Integraciones aprovechables sin desarrollo pesado**: webhooks + Zapier/Make para conectar assessments (TestGorilla/AssessFirst) y para alimentar el motor propio en cada cambio de candidato.

---

## Nivel de confianza y vacíos

**Confianza ALTA (fuentes oficiales de Teamtailor):**
- Existencia de API REST JSON:API, creación de keys, scopes Public/Internal/Admin × Read/Write, restricción de datos de candidato a Admin, endpoints de candidatos, stacks regionales, header `Authorization: Token`.
- Rate limit ~50 req/10s y la recomendación de ~300 ms (confirmado por doc de import oficial y por libs de terceros Nango).
- Catálogo de funciones del Co-pilot, motor OpenAI GPT, activación como add-on por Company Admin, lógica de screening ✓/✕/–.
- Flujo de import y manejo de CV como URL pública temporal.

**Confianza MEDIA (fuentes de terceros consistentes entre sí):**
- Limitación de búsqueda a keyword matching y ausencia de matching semántico / ranking por IA (coincide en skima.ai, recruiting-tools, hirevire y el propio detalle funcional del Co-pilot).
- Rangos de precio y modelo por job slots (Vendr, pin.com, paraform): direccionales, **no oficiales**.

**Confianza BAJA / NO VERIFICADO (vacíos):**
- **Mapeo exacto de qué función está en qué plan** (incl. si la API requiere Enterprise): proviene de un blog (pin.com) y **contradice** la evidencia de que cualquier Company Admin puede crear keys. **No confirmado oficialmente.**
- **Endpoint/forma exacta de descargar los archivos de CV** vía API (atributo `resume`/adjuntos): inferido, no documentado en detalle en las páginas accesibles. *Requiere prueba con la cuenta real.*
- **Paginación**: JSON:API usa `page[size]`/`page[number]`, pero la doc pública renderiza con JS y no pudimos extraer los topes exactos de page size; Nango indica que no hay paginación preconfigurada.
- **Precio específico para El Salvador/Guatemala**: no hay datos regionales; los rangos son de mercados US/EU.
- `docs.teamtailor.com` es una SPA con render por JS; **no fue legible vía fetch**. Para los detalles más finos (esquema de adjuntos, includes permitidos, topes de paginación) conviene revisar el portal de docs con navegador y/o probar con la API key real de Conexión Talento.

---

## Fuentes

1. https://support.teamtailor.com/en/articles/5963369-use-our-teamtailor-api — Oficial. Creación de API keys, scopes Public/Internal/Admin × Read/Write, stacks regionales, restricción de datos de candidato a Admin.
2. https://docs.teamtailor.com/ — Portal oficial de la API (JSON:API). No legible por fetch (SPA); referencia para verificación manual de endpoints/paginación.
3. https://support.teamtailor.com/en/articles/8890189-self-import-via-api — Oficial. Flujo de import por API, manejo de CV vía URL pública, rate limit 50 req/10s y recomendación de 300 ms.
4. https://nango.dev/docs/integrations/all/teamtailor — Tercero (Nango). Confirma rate limit 50/10s, auth `Authorization: Token token=`, header `X-Api-Version`, ausencia de paginación preconfigurada.
5. https://www.getknit.dev/blog/teamtailor-api-directory-YZ2QuV — Tercero (Knit). Lista de endpoints de candidatos/jobs/answers/notes/custom fields y modelo de autenticación.
6. https://support.teamtailor.com/en/articles/8403166-co-pilot-ai-features-overview — Oficial. Catálogo completo de funciones Co-pilot, motor OpenAI GPT, activación como add-on por Company Admin.
7. https://support.teamtailor.com/en/articles/10209597-co-pilot-candidate-screening — Oficial. Lógica de screening (✓/✕/–), fuentes de datos evaluadas, dependencia de calidad de datos.
8. https://skima.ai/blog/product-deep-dives/teamtailor-reviews — Tercero. Limitaciones: keyword matching, sin ranking por IA, sin shortlists, fricción de CV preview, analítica limitada.
9. https://www.pin.com/blog/teamtailor-pricing/ — Tercero. Tramos de precio, modelo job-slot, tabla de funciones por plan (incl. AI/API) — usar con cautela, no oficial.
10. https://www.teamtailor.com/en/integrations/ y https://support.teamtailor.com/en/articles/2861357-this-is-marketplace — Oficial. Marketplace, categorías de integraciones (assessments, HR, e-sign), webhooks.
11. https://zapier.com/apps/teamtailor/integrations — Tercero (Zapier). Conectores Teamtailor + LinkedIn + Webhooks vía Zapier/Make.
12. https://www.vendr.com/buyer-guides/teamtailor — Tercero (Vendr). Datos de compradores: rangos de precio (~US$229/mes a US$72k/año), contrato medio ~US$16.5k.
