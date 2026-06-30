# Puntos de Dolor Priorizados
### Proyecto Conexión Talento — Memoria de Fase de Descubrimiento
*Documento de decisión · Síntesis de 8 análisis expertos, contrastados con una crítica que buscó los puntos débiles*

> **En una frase:** El problema central no es la falta de datos ni de tecnología, sino la falta de orden: un proceso que cada persona ejecuta a su manera y una base de candidatos sin estructura. Hasta resolver eso, automatizar con IA solo acelera el desorden.

---

## 1. Propósito y método

Este documento ordena los problemas de Conexión Talento por gravedad, para decidir **qué resolver primero**, en qué secuencia, y dónde está el valor para el negocio. No es una lista plana: ordena por **severidad** (daño real + cada cuánto ocurre + si se puede revertir + si bloquea todo lo demás) y clasifica cada problema como **operativo, de datos, reputacional o estratégico**.

Aplicamos dos disciplinas sobre el análisis inicial:

- **Cruzar fuentes, no repetir.** Donde varios análisis señalaron el mismo síntoma, lo consolidamos en un solo problema con su causa de fondo compartida. Marcamos las cadenas (por ejemplo: presentar dos veces al mismo candidato, las mentiras sobre haber participado antes y la falta de historial son **un mismo problema de datos visto desde tres ángulos**).
- **Honestidad sobre lo que aún no sabemos.** Todo dato no confirmado por el cliente se marca **⚠️ a validar**. No inventamos cifras. Donde un número depende de un dato pendiente (el honorario por colocación, qué parte de la base sigue vigente, cuánto tiempo dedica Lili), lo decimos.

> **Nota de encuadre importante:** corregimos dos afirmaciones del cliente. (a) *"No tenemos métricas"* es **falso**: el registro de actividad de Team Tailor (el sistema donde guardan los candidatos) ya tiene el histórico; lo que falta es **leerlo**, no los datos. (b) *"La base de 4000 candidatos es oro"* es **prematuro**: hoy es un activo que no se puede usar tal cual, sin depurar, y parte puede ser un riesgo legal. Ambas correcciones cambian el orden de prioridades.

---

## 2. Escala de severidad

| Nivel | Criterio |
|---|---|
| 🔴 **Crítico** | Daño activo o ya ocurrido, golpea ingresos o reputación de forma directa, o es **la causa de fondo / el único punto que, si falla, frena todo el programa**. |
| 🟠 **Alto** | Pérdida de valor importante y repetida; bloquea algo clave; riesgo legal latente con exposición real. |
| 🟡 **Medio** | Riesgo latente u oportunidad perdida; se puede gestionar en fases posteriores sin gran costo por esperar. |

---

## 3. Tabla maestra priorizada (por severidad)

| # | Punto de dolor | Tipo | Severidad |
|---|---|---|---|
| **D1** | El mismo candidato presentado dos veces al mismo cliente | Reputacional | 🔴 Crítico |
| **D2** | Cada quien trabaja distinto (4 personas, 4 criterios; sin una hoja de criterios al recibir la vacante) | Operativo | 🔴 Crítico |
| **D3** | Mala experiencia del candidato / ataques en LinkedIn, justo lo contrario del diferenciador "cercanía" | Reputacional · Estratégico | 🔴 Crítico |
| **D4** | Conocimiento clave solo en la cabeza de las personas + sobrecarga y riesgo de fuga de Lili (puntos únicos de falla) | Operativo · Estratégico | 🔴 Crítico |
| **D5** | Base de 4000 candidatos sin estructura, sin un vocabulario común de habilidades ni control de vigencia | Datos | 🟠 Alto |
| **D6** | No se miden los indicadores (el punto de partida existe, pero no se explota) | Datos | 🟠 Alto |
| **D7** | Sin historial ni memoria de qué candidato se presentó a qué cliente (raíz compartida de D1 y D10) | Datos | 🟠 Alto |
| **D8** | Demasiado trabajo manual + Team Tailor desaprovechado | Operativo | 🟠 Alto |
| **D9** | Datos personales de candidatos pegados en ChatGPT común (brecha activa) | Datos · Legal | 🟠 Alto |
| **D10** | Candidatos mienten sobre haber participado antes | Reputacional | 🟡 Medio |
| **D11** | Intención de vender un comparativo de salarios (bandera legal) | Estratégico | 🟡 Medio |
| **D12** | Tentación de abandonar Team Tailor por impulso | Estratégico | 🟡 Medio |
| **D13** | Concentración de ingresos: reclutamiento = 63% del negocio | Estratégico | 🟡 Medio |
| **D14** | Resistencia al cambio por identidad profesional (miedo a perder el oficio) | Estratégico · Cambio | 🟡 Medio |

---

## 4. Detalle por tipo de dolor

### 4.1 Dolor operativo

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D2 · Cada quien trabaja distinto** 🔴 | Un proceso de 8 pasos ejecutado de 4 formas por 4 reclutadores. No hay plantilla para recibir la vacante ni hoja de criterios para evaluar candidatos (qué es obligatorio, qué es deseable, con qué peso). El cuello de botella real está al **recibir la vacante (pasos 1–2)**, no al filtrar candidatos. | La calidad de la terna depende del "ojo clínico" de Virginia: **no crece ni queda documentado**. Resultados desiguales; imposible aplicar un mismo criterio. *(Cualitativo; se podrá cuantificar contra el punto de partida una vez que se midan los indicadores.)* | Continua (cada vacante) | Falta de un procedimiento escrito y de criterios explícitos; el criterio vive en la cabeza, sin escribirse. | Automatizar sobre esto **multiplica la inconsistencia a velocidad de máquina**; el diferenciador no se replica; no hay base medible para mejorar. Es la causa de fondo de D6 y de que cualquier IA futura trabaje a ciegas. |
| **D4 · Dependencia de personas clave + Lili** 🔴 | Cero documentación. El criterio vive en la cabeza de Virginia (ojo clínico, su instrucción para estandarizar CVs); la operación, en Lili (7am–7pm). | Puntos únicos de falla: si una persona falta, se cae el proceso. La firma no crece ni deja capacidad instalada. **Lili tiene alto riesgo de irse**: su salida se llevaría operación, memoria y la persona que impulsa la adopción, todo a la vez. | Estructural / continua | Conocimiento solo en la cabeza, sin documentar; la capacidad se resuelve contratando gente en vez de ordenar el proceso. | **Colapso operativo si Lili renuncia** antes de extraer su conocimiento. Todo el proyecto depende de su tiempo, que hoy no existe (riesgo de estancamiento). |
| **D8 · Trabajo manual + Team Tailor desaprovechado** 🟠 | Filtrado manual de ~200 CVs por vacante. Funciones de IA y automatizaciones que **ya se pagan** en Team Tailor no se usan. | Se gasta capacidad en tareas repetibles. ~5 días hasta entregar la terna ⚠️ *(la cifra mezcla el tiempo hasta entregar la terna con el tiempo hasta cubrir la vacante; hay que separarlos)*. El filtrado consume ≈ 25–30% del tiempo de Lili ⚠️ *(a validar midiendo su tiempo durante 2 semanas)*. | Por vacante / continua | Proceso no digitalizado; se desconocen las funciones que ya están contratadas. | Sobrecarga permanente; se contrata gente para tapar el síntoma (la "1 persona más"); se paga software que no se aprovecha. |

### 4.2 Dolor de datos

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D5 · Base de 4000 sin estructura** 🟠 | 4000 candidatos sin un vocabulario común de habilidades, sin etiquetas, sin control de vigencia; no se puede buscar por habilidad; nadie sabe cuántos siguen vigentes. **No es "big data"**: cabe en una sola tabla; el problema es el orden, no el volumen. | Activo que no se puede usar tal cual. El "~60% del valor" es **potencial sin realizar** ⚠️ (a validar). Probablemente **30–50% ya no está vigente** ⚠️ (supuesto a medir con una auditoría). | Continua (cada búsqueda que no reutiliza la base = empezar a buscar candidatos desde cero) | Sin un modelo de datos único, sin vocabulario común de habilidades ni control de qué tan actualizada está la base. | Se sigue pagando búsqueda nueva; aplicar IA sobre una base sucia produce **basura con tono de autoridad**; la velocidad y el % de vacantes cubiertas con la propia base que se prometen no se materializan. |
| **D6 · No se miden los indicadores** 🟠 | El cliente declara "cero métricas". **Corrección:** el punto de partida histórico YA existe en el registro de actividad de Team Tailor (fechas y horas, etapas). Lo que falta es **leerlo**. Advertencia: las etapas se usaron de forma inconsistente, así que los tiempos intermedios no son fiables (solo los extremos —apertura y cierre— son confiables). | Imposible probar el retorno de la inversión, defender un precio premium ni fijar metas; se decide por intuición. | Continua | Etapas no estandarizadas (ver D2) + nadie explota el sistema; sin un árbol de indicadores. | Toda promesa de mejora ("mismo día") es **fe, no retorno demostrado**. El propio proyecto carece de vara para medir su éxito; metas sin un punto de partida real. |
| **D7 · Sin historial candidato–cliente** 🟠 | No existe una línea de tiempo que registre candidato–proceso–cliente. Es la **causa de fondo compartida de D1 (presentar dos veces) y D10 (mentiras)**. | Riesgo reputacional repetido; imposible verificar si un candidato ya participó antes; bloquea el "mercado interno" y el historial. | Continua | Sin un sistema que identifique a la misma persona entre registros ni un registro de a quién se ha presentado. **No es problema de IA**: es una verificación automática y exacta (una conexión técnica entre sistemas o una consulta a la base). | Se repiten los duplicados, las mentiras no se detectan, y la relación con el candidato no se reutiliza como activo. |
| **D9 · Datos personales en ChatGPT común** 🟠 | La instrucción para estandarizar CVs probablemente pega los datos personales completos de candidatos en el ChatGPT personal ⚠️ (a confirmar): salida de los datos al extranjero y posible uso para entrenar el modelo. | **Brecha de privacidad activa HOY**, no un riesgo futuro. Exposición legal según el país ⚠️ (por confirmar). | Cada uso de la instrucción (recurrente) | Sin un entorno con acuerdo de protección de datos (el proveedor no usa ni entrena con los datos); sin política de uso de IA. | Sanción legal + daño reputacional; **mancha la credibilidad del primer proyecto** si se escala la IA sin cerrar esto. El costo de cerrarlo es casi nulo. |

### 4.3 Dolor reputacional

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D1 · Mismo candidato dos veces al mismo cliente** 🔴 | Se presentó el mismo candidato dos veces al mismo cliente, sin alerta ni registro. La CEO lo vivió "con vergüenza". | Riesgo directo sobre la cuenta y los honorarios; posible **disputa sobre quién "es dueño" del candidato**. Honorario en riesgo: ⚠️ no se puede cuantificar hasta conocer el honorario por colocación (reclutamiento = 63% de los ingresos). | Ya ocurrió ≥1 vez (conocido); alta probabilidad de repetirse sin control | Falta de un registro de quién presentó a quién y de historial (ver **D7**). | Pérdida de cuenta(s), reclamos de honorarios y desgaste de marca ante los clientes que pagan la mayoría de los ingresos. |
| **D3 · Experiencia del candidato / LinkedIn** 🔴 | El único contacto sistemático con el rechazado es un correo automático a los 15 días. La falta de seguimiento genera **ataques públicos en LinkedIn**. Contradice el diferenciador que declaran: "cercanía al candidato". | El eslogan que quieren **vender** es hoy su mayor pasivo. Daña la marca como empleadora, la atracción de candidatos y lo que justifica el precio premium. | Continua / recurrente | Sin un compromiso de tiempo de respuesta para comunicar ni plantillas; proceso centrado en el cliente, no en el candidato. | Desgaste del diferenciador estratégico central; pérdida de candidatos y reputación. **Encuestar antes de arreglar la comunicación provocaría más reacción negativa** ("me ignoraron y ahora me preguntan cómo me sentí"). |
| **D10 · Mentiras sobre participación previa** 🟡 | Candidatos declaran en falso no haber participado antes en un proceso o con un cliente. | Se decide sobre información falsa; bochorno ante el cliente. | Recurrente | Misma raíz que **D7** (sin historial verificable). | Persiste mientras no exista D7; con el historial se resuelve con una simple consulta. |

### 4.4 Dolor estratégico

| Dolor | Descripción | Impacto en negocio | Frecuencia | Causa raíz | Consecuencia si no se atiende |
|---|---|---|---|---|---|
| **D11 · Vender un comparativo de salarios** 🟡 | Intención de monetizar un comparativo salarial con datos de candidatos y de negociaciones con clientes. | Oportunidad real de ingreso, **pero bandera legal alta**: derecho de competencia, protección de datos, **posibilidad de volver a identificar a personas en un mercado pequeño** (un dato agregado no es lo mismo que anónimo), posible incumplimiento de acuerdos de confidencialidad con clientes. | Latente (aún no lanzado) | Querer monetizar sin base legal, sin anonimización irreversible (que no se pueda volver a identificar a la persona, con un mínimo de personas por cada celda del comparativo) ni consentimiento; el origen de los 4000 ⚠️ no está rastreado (¿se extrajeron de LinkedIn?). | Lanzarlo en crudo = **pleito con los clientes que pagan el 63%**, sanción y daño reputacional. Acción: **congelar** la venta; explorar la vía de un proveedor con licencia o un producto futuro con consentimiento explícito. |
| **D12 · Salir de Team Tailor por impulso** 🟡 | Virginia se declara dispuesta a abandonar Team Tailor. | Migrar 4000 registros sin ordenarlos primero **replicaría el desorden en un sistema más caro**; rompería las integraciones (LinkedIn, pruebas psicométricas) y convertiría a la pyme en responsable directa de custodiar datos personales y de cualquier brecha. | Latente (decisión pendiente) | Frustración por no aprovechar el sistema, confundida con una limitación del producto. | Riesgo sobre la operación que genera el 63%. **No migrar**: primero extraer la información (vía conexión técnica entre sistemas) y exprimir lo ya pagado (incluida la IA del sistema que no usan). |
| **D13 · Concentración en reclutamiento (63%)** 🟡 | Reclutamiento = 63% de los ingresos; ⚠️ posible concentración en pocos clientes (a validar); el otro 37% no se evaluó. | Riesgo de negocio: un incidente reputacional (D1/D3) golpea el **corazón de los ingresos**. | Estructural | Modelo de negocio; dependencia de pocos clientes que pesan mucho. | Vulnerabilidad ante la pérdida de una cuenta ancla; **amplifica la gravedad de todos los dolores reputacionales**. |
| **D14 · Resistencia al cambio (identidad)** 🟡 | Leer CVs y el "ojo clínico" **son el oficio** que da estatus e ingresos. La IA se percibe como una pérdida de ese oficio. Pedir "1 persona más" es la forma elegante de no tocarlo. | Riesgo de adopción: sin diseñar juntos el cambio y sin reencuadrarlo ("la IA potencia tu criterio"; rol de embajadora de marca), el proyecto se queda estancado en piloto. | Latente / estructural | El cambio se percibe como amenaza al estatus y a los ingresos ⚠️ (estructura de incentivos a confirmar); quien impulsa el proyecto (Virginia) es también la artesana en jefe. | Boicot pasivo; la inversión en IA se desperdicia; la capacidad no queda instalada y la dependencia regresa al irse los consultores. |

---

## 5. Interdependencias — la cadena crítica

Los dolores **no son independientes**; tres causas comunes explican la mayoría:

```
D2 (cada quien trabaja distinto) ──► D6 (sin métricas comparables) ──► no hay retorno demostrable
        │
        └──► D8 (manual) ──► sobrecarga de Lili ──► D4 (fuga / punto único de falla)

D7 (sin historial) ──► D1 (presentar dos veces)  y  D10 (mentiras)   [mismo defecto, tres síntomas]

D5 (base sin estructura) ──► requisito previo de cualquier IA y de la velocidad prometida
```

**Tensión de secuencia a resolver (señalada por la crítica que buscó los puntos débiles):** los análisis difieren en qué va primero —datos quiere extraer y ordenar la información, proceso quiere documentar, métricas exige estandarizar las etapas—. La ruta crítica reconciliada es: **estandarizar etapas y la recepción de la vacante (D2) → empezar a leer los datos del sistema (D6) → resolver el historial con una verificación automática y exacta (D7) → recién entonces estructurar la base (D5) y, sobre todo eso, IA**. "Listo para IA" significa proceso documentado, medido y con criterios explícitos, no "tenemos un buen modelo".

---

## 6. Supuestos y precondiciones que bloquean ⚠️

Esto no son "preguntas abiertas": son **condiciones previas que determinan la gravedad y el tamaño de la solución**. Deben cerrarse —idealmente con una prueba rápida de factibilidad, pagada, de 1 semana— antes de comprometer alcance o precio.

| Supuesto / condición previa | Por qué bloquea | Estado |
|---|---|---|
| **País de operación** | Define la ley de datos aplicable, la viabilidad del comparativo de salarios (D11) y la exposición de D9. Es un correo de 5 minutos a Virginia. | ⚠️ Pendiente — cerrar HOY |
| **Conexión técnica, extracción y plan real contratado de Team Tailor** | D5, D6, D7 y D8 dependen de esto. Varios "logros rápidos" se prometen sobre una capacidad **no verificada**. | ⚠️ Pendiente — no prometer prioridad máxima hasta confirmar |
| **Existencia de un set de decisiones de referencia** (poder recuperar el historial de quién entró a la terna y quién no — los casos que enseñan a la IA a elegir como Virginia) | Sin él, calibrar el asistente que ordena candidatos exige que Virginia vuelva a etiquetar casos a mano (la persona más escasa y más resistente) — una dependencia circular. | ⚠️ Probablemente no existe |
| **Honorario por colocación y volumen (vacantes/mes, colocaciones/año)** | Sin esto, el impacto de D1/D8 no se cuantifica y no hay caso de retorno defendible. *(Nota: con 20–60 colocaciones/año ⚠️, las encuestas de satisfacción y las auditorías de sesgo tendrán muy pocos casos para ser fiables.)* | ⚠️ Pendiente |
| **Vigencia y origen/consentimiento de los 4000** | Determina si D5 es un activo o un pasivo, y si D11 es siquiera legal. | ⚠️ Pendiente — auditar una muestra |
| **Identidad de "Víctor"** | Hay un reclutador "Víctor" entre los 4 del cliente y el consultor líder se llama Víctor: aclarar si es homónimo (afecta a quién decide qué y a posibles conflictos de rol). | ⚠️ Pendiente |

---

## 7. Riesgo emergente de diseño (no es un dolor actual, pero lo agravaría)

La salvaguarda que propone el cliente —**rechazar automáticamente a quien quede en el puesto 30 o más** de la lista ordenada— convertiría a D3 de un dolor en un **pasivo legal sistémico**: rechazar sin que una persona lo revise, en una empresa ya atacada en LinkedIn, con un sesgo que nadie puede auditar. **Recomendación:** todo rechazo debe pasar **siempre con una persona validando**, lo que además protege el diferenciador de "cercanía". Lo dejamos documentado aquí para que no se diseñe como mejora algo que sería un agravante.

---

*La severidad y los números se afinarán contra el punto de partida una vez que se empiece a medir (D6) y se confirmen las condiciones previas de la Sección 6. Los ítems marcados ⚠️ son supuestos explícitos, no hechos confirmados por el cliente.*
