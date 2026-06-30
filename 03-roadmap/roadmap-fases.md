# Roadmap por Fases — Conexión Talento
### Programa de estandarización, datos e IA asistida para Reclutamiento y Selección
*Documento de decisión | Borrador para revisión del viernes | Versión 1.0*

---

> **En una frase:** Primero ordenamos y medimos cómo selecciona Conexión Talento; solo después le sumamos IA. Así protegemos el negocio actual y construimos un activo que se queda, en lugar de comprar alivio temporal que se evapora.

---

## Cómo leer este documento

Este roadmap convierte el diagnóstico de las 8 miradas expertas en un **plan accionable que se puede pagar por partes**. Tres decisiones de diseño lo gobiernan, y responden directamente a las críticas más duras que recibió el plan:

1. **Una sola ruta, no fases en paralelo.** Hay un único orden que funciona: **fijar criterios de selección → documentar el proceso → instalar las mediciones → y recién entonces extraer/automatizar la información.** No se automatiza ningún paso sin antes tener su estándar escrito y su punto de partida medido (línea base). Esto es una condición del contrato, no una buena intención. Resuelve la tensión natural entre los frentes: el de datos quiere procesar la información ya, el de proceso quiere documentar primero, el de métricas exige etapas estandarizadas antes de medir.
2. **Condiciones que bloquean, con responsable y fecha**, no "preguntas abiertas". Cuatro supuestos sostienen todo el programa (país de operación, conexión técnica con el sistema de candidatos, permiso de uso de los datos, y si existe un set de decisiones de referencia). Se cierran en una **prueba de factibilidad pagada de 1 semana** ANTES de comprometer alcance o precio de las fases siguientes.
3. **Camino por defecto = "suficientemente bueno con lo que ya se paga".** Activar la IA que Team Tailor ya cobra + procedimientos simples; y construir algo a medida **solo** si el volumen y los números lo justifican. Declaramos abiertamente nuestro conflicto de interés: construir infraestructura nos conviene a nosotros; recomendar exprimir lo que el cliente ya paga le conviene al cliente. Elegimos lo segundo como postura por defecto.

> ⚠️ **Los supuestos a validar van marcados así en todo el documento.** Las cifras de duración, costo y ahorro son rangos ilustrativos hasta cerrar la prueba de factibilidad y conocer el honorario por colocación y el volumen mensual de búsquedas.

---

## Tabla resumen del roadmap

| Fase | Nombre | Objetivo en una línea | Duración | Hito de salida (seguir/parar, cuantificado) |
|---|---|---|---|---|
| **0.0** | **Prueba de factibilidad** (técnica + legal) | Apagar los 4 supuestos que sostienen todo lo demás | **1 sem** (dentro de Fase 0) | Conexión técnica con Team Tailor confirmada · país + ley aplicable confirmados · muestra de cuán vigente está la base · ¿existe set de decisiones de referencia? |
| **0** | **Quick win + Diagnóstico** | Credibilidad temprana visible + foto honesta del "cómo se trabaja hoy" | **2–3 sem** | ⭐ Plantilla de CV adoptada por los 4 + control de duplicados operando + punto de partida medido de 3 indicadores (solo los casos claros) entregado |
| **1** | **Estandarizar, documentar e instrumentar** | Convertir el "ojo clínico" tácito en estándar medible y los datos en estructura | **4–6 sem** | Hoja de criterios + procedimiento de cribado en uso · etapas únicas en Team Tailor · diccionario de datos · mediciones nuevas capturándose |
| **2** | **IA asistida (copiloto)** | Acelerar el proceso YA estandarizado, siempre con una persona validando | **6–10 sem** | El asistente que ordena candidatos coincide ≥X% con el criterio de Virginia en 2 búsquedas reales · herramienta de CV en uso real · 0 rechazos automáticos |
| **3** | **Orquestación, escala y monetización** | Base de datos viva + nuevas líneas de ingreso, condicionadas a la ley | **Trimestral, modular** | Decisión sobre el sistema de candidatos con datos · % de vacantes cubiertas con base propia ≥30–40% ⚠️ · estudio de salarios solo con dictamen legal favorable |

**Duración total estimada del núcleo (Fases 0–2): ~3–5 meses.** La Fase 3 es opcional: empezar pequeño y crecer, modular, y se paga sola con el valor demostrado en las fases previas.

---

## Principios rectores (la ruta crítica resuelta)

```
Prueba factibilidad ─► Reparar comunicación al candidato ─► Estandarizar CRITERIOS (hoja de criterios)
        │                                                          │
        └─► quitar duplicados + CV con marca (quick wins) ─► Etapas únicas en Team Tailor ─► Mediciones nuevas
                                                                   │
                              Extraer/estructurar la base ─► IA copiloto (con persona validando) ─► Escala/monetización
```

**Reglas no negociables del programa:**
- **Ninguna intervención toca una búsqueda en curso.** El 63% de los ingresos sigue fluyendo intacto durante la transformación. Lo aislamos de forma explícita.
- **Reparar antes de medir.** El compromiso de tiempo de respuesta al candidato se arregla ANTES de lanzar cualquier encuesta de satisfacción. Encuestar a candidatos a quienes ya se les dejó de responder, sin haber cerrado ese hueco, genera **más** reacción negativa en LinkedIn, no menos.
- **Siempre una persona validando**, obligatorio en todo rechazo y en la terna (la lista de 3 finalistas). La IA pre-ordena; la persona decide. Se elimina el rechazo automático a los candidatos peor rankeados como decisión final.
- **El presupuesto de la temporal (3 meses) sirve para descargar la OPERACIÓN de Lili** (su pedido real, su seguro contra el riesgo de que renuncie), **no** para tareas de datos para las que no está calificada. La estructuración de datos la hacemos nosotros.

---

## Condiciones que bloquean el arranque (cerrar HOY)

| # | Condición | Por qué bloquea | Responsable | Fecha límite |
|---|---|---|---|---|
| P1 | **País exacto de operación + dónde residen candidatos y clientes** | Define qué ley de datos aplica (El Salvador —operación principal—: Ley de Protección de Datos Personales / Decreto 144 de 2024, **ya vigente**, regulador ACE · Guatemala: aún sin ley, aplica *habeas data*), el registro ante el regulador, la viabilidad del estudio de salarios y la exposición a Europa (GDPR Art. 22 / AI Act) | Virginia (correo de 5 min) | **Lunes** |
| P2 | **Plan contratado de Team Tailor: ¿permite conexión técnica entre sistemas, descargar la información en masa, campos a medida y cuáles son sus límites?** | Sostiene la extracción, el punto de partida histórico, el control de duplicados y las búsquedas inteligentes. Sin esto, media Fase 0–1 colapsa | Consultoría + administrador de Team Tailor del cliente | Prueba sem. 1 |
| P3 | **Origen y permiso de los 4000 candidatos** (¿aplicaron ellos vs los buscamos en LinkedIn?) | Define qué usos secundarios (estudio de salarios, venta cruzada) son legales | Virginia + revisión legal local | Prueba sem. 1 |
| P4 | **¿Existe historial recuperable de "quién entró a terna vs quién no"?** (set de decisiones de referencia) | Sin él, calibrar el asistente obliga a Virginia a re-etiquetar cientos de CVs a mano — un esfuerzo grande que hoy no está financiado | Lili/Virginia | Prueba sem. 1 |

> **Choque de calendario — atención.** La reunión Virginia–Lili es el **martes**; la propuesta es el **viernes**. Los materiales para esa reunión (descripción del rol "Embajador de Marca", el "día de Lili antes/después", mapa de proceso para co-crear) deben estar listos el **lunes**. El martes es el verdadero primer hito político del proyecto.

---

## FASE 0 — Quick win + Diagnóstico ⭐

**Duración:** 2–3 semanas (incluye la prueba de factibilidad en la semana 1).
**Objetivo:** ganar credibilidad con un entregable **visible y tangible** en días, mientras levantamos la foto honesta del "cómo se trabaja hoy" y apagamos los supuestos frágiles. Es nuestro costo de adquisición del cliente: precio deliberadamente fácil de digerir (⚠️ del orden de ~1–1.5 meses de la temporal) a cambio de derechos de caso de referencia y referidos.

### 0.0 — Prueba de factibilidad (semana 1, pagada)
Cierra P2, P3, P4 y valida P1. Entregable: memo de 2 páginas que confirma o ajusta el alcance de las fases siguientes. **Sin esto no prometemos ninguna prioridad inmediata.**

### Entregables concretos

| Entregable | Descripción | ¿Quick win? |
|---|---|---|
| **⭐ Plantilla/procedimiento de CV con marca v1** | Convertir la instrucción que hoy usa Virginia en un activo de la firma: un esquema fijo (la IA ordena la información en un formato validado) + plantilla que siempre produce el mismo formato (la IA normaliza y redacta, NO diseña la página). Versionado, propiedad de la firma. Adoptado por los 4 reclutadores | **SÍ — visible** |
| **⭐ Control de duplicados / registro de a quién se presentó con cada cliente** | Chequeo de regla fija (no IA): consulta directa al sistema o, si el plan de Team Tailor no lo permite, hoja estructurada + regla obligatoria antes de enviar terna. Alerta de duplicado. Cierra un riesgo de reputación que ya ocurrió | **SÍ — emocional** |
| **Cortar la fuga de datos personales hacia el ChatGPT de consumo** | Mover la instrucción a un entorno donde el proveedor no entrena con los datos + acuerdo de protección de datos. Cierra una brecha legal **activa hoy**, a costo casi nulo | **SÍ — riesgo** |
| **Kit de experiencia del candidato v0** | Compromiso mínimo de comunicación (acuse en 48h, rechazo personalizado) + plantillas. **Se despliega ANTES de medir satisfacción** | SÍ — reputación |
| **Punto de partida medido (solo casos claros)** | Reconstruir, a partir del registro de actividad de Team Tailor, el tiempo hasta entregar la terna y el tiempo hasta cubrir la vacante por búsqueda + número de reenvíos. Reportar la mediana (p50) y el 10% más lento (p90), **solo donde el dato es confiable**, con advertencias explícitas donde las etapas son inconsistentes | SÍ — datos |
| **Diagnóstico del "cómo se criba hoy"** | Acompañar 45 min a los 4 reclutadores sobre 1 vacante real (mapa de quién hace qué en el paso 4). Determinar si las 4 formas difieren por **criterio** o solo por **formato** | — |
| **Mapa de actores + auto-registro de horas** | Postura de cada uno (Manuel incluido), palanca para sumarlos; 1 semana de registro de horas en cribado = el "antes" cuantificado | — |
| **Kit para la reunión del martes** | Descripción del rol *Embajador de Marca*, "día de Lili antes/después", mapa de proceso para co-crear | — (entregar **lunes**) |

### Precondiciones
- Acceso a Team Tailor (lectura) y a la instrucción que usa Virginia. Virginia (como patrocinadora) se compromete a adoptarlo públicamente ella primero.
- País confirmado (P1) para cortar la fuga de datos personales y publicar el aviso de privacidad.

### Dependencias
- La prueba de factibilidad (0.0) va antes de cualquier promesa de extracción. El punto de partida histórico **depende de P2**; si no se puede conectar ni descargar la información, se baja a muestreo manual y se comunica como tal.

### Métrica de éxito (seguir/parar hacia Fase 1)
**Fase 0 exitosa = (a) plantilla de CV adoptada por los 4 reclutadores + (b) control de duplicados operando, con ≥1 duplicado real detectado o evitado + (c) punto de partida de 3 indicadores (casos claros) entregado + (d) brecha de ChatGPT cerrada.** Si no se cumplen (a)+(b), **paramos antes de Fase 1.**

---

## FASE 1 — Estandarizar, documentar e instrumentar

**Duración:** 4–6 semanas.
**Objetivo:** convertir el conocimiento tácito (el "ojo clínico" de Virginia) en un **estándar explícito, medible y replicable**, y poner la base de datos en estructura. Esta es la fase de mayor valor real y el activo que ningún competidor con IA puede copiar sin la artesanía detrás. **El entregable más valioso de los primeros 60 días no tiene una sola línea de código.**

### Entregables concretos

| Entregable | Descripción |
|---|---|
| **Hoja de criterios de toma del mandato + procedimiento de cribado con criterios ponderados** | Co-diseñado en un taller con los 4 (que lo construyan = que lo adopten). Criterios, pesos, lo imprescindible vs lo deseable, anclas para evaluar, señales de descarte, definición de éxito a 90 días. Es el "deber ser" de los pasos 1–2 y 4 |
| **Etapas únicas en Team Tailor** | 6–8 etapas con criterios de entrada/salida (p.ej. terna = exactamente 3 finalistas validados), obligatorias para los 4. **Requisito duro** de cualquier medición del embudo de aquí en adelante |
| **Captura de mediciones nuevas (línea base hacia adelante)** | 6–8 campos obligatorios al abrir cada búsqueda (fecha de apertura, rango salarial, jefe que contrata, familia del rol, fuente, fecha de terna, fecha de oferta aceptada) |
| **Árbol de indicadores en 1 página** | Métrica guía: % de vacantes cubiertas dentro del compromiso de tiempo + colocaciones por reclutador. Ramas: velocidad, calidad, experiencia, activo/base, riesgo. Satisfacción con 1 pregunta (1–5), reportando siempre cuántas respuestas hubo; recomendación (NPS) solo con 30 o más respuestas. ⚠️ El tiempo hasta cubrir la vacante se reporta, **no** se promete (no lo controlan) |
| **Diccionario de datos + vocabulario común de habilidades y sectores (ESCO + capa local)** | Vocabulario estándar ANTES de enriquecer: habilidades, sectores, estados del candidato (vigente/en proceso/no vigente/no contactar). ESCO como esqueleto + una capa curada de 15–30 títulos centroamericanos. ⚠️ La curaduría local NO es gratis: es trabajo real |
| **Capa de extracción vía conexión técnica sobre Team Tailor (NO migrar)** | Base de datos propia (Postgres) + almacenamiento de los CVs. Sincronización incremental. **Solo si el plan de Team Tailor lo permite.** La decisión de salir del sistema de candidatos se pospone a Fase 3 |
| **Marco de gobierno de datos (registro de datos que exige la ley, versión ligera)** | Inventario de qué datos se tratan, con qué permiso para cada fin, cuánto se guardan y cuándo se borran, aviso de privacidad en el momento de aplicar, consentimiento separado por uso (reclutamiento / capacitación / estudios de salarios). **Acuerdo de protección de datos cliente–consultora**: al exportar datos personales pasamos a ser responsables de tratarlos; cifrado, control de accesos, borrado al cierre |
| **Puerta "Listo para IA" (checklist de 1 página)** | Lo que cada procedimiento debe aprobar antes de construir su asistente: entradas y salidas documentadas, criterios explícitos, datos estructurados, excepciones y a quién se escala, indicador + punto de partida, set de decisiones de referencia, límites claros de lo que NO debe hacer |

### Precondiciones
- Fase 0 superada. **Tiempo protegido de Lili (4–6 h/sem) para co-diseñar**, financiado al descargar su operación con la temporal. Disposición de Virginia a documentar su criterio (vale la pena retar este punto de frente).
- País y ley aplicable confirmados (P1, P3) para el gobierno de datos y la extracción.

### Dependencias
- El diccionario de datos va antes de cualquier enriquecimiento. Las etapas únicas van antes de tener mediciones limpias. El gobierno de datos va antes de tocar la base.

### Métrica de éxito (seguir/parar hacia Fase 2)
Hoja de criterios + procedimiento de cribado **en uso** por los 4 · etapas únicas aplicándose en ≥90% de búsquedas nuevas · diccionario de datos v1 aprobado · mediciones nuevas capturándose · puerta "Listo para IA" aprobada para el paso 4. **Si el procedimiento no se adopta, no se construye el asistente.**

---

## FASE 2 — IA asistida (copiloto, siempre con una persona validando)

**Duración:** 6–10 semanas, **modular por asistente**.
**Objetivo:** acelerar el proceso **ya estandarizado** sin escalar la inconsistencia. **No** se construyen los "6 agentes": de ellos, 5 son herramientas con salida estructurada y solo 1 (el que busca candidatos) es realmente autónomo. Se prueban **1–2** donde la ganancia es clara y el riesgo bajo.

### Reencuadre técnico
De "6 agentes" pasamos a **3 herramientas de regla fija + 1 coordinador que enruta con reglas fijas y siempre con persona validando.** Las reglas del cliente (los 10 mejores = llamada · del 10 al 20 = abierto · del 30 en adelante = rechazo cordial) se materializan **en código** (salida estructurada, lista permitida por paso), no como instrucción a la IA. La IA no puede "opinar fuera de su alcance" porque la arquitectura no se lo permite. **Esta barrera es el mejor mensaje para la adopción: "tú decides, la IA pre-ordena".**

### Entregables concretos

| Entregable | Descripción |
|---|---|
| **Herramienta de CV con marca, ya como producto** | Ordena la información a un esquema + plantilla de formato fijo. Riesgo nulo (no decide sobre personas), entregable visible. Evolución directa del quick win de Fase 0 |
| **Asistente que ordena candidatos según tus criterios** | Procesa así: **quitar datos personales** (foto/edad/estado civil/origen) → extraer evidencia contra la hoja de criterios → calificar con cita textual del CV (sin inventar) → ordenar. Construido **CON** Virginia sobre sus criterios + set de decisiones de referencia. La IA pre-ordena; **la persona aprueba los 10 mejores y la terna** |
| **Piloto de concordancia (con persona validando)** | En 1–2 búsquedas reales: la IA ordena, el reclutador valida por su cuenta; se mide "la IA coincidió en X de 10". Confianza por evidencia, no por fe. Regla: gana la persona, y se ajustan los criterios |
| **Auditoría de sesgo del asistente** | Tasa de selección por género/edad; se excluyen explícitamente las variables que disfrazan datos prohibidos; el resultado se documenta **antes** de usarlo en producción |
| **Entrevista previa por voz (transcripción comprada, no construida)** | Consentimiento de grabación → transcripción → resumen estructurado por esquema (competencias con cita, señales, preguntas de seguimiento). La IA no concluye si el candidato es apto |

### Precondiciones (puerta "Listo para IA" aprobada)
- Hoja de criterios + set de decisiones de referencia existentes y validados por Virginia (P4). Etapas únicas y punto de partida de Fase 1 operando. Acuerdos de protección de datos firmados con los proveedores de IA y de transcripción. Validación por persona configurada como obligatoria.

### Dependencias
- **Dependencia circular a romper (explícita):** liberar a Lili requiere la IA de cribado → que requiere el set de decisiones de referencia → que requiere tiempo de Virginia. **Se rompe** descargando la operación de Lili con la temporal (Fase 0–1) y **extrayendo el conocimiento de Virginia en las primeras 2–3 semanas** (para mitigar el riesgo de que renuncie), no al final.

### Métrica de éxito (seguir/parar hacia Fase 3)
Coincidencia IA–criterio de Virginia ≥ **X%** ⚠️ (umbral a fijar con ella sobre el set de decisiones de referencia) en 2 búsquedas reales · 0 rechazos automáticos sin revisión humana · auditoría de sesgo sin disparidad relevante · reducción medible del tiempo hasta entregar la terna vs el punto de partida (meta: 5 días → **48–72 h**, **no** "el mismo día"). **Si la IA no replica el criterio que el cliente reconoce como propio, no se escala.**

---

## FASE 3 — Orquestación, escala y monetización (empezar pequeño y crecer)

**Duración:** trimestral, modular, **se paga sola** con el valor ya demostrado.
**Objetivo:** convertir la base en un activo vivo y abrir nuevas líneas de ingreso, **estrictamente condicionadas a la base legal cerrada en Fase 1.** Aspiracional, no inmediata.

### Entregables concretos (todos opcionales, cada uno con su propia puerta)

| Entregable | Condición de activación |
|---|---|
| **Estructurar + enriquecer la base** (la IA ordena los CVs en campos, unifica registros de la misma persona, califica cuán vigente está, búsqueda inteligente) | Diccionario de datos y gobierno de Fase 1 cerrados. ⚠️ Procesar los CVs cuesta centavos de cómputo, pero **semanas de control de calidad, quitar duplicados y mapeo** — no subestimar |
| **Portal de auto-actualización del candidato (base interna)** | Permiso resuelto. Mantiene la base al día sin trabajo manual y resuelve el dolor de LinkedIn |
| **Decisión sobre el sistema de candidatos: potenciar vs migrar** | Con datos reales de los límites de la conexión técnica y del costo. **NO antes.** Migrar sin estructura replica el desorden en un sistema más caro y nos hace responsables de la seguridad y las brechas |
| **Buscador de candidatos autónomo** | Base estructurada + barreras validadas |
| **Estudio de salarios (benchmark)** | ⚠️ **Solo con dictamen legal favorable.** Requiere: contratos que permitan reutilizar los datos salariales, anonimización irreversible (un mínimo de casos por celda — en un mercado pequeño el "director financiero de la empresa X" se vuelve a identificar aunque esté agregado), y consentimiento separado. **Camino alternativo positivo:** aliarse con un proveedor que ya tiene la licencia de datos salariales. Puede estar muerto legalmente desde el inicio; no se ancla la propuesta en él |
| **Venta cruzada de capacitaciones a la base** | Consentimiento separado, con aceptación explícita. Reutilizar datos de reclutamiento para marketing sin permiso viola la regla de usar los datos solo para el fin con que se recogieron |

### Precondiciones
Base legal cerrada y rastreada hasta el origen · muestreo que confirme que la base está lo bastante vigente para justificar la inversión · números unitarios positivos demostrados.

### Métrica de éxito
% de vacantes cubiertas con base propia: de un punto de partida desconocido → **30–40% en 6–9 meses** ⚠️ · base vigente ≥50% ⚠️ · nueva línea de ingreso lanzada **solo** si pasó la puerta legal · decisión sobre el sistema de candidatos tomada con caso de negocio cuantificado.

---

## Economía del programa y asequibilidad (lo que la crítica exigió)

> **Honestidad sobre el dinero, no un menú sin precios.**

- **Precio de referencia que el cliente tiene en la cabeza:** ~US$1.5k–2.7k (3 meses de temporal). Competir contra ese número nos posiciona como mano de obra. **Reencuadre:** "una temporal añade capacidad por 3 meses y se va dejando el mismo desorden; nosotros instalamos estándar + datos + métricas que quedan y se suman."
- **El costo total de construir todo (Fases 0–3) supera con holgura el tope mental del cliente.** ⚠️ Por eso el **camino por defecto es comprar/activar lo existente**: encender la IA que Team Tailor ya cobra + procedimientos simples + control de duplicados en hoja o campo. Lo construido a medida (búsqueda inteligente, asistentes a la medida, transcripción por voz) se reserva **solo** si el volumen (⚠️ ¿20–60 colocaciones/año?) y el honorario por colocación lo justifican.
- **Plantilla de números unitarios (lista para enchufar el dato que falta):**
  `Recuperación de la inversión por fase = (honorario por colocación × colocaciones extra ganadas por más velocidad y más cobertura con base propia) − costo del sistema`
- **⚠️ Dato que bloquea todo cálculo de retorno:** honorario por colocación + volumen de búsquedas por mes. Primera pregunta de la reunión, no un detalle.
- **Validez estadística:** con 20–60 colocaciones/año, la recomendación (NPS), la precisión del asistente y la auditoría de sesgo tienen pocos casos. Reportar siempre conteos absolutos y cuántos casos hay; no montar maquinaria de datos pesada para un volumen que no da significancia.

### Cuadro de alternativas (para adelantarse a lo que Virginia ya piensa)

| Opción | Costo | Activo resultante | Riesgo |
|---|---|---|---|
| No hacer nada | $0 | Sigue el caos, sigue el daño en LinkedIn, sigue el riesgo de reenviar al mismo candidato | Erosión de reputación |
| Solo la temporal | ~$2.7k | Alivio de 3 meses, **cero capacidad instalada**, la dependencia vuelve en el mes 4 | Dinero evaporado |
| Firma grande | $$$ | Presentación genérica, sin cercanía al negocio | Caro, lento, sin apropiación |
| **Nosotros (este roadmap)** | Por fase, con decisión seguir/parar | Estándar + datos + métricas que quedan y se suman | Acotado por las puertas de decisión |

---

## Recursos y capacidad de entrega (ambos lados)

| Frente | Quién | Nota |
|---|---|---|
| Data/IA, arquitectura, métricas | Víctor (consultoría) | Núcleo de competencia |
| **Dominio RRHH / "deber ser"** | **Lili como co-autora obligatoria** | ⚠️ Víctor NO es de RRHH; un proceso diseñado sin Lili será rechazado por quienes lo ejecutan |
| **Legal / protección de datos / competencia** | **Subcontratar abogado local** | Reconocemos no tener esta competencia en casa. Sumarlo antes de cualquier producto de datos |
| Transcripción de voz en español regional | Comprar, no construir | — |
| Operación de Lili (descarga) | Temporal (3 meses) | Su pedido real + seguro contra renuncia. NO hace tareas de datos |

> ⚠️ **Choque de nombres a aclarar:** el consultor líder se llama Víctor y hay un reclutador "Víctor" en el cliente. Confirmar si son la misma persona (afecta el gobierno del proyecto y el conflicto de rol).

---

## Riesgos transversales y mitigaciones

| Riesgo | Severidad | Mitigación |
|---|---|---|
| **Renuncia de Lili por agotamiento (7am-7pm)** — es a la vez punto único de falla, impulsora del proyecto y cuello de botella | **Crítica** | Descargar su operación en semana 1; extraer su conocimiento en sem. 2–3; presentar la temporal como seguro de retención |
| Automatizar el desorden (presión propia por entregar IA vistosa) | Alta | La puerta "Listo para IA" no se negocia; el quick win es un procedimiento, no un asistente |
| La conexión técnica con Team Tailor no viene en el plan contratado | Alta | La prueba de factibilidad lo cierra antes de prometer; plan B = muestreo manual comunicado como tal |
| El set de decisiones de referencia no existe | Alta | Confirmar en la prueba; si no existe, financiar su creación explícitamente con tiempo de Virginia |
| El estudio de salarios = bomba legal (re-identificación, acuerdos de confidencialidad) | Alta | Fuera de la ruta crítica; condicionado a dictamen; camino positivo vía proveedor con licencia |
| Primer proyecto fallido = **anti-referencia** que nos hunde | Alta | Decisiones seguir/parar y criterios de corte por fase; alcance quirúrgico; no sobre-prometer |
| Discriminación algorítmica a escala | Alta | Quitar datos personales + auditoría de sesgo antes de producción; persona validando siempre |
| Continuidad del 63% de ingresos durante la transformación | Media | Regla "ninguna intervención toca una búsqueda en curso" |
| Estandarizar de más y matar el diferenciador (el oficio) | Media | Estandarizar el trabajo de trastienda; **preservar** el juicio humano en la terna, la negociación y la relación con el candidato |

---

## El reto a Virginia (con un SÍ, no con un muro de NOs)

La propuesta dice "todavía no" a casi todo lo que ella amó: "el mismo día", los 6 agentes, vender el estudio de salarios, salir del sistema de candidatos, la persona extra. Para que no se sienta sermoneada por un experto en datos sin credibilidad de dominio, el reencuadre es de **secuencia, no de negación**:

- *"Tu visión de clase mundial y cercanía es correcta. La estamos protegiendo: si automatizamos sobre el caos actual, escalamos la inconsistencia a velocidad de máquina y destruimos justo el 'ojo clínico' que te hace premium."*
- *"Tu diferenciador no será la IA — la disciplina de proceso lo será. La IA es la última milla, no la primera."*
- *"El pedido de Lili de 'una persona más' es la trampa elegante de no tocar el oficio: un quinto reclutador sin estándar solo añade una quinta forma de hacer las cosas. Le devolvemos sus 4 horas y la subimos de operativa a embajadora de marca."*
- *"El estudio de salarios es tu mayor oportunidad Y tu mayor riesgo: lo construimos bien, no rápido — o con un socio que ya tiene la licencia."*

---

## Próximos pasos inmediatos

1. **Lunes:** Virginia confirma el país (P1) y entrega los materiales para la reunión con Lili.
2. **Martes:** reunión Virginia–Lili — ganar a Lili como co-autora y embajadora (es un punto de fallo político, no logístico).
3. **Viernes:** presentar este roadmap + opciones de precio por fase + **un adelanto tangible** (un CV real reformateado con su marca + el concepto de control de duplicados). Mostrar, no prometer.
4. **Arranque:** prueba de factibilidad (1 semana) que apaga los 4 supuestos antes de comprometer alcance y precio de las Fases 1–3.

> ⚠️ **Datos a validar para cerrar cifras:** país; honorario por colocación y modelo de cobro; volumen de búsquedas por mes y colocaciones por año; plan y conexión técnica de Team Tailor; % de la base vigente y con permiso; existencia del set de decisiones de referencia; si el cliente devuelve retención a 90 días; presupuesto real más allá del tope mental de la temporal.
