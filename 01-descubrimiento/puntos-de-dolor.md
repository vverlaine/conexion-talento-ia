# Puntos de Dolor Priorizados
### Proyecto Conexión Talento — Memoria de Fase de Descubrimiento
*Documento de decisión · Síntesis de 8 lentes expertas reconciliadas con la crítica adversarial*

---

## 1. Propósito y método

Este documento prioriza los puntos de dolor de Conexión Talento para anclar el alcance, la secuencia y el caso de valor del compromiso. La priorización **no** es un inventario plano: ordena por **severidad** (daño real + frecuencia + reversibilidad + si bloquea todo lo demás) y clasifica cada dolor como **operativo, de datos, reputacional o estratégico**.

Dos disciplinas se aplicaron sobre el análisis crudo:
- **Triangulación, no eco.** Donde varias lentes señalaron el mismo síntoma, consolidamos en un solo dolor con su causa raíz compartida y marcamos las cadenas (p. ej., el reenvío de candidato, las mentiras de participación previa y la falta de historial son **un mismo problema de datos visto desde tres ángulos**).
- **Honestidad sobre los supuestos.** Todo dato no confirmado por el cliente se marca **⚠️ a validar**. No inventamos cifras del cliente; donde la cuantificación depende de un dato pendiente (fee por colocación, vigencia de la base, % de tiempo de Lili), lo decimos.

> **Nota de encuadre crítica:** dos afirmaciones del cliente se corrigen en este documento. (a) *"Cero métricas"* es **falso a nivel de datos**: el event log de Team Tailor ya registra el histórico; la carencia es de **lectura**, no de datos. (b) *"La base de 4000 es oro"* es **prematuro**: hoy es un activo ilíquido sin refinar, y parte puede ser pasivo legal. Ambas correcciones cambian el orden de severidad.

---

## 2. Escala de severidad

| Nivel | Criterio |
|---|---|
| 🔴 **Crítico** | Daño activo o ya materializado, golpea ingresos/reputación de forma directa, o es **causa raíz / punto único de falla** que bloquea el resto del programa. |
| 🟠 **Alto** | Pérdida de valor significativa y recurrente; habilitador clave bloqueado; riesgo legal latente con exposición real. |
| 🟡 **Medio** | Riesgo latente o pérdida de oportunidad; gestionable en fases posteriores con bajo costo de espera. |

---

## 3. Tabla maestra priorizada (por severidad)

| # | Punto de dolor | Tipo | Severidad |
|---|---|---|---|
| **D1** | Mismo candidato presentado dos veces al mismo cliente | Reputacional | 🔴 Crítico |
| **D2** | Cero estandarización del proceso (4 personas, 4 criterios; intake sin scorecard) | Operativo | 🔴 Crítico |
| **D3** | Experiencia de candidato pobre / ataques en LinkedIn vs. diferenciador "cercanía" | Reputacional · Estratégico | 🔴 Crítico |
| **D4** | Conocimiento tácito sin documentar + sobrecarga/fuga de Lili (puntos únicos de falla) | Operativo · Estratégico | 🔴 Crítico |
| **D5** | Base de 4000 candidatos sin estructura, taxonomía ni vigencia | Datos | 🟠 Alto |
| **D6** | Ausencia de instrumentación/lectura de métricas (la baseline existe, no se explota) | Datos | 🟠 Alto |
| **D7** | Sin historial/memoria candidato–cliente (raíz compartida de D1 y D10) | Datos | 🟠 Alto |
| **D8** | Trabajo manual excesivo + ATS (Team Tailor) subutilizado | Operativo | 🟠 Alto |
| **D9** | PII de candidatos inyectada en ChatGPT de consumo (brecha activa) | Datos · Legal | 🟠 Alto |
| **D10** | Candidatos mienten sobre participación previa | Reputacional | 🟡 Medio |
| **D11** | Intención de vender un benchmark de compensaciones (bandera legal) | Estratégico | 🟡 Medio |
| **D12** | Tentación de abandonar el ATS por impulso | Estratégico | 🟡 Medio |
| **D13** | Concentración: R&S = 63% de ingresos | Estratégico | 🟡 Medio |
| **D14** | Resistencia al cambio por identidad profesional (deskilling) | Estratégico · Cambio | 🟡 Medio |

---

## 4. Detalle por tipo de dolor

### 4.1 Dolor operativo

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D2 · Cero estandarización** 🔴 | Un proceso de 8 pasos ejecutado de 4 formas por 4 reclutadores. No hay plantilla de intake ni scorecard (must-have / nice-to-have, pesos). El cuello de botella real es el **intake (pasos 1–2)**, no el cribado. | La calidad de la terna depende del "ojo clínico" de Virginia: **no escala ni se documenta**. Matches inconsistentes; imposible aplicar criterio uniforme. *(Cualitativo; cuantificable contra baseline una vez instrumentada.)* | Continua (cada vacante) | Falta de SOP y de rúbrica explícita; criterio tácito. | Automatizar sobre esto **escala la inconsistencia a velocidad de máquina**; el diferenciador no se replica; no hay base medible para mejorar. Es la causa raíz de D6 y de la baja señal de cualquier IA futura. |
| **D4 · Dependencia de personas clave + Lili** 🔴 | Cero documentación. El criterio vive en la cabeza de Virginia (ojo clínico, prompt de CV); la operación, en Lili (7am–7pm). | Puntos únicos de falla. La firma no escala ni deja capacidad instalada. **Lili es flight-risk**: su salida se llevaría operación, memoria y sponsor de adopción a la vez. | Estructural / continua | Conocimiento tácito no documentado; capacidad resuelta con headcount en vez de proceso. | **Colapso operativo si Lili renuncia** antes de extraer su conocimiento. El proyecto entero depende de su tiempo, que hoy no existe (riesgo de estancamiento). |
| **D8 · Trabajo manual + ATS subutilizado** 🟠 | Cribado manual de ~200 CVs por vacante. Funciones de IA y automatizaciones que **ya se pagan** en Team Tailor no se usan. | Capacidad consumida en tareas repetibles. ~5 días a terna ⚠️ *(la cifra mezcla time-to-submit con time-to-fill; a separar)*. Cribado ≈ 25–30% del tiempo de Lili ⚠️ *(a validar con time-tracking de 2 semanas)*. | Por vacante / continua | Proceso no digitalizado; desconocimiento de las funciones contratadas. | Sobrecarga persistente; se contrata headcount para tapar el síntoma (la "1 persona más"); se paga por software no aprovechado. |

### 4.2 Dolor de datos

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D5 · Base de 4000 sin estructura** 🟠 | 4000 candidatos sin taxonomía de skills, sin etiquetas, sin protocolo de vigencia; no buscable por skill; nadie sabe cuántos vigentes. **No es "big data"**: cabe en una tabla; el problema es estructura, no volumen. | Activo ilíquido. El "~60% del valor" es **potencial no realizado** ⚠️ (a validar). Probable **30–50% no vigente** ⚠️ (supuesto a medir con auditoría). | Continua (cada búsqueda que no reutiliza la base = sourcing desde cero) | Sin modelo de datos canónico, taxonomía ni gobernanza de frescura. | Se sigue pagando sourcing nuevo; aplicar IA/RAG sobre base sucia produce **basura con tono de autoridad**; la velocidad e internal-fill prometidos no se materializan. |
| **D6 · Sin instrumentación de métricas** 🟠 | El cliente declara "cero métricas". **Corrección:** la baseline histórica YA existe en el event log de Team Tailor (timestamps, etapas). La carencia es de **lectura**. Caveat: etapas usadas inconsistentemente contaminan tiempos intermedios (solo extremos —apertura/cierre— son confiables). | Imposible probar ROI, defender precio premium ni fijar metas; se decide por intuición. | Continua | Etapas no estandarizadas (ver D2) + nadie explota el ATS; sin árbol de KPIs. | Toda promesa de mejora ("mismo día") es **fe, no ROI**. El propio proyecto carece de vara de éxito; metas-fantasía sin ancla. |
| **D7 · Sin historial candidato–cliente** 🟠 | No existe línea de tiempo candidato–proceso–cliente. Es la **causa raíz compartida de D1 (reenvío) y D10 (mentiras)**. | Riesgo reputacional recurrente; imposible verificar participación previa; bloquea el "mercado interno" / historial. | Continua | Sin entity resolution ni log de presentaciones. **No es problema de IA**: es un check determinista (API/SQL). | Reincidencia de duplicados, mentiras no detectadas, y la relación con el candidato no se reutiliza como activo. |
| **D9 · PII en ChatGPT de consumo** 🟠 | El "prompt" de estandarización de CV probablemente inyecta PII completa de candidatos en ChatGPT personal ⚠️ (a confirmar): transferencia internacional y posible uso para entrenamiento. | **Brecha de privacidad activa HOY**, no riesgo futuro. Exposición regulatoria según país ⚠️ (por confirmar). | Cada uso del prompt (recurrente) | Sin entorno con DPA / no-entrenamiento; sin política de uso de IA. | Sanción regulatoria + daño reputacional; **mancha la credibilidad del primer proyecto** si se escala la IA sin cerrarla. Cierre de costo casi nulo. |

### 4.3 Dolor reputacional

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D1 · Mismo candidato dos veces al mismo cliente** 🔴 | Se presentó el mismo candidato dos veces al mismo cliente, sin alerta ni registro. La CEO lo vivió "con vergüenza". | Riesgo directo sobre la cuenta y los honorarios; posible **disputa de propiedad de candidato**. Honorario en riesgo: ⚠️ no cuantificable hasta conocer el fee por colocación (R&S = 63% de ingresos). | Materializado ≥1 vez (conocido); alta probabilidad de repetición sin control | Ausencia de *submission ownership* y de historial (ver **D7**). | Pérdida de cuenta(s), reclamos de honorarios y erosión de marca ante los clientes que pagan la mayoría de los ingresos. |
| **D3 · Candidate experience / LinkedIn** 🔴 | El único contacto sistemático con el rechazado es un correo automático a 15 días. La falta de seguimiento genera **ataques públicos en LinkedIn**. Contradice el diferenciador declarado: "cercanía al candidato". | El eslogan que quieren **vender** es hoy su mayor pasivo. Daña marca empleadora, atracción y el sustento del precio premium. | Continua / recurrente | Sin SLA de comunicación ni plantillas; proceso centrado en el cliente, no en el candidato. | Erosión del diferenciador estratégico central; pérdida de candidatos y reputación. **Encuestar antes de reparar el SLA provocaría más backlash** ("me ignoraron y ahora me preguntan cómo me sentí"). |
| **D10 · Mentiras de participación previa** 🟡 | Candidatos declaran falsamente no haber participado antes en un proceso/cliente. | Decisiones sobre información falsa; bochorno ante el cliente. | Recurrente | Misma raíz que **D7** (sin historial verificable). | Persiste mientras no exista D7; con el historial se resuelve con un simple *lookup*. |

### 4.4 Dolor estratégico

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D11 · Vender benchmark de compensaciones** 🟡 | Intención de monetizar un benchmark salarial con datos de candidatos y negociaciones con clientes. | Oportunidad real de ingreso, **pero bandera legal alta**: derecho de competencia/antitrust, protección de datos, **re-identificación en mercado pequeño** (agregado ≠ anónimo), posible violación de NDAs con clientes. | Latente (aún no lanzado) | Querer monetizar sin base legal, anonimización (k-anonimato, N mínimo por celda) ni consentimiento; origen de los 4000 ⚠️ no trazado (¿scraping de LinkedIn?). | Lanzarlo crudo = **litigio con los clientes que pagan el 63%**, sanción y daño reputacional. Acción: **congelar** la venta; explorar vía proveedor licenciado o producto futuro con consentimiento granular. |
| **D12 · Salir del ATS por impulso** 🟡 | Virginia se declara dispuesta a abandonar Team Tailor. | Migrar 4000 registros sin taxonomía **replicaría el desorden en un sistema más caro**; rompería integraciones (LinkedIn, psicométricas) y convertiría a la PYME en procesadora de PII responsable de seguridad y brechas. | Latente (decisión pendiente) | Frustración por subutilización confundida con limitación del producto. | Riesgo sobre la operación que genera el 63%. **No migrar**: primero extraer por API y exprimir lo ya pagado (incluida la IA del ATS que no usan). |
| **D13 · Concentración en R&S (63%)** 🟡 | R&S = 63% de ingresos; ⚠️ posible concentración en pocos clientes (a validar); el otro 37% no evaluado. | Riesgo de negocio: un incidente reputacional (D1/D3) golpea el **núcleo de ingresos**. | Estructural | Modelo de negocio; dependencia del Pareto. | Vulnerabilidad ante pérdida de cuenta ancla; **amplifica la severidad de todos los dolores reputacionales**. |
| **D14 · Resistencia al cambio (identidad)** 🟡 | Leer CVs y el "ojo clínico" **son el oficio** que da estatus e ingresos. La IA se percibe como *deskilling*. La petición de "1 persona más" es la forma elegante de no tocar el oficio. | Riesgo de adopción: sin co-diseño y reencuadre ("la IA potencia tu criterio"; rol de embajador de marca), el proyecto se estanca en piloto. | Latente / estructural | Cambio percibido como amenaza a estatus/ingresos ⚠️ (estructura de incentivos a confirmar); sponsor (Virginia) es también la artesana en jefe. | Sabotaje pasivo; inversión en IA desperdiciada; el activo no queda instalado y la dependencia regresa al irse los consultores. |

---

## 5. Interdependencias — la cadena crítica

Los dolores **no son independientes**; tres raíces comunes explican la mayoría:

```
D2 (sin estandarización) ──► D6 (sin métricas comparables) ──► no hay ROI demostrable
        │
        └──► D8 (manual) ──► sobrecarga de Lili ──► D4 (fuga / punto único de falla)

D7 (sin historial) ──► D1 (reenvío)  y  D10 (mentiras)   [mismo defecto, tres síntomas]

D5 (base sin estructura) ──► precondición de cualquier IA/RAG y de la velocidad prometida
```

**Tensión de secuencia a resolver (señalada por la crítica adversarial):** las lentes difieren en qué va primero —datos quiere extraer/parsear, proceso quiere documentar, métricas exige estandarizar etapas—. La ruta crítica reconciliada es: **estandarizar etapas e intake (D2) → instrumentar lectura del ATS (D6) → resolver historial determinista (D7) → recién entonces estructurar la base (D5) y, sobre todo eso, IA**. "Listo para IA" significa proceso documentado, medido y con criterios explícitos, no "tenemos un buen modelo".

---

## 6. Supuestos y precondiciones bloqueantes ⚠️

Estos no son "preguntas abiertas": son **precondiciones que gatean la severidad y el dimensionamiento**. Deben cerrarse —idealmente vía un *spike* de factibilidad pagado de 1 semana— antes de comprometer alcance o precio.

| Supuesto / precondición | Por qué bloquea | Estado |
|---|---|---|
| **País de operación** | Define ley de datos, viabilidad del benchmark (D11) y exposición de D9. Es un email de 5 minutos a Virginia. | ⚠️ Pendiente — cerrar HOY |
| **API / export / tier real de Team Tailor** | D5, D6, D7 y D8 cuelgan de esto. Varios "quick wins" se prometen sobre una capacidad **no verificada**. | ⚠️ Pendiente — no prometer P0 hasta confirmar |
| **Existencia de un golden set** (historial recuperable de quién entró a terna y quién no) | Sin él, calibrar cualquier ranker exige re-etiquetado manual de Virginia (la persona más escasa y resistente) — dependencia circular. | ⚠️ Probablemente inexistente |
| **Fee por colocación y volumen (vacantes/mes, colocaciones/año)** | Sin esto, el impacto de D1/D8 no se cuantifica y no hay caso de ROI defendible. *(Nota: con 20–60 colocaciones/año ⚠️, NPS y auditorías de sesgo tendrán n insuficiente.)* | ⚠️ Pendiente |
| **Vigencia y origen/consentimiento de los 4000** | Determina si D5 es activo o pasivo, y si D11 es siquiera legal. | ⚠️ Pendiente — auditoría de muestreo |
| **Identidad de "Víctor"** | Hay un reclutador "Víctor" entre los 4 del cliente y el consultor líder se llama Víctor: aclarar si es homónimo (afecta gobernanza/conflicto de rol). | ⚠️ Pendiente |

---

## 7. Riesgo emergente de diseño (no es un dolor actual, pero lo amplificaría)

El guardarraíl propuesto por el cliente de **auto-rechazo automático para rank 30+** convertiría a D3 de un dolor en un **pasivo legal sistémico**: rechazo sin revisión humana sobre una empresa ya atacada en LinkedIn, con sesgo no auditable. **Recomendación:** todo rechazo debe ser *human-in-the-loop*, lo que además protege el diferenciador de "cercanía". Se documenta aquí para que no se diseñe como mejora lo que sería un agravante.

---

*Severidad y cuantificación se refinarán contra la línea base una vez instrumentada (D6) y confirmadas las precondiciones de la Sección 6. Los ítems marcados ⚠️ son supuestos explícitos, no hechos del cliente.*
