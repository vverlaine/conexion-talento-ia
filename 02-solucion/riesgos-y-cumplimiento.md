# Riesgos, privacidad y cumplimiento
### Memoria del proyecto Conexión Talento — Entregable de gobierno

> **Propósito.** Este documento consolida la exposición a riesgos del programa y fija la postura de cumplimiento que condiciona qué se puede construir, vender y automatizar —y en qué orden—. Es deliberadamente **contundente** en protección de datos de candidatos porque ahí está la mayor distancia entre lo que el cliente *quiere hacer* y lo que *puede hacer legalmente*. Las recomendaciones priman la integridad sobre el tamaño del encargo: en nuestro primer proyecto, una bandera legal mal gestionada no es un riesgo de negocio, es existencial.

---

## 1. Resumen ejecutivo

La mayor amenaza de este programa **no es técnica, es de cumplimiento y secuencia**. El cliente quiere monetizar una base de ~4.000 candidatos (vender un benchmark de compensaciones, hacer cross-sell de capacitaciones) y automatizar el cribado con auto-rechazo —exactamente los dos frentes con mayor exposición legal y reputacional, y donde menos margen de error tenemos.

**Los cinco riesgos que pueden hundir el proyecto, en orden de severidad:**

| # | Riesgo | Por qué es crítico |
|---|--------|--------------------|
| 1 | **Monetización ilícita de datos de candidatos** (benchmark + cross-sell sin base legal) | Reutilizar datos recolectados para reclutamiento con fines comerciales viola limitación de finalidad; el benchmark añade riesgo de re-identificación, antitrust y ruptura de NDAs con los clientes que pagan el 63% de los ingresos. |
| 2 | **Discriminación algorítmica en el cribado** | Rankear sobre datos históricos replica sesgo (género, edad, foto, origen); el auto-rechazo en rank 30+ sin humano lo sistematiza a escala de 200 CVs por proceso. |
| 3 | **Brecha de PII activa HOY** (CVs pegados en ChatGPT de consumo) | No es riesgo futuro: es transferencia internacional de datos y posible entrenamiento del modelo, en curso. |
| 4 | **Promesa de quick wins sobre supuestos no verificados** (API de Team Tailor, golden set, país) | Toda la Fase 0 cuelga de capacidades que nadie confirmó. Prometer y no cumplir quema el primer cliente. |
| 5 | **Fuga de Lili (flight risk)** | Punto único de falla, champion y cuello de botella, a 7am–7pm. Si renuncia antes de extraer su conocimiento, se va la operación, la memoria y la adopción de golpe. |

**Postura de gobierno (decisiones que tomamos HOY, no en Fase 3):**
- **CONGELAR** toda venta de benchmark y todo cross-sell a la base hasta cerrar base legal, consentimiento y anonimización. Esfuerzo cero, evita el peor riesgo.
- **HUMANO OBLIGATORIO** antes de cualquier comunicación de rechazo. La IA pre-ordena; nunca decide ni comunica sola.
- **CORTAR** el uso de ChatGPT de consumo con datos de candidatos esta semana.
- **NO PROMETER** ningún entregable que dependa de la API de Team Tailor antes de un *spike de factibilidad* que la verifique (ver §3).

---

## 2. Cómo leer este registro (metodología)

- **Probabilidad** e **Impacto** en escala Alta / Media / Baja. **Severidad** = combinación (🔴 crítico / 🟠 alto / 🟡 medio).
- Cada riesgo tiene **dueño nominal** y **disparador de mitigación**. Sin dueño, un riesgo es un deseo.
- Los supuestos no confirmados se marcan **⚠️ a validar**. No los disfrazamos de hechos: son precondiciones.
- Este documento **reconcilia** las tensiones entre las lentes de análisis (datos vs. proceso vs. métricas) que, de no resolverse, dejan la ruta crítica flotando (ver §3 y §8).

---

## 3. Precondiciones bloqueantes (apagar antes de cotizar)

La crítica adversarial fue certera: varios "quick wins P0" descansan sobre supuestos que **nadie verificó**. Los reencuadramos de "preguntas abiertas" a **precondiciones con dueño y contingencia**. Recomendamos una **Fase −1: Spike de Factibilidad Técnica y Legal (1 semana, pagada)** antes de comprometer alcance o precio.

| Precondición | Por qué bloquea | Dueño | Contingencia si falla |
|---|---|---|---|
| **País de operación y de residencia de candidatos/clientes** ⚠️ | Define ley aplicable, registro de base ante regulador, plazos, sanciones y **viabilidad del benchmark**. Es un correo de 5 min a Virginia; resolverlo HOY. | Virginia / Consultor líder | Sin país no hay scoping legal: no se cotiza Fase 1+. |
| **API / export / tier de Team Tailor** ⚠️ | Sostiene extracción, baseline retrospectiva, dedup y RAG. | Consultor líder + soporte TT | Si no hay export masivo: trabajar dentro de TT (campos/vistas), posponer almacén propio. |
| **Existencia de golden set** (historial recuperable de quién entró a terna vs. no) ⚠️ | Sin él no se calibra ni se audita el Screener. Con CERO documentación, probablemente **no existe** y crearlo exige tiempo de Virginia (el recurso más escaso y resistente). | Virginia | Sin golden set: el cribado IA se pospone; no se promete en Fase 2. |
| **Origen y consentimiento de los 4.000** ⚠️ (¿aplicaron voluntariamente o fueron sourced/scraped de LinkedIn?) | Cambia por completo la base legal para cualquier uso secundario. | Virginia | Si origen no trazable: la base es pasivo legal, no activo monetizable. |
| **Candidatos o clientes en la UE** ⚠️ | Activa GDPR Art. 22 (decisión automatizada) y EU AI Act (cribado = alto riesgo, Anexo III). | Virginia | Si hay exposición UE: gap assessment obligatorio antes de operar IA de selección. |

> **Regla de oro:** no prometemos ningún P0 que cuelgue de una capacidad no confirmada. El spike apaga estos supuestos o los confirma; recién entonces se fija precio y alcance.

---

## 4. Registro de riesgos

### 4.1 Riesgos legales y de cumplimiento

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Dueño |
|----|--------|:---:|:---:|:---:|------------|-------|
| L1 | **Venta del benchmark de compensaciones sin base legal** (re-identificación en mercado pequeño, antitrust por intercambio de datos salariales entre empresas, violación de NDAs con clientes) | Alta | Alto | 🔴 | Congelar el producto. Reconstruir solo en Fase 3 con: consentimiento granular, anonimización por k-anonimato (N mínimo por celda rol×sector×país), validación legal local y verificación contractual del derecho a reutilizar datos de comp. | Consultor + abogado local ⚠️ |
| L2 | **Cross-sell de capacitaciones a la base = violación de limitación de finalidad** | Alta | Alto | 🔴 | Bloquear hasta tener opt-in separado por finalidad. Datos de reclutamiento ≠ datos de marketing. | Consultor + Virginia |
| L3 | **Inyección de PII en ChatGPT de consumo** (brecha activa) | Alta (en curso) | Alto | 🔴 | Prohibir hoy. Migrar el prompt a ChatGPT Enterprise/Team o API con no-entrenamiento + DPA. | Consultor líder |
| L4 | **Operar sin aviso de privacidad ni consentimiento trazable** en el punto de aplicación | Alta | Alto | 🟠 | Publicar aviso de privacidad en el formulario (LinkedIn/TT): finalidades, base legal, plazos, derechos ARCO. | Virginia |
| L5 | **Falta de registro de base de datos ante el regulador** (PRODHAB-CR / ANTAI-PA según país ⚠️) | Media | Alto | 🟠 | Checklist legal de 1 página por país; registrar si aplica. | Abogado local ⚠️ |
| L6 | **Sin política de retención** (4.000 retenidos indefinidamente, "no saben cuántos vigentes") | Alta | Medio | 🟠 | Definir plazos, trazar origen del consentimiento, purgar/anonimizar caducos (RoPA-lite). | Consultor + Virginia |
| L7 | **Grabación de pre-screening sin consentimiento explícito** (la voz puede ser dato biométrico; transcripción + detección de competencias = profiling) | Media | Alto | 🟠 | Guion de consentimiento al inicio de cada llamada; definir almacenamiento y retención de audios/transcripciones. | Lili / reclutadores |
| L8 | **La consultora se vuelve sub-procesadora de PII** al exportar la base a un almacén propio | Media | Alto | 🟠 | DPA cliente–consultora, cifrado, control de accesos, ubicación definida de los datos, borrado al cierre del engagement. | Consultor líder |
| L9 | **Decisión automatizada sin intervención humana** (auto-rechazo rank 30+, correo a 15 días) — incumple GDPR Art. 22 si hay exposición UE | Media | Alto | 🟠 | HITL obligatorio (ver §6). Logging de cada decisión con justificación citada. | Consultor + Lili |

### 4.2 Riesgos técnicos

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Dueño |
|----|--------|:---:|:---:|:---:|------------|-------|
| T1 | **API/export de Team Tailor limitado o rate-limited** ⚠️ | Media | Alto | 🟠 | Verificar en spike (§3). Diseñar capa portable; plan B dentro de TT. | Consultor líder |
| T2 | **RAG/búsqueda vectorial sobre base sucia** → recuperación basura con alta confianza | Alta | Alto | 🟠 | Orden obligatorio: identidad → estructura → frescura → taxonomía → *recién ahí* embeddings. No saltar a lo vectorial primero. | Consultor de datos |
| T3 | **Alucinación de cifras salariales/mercado** por LLM presentadas como autoridad | Alta | Alto | 🔴 | Prohibir cifras generadas por el modelo. Solo fuentes licenciadas o dataset propio con N mínimo, citadas con fuente y fecha. | Consultor de datos |
| T4 | **Errores de resolución de identidad**: fusionar dos personas distintas expone historial ajeno (brecha de privacidad); no fusionar deja pasar duplicados | Media | Alto | 🟠 | Umbrales conservadores, revisión humana de matches dudosos, fusión **reversible** (enlazar, no borrar). | Consultor de datos |
| T5 | **Alucinación en parsing de CV** (skills/fechas inventadas) | Media | Medio | 🟡 | Esquema de salida estricto, validación de consistencia, muestreo humano 5–10%, trazar siempre al CV fuente. | Consultor de datos |
| T6 | **Migración precipitada fuera de Team Tailor** rompe integraciones (LinkedIn, psicométricas, rechazos) y traslada seguridad/brechas a una PYME de 10 personas | Media | Alto | 🟠 | NO migrar. Augmentar vía API primero; decidir con datos y análisis de riesgo de seguridad, no por entusiasmo. | Consultor + Virginia |
| T7 | **Sobre-ingeniería "agéntica"** (6 agentes autónomos sin proceso ni métricas = ingobernable) | Media | Medio | 🟡 | Reframe: 3 herramientas deterministas + 1 orquestador con routing determinista y HITL. Autonomía solo donde aporta (Sourcer). Guardarraíles como código (structured output), no como instrucción de prompt. | Consultor de IA |

### 4.3 Riesgos de adopción y capacidad de entrega

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Dueño |
|----|--------|:---:|:---:|:---:|------------|-------|
| A1 | **Fuga de Lili (burnout, 7am–7pm)** — punto único de falla, champion y cuello de botella | Media | Alto | 🔴 | Liberar su tiempo PRIMERO. Extraer su conocimiento en semanas 2–3 (no en Fase 1 tardía). Enmarcar la temporal como **seguro anti-fuga**, no solo alivio. | Virginia |
| A2 | **Resistencia por identidad profesional** (la IA percibida como deskilling del "ojo clínico") | Alta | Alto | 🟠 | Narrativa "la IA potencia tu criterio, tú decides". Co-diseño de la rúbrica (ellos son autores). El guardarraíl "la IA no opina" es el mensaje central de adopción, no una restricción técnica. | Consultor de cambio |
| A3 | **Conflicto sponsor-usuario**: Virginia decide el cambio y es reclutadora con método propio | Media | Alto | 🟠 | Pacto de que adopta primero y públicamente (su prompt de CV como prueba). Coaching de sponsor 30 min/sem. | Consultor de cambio |
| A4 | **Presupuesto del temp quemado en backfill operativo** → cero capacidad instalada, dependencia regresa en mes 4 | Media | Medio | 🟡 | Usar el temp para **descargar la operación de Lili** (su pedido real) y proteger horas de ella y de Virginia para diseño. No poner al temp a etiquetar contra ESCO (es trabajo calificado). | Virginia |
| A5 | **Capacidad de NUESTRA consultora**: boutique, primer proyecto, líder sin RRHH ni compliance in-house | Alta | Alto | 🟠 | Plan de staffing explícito: qué hace el consultor, qué se **subcontrata** (legal de datos, ASR), y qué se co-autora con Lili (cubre el gap de dominio HR). No prometer "McKinsey/BCG" en frentes sin capacidad declarada. | Consultor líder |
| A6 | **Dependencia circular en la ruta crítica** sin dueño: estandarizar etapas ← liberar a Lili ← IA de cribado ← golden set ← tiempo de Virginia | Alta | Alto | 🟠 | **Romper el ciclo** así: (1) temp descarga operación de Lili → libera 4–6h/sem de Lili; (2) Lili y Virginia co-documentan rúbrica/golden set *manualmente* en sesiones cronometradas de 45 min; (3) recién entonces se construye el Screener. Ver §8. | Consultor líder |

### 4.4 Riesgos reputacionales

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Dueño |
|----|--------|:---:|:---:|:---:|------------|-------|
| R1 | **Reenvío del mismo candidato 2 veces al mismo cliente** (ya materializado) | Alta | Alto | 🟠 | Registro de presentaciones candidato×cliente×fecha + regla de no-reenvío + alerta de duplicado. Check **determinista** (SQL/API), no IA. Quick win de horas. | Consultor de datos |
| R2 | **Ataques en LinkedIn por mala experiencia de candidato** — el diferenciador que venden ("cercanía") es hoy su mayor pasivo | Alta | Alto | 🟠 | SLA de comunicación (acuse 48h, actualización de estado, rechazo personalizado) **antes** de medir CSAT. Rol de "embajador de marca". | Consultor + Lili |
| R3 | **Encuestar a candidatos enojados antes de reparar el SLA** → más backlash ("me ignoraron y ahora preguntan cómo me sentí") | Media | Medio | 🟡 | Secuenciar: reparar comunicación PRIMERO, lanzar CSAT después. | Consultor de cambio |
| R4 | **Auto-rechazo por IA sin humano** amplifica el daño reputacional ya existente y expone a sesgo no auditable | Media | Alto | 🔴 | HITL obligatorio (§6). Rechazos en batch revisado antes de enviar. | Lili |
| R5 | **Primer proyecto fallido = anti-referencia** (no caso de éxito), por brecha presupuesto/recursos | Media | Alto | 🟠 | Kill-criteria y go/no-go con cifras (§7). Alcance quirúrgico. No "casi regalar" Fase 0 asumiendo éxito sin verificar precondiciones. | Consultor líder |
| R6 | **Sobrepromesa de "mismo día"** a una CEO enamorada del concepto | Media | Medio | 🟡 | Enterrar "mismo día", no reprogramarlo a Fase 3. Prometer time-to-submit (controlable) y mejoras sobre baseline propia. | Consultor comercial |

---

## 5. Protección de datos de candidatos — sección contundente

> Esta es la sección que el cliente menos quiere oír y más necesita. La base de 4.000 candidatos **no es "oro" todavía**: una parte relevante es **pasivo legal** —consentimiento dudoso, origen no trazable, datos caducos, sin finalidad de venta declarada—. Monetizarla tal cual dispararía justo el daño reputacional que el cliente teme, **más** exposición regulatoria real. El valor se materializa *después* de arreglar la capa de base legal, no antes.

### 5.1 Marco legal aplicable — El Salvador (vigente) + Guatemala ✅

**Jurisdicción confirmada:** El Salvador (operación primaria) y Guatemala (secundaria). Esto cambia el tono: **El Salvador YA regula** —no es un marco laxo como se asumía—, así que el cumplimiento es obligación de hoy, no opción de mañana. Lo convertimos en argumento de venta ("cumplimiento por diseño"). Detalle y fuentes en [`99-research/marco-legal-datos-sv-gt.md`](../99-research/marco-legal-datos-sv-gt.md).

| País | Ley / Regulador | Implicación para Conexión Talento |
|------|-----------------|-------------|
| **El Salvador** (primario) | **Ley de Protección de Datos Personales — Decreto 144/2024, VIGENTE**, con regulador propio | **Es sujeto obligado HOY:** consentimiento por finalidad, derechos del titular, retención, registro de tratamientos, responsable de datos y protocolo de brechas. El benchmark de compensaciones **solo es lícito anonimizado de forma irreversible y agregada (k-anonimato)**. |
| **Guatemala** (secundario) | Sin ley general aún (habeas data constitucional; iniciativas en trámite) | Menos obligaciones formales, pero **no exime** de responsabilidad civil/contractual. Aplicamos el estándar salvadoreño como anticipación y diferenciador. |
| **UE** (solo si aplica) ⚠️ | GDPR + EU AI Act | Solo si hay candidatos/clientes en la UE. *Pregunta de scoping temprana.* |

> ⚠️ **A validar antes de citar en contrato o lanzar el benchmark:** el articulado exacto del Decreto 144/2024 provino de fuente secundaria; **se requiere dictamen de un abogado salvadoreño** y cotejo contra el Diario Oficial, más revisar el reglamento/lineamientos del regulador posteriores a su entrada en vigor (donde estarían las reglas concretas de retención, registro y decisiones automatizadas).

Y si hay **candidatos o clientes en la UE** ⚠️: GDPR Art. 22 (decisión automatizada exige intervención humana, explicación y derecho a impugnar) + EU AI Act (cribado de candidatos = **alto riesgo**, Anexo III, con gestión de riesgo, gobernanza de datos, supervisión humana, transparencia y logging obligatorios). Es también blindaje frente a clientes multinacionales.

### 5.2 Base legal y limitación de finalidad — el principio que el cliente está a punto de violar

Los datos se recolectaron para **una finalidad: postular a una vacante**. Cualquier uso secundario (benchmark comercial, marketing de capacitaciones) **excede esa finalidad** y requiere una de dos cosas:
1. **Consentimiento separado y específico** para la nueva finalidad, o
2. **Interés legítimo documentado** + mecanismo de opt-out funcional (y aun así, no aplica a datos sensibles ni a venta de datos).

**Sin esto, no hay base legal.** "Tenemos sus datos" no equivale a "podemos usarlos para lo que queramos".

### 5.3 Consentimiento granular — el diseño correcto

Implementar **opt-in granular** desde el formulario de aplicación:

- ☐ Tratamiento de mis datos para **procesos de reclutamiento** (base del servicio).
- ☐ Recibir **ofertas de capacitación / formación** (cross-sell — finalidad separada).
- ☐ Inclusión **anonimizada** en **estudios de compensación** (benchmark — finalidad separada).

Más: gestión de preferencias, opt-out funcional, y **registro de la fecha y el origen del consentimiento como campo de datos**. Esto **habilita** la monetización de forma lícita en vez de bloquearla.

### 5.4 Por qué VENDER el benchmark de compensaciones es la bandera roja #1

Es, a la vez, la mayor oportunidad de monetización **y** el mayor riesgo. Vendido "crudo" es una **factura legal con tono de autoridad**, no un producto. Cuatro razones convergentes:

1. **Origen de los datos confidencial.** Las cifras salariales provienen de expectativas de candidatos y de **negociaciones con clientes**, muy probablemente cubiertas por NDA o cláusulas de confidencialidad. Venderlas puede **violar contratos con los propios clientes que pagan el 63% de los ingresos** → litigio con quien más te importa.
2. **Re-identificación en mercado pequeño.** En Centroamérica, "el salario del CFO de la empresa X" sigue siendo atribuible **aun agregado**. **Anonimizado ≠ libre de usar.** Sin umbrales de k-anonimato (N mínimo de empresas/registros por celda), es un incidente esperando ocurrir.
3. **Riesgo de derecho de competencia (antitrust).** El intercambio de datos de compensación entre empresas puede constituir colusión según la jurisdicción. Requiere validación legal local explícita.
4. **Alucinación si lo genera un LLM.** Sin fuente licenciada (Mercer/Korn Ferry/encuestas locales) o dataset propio estadísticamente válido (con N por celda), las cifras son inventadas con apariencia de rigor.

**Decisión de gobierno: CONGELAR la venta del benchmark.** No se promete en la propuesta del viernes. Camino positivo (para honrar la ambición de Virginia, no solo decir "no"): explorar una **alianza con un proveedor licenciado de comp-data**, o construir el producto en Fase 3 con consentimiento granular + anonimización por diseño + validación contractual y legal. **Bien, no rápido.**

### 5.5 Cross-sell de capacitaciones sin consentimiento adecuado — la otra bandera roja

Es **exactamente el mismo vector** que ya les genera ataques en LinkedIn (contacto no deseado / falta de seguimiento). Monetizar mal **amplifica el daño reputacional que dicen temer**. No se hace cross-sell a la base sin el opt-in específico de §5.3. Punto.

### 5.6 Brecha activa HOY — el prompt de Virginia en ChatGPT

El "prompt" para estandarizar CVs casi seguro **inyecta PII completa de candidatos en ChatGPT de consumo**: transferencia internacional de datos y posible uso para entrenamiento del modelo. **Es una brecha en curso, no un riesgo futuro.** Cortar esta semana: prohibir pegar CVs en ChatGPT personal; migrar a Enterprise/Team o API con no-entrenamiento + DPA. Costo casi nulo, cierra el riesgo de inmediato.

### 5.7 Retención, inventario y la consultora como procesadora

- **RoPA-lite:** registro de actividades de tratamiento (qué datos, de dónde, con qué base legal, dónde se almacenan, con quién se comparten, cuánto se conservan).
- **Política de retención:** plazos definidos, purga/anonimización de caducos. Una base retenida indefinidamente viola limitación de conservación.
- **La consultora se vuelve sub-procesadora** al exportar los 4.000 a un almacén propio: exige **DPA cliente–consultora**, cifrado, control de accesos, ubicación definida y **borrado al cierre**. Introducimos un nuevo vector de brecha; hay que cerrarlo *antes* de tocar la base.

### 5.8 Historial de candidato — legítimo, pero con límites

El historial candidato×cliente para evitar el reenvío duplicado es **legítimo y resuelve un riesgo reputacional real**. PERO: **no** convertirlo en lista negra compartida entre clientes, **ni** en decisión adversa automatizada. El historial **informa al reclutador**; no excluye automáticamente.

---

## 6. Sesgo en cribado automático, explicabilidad y decisión humana

### 6.1 El riesgo: discriminación a escala

Puntuar/rankear sobre datos históricos **replica la discriminación histórica** —género, edad, nombre, foto u origen como proxies—. El caso emblemático es la herramienta de reclutamiento **descartada por Amazon** por sesgo de género. Sin auditoría, el Screener/Ranker sistematiza discriminación sobre **200 CVs por proceso**, con responsabilidad legal-laboral directa para la consultora **y** para el cliente final.

Agravante centroamericano: los CVs suelen incluir **foto, edad, estado civil y nacionalidad**. Alimentar eso directo al scorer **inyecta sesgo medible**.

### 6.2 Controles obligatorios antes de poner cualquier IA de cribado en producción

1. **Des-identificación de PII (PII stripping)** antes del scoring: remover foto, edad, estado civil, nacionalidad, nombre, señales de maternidad. Por equidad y por defendibilidad del proceso.
2. **Exclusión explícita de variables proxy prohibidas** de las features del modelo.
3. **Auditoría de sesgo:** medir *selection rate* por grupo (género/edad) y disparidad; documentar el resultado.
4. **Golden set + rúbrica construidos CON Virginia** ⚠️: convertir su "ojo clínico" en una matriz explícita (criterios, pesos, escalas, ejemplos) anclada en decisiones históricas. Sin esto, el scorer no replica su criterio, el cliente lo rechaza, y no hay forma de medir accuracy ni sesgo. **Es el artefacto más crítico del proyecto** y no debe definirlo un equipo no-RRHH solo.
5. **Caveat estadístico de boutique** ⚠️: con ~20–60 colocaciones/año, la auditoría de sesgo y el accuracy del ranker tienen **n insuficiente** para significancia robusta. Reportar siempre el n; tratar resultados como indicativos, no como prueba. Esto refuerza por qué el cribado IA es Fase 2+, no un quick win.

### 6.3 Explicabilidad y decisión humana (human-in-the-loop)

| Principio | Implementación |
|-----------|----------------|
| **La IA pre-ordena; el humano decide.** | El ranking **nunca** es decisión final automática. Reclutador valida top 10 y terna. |
| **Eliminar el auto-rechazo (rank 30+, correo a 15 días) como decisión final sin revisión.** | Rechazos en **batch revisado** antes de enviar, o HITL caso por caso. Protege cumplimiento (GDPR Art. 22) **y** el diferenciador de "cercanía". |
| **Cada score con justificación citada al CV.** | Sin inventar: la IA extrae evidencia contra los criterios del perfil y cita la fuente textual. Logging de cada decisión. |
| **Protocolo de discrepancia.** | Cuando IA y humano difieren: **gana el humano** y se ajusta la rúbrica. La confianza se construye mostrando "la IA coincidió en X de 10", no por fe. |
| **Guardarraíles como código.** | Los umbrales (top10 / 10–20 / 30+) disparan acciones por reglas deterministas, con **gate humano** en rechazos y terna. "La IA no opina fuera de scope" se fuerza con *structured output*, no con una instrucción de prompt. |

---

## 7. Recomendaciones: qué hacer / qué NO hacer

### ✅ HACER (acciones de bajo esfuerzo y alto valor, secuenciadas)

1. **Confirmar el país HOY** ⚠️ y producir un checklist legal de 1 página (ley aplicable, registro, plazos, sanciones). Designar un **responsable de datos** interno (Virginia o Lili).
2. **Cortar el ChatGPT de consumo** con PII de candidatos esta semana (Enterprise/API + DPA + no-entrenamiento).
3. **Implementar el registro de presentaciones** candidato×cliente×fecha con alerta de duplicado (determinista, SQL/API). Cierra R1 en días.
4. **Publicar el aviso de privacidad** en el formulario de aplicación (finalidades, base legal, plazos, derechos).
5. **Reparar el SLA de comunicación al candidato** *antes* de lanzar cualquier encuesta CSAT (evita R3).
6. **HITL obligatorio** en todos los rechazos, desde ya.
7. **Levantar el inventario de datos (RoPA-lite)** y la política de retención; muestrear vigencia real de la base antes de invertir en enriquecerla.
8. **Firmar DPAs** con Team Tailor, proveedor de IA/ASR y OpenAI; **DPA cliente–consultora** para nuestro rol de procesador.
9. **Ejecutar el Spike de Factibilidad (Fase −1)** que apaga los supuestos frágiles (§3) antes de cotizar.
10. **Construir la rúbrica/golden set CON Virginia** antes de escribir una línea de código del Screener.

### ⛔ NO HACER (líneas rojas del programa)

1. **NO vender el benchmark de compensaciones** hasta tener base legal, anonimización por k-anonimato, validación antitrust y verificación contractual. No prometerlo el viernes.
2. **NO hacer cross-sell** a la base sin opt-in específico y separado.
3. **NO dejar que la IA rechace ni comunique** a un candidato sin revisión humana.
4. **NO alimentar el scorer con PII sensible** (foto, edad, estado civil, origen, nombre).
5. **NO exponer cifras salariales generadas por un LLM** como si fueran datos.
6. **NO migrar fuera de Team Tailor** ni extraer la base antes de tener taxonomía, protocolo de vigencia y un caso de negocio con datos.
7. **NO tratar "anonimizado" como sinónimo de "libre de regulación"**, ni asumir que los 4.000 tienen consentimiento válido para monetización.
8. **NO poner al temp a hacer ingeniería de datos** mientras Lili sigue ahogada: se quema la champion (A1/A4).
9. **NO construir los 6 "agentes"** sobre un proceso sin estandarizar: escala la inconsistencia a velocidad de máquina.
10. **NO sobre-prometer** "mismo día" ni ROI sin línea base propia.

### Go/No-Go y kill-criteria (cifras, no adjetivos) ⚠️

Estos umbrales deben calibrarse con el cliente; se proponen como ancla:

- **Fase −1 (Spike) supera el gate si:** API/export de TT confirmado **o** plan B viable definido **+** país y consentimiento confirmados **+** evidencia de golden set utilizable (o plan financiado para crearlo). **Si no → no se cotiza Fase 1; se replantea.**
- **Fase 0 exitosa si:** ≥X% de duplicados detectados por el dedup **+** plantilla de CV adoptada por los 4 reclutadores **+** baseline de 3 KPIs entregada. **Si no → se detiene antes de Fase 1.**
- **Kill-criteria de cumplimiento (absoluto):** si no se puede establecer base legal/consentimiento para el tratamiento de la base, **se detiene toda iniciativa de monetización**, sin excepción.

---

## 8. Reconciliación de la ruta crítica (resolviendo la tensión entre análisis)

Las lentes de análisis se contradicen en la secuencia, y dejarlo sin resolver es un riesgo en sí mismo. Lo reconciliamos:

- **Datos** quiere extraer/parsear la base en Fase 1. **Proceso** quiere documentar primero. **Métricas** exige etapas estandarizadas antes de medir.
- **Ruta crítica acordada:** (1) **Spike de factibilidad** (apaga supuestos) → (2) **liberar a Lili** vía temp que descarga su operación → (3) **estandarizar etapas + extraer rúbrica/golden set** (proceso y métricas en paralelo, manualmente) → (4) **baseline honesta** (solo extremos confiables: time-to-submit, time-to-fill; intermedios con caveat por etapas inconsistentes) → (5) **extracción/enriquecimiento de datos** sobre cimiento limpio → (6) **IA asistida con HITL** sobre proceso ya estandarizado.
- Esto **rompe la dependencia circular** (A6): el conocimiento de Virginia se documenta *manualmente* primero; la IA viene después, no antes.

---

## 9. Supuestos a validar ⚠️ (consolidado)

| Supuesto | Por qué importa | Cómo confirmarlo |
|----------|-----------------|------------------|
| País de operación y residencia de datos | Define todo el marco legal y la viabilidad del benchmark | Correo a Virginia (HOY) |
| API/export/tier de Team Tailor | Sostiene extracción, baseline, dedup | Spike técnico |
| Existencia de golden set recuperable | Calibración y auditoría del Screener | Revisión con Virginia |
| Origen y consentimiento de los 4.000 | Base legal para cualquier uso secundario | Auditoría de origen |
| Exposición a la UE (candidatos/clientes) | Activa GDPR Art. 22 + AI Act | Confirmar con Virginia |
| Qué consentimiento presenta hoy TT al aplicar | Determina usos secundarios válidos | Revisar config de TT |
| Contratos con clientes permiten reutilizar comp-data | Viabilidad legal del benchmark | Revisión de NDAs |
| Costo total del programa vs. capacidad de pago del cliente | Asequibilidad para una PYME (techo mental ~US$2.7k ⚠️) | Modelo de economía unitaria |
| Capacidad de entrega de la consultora (legal/ASR subcontratados) | Viabilidad de cumplir el estándar prometido | Plan de staffing |

---

*Documento de gobierno. La postura de cumplimiento aquí descrita es vinculante para el diseño de las fases: ninguna iniciativa de automatización o monetización avanza sin cerrar las precondiciones legales y de consentimiento que le corresponden.*
