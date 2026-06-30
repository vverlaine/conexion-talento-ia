# Diagnóstico de Situación Actual
### Conexión Talento — Proyecto "Conexión Talento IA" | Fase de Descubrimiento

---

> **En una frase:** El problema de Conexión Talento no es falta de tecnología ni de personal, es falta de un proceso ordenado y medible; automatizar el desorden con IA solo lo haría más rápido y dañaría justo lo que la hace premium.

---

## 0. Cómo leer este documento

Esto es un **diagnóstico**, no una propuesta. Sirve para fijar una verdad común y honesta sobre dónde está hoy Conexión Talento en cinco frentes: proceso, datos, tecnología, métricas y personas. También compara su proceso de reclutamiento de 8 pasos con cómo debería funcionar, y da un veredicto sobre el sistema Team Tailor.

Dos reglas guían todo el documento:

1. **Distinguimos lo que sabemos de lo que suponemos.** Todo dato que el cliente aún no ha confirmado lleva ⚠️ y se trata como *supuesto por validar*, no como hecho. Varios de esos supuestos son **bloqueantes**: condicionan el alcance, el riesgo legal y si el proyecto es viable. No los dejamos como "preguntas abiertas": los elevamos a **condiciones previas, cada una con un responsable**.
2. **Separamos el síntoma de la causa.** El cliente vive el problema como "me falta una persona" y la solución como "6 agentes de IA". El diagnóstico sostiene otra cosa y la respalda con evidencia.

---

## 1. Síntesis ejecutiva (lo esencial primero)

> **Tesis central:** Conexión Talento no tiene un problema de tecnología ni de capacidad; tiene un problema de **disciplina de proceso**. Corre un proceso de 8 pasos que cuatro personas ejecutan de cuatro maneras distintas, sin un estándar escrito, sin nada medido, y con un activo de datos (4.000 candidatos) que hoy es **potencial sin pulir, no "oro" listo para usar**. Automatizar este estado con IA no resolvería nada: **multiplicaría la inconsistencia a velocidad de máquina** y desgastaría justo el "ojo clínico" y la cercanía al candidato que hacen premium a la firma.

**Los cinco hechos que definen el punto de partida:**

| # | Hallazgo | Qué significa para el negocio |
|---|----------|-------------|
| 1 | El verdadero cuello de botella **no es revisar 200 CVs**, es el arranque del encargo (pasos 1–2): entender bien el puesto. Sin una hoja de criterios para evaluar candidatos (*scorecard*) acordada, los 4 reclutadores aplican 4 criterios distintos y la terna depende del juicio de Virginia, que no se puede multiplicar. | Si entra basura, sale basura: acelerar la revisión sin ordenar el origen produce malas coincidencias más rápido. |
| 2 | La promesa de marca —"cercanía al candidato"— **choca con la realidad operativa**: los critican en LinkedIn por no dar seguimiento; el único contacto sistemático con quien se rechaza es un correo automático a los 15 días. | El diferenciador que quieren *vender* es hoy su mayor **riesgo de reputación**. |
| 3 | "Cero métricas" es **parcialmente falso**. Team Tailor (el sistema donde guardan los candidatos) registra fechas y etapas. Existe un **punto de partida medido recuperable** ⚠️ (sujeto a verificar que se pueda extraer la información del sistema y a que las etapas se usaron de forma inconsistente). El problema es de **lectura**, no de que no exista. | El punto de partida es recuperable, pero **solo confiable en los extremos** (apertura → terna → cierre); los tiempos intermedios son ruido hasta ordenar las etapas. |
| 4 | Enviar el mismo candidato dos veces al mismo cliente **no es una anécdota**: es que nadie es dueño de qué se presentó ni hay historial. Es un fallo de control simple, no un problema de IA. | Daño de reputación **ya ocurrido**; se corrige con un registro simple, no con un modelo de IA. |
| 5 | La base de 4.000 candidatos **todavía no es "oro"**. No hay identificador único por persona, ni vocabulario común de habilidades, ni forma de saber quién sigue vigente. Estimación gruesa ⚠️: entre 30% y 50% podría estar desactualizado. El número honesto es "candidatos vigentes y contactables", probablemente **entre 1.500 y 2.500** ⚠️. | El "60% del valor" es potencial **condicionado** a una estructura de datos que aún no existe. |

**Madurez global:** Conexión Talento está en un **Nivel 1–2 de 5 ("Inicial / Reactivo")** en madurez digital. El conocimiento vive en la cabeza de las personas, los procesos son artesanales y los datos no están gobernados. Esto **no es una crítica**: es lo típico de una PYME consultora exitosa cuyo valor está en el criterio humano. El reto es industrializar la parte operativa (la "trastienda") sin convertir en commodity el oficio.

---

## 2. Supuestos bloqueantes (condiciones previas, no "preguntas abiertas")

Aquí la revisión crítica es contundente y la asumimos: **no se puede dimensionar ni prometer nada** mientras estos supuestos sigan abiertos. Cada uno tiene responsable y plazo.

| ID | Supuesto por validar ⚠️ | Por qué bloquea | Responsable / Cómo se cierra |
|----|----------------------|-----------------|------------------------|
| **B1** | **País exacto de operación** (y dónde residen candidatos y clientes). | Define qué ley de datos aplica (Ley 8968 Costa Rica + PRODHAB · Ley 81 Panamá + ANTAI · Ley 787 Nicaragua · *habeas data* Guatemala), si el comparativo salarial es viable, y la exposición a la normativa europea (GDPR / EU AI Act) si hay datos de la UE. | **Virginia — correo de 5 minutos. Cerrar HOY.** Es el dato más barato y más estructural del proyecto. |
| **B2** | **Acceso real a los datos de Team Tailor** (conexión técnica entre sistemas, capacidad de extraer la información y nivel de plan contratado). | Toda la estrategia de datos y el punto de partida histórico cuelgan de esto. Si el plan limita las consultas o no deja descargar la información, se cae medio diagnóstico cuantitativo. | Consultor — verificación técnica directa en la cuenta. **No prometer ninguna victoria rápida de datos hasta confirmarlo.** |
| **B3** | **Existencia de un set de decisiones de referencia** (los casos que enseñan a la IA a elegir como Virginia): el historial recuperable de quién entró a terna y quién no. | Sin él no se puede calibrar ni evaluar un asistente que ordene candidatos contra el criterio de Virginia. Con "cero documentación", **probablemente no existe**, y construirlo consume el recurso más escaso: el tiempo de Virginia. | Consultor + Virginia — auditoría del sistema. Tratarlo como **trabajo serio**, no como algo que ya está dado. |
| **B4** | **Origen y consentimiento de los 4.000** (¿aplicaron voluntariamente o se extrajeron de LinkedIn?). | Cambia por completo la base legal para reutilizar o monetizar esos datos y el porcentaje que sigue vigente. | Muestreo de vigencia + revisión de los términos de aplicación actuales. |
| **B5** | **Modelo de honorarios y volumen** (cobro por colocación, encargos por mes, colocaciones al año ⚠️ est. 20–60). | Define la economía del negocio, el retorno y la **validez estadística** de toda métrica de embudo (a este volumen, encuestas de satisfacción y auditorías de sesgo tienen demasiados pocos casos para ser fiables). | Virginia — primera pregunta de delimitación del proyecto. |

> **Regla de gobierno:** ninguna afirmación con cifras de este diagnóstico se da por "hecho" hasta cerrar B1–B5. Lo que sigue se construye sobre lo observable y marca explícitamente lo que es supuesto.

---

## 3. Diagnóstico de madurez por dimensión

Escala: **1 Inicial · 2 Reactivo · 3 Definido · 4 Gestionado · 5 Optimizado.**

| Dimensión | Nivel actual | Evidencia (cómo está hoy) | Mínimo deseable (Nivel 3) | Brecha clave |
|-----------|:---:|-------------|------------------------|--------------|
| **Procesos** | **1 → 2** | Un proceso de 8 pasos, ejecutado de 4 formas distintas. Cero documentación. Único activo semi-estándar: el "prompt" de CV de Virginia (sin control de versiones, vive en su cuenta personal). | Un instructivo por paso con responsable claro (quién hace qué en cada paso), compromisos de tiempo de respuesta, entradas y salidas, y una hoja de criterios para evaluar candidatos al arranque. El estándar como **propiedad de la firma**, no de las personas. | Aún no se sabe si las 4 formas difieren en el **criterio** (qué evalúan) o en el **formato** (cómo lo registran). **Resolverlo es requisito antes de delimitar el proyecto.** ⚠️ |
| **Datos** | **1** | 4.000 registros sin identificador único, sin vocabulario común de habilidades, sin etiquetas, sin forma de saber quién sigue vigente. Duplicados confirmados (el candidato reenviado). No saben cuántos siguen vigentes. | Un modelo de datos ordenado (Candidato / Aplicación / Vacante / Cliente / Habilidad / Evento), un identificador único por persona, una señal de vigencia y un vocabulario común de habilidades (base ESCO + ajuste local ⚠️ requiere trabajo real de curaduría). | Hoy el dato es un **pasivo legal y operativo**, no un activo. El "60% del valor" está sin materializar. |
| **Tecnología** | **2** | Team Tailor en uso real (integración con LinkedIn, pruebas psicométricas, rechazos automáticos). Funciones de IA **pagadas y sin usar**. ChatGPT de consumo manejando datos personales de candidatos (**fuga de datos activa**). | Aprovechar lo que ya se paga antes de construir nada. Una capa que coordine los pasos de forma controlada sobre la conexión técnica al sistema. Cortar el uso de datos personales en ChatGPT de consumo (pasar a Enterprise/API con compromiso de no entrenar con los datos + acuerdo de protección de datos: el proveedor no usa ni entrena con la información). | Es subutilización, no carencia. El problema es de **adopción y configuración**, no de falta de herramientas. |
| **Métricas** | **1** | "No hay métricas", según declaran. Sin indicadores de industria. Sin punto de partida medido. Sin seguimiento del plan a 90 días (que ya entregan y es, sin saberlo, su medida de calidad de la contratación). | Un árbol de unos 10 indicadores con una métrica guía (% de vacantes cubiertas dentro del tiempo comprometido + colocaciones por reclutador). Capturar datos de aquí en adelante y reconstruir el histórico con sus advertencias. | Los datos **existen** en el sistema pero nadie los lee. La brecha es de **medir y leer**, no de generar datos. |
| **Personas** | **2** | 4 reclutadores + 1 temporal. El conocimiento clave está concentrado en Virginia ("ojo clínico") y Lili (operación). Lili trabaja de 7am a 7pm: es punto único de falla **y riesgo real de que se vaya**, sin gestionar. | Nombrar a un dueño del proceso; extraer y documentar el conocimiento; crear un rol de "Embajador de Marca / Experiencia del Candidato" que convierta a la persona extra de simple relevo en capacidad nueva. | Dependencia crítica de 2 personas. Si Lili renuncia por agotamiento antes de extraer su conocimiento, se pierden de golpe la operación, la memoria y el principal apoyo interno al proyecto. |

**Lectura transversal:** la firma es fuerte donde está su valor (criterio humano, relación) y débil donde ese valor se industrializa (proceso, dato, medición). El proyecto debe **estandarizar sin piedad la trastienda** (revisión, etiquetado, formateo, registro) y **preservar el juicio humano** en terna, negociación y relación con el candidato. Estandarizar de más el diferenciador lo destruye.

---

## 4. Mapa del proceso de reclutamiento: "cómo es hoy" vs. "cómo debería ser"

> **Nota de método:** este mapa documenta el flujo tal como lo declaran. La diferencia **criterio vs. formato** en las 4 variantes (sobre todo el paso 4) **no está resuelta** y hay que levantarla acompañando una vacante real de principio a fin antes de diseñar el "deber ser" definitivo. Lo que sigue es el armazón, no el instructivo final.

| # | Paso | Cómo es hoy | Cómo debería ser | Responsable | Brecha / Riesgo |
|---|------|---------------------|-------------------|-------|-----------------|
| **1** | **Perfilamiento** | Tácito, depende del reclutador. No se captura el contexto de forma ordenada. | Reunión de arranque estructurada **con el cliente**: contexto, 3–5 competencias críticas, definición de éxito a 90 días. | Reclutador (consultivo) | **Cuello de botella real.** Sin esto, ningún paso posterior tiene criterio. |
| **2** | **Redacción del perfil de puesto** | Variable, no se ajusta de forma consistente al tamaño y contexto de la empresa. | Una sola plantilla ajustable. Separar lo imprescindible de lo deseable, con **pesos**. | Reclutador | Sin pesos explícitos, todo lo que viene después se vuelve subjetivo. |
| **3** | **Búsqueda de candidatos (sourcing)** | Manual; búsquedas + preguntas para descubrir el perfil real (artesanal, sin documentar). | Búsqueda estándar + usar la base interna como **primera fuente** (hoy no se mide el % de vacantes cubiertas con la propia base). | Reclutador | Único paso genuinamente "agéntico" (decisiones que se van encadenando). La base propia se aprovecha poco. |
| **4** | **Revisión de ~200 CVs** (puntuar → top 10 → terna) | **4 personas, 4 criterios.** La hoja de criterios vive tácita en el "ojo clínico" de Virginia. Es donde se consumen más horas. | Hoja de criterios explícita y con pesos + set de decisiones de referencia. Revisión asistida **siempre con una persona validando**. | Reclutador + dueño del estándar | **Pieza central de la estandarización.** Escribir esa hoja de criterios vale ~80% de toda esta fase. |
| **5** | **Entrevista telefónica previa** ("a veces grabada" → IA) | Sin banco de preguntas ligado a la hoja de criterios. Grabación inconsistente y **sin consentimiento documentado** ⚠️. | Entrevista **estructurada** (predice el desempeño ~2x mejor) con guion por competencia + consentimiento de grabación. | Reclutador | Sin estructura, transcribir con IA aporta **ruido, no señal**. Riesgo legal por grabar sin permiso. |
| **6** | **Terna** | Depende del juicio de Virginia; sin un filtro de calidad uniforme. | Terna = exactamente 3 finalistas validados contra la hoja de criterios. **Verificación anti-duplicado obligatoria**. | Virginia / reclutador | Oficio a preservar. Pero requiere una comprobación automática antes de enviar. |
| **7** | **Negociación / cierre con cliente** (plan de desarrollo a 90 días) | Se entrega como "valor"; **no se mide** ni se recupera el dato a los 90 días. | Dejar por contrato la **devolución del dato de retención/desempeño a los 90 días** = indicador de calidad de la contratación + gancho para vender más servicios. | Virginia | Oficio a preservar. Hoy están regalando la métrica más vendible de todas. |
| **8** | **Formateo de CV con la marca** | El "prompt" de Virginia en ChatGPT de consumo. **Único proceso semi-estándar**, sin control de versiones, con **datos personales en herramienta de consumo (fuga activa)**. | Plantilla fija (el diseño no lo decide la IA) + extracción de datos a un formato fijo. Con control de versiones y propiedad de la firma. Entorno con compromiso de no entrenar con los datos + acuerdo de protección de datos. | Dueño del estándar | **Candidato natural a la primera victoria rápida**: bajo esfuerzo, alta visibilidad. |

### 4.1 Los "6 agentes": reencuadre honesto

El cliente imagina 6 agentes de IA. El diagnóstico técnico es claro: **de los 6, solo 1 (el de búsqueda) es de verdad un agente.** Los otros 5 son cadenas de instrucciones / herramientas con salida ordenada y un enrutamiento automático fijo.

| "Agente" que imagina el cliente | Qué es en realidad | Veredicto |
|-----------------------------------|--------------------|------------------------|
| 1. Perfilador | Herramienta de plantillas + consulta a fuentes curadas | Requiere una biblioteca de competencias/salarios **verificable**; las cifras salariales **nunca** las inventa la IA. |
| 2. Redactor | Plantilla con IA que normaliza el texto | Depende del instructivo del paso 2. |
| 3. Buscador (Sourcer) | **Único agente de verdad** (búsqueda que se encadena) | Aspiracional; depende de tener la base estructurada. |
| 4. Asistente que ordena candidatos (Screener/Ranker) | Puntúa contra la hoja de criterios y ordena | El de **mayor palanca**, pero exige el set de decisiones de referencia y quitar los datos personales antes de procesar. La persona valida el top 10. |
| 5. Entrevistador previo | Transcripción automática (comprar) + resumen ordenado | Requiere consentimiento + entrevista estructurada previa. |
| 6. Generador de CV | Extracción a formato fijo + plantilla fija | **Victoria rápida** de menor riesgo. |

> **Conclusión:** no se construyen 6 agentes en paralelo. Se construyen **3 herramientas fiables y controladas** (CV, quitar duplicados, revisión asistida) siempre con una persona validando, **sobre un proceso ya estandarizado**, y se reserva la autonomía de un agente solo donde aporta. El guardarraíl que pide el cliente —"la IA no opina fuera de su alcance"— es correcto y debe quedar **escrito en el código** (la salida forzada a un formato fijo), no como una mera instrucción de texto.

### 4.2 Corrección crítica al guardarraíl de auto-rechazo

El guardarraíl que propone el cliente —candidato en posición 30 o más = **rechazo cordial automático**— es el **mayor riesgo legal y de reputación del diseño**. En una empresa a la que **ya critican en LinkedIn** por falta de seguimiento, dejar que la IA rechace sin aprobación humana agranda el problema y constituye una **decisión automatizada** (con exposición europea es exigible que intervenga una persona; hay perfilado de por medio). **Recomendación firme: el rechazo debe pasar siempre por una persona** —o como mínimo, revisar el lote antes de enviar—. Además de cumplir la ley, esto **protege el diferenciador de cercanía**.

---

## 5. Evaluación de Team Tailor

### 5.1 Qué hace bien (y ya se paga)

- **Integración con LinkedIn** (enlace de aplicación) funcionando.
- **Envío automático de pruebas psicométricas** funcionando.
- **Correos automáticos de rechazo** (a los 15 días) — funcionan, aunque su momento y tono son parte del problema de experiencia.
- **Registro silencioso de eventos** (fechas, movimientos de etapa) sobre ~4.000 candidatos → **un punto de partida histórico latente**.
- **Acuerdo de protección de datos y funciones de cumplimiento ya integradas** como procesador de datos: importante, porque migrar a un sistema propio **le cargaría a una PYME de 10 personas** toda la responsabilidad de seguridad, aviso de brechas y atención de derechos de los titulares (acceso, rectificación, cancelación, oposición).
- **Funciones de IA incluidas** en el plan ⚠️ (alcance por confirmar) — **pagadas y sin usar**.

### 5.2 Qué no hace bien (o no se está usando)

- **Subutilización severa:** las funciones de IA pagadas no se usan; se hace trabajo manual a pesar de tener las herramientas.
- **Etapas usadas de forma inconsistente** (4 personas) → ensucia los tiempos intermedios del embudo.
- **Sin campos ni etiquetas estructuradas** que hagan la base buscable por habilidad.
- **Sin aprovechar la verificación anti-duplicado** → permitió reenviar el mismo candidato.

### 5.3 Decisión: ¿potenciar o reemplazar?

> **Veredicto: POTENCIAR. No migrar — todavía y probablemente no.** El deseo de Virginia de dejar el sistema es comprensible pero **resuelve el problema equivocado**: migrar 4.000 registros sin vocabulario común ni protocolo solo replicaría el desorden en un sistema nuevo y más caro, y pondría en riesgo la operación que genera el **63% de los ingresos**.

**Criterios de decisión (a evaluar con datos, no por impulso):**

| Criterio | Umbral que justificaría **potenciar** (opción por defecto) | Umbral que justificaría **reemplazar** |
|----------|------------------------------------------------|----------------------------------------|
| **Acceso a los datos** (B2) | Se puede conectar a otros sistemas y descargar toda la información en el plan actual → se extrae y enriquece **por fuera** sin migrar. | No se puede descargar masivamente / un límite de consultas tan bajo que impide explotar el dato. |
| **Funciones de IA pagadas** | Cubren coincidencia/revisión/transcripción con calidad aceptable → exprimirlas antes de construir. | No existen o no sirven para este caso. |
| **Costo total de propiedad** | Cuesta menos quedarse que construir + operar + asumir el cumplimiento legal. | Quedarse cuesta más, demostrado **con caso de negocio**. |
| **Riesgo de seguridad/cumplimiento** | Mantener el acuerdo de protección de datos y los controles de Team Tailor reduce la exposición de la PYME. | Solo si hay controles propios equivalentes. |
| **Volumen** ⚠️ (20–60 colocaciones/año) | A este volumen, **construir a medida probablemente da retorno negativo durante años**. Favorece comprar. | Solo si el volumen crece de forma material. |

> **Declaración de integridad (asumida de la revisión crítica):** existe un **conflicto de interés estructural** —nuestro ingreso crece cuanto más se construya a medida—. La recomendación honesta para el primer proyecto es **exprimir lo que Team Tailor ya cobra y comprar complementos antes de construir infraestructura propia**. Lo declaramos abiertamente. La decisión de potenciar vs. reemplazar se toma en una fase posterior, **con los datos de B2 y B5**, no en este diagnóstico.

---

## 6. Riesgos del estado actual (priorizados)

| Severidad | Riesgo | Naturaleza | Mitigación inmediata |
|:---:|--------|-----------|----------------------|
| 🔴 **Crítico** | **Fuga activa de datos personales**: CVs de candidatos en ChatGPT de consumo. | Legal / hoy | Cortar el uso; pasar a un entorno con compromiso de no entrenar con los datos + acuerdo de protección de datos. Costo casi nulo. |
| 🔴 **Crítico** | **Reenvío del mismo candidato al mismo cliente**, ya ocurrido. | Reputacional / operativo | Registro de presentaciones (candidato × cliente × fecha) + regla de no reenvío. Automático, cuestión de días. |
| 🔴 **Crítico** | **Riesgo de que Lili se vaya** (7am–7pm, punto único de falla, principal apoyo interno a la adopción). | Humano / continuidad | Aliviarla **antes** de pedirle documentar; extraer su conocimiento en las primeras 2–3 semanas; presentar a la temporal como **seguro anti-fuga**. |
| 🟠 **Alto** | **Comparativo salarial** que el cliente quiere vender ya. | Legal (competencia/datos) | **Congelar la venta.** Aun agregado, en un mercado pequeño se puede volver a identificar a personas y empresas; posible violación de acuerdos de confidencialidad. Camino positivo: alianza con un proveedor con licencia, o un producto futuro con consentimiento específico. |
| 🟠 **Alto** | **Daño de reputación en LinkedIn** por mala experiencia del candidato. | Reputacional | Compromiso de tiempo de respuesta en la comunicación + plantillas. **Arreglar ese compromiso antes de lanzar encuestas de satisfacción** (encuestar a candidatos ya molestos provoca más reacción negativa). |
| 🟠 **Alto** | **Sesgo del algoritmo** si se revisara sobre datos históricos con datos personales (foto, edad, estado civil, comunes en los CVs de la región). | Legal-laboral / ético | Quitar los datos personales antes de puntuar; auditar el impacto desigual antes de pasar a producción. |
| 🟡 **Medio** | **Sobrevaloración del activo de datos** (el supuesto del "60%"). | Estratégico | Auditar la vigencia **antes** de invertir en enriquecer. |
| 🟡 **Medio** | **Continuidad operativa**: el 63% de los ingresos debe seguir fluyendo durante la transformación. | Negocio | Guardarraíl: ninguna intervención toca un encargo en curso. |

---

## 7. Tensiones entre dimensiones y ruta crítica

La revisión crítica señaló, con razón, que las distintas perspectivas **se contradicen en el orden** y nadie las reconcilia. Lo hacemos aquí explícitamente:

- **Datos** quiere extraer y procesar en paralelo desde temprano.
- **Procesos** quiere documentar primero ("no automatizar el desorden").
- **Métricas** necesita etapas estandarizadas antes de medir el embudo.

**Reconciliación — una sola ruta crítica:**

```
B1 país (HOY) ─┐
B2 datos TT ───┼──► [Prueba rápida de factibilidad técnica + legal, 1 sem]
B3 set ref. ───┤        │
B4 consent. ───┘        ▼
                 Estandarizar etapas + hoja de criterios de arranque (proceso)
                        │
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
   Punto de         Victorias       Auditoría de
   partida          rápidas         vigencia de la
   (extremos)       controladas     base (radiografía
   con avisos       (duplicados,    real)
                    CV)
          └─────────────┼──────────────┘
                        ▼
        Solo entonces: enriquecer datos + IA asistida
```

**Dependencia circular que hay que romper (la señaló la revisión crítica):** para estandarizar las etapas hay que **liberar a Lili**; para liberarla ayuda la IA de revisión; para esa IA hace falta el set de decisiones de referencia; y ese set requiere tiempo de Virginia (el recurso más escaso y el que más se resiste, porque toca su identidad).

> **Cómo se rompe:** la asistente temporal **descarga la operación de Lili** (lo que ella de verdad pidió) para liberar 4–6 h/semana de tiempo protegido de Lili y Virginia, dedicado a **co-diseñar** el estándar y etiquetar el set de decisiones de referencia. **No** se usa la temporal para "hacer data" mientras Lili sigue ahogada —eso quemaría a la principal aliada interna en el mes 2.

---

## 8. Qué NO concluye este diagnóstico (límites de honestidad)

Para no caer en el mismo error que le señalamos al cliente —prometer sobre supuestos frágiles—, declaramos los límites:

- **No afirmamos** que el punto de partida esté listo "en 2 semanas": depende de B2 y los tiempos intermedios estarán contaminados hasta ordenar las etapas. Solo los **extremos** serán confiables.
- **No afirmamos** que procesar 4.000 CVs sea trivial: el cómputo cuesta ⚠️ ~US$40–150, pero la **revisión de calidad, quitar datos personales, eliminar duplicados y mapear al vocabulario común son semanas de trabajo calificado**, no centavos.
- **No afirmamos** el ahorro de "10–15 h/semana de Lili": es estimación hasta medir su tiempo real durante 2 semanas. El retorno de "IA vs. contratar" se calcula **contra el costo de construir**, no solo contra el costo de la temporal.
- **No afirmamos** que la base valga "60%": es marketing interno hasta que la auditoría de vigencia (B4) lo confirme o lo desmienta con datos.
- **No tratamos** el comparativo salarial como una línea de ingreso real: puede estar **legalmente muerto de origen** según B1/B4.

---

## 9. Conclusión del diagnóstico

Conexión Talento es una firma **valiosa y bien posicionada** cuyo problema no es la falta de tecnología, sino la **falta de disciplina de proceso, de medición y de gobierno del dato**. El estado actual es coherente con una PYME exitosa que creció sobre talento artesanal; el reto —y la oportunidad— es **industrializar la trastienda sin matar el oficio que la hace premium**.

El camino correcto está claro y va **a contracorriente del impulso inicial del cliente** (6 agentes, "mismo día", vender el comparativo salarial, salir del sistema, contratar una persona más):

1. **Cerrar los 5 supuestos bloqueantes** (empezando por el país, hoy).
2. **Estandarizar, digitalizar y documentar** antes de automatizar.
3. **Recuperar el punto de partida** y empezar a medir lo que sí se controla (tiempo hasta entregar la terna, % de vacantes cubiertas dentro del tiempo comprometido, % cubierto con la propia base), no lo ajeno ("mismo día").
4. **Potenciar Team Tailor**, no reemplazarlo, hasta tener datos.
5. **Reparar la experiencia del candidato** —la "cercanía" prometida— como un proceso verificable, no como un eslogan.

> **La afirmación más defendible de todo el diagnóstico:** el primer entregable de valor para Conexión Talento **no tiene una sola línea de código**. Es una hoja de criterios para evaluar candidatos al arranque, un compromiso de tiempo de respuesta hacia el candidato y un registro anti-duplicado —artesanía de proceso que ningún competidor con IA puede copiar sin el criterio humano detrás—. Si una persona nueva no puede seguir el instructivo, la IA tampoco.

---
*Documento de diagnóstico — Fase de Descubrimiento. Las cifras marcadas ⚠️ son supuestos por validar y no deben citarse como hechos confirmados del cliente hasta cerrar las condiciones previas B1–B5.*
