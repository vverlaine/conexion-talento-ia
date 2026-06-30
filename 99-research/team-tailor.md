# Team Tailor — capacidades, IA, datos e integraciones

> Brief de investigación para Conexión Talento. Fecha: 2026-06-29. Foco: viabilidad de extraer ~4.000 candidatos con sus CVs, evaluar la IA nativa y decidir entre **augmentar** o **reemplazar** el ATS (el sistema donde guardan los candidatos, Team Tailor).

---

## En lenguaje ejecutivo (lo que importa para el negocio)

- **Recomendación: AUGMENTAR, no reemplazar.** Mantener Team Tailor como el sistema oficial donde viven los candidatos (registro, marca de empleador, flujo, cumplimiento) y construir **nosotros** el motor de búsqueda por habilidades. Cambiar de sistema destruiría valor (marca, flujo, histórico) y no resolvería el problema real.
- **La base es nuestra y se puede sacar.** Los ~4.000 candidatos con sus CVs se pueden descargar a un repositorio propio. No hay candado que lo impida; sí hay que programar la extracción (no es un botón).
- **La descarga es cuestión de horas, no días.** El único freno es un límite de velocidad (~5 peticiones por segundo) que se maneja con un script bien hecho.
- **La IA que trae Team Tailor (Co-pilot) NO busca talento por habilidades.** Es un asistente de redacción y de pre-filtrado por criterios candidato-a-candidato; no ordena ni encuentra "perfiles parecidos a X" en toda la base. Su búsqueda es por palabras exactas. Justo lo que el cliente necesita es lo que esta herramienta no hace.
- **El diferenciador de nuestra propuesta es exactamente esa brecha:** búsqueda inteligente por habilidades sobre toda la base, con resultados ordenados. Eso lo construimos nosotros.
- **Costo del ATS: opaco y por vacantes activas, no por usuario.** Rango de mercado ~US$2.750 a US$72.000+/año; contrato medio ~US$16.500/año; mínimo 12 meses. Para una boutique, la franja baja-media es la realista. El Co-pilot es un complemento de pago en los planes superiores.
- **El Co-pilot puede convivir con nuestra solución**, no compite: sirve para tareas operativas (resumir CVs, borradores, detectar sesgo). Evaluar si su costo se justifica según el plan.
- **Antes de la propuesta hay que confirmar 4 cosas con Team Tailor:** (1) en qué región está la cuenta, (2) qué permisos tiene la clave de acceso actual y si el plan la incluye, (3) que la descarga de CVs funciona en la cuenta real, (4) qué incluye exactamente el plan (Co-pilot, conexión técnica, avisos automáticos).

---

## Resumen ejecutivo

- **La extracción completa de la base es viable vía API REST** (la conexión técnica entre sistemas), no por un botón de "Export CSV/todo". Teamtailor expone una API pública (formato JSON:API) con endpoints (puntos de conexión) de candidatos; con una **clave de acceso de nivel Admin + lectura** se puede recorrer y descargar los ~4.000 candidatos, sus campos, respuestas, notas y la URL de su CV. Hay que **programar un script** (no es autoservicio de pantalla).
- **El límite de velocidad es el principal cuello de botella, no un bloqueo**: ~**50 peticiones por cada 10 segundos** (~5/s); con manejo de paginación e `includes`, bajar 4.000 candidatos + adjuntos es cuestión de **horas, no días**. Recomiendan ~300 ms entre llamadas.
- **La IA nativa ("Co-pilot") es un asistente de redacción y pre-filtrado por criterios (screening), NO un buscador inteligente de talento por habilidades**. Evalúa candidato-por-aplicación contra criterios (✓ / ✕ / – ) y resume CVs, pero **no ordena ni hace búsqueda por similitud sobre toda la base**. Reseñas independientes confirman que el "smart search" es esencialmente **búsqueda por palabras exactas (keyword matching)**, sin puntajes de ajuste ni listas cortas ordenadas por IA.
- **El Co-pilot es un complemento de pago (add-on)** (potenciado por modelos GPT de OpenAI), activable por el Company Admin, y disponible en los **planes superiores** (Business/Pro/Enterprise), no en el plan de entrada.
- **Precios opacos y modelo por "job slots" (vacantes activas)** (no por usuario; usuarios ilimitados). Rango de mercado: **~US$2.750 hasta US$72.000+/año**, contrato medio **~US$16.500/año**, mínimo **12 meses** y escaladores anuales del 3-8%. Para una boutique como Conexión Talento, la franja baja-media es la realista.
- **Buen ecosistema de integraciones**: avisos automáticos (webhooks, eventos de candidato), Zapier/Make, LinkedIn (RSC), y un Marketplace con pruebas psicométricas/técnicas (TestGorilla, AssessFirst, Codility, CodinGame, PerformanSe, JobMatch, etc.).
- **Recomendación: AUGMENTAR.** Mantener Teamtailor como **sistema de registro** (ATS, marca de empleador, flujo, cumplimiento) y **extraer la base a un motor propio de búsqueda inteligente por habilidades** (vectores semánticos + procesamiento de CVs). Es lo que el cliente realmente necesita y es justo donde Teamtailor es débil; reemplazar destruiría valor (marca de empleador, flujo, datos históricos) sin resolver el problema de búsqueda.

---

## Hallazgos detallados

### 1) Exportación / extracción de datos de candidatos

**Sí existe API REST pública (conexión técnica entre sistemas) y permite extraer la base.** Características confirmadas:

- **Especificación**: JSON:API (`application/vnd.api+json`). Endpoints (puntos de conexión) sobre `https://api.teamtailor.com/v1/...` (stack EU/Irlanda). Hay stacks regionales: **NA** `api.na.teamtailor.com` (Oregon) y **AU** `api.au.teamtailor.com`. *Conviene verificar en qué región está la cuenta de Conexión Talento.*
- **Autenticación**: token en header `Authorization: Token token=<API_KEY>` más header obligatorio `X-Api-Version`. La clave se crea en **Settings → Integrations → API keys** (solo Company Admin). Las claves **no se editan**, solo se borran.
- **Niveles de acceso (scopes)**: tres niveles (**Public / Internal / Admin**) × tres operaciones (**Read / Write / Read-Write**). **Los datos de candidatos están restringidos y requieren nivel Admin.** Para una extracción de solo lectura, lo ideal es **Admin + Read**.
- **Endpoints de candidatos** (lectura):
  - `GET /v1/candidates` — lista paginada de candidatos.
  - `GET /v1/candidates/{id}` — candidato individual.
  - Relacionados: `job-applications`, `answers` (respuestas a preguntas), `notes`, `custom-field-values`, `jobs`. Permite reconstruir todo el contexto del candidato.
- **Filtros y orden**: la API soporta `filter` por email, departamento, rol, ubicaciones, regiones y fechas de creación/actualización, y `sort` por atributos. Útil para extracciones incrementales (solo lo cambiado desde la última corrida).
- **CV / resume**: el modelo de candidato incluye un atributo de **resume** (URL del archivo). En el flujo de *import* el CV se maneja como URL pública descargable; en lectura, el CV se obtiene siguiendo la URL del adjunto. **La descarga masiva de los PDFs/CVs es factible**, aunque la documentación pública no detalla exhaustivamente el endpoint de adjuntos — *punto a validar con la cuenta real y una clave Admin.*
- **Formato**: la salida nativa es **JSON** (JSON:API). **No hay un "Export CSV de toda la base con CVs" en la pantalla**; el CSV se generaría del lado de Conexión Talento tras la extracción por API.
- **Límite de velocidad**: **~50 req / 10 s** (~5/s); exceder devuelve **HTTP 429**. Recomendación oficial: ~300 ms entre llamadas. La librería Nango marca que **no trae paginación preconfigurada**, es decir, **el cursor/paginación JSON:API (`page[size]`, `page[number]`) hay que implementarlo a mano**.
- **Volumen 4.000 candidatos**: a ~5 req/s, listar con paginación (p. ej. 30/página) + traer relaciones e `includes` + descargar CVs es perfectamente abordable en una sola corrida de **pocas horas**. No hay un tope documentado que impida bajar la base completa.
- **Import (contexto)**: existe "Self-import via API" para *cargar* candidatos (crear candidato → custom fields → answers → notes; el CV se sube a un servidor público y se pasa la URL). **Es unidireccional (import)**; la "exportación" no es una función empaquetada, se hace leyendo los mismos endpoints.

> **Conclusión técnica:** extraer toda la base (datos + CVs) hacia un sistema propio **es técnicamente viable y soportado**, mediante un script contra la API con clave Admin/Read. No esperar un export de un clic.

### 2) Funciones de IA ("Co-pilot")

- **Motor**: potenciado por **modelos GPT de OpenAI** ("la misma tecnología que ChatGPT").
- **Catálogo de funciones** (agrupadas):
  - *Candidate insights*: **Ask Co-pilot**, **Candidate screening** (pre-filtrado), **Candidate suggestions**, **Resume summaries** (resúmenes de CV), **Resume parser** (procesa el CV).
  - *Interview prep*: sugerencias de skills/traits, sugerencias de preguntas para interview kits, preguntas de aplicación, **detección de discriminación/sesgo**.
  - *Meetings & feedback*: **meeting insights** (resúmenes/transcripciones), respuestas de interview kit, **borradores de email de rechazo**.
  - *Content*: borradores de descripción de puesto, asistente del editor, traducción de preguntas.
  - *Analytics*: constructor de bloques de gráficos.
- **Cómo funciona el pre-filtrado (screening)**: evalúa cada candidato/aplicación contra **criterios definidos** usando resume, cover letter, respuestas a preguntas, comentarios, dirección, tags y custom fields (no privados). Devuelve **✓ (cumple) / ✕ (no cumple) / – (datos insuficientes)**. **Es evaluación por criterios, aplicación por aplicación**, no un ordenamiento global por probabilidad.
- **Disponibilidad**: **complemento de pago (add-on)** que un **Company Admin activa** en el "Add-on feature center". Según análisis de planes, **se incluye en los tramos Business/Pro/Enterprise, no en el de entrada**.

### 3) Planes y precios

- **Modelo**: por **job slots** (vacantes abiertas simultáneas), **no por asiento**; **usuarios ilimitados** y publicaciones ilimitadas en la mayoría de contratos.
- **Sin precios públicos** (solo cotización a medida; prueba de 14 días, sin tier gratuito).
- **Rango de mercado (datos de compradores)**: desde **~US$2.750/año (~US$229/mes)** en pequeño, **US$600-1.200/mes** en medio, hasta **US$72.000+/año** enterprise. **Contrato medio ~US$16.500-17.000/año.**
- **Diferencias por plan** (según análisis de mercado, *no oficial*): el **AI Co-pilot, SSO, nurture campaigns y SMS completo** aparecen en Business+; **CSM dedicado y capacidades avanzadas de API/data warehouse** se asocian a Enterprise.
- **Condiciones**: mínimo **12 meses**, sin mes-a-mes; **escaladores anuales 3-8%**; posibles fees de implementación (US$0-5.000+), overage de job slots y de SMS, integraciones premium con costo extra.

> ⚠️ La tabla de "qué plan incluye API" proviene de un blog de terceros (pin.com) y **debe confirmarse con un Account Executive**: hay evidencia de que **la creación de claves de API está disponible para Company Admins** con independencia de un tier "Enterprise". No asumir que la API está bloqueada en planes bajos.

### 4) Integraciones relevantes

- **Avisos automáticos (webhooks) nativos**: disparan eventos (p. ej. "Candidate Event") para enviar candidatos a sistemas HR, lanzar pruebas, e-signing o background checks.
- **Zapier / Make**: conectores disponibles (incluido "Webhooks by Zapier"), permiten orquestar flujos sin código hacia cientos de apps.
- **LinkedIn**: integración **LinkedIn RSC (Recruiter System Connect)** y LinkedIn Ads vía Zapier.
- **Marketplace por categorías**: Assessments, CRM, E-signing, Employer Branding, HR Systems, Reference/Background Checking.
- **Pruebas psicométricas/técnicas** (partners citados): **TestGorilla, AssessFirst, Codility, CodinGame, Talegent, PerformanSe, JobMatch, Pipplet, Astronaut, Evalart, Psigma**.

### 5) Limitaciones para búsqueda inteligente por habilidades

Este es el punto crítico para el caso de Conexión Talento, y la evidencia es consistente:

- **No hay búsqueda por similitud nativa**: el pre-filtrado/búsqueda de CVs se apoya en **búsqueda por palabras exactas (keyword matching)**, no en análisis por similitud de significado ni alineación de habilidades sofisticada.
- **Co-pilot ≠ motor de búsqueda inteligente**: funciona como **asistente de redacción + pre-filtrado por criterios**; **no ordena candidatos con puntajes de ajuste transparentes** ni genera **listas cortas ordenadas por IA**. La selección de finalistas sigue siendo **manual**.
- **Competencias/skills** se almacenan como atributos del candidato y sirven de **filtro estructurado** (columna en la pestaña Candidates), pero eso es **filtrado exacto por etiqueta**, no búsqueda por similitud de significado ("encuéntrame perfiles parecidos a X aunque no usen las mismas palabras").
- **Fricciones reportadas**: ventana de previsualización de CV pequeña, datos del candidato fragmentados en múltiples lugares (notas, scores, mensajes, feedback), y analítica de fábrica limitada.

> En resumen: Teamtailor **no resuelve** "búsqueda inteligente de los 4.000 candidatos por habilidades/seniority/idioma con ordenamiento de resultados". Justo el corazón del proyecto.

---

## Qué significa para Conexión Talento

1. **El dato es recuperable y portable.** No hay candado duro: con una clave Admin/Read se puede construir un **proceso de extracción** (candidatos + relaciones + CVs) hacia un repositorio propio (data lake / Postgres + almacenamiento para los PDFs). Esto habilita el sistema de búsqueda propio sin pelear con la pantalla del ATS.
2. **El sistema de búsqueda inteligente lo construimos nosotros, no lo compramos a Teamtailor.** Procesar los CVs → extraer de forma estructurada habilidades/experiencia → **búsqueda por similitud de significado (vectores)** → ordenamiento de resultados. Es exactamente la brecha de Teamtailor y el diferenciador de valor de nuestra propuesta.
3. **Diseñar para el límite de velocidad desde el día 1.** 50 req/10s obliga a: extracción inicial completa + **sincronización incremental** vía `filter` por `updated-at` y/o **avisos automáticos (webhooks)** para mantener el espejo actualizado casi en tiempo real sin reprocesar todo.
4. **Estandarización de datos = prerrequisito.** El pre-filtrado de Co-pilot y nuestra búsqueda dependen de calidad/completitud de datos. Conviene **estandarizar custom fields, etiquetas de habilidades y estructura de candidato en Teamtailor** (parte del encargo de "estructurar la base") para que tanto el ATS como el motor propio rindan.
5. **El Co-pilot puede convivir, no compite con nuestra solución.** Sirve para tareas operativas (resúmenes de CV, borradores, detección de sesgo, pre-filtrado por criterios en una vacante puntual). Nuestro motor cubre lo que él no hace: **búsqueda por similitud sobre toda la base**. Evaluar si el complemento justifica su costo según el plan contratado.
6. **Validaciones comerciales antes de la propuesta**: (a) confirmar **región de la cuenta (EU/NA/AU)** — define el endpoint; (b) confirmar **nivel de acceso de la clave de API actual** y si el plan vigente la incluye; (c) confirmar acceso a **descarga de CVs** vía API con la cuenta real; (d) pedir a Teamtailor el **detalle de qué incluye su plan** (Co-pilot, API, avisos automáticos).
7. **Integraciones aprovechables sin desarrollo pesado**: avisos automáticos (webhooks) + Zapier/Make para conectar pruebas (TestGorilla/AssessFirst) y para alimentar el motor propio en cada cambio de candidato.

---

## Nivel de confianza y vacíos

**Confianza ALTA (fuentes oficiales de Teamtailor):**
- Existencia de API REST JSON:API, creación de claves, niveles Public/Internal/Admin × Read/Write, restricción de datos de candidato a Admin, endpoints de candidatos, regiones, header `Authorization: Token`.
- Límite de velocidad ~50 req/10s y la recomendación de ~300 ms (confirmado por doc de import oficial y por libs de terceros Nango).
- Catálogo de funciones del Co-pilot, motor OpenAI GPT, activación como complemento por Company Admin, lógica de pre-filtrado ✓/✕/–.
- Flujo de import y manejo de CV como URL pública temporal.

**Confianza MEDIA (fuentes de terceros consistentes entre sí):**
- Limitación de búsqueda a palabras exactas (keyword matching) y ausencia de búsqueda por similitud / ordenamiento por IA (coincide en skima.ai, recruiting-tools, hirevire y el propio detalle funcional del Co-pilot).
- Rangos de precio y modelo por vacantes activas (job slots) (Vendr, pin.com, paraform): direccionales, **no oficiales**.

**Confianza BAJA / NO VERIFICADO (vacíos):**
- **Mapeo exacto de qué función está en qué plan** (incl. si la API requiere Enterprise): proviene de un blog (pin.com) y **contradice** la evidencia de que cualquier Company Admin puede crear claves. **No confirmado oficialmente.**
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
