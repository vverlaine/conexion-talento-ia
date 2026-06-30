# Propuesta comercial — Conexión Talento
### Diseñar el sistema operativo de un reclutamiento de clase mundial
**Borrador para revisión interna — preparado para Virginia, CEO**
*Documento de trabajo, sujeto a validación de supuestos. Versión para pulir antes de la entrega del viernes.*

---

## 1. Nuestro entendimiento del reto

Virginia, en nuestras conversaciones nos quedó clara una ambición concreta: que Conexión Talento sea una **consultora de RRHH de clase mundial**, con la **cercanía al candidato** como diferenciador y la velocidad como promesa. También nos pediste algo poco común y que valoramos: que **te retemos**, no que te complazcamos. Esta propuesta honra ese pedido.

Lo que vemos hoy es una firma con un activo real —tu ojo clínico, 20 años de oficio, una base de ~4.000 candidatos y un ATS capaz— operando **sin la columna vertebral que vuelve ese talento escalable**: sin estándar común, sin documentación y sin métricas. El síntoma que más duele (Lili de 7am a 7pm pidiendo "una persona más") no es un problema de manos; es un problema de **proceso**.

**La tesis que proponemos, y que te invitamos a debatir:**

> El diferenciador de Conexión Talento **no será la IA ni el "mismo día"**. Será la **disciplina de proceso** que ningún competidor puede copiar sin el criterio humano detrás. La IA llega *después*, para acelerar un proceso ya ordenado —nunca para escalar el desorden a velocidad de máquina.

Esto no es renunciar a tu visión de los "6 agentes" ni a la velocidad: es **secuenciarla para que funcione**. Primero estandarizar → digitalizar → documentar y medir; luego automatizar lo que ya probó su criterio.

### Lo que esta propuesta dice "SÍ" (y honra tu ambición)
- **SÍ** a la velocidad: time-to-terna de ~5 días a 48–72h es alcanzable y medible. *(El "mismo día" lo reservamos para coincidencias servidas desde tu base ya enriquecida — es la meta de horizonte, no la promesa de arranque.)*
- **SÍ** a la cercanía al candidato: la convertimos de eslogan en **proceso verificable** (SLA de comunicación), y al "reclutador extra" en **embajador de marca**, no en capacidad bruta.
- **SÍ** a la IA, con criterio: pilotos donde el ROI es claro y el riesgo bajo, sobre proceso estandarizado y con tu ojo clínico como el criterio que *entrena* la IA.
- **SÍ** a monetizar tu base y al benchmark de compensaciones — por un **camino legal y construido bien**, no rápido y expuesto.

### Lo que te retamos a reconsiderar
| Idea inicial | Nuestro reto | Por qué |
|---|---|---|
| "Necesitamos una persona más" | El cuello de botella es de **proceso**, no de manos. Un 5º reclutador sin estándar = una 5ª forma de hacer las cosas. | Estandarizar el intake y el cribado libera más capacidad que una contratación. |
| "6 agentes de IA" | Hoy son **6 procedimientos aún no escritos**. 5 de 6 no son "agentes": son herramientas con salida estructurada. | Automatizar sin estándar produce malos *matches* más rápido. |
| "La base de 4.000 es oro (~60% del valor)" | Es **oro sin refinar e ilíquido**: sin identidad única, ~30–50% probablemente vencida ⚠️, sin etiquetas. | El valor llega *tras* estructurarla, no antes. La mediremos antes de invertir en ella. |
| "Vender el benchmark de compensaciones" | **Bandera legal grande.** Bajo la ley salvadoreña vigente (Decreto 144/2024), **solo es comercializable sobre datos anonimizados de forma irreversible y agregada** (k-anonimato). No entra al camino crítico hasta validar base legal con abogado local. | En mercados pequeños, "agregado" sigue siendo re-identificable; puede chocar con NDA de tus clientes. |
| "Salir del ATS (Team Tailor)" | **No precipitarse.** Se exprime y se extrae por API primero; migrar es decisión posterior, con datos. | Migrar 4.000 registros sin estructura replica el desorden en un sistema más caro. |

> **Nota de transparencia (y de integridad).** Somos una consultora de Data e IA: nos conviene construir cosas a la medida. Por eso lo decimos explícito: **primero exprimimos las funciones de IA que Team Tailor ya te cobra y no usan**, y solo recomendamos construir lo propio cuando el volumen y la economía lo justifiquen. En un primer proyecto, tu confianza vale más que el tamaño de nuestro encargo.

---

## 2. El hallazgo más explotable: no partes de cero

Hay una buena noticia que cambia el tono del proyecto: **"cero métricas" no es del todo cierto**. Team Tailor lleva años registrando, en silencio, marcas de tiempo y movimientos de etapa de tus ~4.000 candidatos. Existe una **línea base histórica recuperable** —enterrada en el ATS— que podemos minar *sin instrumentar nada nuevo*, siempre que el plan contratado permita exportarla (lo confirmamos en la primera semana; ver Fase 0).

Igual de importante: los dos dolores más visibles tienen solución **barata y rápida**, y no requieren IA:
1. **"Mandé el mismo candidato dos veces al mismo cliente."** Es un control de proceso ausente, no un problema de IA. Un registro de presentaciones (candidato × cliente × fecha) con alerta de duplicado lo lleva a ~0 en días.
2. **"4 personas, 4 formatos de CV."** Tu *prompt* de CV con branding ya es un estándar embrionario. Formalizarlo como activo de la firma es un quick win visible en la primera semana.

---

## 3. Enfoque por fases (flexible y reordenable)

Diseñamos el programa como **fases con puertas de decisión (go/no-go)**: cada fase termina con un resultado medible que habilita —o detiene— la siguiente. Tú decides el ritmo y el orden; si una fase "te quita el oxígeno", se reordena. **Nada se automatiza sin haber pasado por la "Puerta Listo para IA"** (ver §6).

```
Fase 0          Fase 1               Fase 2              Fase 3
Factibilidad    Estándar +           IA asistida         Activo de datos
+ Quick Wins    Documentar + Medir   (piloto por módulo) (base, mercado interno,
2–3 semanas     4–6 semanas          por evidencia        benchmark legal)
                                     no por promesa       land-and-expand
   │                │                     │                    │
 PUERTA 0         PUERTA 1             PUERTA 2             PUERTA 3
```

### Resolviendo la tensión de secuencia (la ruta crítica acordada)
Tres disciplinas piden cosas distintas "primero": datos quiere extraer y parsear; proceso quiere documentar; métricas exige etapas estandarizadas. **La reconciliamos así:**
1. **Estandarizar las etapas del ATS** (prerrequisito de toda métrica limpia) → Fase 1, temprano.
2. **Documentar el SOP de cribado + extraer la rúbrica de tu ojo clínico** (insumo de todo lo demás) → Fase 1.
3. **Extraer/parsear la base** corre *en paralelo* en Fase 1, pero solo se *enriquece y vuelve buscable* en Fase 3, sobre el diccionario de datos ya definido.

### Rompiendo la dependencia circular (huevo y gallina)
Para estandarizar hace falta tiempo de Lili; Lili está saturada; liberarla "del todo" requiere IA; la IA requiere tu rúbrica documentada; documentarla requiere *tu* tiempo. **Lo rompemos por el eslabón más barato:**
- La **asistente temporal** (presupuesto ya aprobado) **descarga la operación de Lili** —su pedido real— para liberarle **4–6h/semana protegidas** de diseño de proceso. No la ponemos a hacer ciencia de datos.
- Tu ojo clínico se documenta **con sesiones cortas (45 min, cronometradas)**, no con talleres maratónicos.
- **Extraemos el conocimiento de Lili y tuyo en las primeras 2–3 semanas**, como seguro ante imprevistos (mitiga el riesgo de que su sobrecarga interrumpa el proyecto).

---

## 4. Entregables y tiempos por fase

### Fase 0 — Factibilidad, Diagnóstico y Quick Wins · 2–3 semanas
*Objetivo: apagar los supuestos frágiles y entregar valor visible y tangible de inmediato.*

**0.A — Spike de factibilidad técnica y legal (semana 1, bloqueante).** Antes de comprometer alcance de fases posteriores confirmamos:
- API/export/tier real de **Team Tailor**: la base **sí es extraíble por API REST** con una *key* Admin/Read (verificado en investigación), pero la **descarga masiva de los PDF de CV no está confirmada** y hay límite de ~5 llamadas/seg — lo probamos contra tu cuenta real en la semana 1. Ver [`99-research/team-tailor.md`](../99-research/team-tailor.md).
- **Marco legal:** El Salvador **ya tiene Ley de Protección de Datos Personales vigente (Decreto 144/2024)** — Conexión Talento **es sujeto obligado hoy**. Validamos consentimiento por finalidad, registro de tratamientos, retención y el estatus en Guatemala. *El articulado exacto y el lanzamiento del benchmark requieren visto bueno de un abogado salvadoreño* (nosotros diseñamos el cumplimiento, no damos opinión legal vinculante). Ver [`99-research/marco-legal-datos-sv-gt.md`](../99-research/marco-legal-datos-sv-gt.md).
- **Muestreo de vigencia** de la base: ¿cuántos de los 4.000 son contactables y vigentes de verdad?
- ¿Existe **historial recuperable** de ternas pasadas que sirva de *golden set* para calibrar la IA, o hay que construirlo?

**0.B — Quick wins de credibilidad:**
- **Registro de presentaciones anti-duplicado** con regla obligatoria antes de enviar terna (hoja o campo en ATS). Cierra un riesgo reputacional ya materializado.
- **Plantilla/SOP de CV con branding v1**, formalizando tu *prompt* como activo versionado de la firma (no en tu cabeza ni en tu cuenta personal). **Teaser para el viernes: un CV real, ya reformateado.**
- **Cierre de brecha activa de privacidad:** dejar de pegar CVs en ChatGPT de consumo; migrar a un entorno con no-entrenamiento y DPA. Costo casi nulo, riesgo cerrado.
- **Auditoría exprés de Team Tailor:** activar funciones de IA y automatizaciones que *ya pagas y no usas*.
- **Mapa de actores y "antes/después de Lili"** para la reunión del martes (ver §10).

**Entregable de la fase:** informe de factibilidad (semáforo verde/amarillo/rojo por supuesto) + tablero de línea base retrospectiva *si el ATS lo permite* (con caveats honestos: confiables los extremos —apertura, terna, cierre—; los tiempos intermedios, indicativos).

---

### Fase 1 — Estandarizar, Documentar y Medir · 4–6 semanas
*Objetivo: la columna vertebral. Aquí vive el valor real y la capacidad que se queda.*

- **Mapa de proceso "deber ser" de los 8 pasos** con responsable (RACI), SLA por etapa y dueño de proceso nombrado. **Co-autorado con Lili y el equipo** (no impuesto): *ownership = adopción*.
- **SOP de cribado/ranking con rúbrica explícita ponderada** —tu ojo clínico hecho criterios, pesos y escalas— + **golden set** de decisiones de referencia. *Este es el entregable estrella: estandariza el dolor más caro y de-riesga la futura IA.*
- **Plantilla de intake/scorecard de 1 página por vacante** (must-have / nice-to-have / pesos / definición de éxito a 90 días). Sin esto, ningún agente tiene criterio que aplicar.
- **Estandarización de etapas (stage-gates) en Team Tailor** + 6–8 campos obligatorios al abrir mandato. Habilita la analítica forward.
- **Árbol de métricas en 1 página:** 1 North Star (*fill rate* dentro de SLA + colocaciones/reclutador) y ~10 KPIs con dueño, definición y fuente. *Time-to-submit* como meta agresiva; *time-to-fill* se reporta, no se promete.
- **Kit de candidate experience:** SLA de comunicación + plantillas. *Reparamos el seguimiento ANTES de lanzar encuestas de satisfacción* (encuestar a quien ya está molesto sin antes responderle genera más reacción negativa).
- **Marco de gobernanza de datos (RoPA-lite):** inventario, base legal por finalidad, retención y consentimiento. Barato de redactar, caro de omitir.
- **Diccionario de datos y taxonomía v1** (skills/sectores/estados de vigencia), base de ESCO + overlay local de Centroamérica. *Prerrequisito para que enriquecer la base produzca activo y no ruido.*

---

### Fase 2 — IA asistida, piloto por módulo · por evidencia, no por promesa
*Objetivo: acelerar lo que ya probó su criterio. Solo módulos que pasen la "Puerta Listo para IA".*

- **Screener/Ranker asistido** sobre el SOP+rúbrica+golden set: des-identifica PII (foto/edad/estado civil) → puntúa contra el scorecard con justificación citada al CV → pre-ordena. **El humano valida top 10 y terna; la IA nunca decide el rechazo sola.** Guardarraíles como código: top10=llamada · 10–20=abierto · 30+=rechazo cordial **revisado por humano**.
- **Generador de CV con branding productizado:** extracción a esquema fijo + plantilla determinista (el layout no se deja al modelo).
- **Medición contra la línea base de Fase 1** + auditoría de sesgo (tasas de selección por grupo; exclusión de variables proxy).
- *Opcionales por evidencia:* Entrevistador pre-screening (ASR comprado, no construido; con consentimiento de grabación). Perfilador y Redactor entran si el caso lo justifica.

---

### Fase 3 — El activo de datos (land-and-expand) · horizonte de crecimiento
*Objetivo: convertir la base en activo líquido y abrir nuevas líneas. Aspiracional, condicionada a las fases previas.*

- **Estructuración y enriquecimiento de la base** (parsing a campos estructurados, resolución de identidad/golden record, score de vigencia) → búsqueda por skill e *internal-fill rate*.
- **Mercado interno / historial de candidato** + portal de auto-actualización (mejora candidate experience y refresca vigencia sin trabajo manual).
- **Decisión informada augmentar-vs-migrar Team Tailor** (con datos y caso de negocio, incluyendo el análisis de riesgo de seguridad de volverte tú el custodio de la PII).
- **Benchmark de compensaciones** — *solo* con validación legal por país, anonimización con k-anonimato, fuentes lícitas y consentimiento granular. Camino alternativo a explorar: **alianza con un proveedor licenciado de datos salariales**, en lugar de generar las cifras tú.
- **Cross-sell de capacitaciones** a la base, condicionado a consentimiento separado.

---

## 5. Modelo de inversión (pricing por fase)

**Principio de diseño:** *fixed-fee por fase*, que acota tu riesgo y el nuestro y permite reordenar. **Sin retainer ni success-fee al inicio** (no hay aún línea base para medir éxito ni proceso estable). Un componente variable —atado a una métrica medible, p. ej. reducción de time-to-terna— solo se introduce en Fase 3, nunca antes de tener línea base.

> **Reencuadre del ancla de precio.** Una asistente temporal añade capacidad lineal por 3 meses y luego desaparece dejando el mismo desorden. Nosotros instalamos **estándar + documentación + métricas + activos que se quedan y se componen**. No vendemos manos; instalamos el sistema operativo de la firma.

| Fase | Naturaleza del fee | Lógica de inversión | Rango ⚠️ *(indicativo USD, a calibrar con tarifa local)* |
|---|---|---|---|
| **0 · Factibilidad + Quick Wins** | Fijo, deliberadamente digerible | "Sí" fácil. Cercano al costo de ~1–1.5 meses de la temporal. Lo tratamos casi como costo de adquisición a cambio de derechos de caso/referidos. **El 100% acredita a Fase 1 si avanzas** (reductor de riesgo, no descuento). | **US$1.800 – 3.500** |
| **1 · Estándar + Documentar + Medir** | Fijo, mayor | **Aquí está el valor real.** Capacidad instalada que se queda. | **US$6.000 – 14.000** |
| **2 · IA asistida** | Fijo **por módulo** | Pagas solo los módulos que pasan la Puerta. Modular = control de gasto. *(Screener/Ranker ~US$4–8k · Generador de CV ~US$2–5k.)* | **US$5.000 – 16.000** |
| **3 · Activo de datos** | Fijo por componente + posible kicker por métrica | Land-and-expand. Se autofinancia con el valor demostrado en fases previas. | **US$12.000+** por componente, a definir con datos |

> **Arranque realista (Fases 0–2): ~US$13.000–33.000**, consistente con el benchmark de mercado para transformación+IA en PYMEs de LATAM (~US$14–36k; ver [`99-research/pricing-engagement.md`](../99-research/pricing-engagement.md)). **No te pedimos comprometerte con todo:** decides fase por fase. Las cifras son indicativas y se cierran al calibrar tu *fee* por colocación y la tarifa local (Fase 0).

### Los tres modelos de cobro (tú eliges — esta es tu decisión)

Te presentamos los tres, con nuestra recomendación honesta para un *primer* trabajo conjunto:

| Modelo | Cómo funciona | A favor | En contra | Cuándo encaja |
|---|---|---|---|---|
| **A · Fixed-fee por fase** ✅ *recomendado para arrancar* | Precio cerrado por los entregables de cada fase; pagas solo lo que apruebas en cada puerta | Acota tu riesgo y el nuestro; reordenable; sin sorpresas; ideal para construir confianza | Exige definir bien el alcance de cada fase de entrada | **Fases 0–2.** El modelo correcto para empezar |
| **B · Retainer mensual** | Cuota fija mensual (estimado **US$2.500–5.000/mes ⚠️**) por acompañamiento y operación continua | Flujo predecible; nos vuelve socios de operación, no de proyecto; bueno para mejora continua | Requiere confianza ya probada; sin entregables atados, puede sentirse difuso al inicio | **Fase 3 / operación**, una vez instalado el sistema |
| **C · Híbrido base + éxito** | Fee base reducido por fase **+** *kicker* atado a una métrica (p. ej. % de reducción de time-to-terna, o monto por colocación incremental) | Alinea incentivos; demuestra que apostamos por el resultado | **Imposible de medir sin línea base ni proceso estable** — premiar/penalizar sobre datos sucios es injusto para ambos | **Solo Fase 3**, nunca antes de tener línea base limpia |

**Nuestra recomendación:** **Fixed-fee por fase (A) para las Fases 0–2**, y *recién* en Fase 3 evaluar pasar a **retainer (B)** para la operación continua e introducir un **componente de éxito (C)** sobre una métrica ya medible. Cobrar por éxito hoy —sin línea base— sería venderte humo con otra etiqueta. **Decídelo tú:** si prefieres retainer desde el inicio por previsibilidad de caja, lo estructuramos; solo seríamos transparentes en que, sin línea base, el "éxito" aún no es medible.

### Chequeo de asequibilidad y honestidad de ROI
Tenemos que ser directos: el **programa completo end-to-end** (ingeniería de datos + IA + legal + cambio) es un esfuerzo de varios meses y **excede con holgura el techo de "3 meses de temporal"**. Por eso el diseño es **modular y autofinanciado**: no te pedimos comprometerte con todo. Empiezas por Fase 0–1 —lo que sí cabe en tu economía y entrega valor real— y **cada fase siguiente se justifica con su propio KPI de ROI** antes de avanzar.

**Opciones de alcance (para tu decisión):**
- **Opción A — "Suficientemente bueno" (BUY):** Fase 0 + Fase 1 ligera. Exprimir la IA que Team Tailor ya cobra, SOPs livianos, dedup, plantilla de CV, línea base. *Máximo valor por dólar; recomendada si el volumen no justifica construir.*
- **Opción B — "Sistema + piloto IA":** A + Fase 2 (Screener/Ranker y CV con branding). Recomendada si la línea base confirma el ahorro de horas.
- **Opción C — "Activo de datos":** B + Fase 3. Solo cuando la economía unitaria lo respalde con datos.

### Plantilla de economía unitaria (para llenar el martes con tu dato de fee)
> **Payback por fase = (fee por colocación × colocaciones incrementales por mayor velocidad / internal-fill) − costo del sistema.**
> Falta un único dato —**tu fee promedio por colocación**— para volverla concreta. Es la primera conversación del martes.

### El cuadro de alternativas (por qué nosotros)
| Opción | Costo | Qué obtienes | Qué queda al final |
|---|---|---|---|
| **No hacer nada** | $0 directo | Sigue el desorden; Lili a 7am-7pm; riesgo reputacional vivo | Nada; el problema crece |
| **Solo la temporal (3 meses)** | ~US$1.5k–2.7k ⚠️ | Alivio temporal | Nada permanente; dependencia regresa en el mes 4 |
| **Firma grande** | Alto | Marca, deck | Solución genérica, sin tu ojo clínico; te tratan como cuenta menor |
| **Nosotros** | Modular, por fase | Sistema + capacidad instalada + métricas + tu criterio codificado | **Un activo que se queda y se compone** |

---

## 6. La "Puerta Listo para IA" (nuestro compromiso anti-desorden)

Ningún proceso se automatiza sin aprobar este checklist de 1 página. Es la garantía contractual de que **no automatizamos el caos**:

1. Entrada/salida documentada con ejemplos.
2. Criterios de decisión explícitos (rúbrica).
3. Estructura de datos estándar.
4. Excepciones y escalamiento humano definidos.
5. Métrica de calidad y línea base establecidas.
6. Golden set para evaluación.
7. Guardarraíles de lo que la IA **NO** debe hacer.

> *Regla simple: si un humano nuevo no puede ejecutar el SOP, la IA tampoco.*

---

## 7. Supuestos (a validar)

Marcamos como ⚠️ todo lo que aún no confirmamos. Varios son **precondiciones bloqueantes**, no detalles:

- ✅ **País de operación: El Salvador (primario) + Guatemala (secundario).** El Salvador ya regula datos personales (Decreto 144/2024); Guatemala aún no tiene ley general. *Falta validar oficialmente con Virginia el consentimiento de la base y si hay candidatos/clientes en la UE (activaría GDPR/EU AI Act).*
- ⚠️ **Team Tailor expone API/export en el tier contratado.** Si no, varios entregables de Fase 0–1 cambian; hay plan B (captura manual acotada).
- ⚠️ **Existencia de un golden set** (historial recuperable de ternas pasadas). Si no existe, construirlo requiere tiempo de Virginia y se dimensiona aparte.
- ⚠️ **Vigencia real de la base:** estimamos 30–50% no vigente; se mide en Fase 0 antes de invertir en enriquecerla.
- ⚠️ **Fee por colocación y volumen de mandatos/mes.** Sin esto no hay caso de ROI cuantificado.
- ⚠️ **Origen y consentimiento de los 4.000** (¿aplicaron o fueron sourced de LinkedIn?). Define qué usos secundarios son lícitos.
- ⚠️ **Colisión de nombres:** el consultor líder y un reclutador del equipo se llaman ambos "Víctor". Confirmar si son la misma persona o homónimos (afecta gobernanza y roles).
- ⚠️ **Disponibilidad real de Virginia y Lili** para sesiones de documentación (horas protegidas).

**Sobre nuestra propia capacidad (transparencia de entrega):** somos una boutique. El núcleo data/IA/proceso lo entregamos nosotros; la **asesoría legal de protección de datos y antitrust la subcontratamos** con un especialista local, y el **ASR** se compra, no se construye. El cronograma refleja un equipo pequeño y enfocado: por eso priorizamos quirúrgicamente.

---

## 8. Qué necesitamos de Conexión Talento

| Necesitamos | Para qué | Cuándo |
|---|---|---|
| Confirmar el **país** de operación | Desbloquear todo el marco legal y el scoping | Esta semana |
| **Accesos a Team Tailor** (lectura/export) y plan contratado | Verificar API y minar la línea base | Semana 1 |
| **Fee por colocación + volumen** de mandatos/mes | Construir el caso de ROI | Reunión del martes |
| **Horas protegidas** de Virginia (golden set) y Lili (co-diseño) | Romper la dependencia circular | Desde semana 1 |
| Redirigir la **temporal** a descargar la operación de Lili | Liberar a Lili sin recrear dependencia | Acuerdo previo al martes |
| Designar un **dueño interno** del estándar | Que la capacidad se quede cuando salgamos | Fase 1 |
| Confirmar **decisor económico** y ciclo de aprobación | Cerrar bien | Antes del cierre |

---

## 9. Criterios de éxito y de "kill" (números, no adjetivos)

Para no desangrarnos —ni hacerte gastar— en algo que no funciona, cada puerta tiene umbrales concretos *(a calibrar con tus datos ⚠️)*:

- **Puerta 0 (go/no-go a Fase 1):** factibilidad de API confirmada **o** plan B definido; vigencia de base medida; plantilla de CV adoptada por los 4 reclutadores; registro anti-duplicado en uso; línea base de ≥3 KPIs entregada. *Si no se cumplen, paramos y reescopeamos antes de invertir en Fase 1.*
- **Puerta 1 (go a Fase 2):** etapas estandarizadas en ATS; SOP de cribado + rúbrica firmados por el equipo; golden set armado; time-to-terna baseline medido. *La IA no arranca sin esto.*
- **Puerta 2 (go a Fase 3):** concordancia IA-vs-ojo clínico ≥ umbral acordado en 1–2 búsquedas reales; auditoría de sesgo sin disparidad relevante; mejora medible de time-to-terna. *Sin evidencia, no se escala.*

---

## 10. Nota para la reunión del martes con Lili

**El martes —no el viernes— es el verdadero primer hito del proyecto.** Lili es a la vez el cuello de botella, la *champion* natural y un punto único de falla. Si percibe que el sistema amenaza su rol o su headcount, la adopción muere desde adentro. Los artefactos de abajo deben estar **listos el lunes**.

**Qué llevar (munición para Virginia):**
1. **Job description del rol "Embajador de Marca / Candidate Experience"** (1 página): el rol extra **no** es backfill de cribado; es seguimiento al candidato, cierre del loop (los que hoy atacan en LinkedIn) y curaduría de la base. *Desactiva el miedo a "la IA me reemplaza" creando un rol que la IA no puede hacer.*
2. **"Un día de Lili: antes vs. después"** (1 página): cómo el sistema le devuelve 4 horas diarias y la sube de operativa a estratega y dueña del estándar.
3. **Mapa de los 8 pasos con Lili como co-autora/validadora** (cubre que el liderazgo data/IA no es de RRHH; ella es la fuente de verdad del oficio).
4. **Encuadre de la temporal:** los 3 meses descargan la **operación** de Lili (su pedido real) y protegen sus horas para co-diseñar —no para tapar el caos.

**Mensajes clave para Lili:**
- *"No te reemplazamos: te devolvemos tus tardes y te volvemos dueña del nuevo estándar."*
- *"La IA pre-ordena; tú decides. El criterio final siempre es humano."* (El guardarraíl "la IA no opina fuera de lo definido" es, bien contado, el mejor argumento de adopción.)

**Para Virginia, como sponsor:** el cambio se modela desde arriba. Tu *prompt* de branding ya es la prueba de que "estás dentro". Te pediremos adoptar primero y públicamente, y ofrecer tu ojo clínico como **el criterio que entrena la IA**, no como algo que la IA amenaza.

---

## 11. Blindajes del consultor (uso interno — no va al cliente)

> Añadido tras el **Consejo LLM #01** ([`../00-memoria/consejo-llm-01.md`](../00-memoria/consejo-llm-01.md)). Cierra los riesgos que el consejo detectó del lado de Víctor, no del cliente.

### 11.1 Contrato por hitos (pago atado a puertas)
- **Fase 0 pagada por adelantado** (US$2.500). Sin anticipo, no arranca.
- Cada fase siguiente se **firma y factura por separado**, contra entregables aprobados en la puerta anterior. No hay compromiso de US$39k el viernes.
- **Protege a ambos:** Virginia solo paga lo que ya vio funcionar; Víctor no ejecuta meses sin cobrar ni se ata a un alcance aún no verificable.

### 11.2 Propiedad intelectual / reutilización de metodología
- Víctor **conserva** su metodología, plantillas, rúbricas y marco — anonimizados, **sin** la base de candidatos ni datos del cliente — para usarlos con clientes **no competidores**. *Definir "competidor" en sentido **estrecho**: otra boutique de headhunting en SV/GT sobre el mismo segmento. El reúso **cross-industria y cross-función** queda explícitamente permitido —si no, en RRHH-Centroamérica casi cualquier firma sería "competidora" y la cláusula quedaría hueca, vaciando la economía del primer cliente (§11.6).*
- Línea clara: la **metodología es de Víctor**; los **datos y el contenido específico son del cliente**.
- Esto convierte al cliente cero en **palanca de la firma**, no en un callejón sin salida. Dejarlo por escrito desde ya evita discusión futura. *(Esta es la jugada del "Expansionista": va al contrato, no al pitch.)*

### 11.3 Caveat legal de datos (congelar monetización)
- Los 4.000 candidatos consintieron para **R&S**, NO para entrenar un activo revendible.
- Cualquier monetización (benchmark, marketplace) exige **nueva base de licitud + dictamen de abogado salvadoreño** (Decreto 144/2024) y cuidado con la **transferencia SV–GT**.
- **Congelar** toda venta de la base hasta ese dictamen. No prometérselo a Virginia como ingreso.

### 11.4 Flujo de caja y capacidad de Víctor
- Es **una persona** que vende, administra y ejecuta. 53–77 jornadas ≈ **5–6 meses** ajustados: riesgo real de subcotizar y desbordarse.
- **Cobrar Fase 0 por adelantado.** **No firmar F1–F2** hasta verificar la API/export de Team Tailor.
- Dimensionar dedicación real y **subcontratar lo legal/ASR** en vez de absorberlo.
- **Reversión de riesgo des-apilada (Consejo #05):** se quitó el "put gratis". Se **eliminó la devolución del anticipo**; el de-riesgo queda en (1) 100% acreditable, (2) los activos son tuyos, (3) **gate objetivo de Puerta 0**. La garantía ya no cuelga del juicio subjetivo "valor claro".
- **⚠️ Autocanibalización de la Fase 1 (decisión comercial de Víctor antes del viernes):** $9.500 − $2.500 (crédito 100% de F0) = ~$7.000 por hasta 30 jornadas ≈ **~$233/jornada** — tarifa de junior para un estándar "McKinsey". El crédito que de-riesga a Virginia te canibaliza. **Opciones:** (a) subir F1 al rango **~$12–14k**; o (b) acreditar F0 **parcial (50%)** en vez de 100%. *Recomendación: como es el primer cliente y la referencia vale más que el margen, mantén el gesto generoso del 100% pero **sube F1** — no regales ambos.* No se cambió el "100% acreditable" del doc cliente sin tu visto bueno.

### 11.5 Build vs. buy (declaración de conflicto de interés)
- Primero **exprimir las funciones de IA que Team Tailor ya cobra** y herramientas baratas existentes.
- Construir custom **solo** cuando volumen y economía lo justifiquen con datos reales.
- En el primer proyecto, la **integridad pesa más que el tamaño del encargo**: recomendar lo barato cuando alcanza construye la relación que paga las fases siguientes.

### 11.6 Si la Fase 0 sale roja + economía del primer cliente (punto ciego del Consejo #03)

**El activo real de este engagement no es el fee: es el caso referenciable + la IP.** Una F0 tibia o fallida no cuesta $2.500; mata el testimonio, la prueba social y la primera referencia de la firma. Reencuadrar toda la economía del cierre alrededor de **asegurar referencia + IP**, no de maximizar margen.

**Guion si la Puerta 0 sale roja** (la base está demasiado sucia / la API no exporta / la tesis de proceso no se valida):
- **Qué se entrega igual:** el semáforo honesto, la plantilla/SOP de CV, el registro anti-duplicado y la línea base posible — son de Virginia pase lo que pase (ya prometido en el doc cliente).
- **Cómo se protege la referencia:** un *post-mortem* franco con recomendación de camino "BUY suficientemente bueno" (activar la IA que Team Tailor ya cobra + SOPs livianos). Honestidad = la mejor publicidad para el segundo cliente.
- **Qué se lleva Víctor:** la metodología/plantillas anonimizadas (IP reutilizable, §11.2) y el aprendizaje para el siguiente prospecto.

**Riesgo de concentración + BATNA:** la firma apuesta su primer proyecto **y** su IP **y** su canal de distribución a una sola clienta. El BATNA real de Virginia es **renovar solo la temporal y decir no**. Mitigación: tener un **segundo prospecto** en el radar antes del viernes para no negociar desde la necesidad, y no atar decisiones estratégicas (precio, alcance) a que Virginia diga sí.

**Bus factor:** Víctor entregando "McKinsey" solo, con ruta crítica dependiente de terceros (legal/ASR) sin colchón. Nombrar un plan de respaldo mínimo.

| # | Acción | Responsable | Fecha |
|---|---|---|---|
| 1 | Confirmar país + fee/colocación + accesos Team Tailor | Virginia | Esta semana |
| 2 | Preparar los 4 artefactos para la reunión con Lili | Nosotros | **Lunes** |
| 2b | **Montar y probar el entorno con DPA** (Claude for Work / API no-entrenamiento) con un CV sintético — *bloqueante del teaser legal del viernes* | **Nosotros** | **Lunes** |
| 3 | **Reunión Virginia ↔ Lili** (alinear rol y temporal) | Virginia + Lili | **Martes** |
| 4 | Entregar **propuesta pulida + teaser** (**CV real anonimizado** reformateado con branding, en entorno con DPA + concepto de dedup) | Nosotros | **Viernes** |
| 5 | Decisión de alcance (Opción A/B/C) y arranque de Fase 0 | Virginia | Semana siguiente |

---

*Gracias por la confianza y por pedirnos que te retemos: es exactamente así como se construye una relación de clase mundial. Esta propuesta es un borrador vivo —la afinamos contigo antes del viernes.*

> **Pendientes para pulir antes de entregar (uso interno, eliminar en la versión final):** insertar cifras de pricing una vez calibradas con tarifa local y fee de colocación; confirmar país y reemplazar los ⚠️ resueltos; ajustar umbrales go/no-go con datos reales; validar capacidad/calendario del equipo de entrega.
