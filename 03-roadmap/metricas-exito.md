# Cuadro de Métricas de Éxito — Conexión Talento

**Proyecto:** Estandarización → Digitalización → IA para Reclutamiento y Selección
**Entregable:** Cuadro de mando de KPIs + Tablero de arranque (Semana 1)
**Preparado por:** [Consultora] · **Versión:** 1.0 · **Estado:** Borrador para validación con Virginia y Lilian

---

## 1. Propósito y principios de diseño

Este cuadro de mando convierte el "no tenemos métricas" en un sistema de medición **honesto, accionable y defendible** desde la primera semana. No es un tablero aspiracional: es la vara contra la cual se demostrará el ROI de cada fase del proyecto.

Está construido sobre seis principios, varios de los cuales **corrigen errores que detectó nuestra propia revisión adversarial**:

1. **Medimos lo que controlamos como titular.** *Time-to-submit* (entrega de terna) es nuestro KPI estrella de velocidad; *time-to-fill* (cierre) lo reportamos pero **no lo prometemos**, porque depende de la decisión del cliente y del preaviso del candidato. El "5 días → mismo día" **se retira** del cuadro de KPIs: es narrativa de venta, no una meta medible y controlable.
2. **Metas sobre línea base propia, nunca cifras absolutas.** Comprometemos *mejoras relativas* sobre el baseline que levantemos, no números de industria que no controlamos. Es el argumento land-and-expand: "medimos antes, mejoramos, lo demostramos".
3. **A volumen de boutique, la estadística manda.** Con ~20–60 colocaciones/año (⚠️ **supuesto a validar**), el NPS y muchas tasas de embudo son ruido. Arrancamos con **CSAT** (% de satisfechos + conteo absoluto) y reservamos NPS para n≥30 acumulado. **Siempre se reporta el n al lado del número.**
4. **Percentiles, no promedios.** Los tiempos se reportan en p50/p90; un promedio con n pequeño miente.
5. **Reparar antes de medir.** El CSAT al **candidato** se lanza **después** de arreglar el SLA de comunicación; encuestar a candidatos ya molestos (los que atacan en LinkedIn) provocaría más backlash, no señal.
6. **Línea base con caveats explícitos.** Los datos del ATS están contaminados por etapas usadas de 4 formas distintas. Solo los **extremos** del proceso (apertura → terna → cierre) son confiables; los tiempos intermedios se etiquetan "indicativo" hasta estandarizar etapas.

---

## 2. Precondiciones bloqueantes (cierran ANTES de prometer cualquier KPI)

> Estas no son "preguntas abiertas": son **precondiciones con dueño y fecha**. La mitad del valor de medición cuelga de ellas. Recomendamos un **Spike de Factibilidad pagado de 1 semana** antes de comprometer metas.

| # | Precondición | Por qué bloquea la medición | Dueño | Estado |
|---|--------------|------------------------------|--------|--------|
| P1 | **País de operación** | Define ley de datos, viabilidad de medir/almacenar PII y del benchmark | Virginia (email, 5 min) | ⚠️ Pendiente |
| P2 | **API / export / tier de Team Tailor** | Sin export del event log, la línea base retrospectiva no es viable en semanas; habría que medir solo hacia adelante | Consultora (spike) | ⚠️ No verificado |
| P3 | **Volumen real** (mandatos/mes, colocaciones/año, clientes activos) | Define qué métricas tienen n suficiente y cuáles son ruido | Virginia | ⚠️ Pendiente |
| P4 | **¿El cliente devuelve retención/desempeño a 90 días?** | Sin esto, el KPI de calidad de contratación muere; debe **clausularse** en el plan a 90 días que ya entregan | Virginia + Legal | ⚠️ Pendiente |
| P5 | **% de la base con consentimiento y datos <12 meses** | Es el **denominador** de la salud de base y del % de cobertura interna; hoy nadie lo sabe | Spike (muestreo) | ⚠️ Pendiente |

**Regla de oro:** ningún KPI de este cuadro se "promete" como meta firme el viernes hasta que P1–P5 estén cerradas. Lo que se entrega el viernes es **el marco de medición y el tablero de arranque**, no las metas absolutas.

---

## 3. Árbol de métricas (1 página)

```
                    NORTH STAR
        Fill rate dentro de SLA (% de mandatos cerrados a tiempo)
                            +
              Colocaciones por reclutador / mes
                            │
   ┌──────────────┬─────────┴───────┬──────────────┬──────────────┐
VELOCIDAD       CALIDAD         EXPERIENCIA      ACTIVO/BASE      RIESGO/
(controlable)  (triangulada)   (diferenciador)  (apalancamiento) CONTROL
   │              │                 │                │              │
- Time-to-      - Submit-to-      - CSAT cliente   - % base        - Incidentes
  submit          interview       - CSAT candidato   vigente         de duplicado
- Time-to-fill  - Aceptación      - SLA 1er        - % etiquetada  - % rechazos
  (reportar,      de terna          contacto       - % cobertura     con revisión
  no prometer)  - Rotación 90d    - Ghosting rate    interna          humana
                - CSAT hiring                        (internal-fill)
                  manager
```

**North Star:** combina volumen (colocaciones/reclutador) con cumplimiento de promesa (fill rate dentro de SLA). Evita premiar velocidad aislada, que incentivaría ternas flojas.

---

## 4. Cuadro de mando detallado de KPIs

> **Leyenda de fase:** **F0** Diagnóstico + Quick Win · **F1** Estandarización + Líneas base + Stage-gates · **F2** IA asistida (piloto) · **F3** Base como producto.
> Las metas son **rangos ilustrativos conservadores sobre baseline propio**; se calibran tras el spike. ⚠️ = supuesto a validar.

### 4.1 Velocidad

| KPI | Definición | Fórmula | Cómo capturar la línea base HOY (sin histórico) | Meta realista | Fase |
|-----|------------|---------|--------------------------------------------------|---------------|------|
| **Time-to-submit** *(KPI estrella)* | Días hábiles desde apertura del mandato hasta entrega de la terna al cliente | `fecha_entrega_terna − fecha_apertura_mandato` (p50 y p90) | **Retrospectivo (preferido):** exportar timestamps de los últimos 10–15 mandatos cerrados del ATS — extremos confiables ⚠️ depende de P2. **Fallback:** registro manual prospectivo en hoja desde Semana 1, fecha de apertura y de terna por mandato nuevo | Reducir el p50 propio **−30% a −50%** al cerrar F1 (ej. de 5 d → 48–72 h); meta agresiva por ser controlable | F0 (baseline) → F1 (meta) |
| **Time-to-fill** *(reportar, no prometer)* | Días desde apertura hasta oferta aceptada | `fecha_oferta_aceptada − fecha_apertura_mandato` (p50/p90) | Mismo export retrospectivo (extremos confiables) o registro manual prospectivo | **No se compromete meta absoluta** (depende del cliente y del candidato); se reporta tendencia | F0 (baseline) |
| **Time-to-first-submit** | Días hasta el **primer** candidato presentado (señal temprana de tracción del sourcing) | `fecha_primer_candidato − fecha_apertura` | Registro manual prospectivo desde Semana 1 | Indicativo en F1 tras estandarizar etapas | F1 |

### 4.2 Calidad del candidato (no se mide directo: se triangula con 4 proxies)

| KPI | Definición | Fórmula | Cómo capturar la línea base HOY | Meta realista | Fase |
|-----|------------|---------|----------------------------------|---------------|------|
| **Submit-to-interview rate** | % de candidatos presentados que el cliente decide entrevistar | `# candidatos entrevistados por cliente / # candidatos presentados` | Conteo retrospectivo del ATS sobre últimos mandatos ⚠️ P2; o registro manual por terna | Subir vs baseline propio al introducir scorecard de intake (F1) | F1 |
| **Tasa de aceptación de terna** | % de ternas en que el cliente avanza ≥1 finalista a entrevista/oferta | `# ternas con ≥1 avance / # ternas presentadas` | Conteo manual sobre las últimas 10–15 ternas (preguntar al equipo) + prospectivo desde Semana 1 | ⚠️ Baseline desconocido; subir tras intake/scorecard estandarizado | F1 |
| **Rotación / retención a 90 días** *(el KPI más vendible)* | % de colocados que dejan el puesto (o son reemplazados) dentro de 90 días | `# bajas ≤90 d / # colocaciones` | **No existe histórico de seguimiento.** Arranque: (a) **clausular** la devolución del dato en el plan a 90 días que ya entregan (P4); (b) cohorte prospectiva desde la próxima colocación; (c) llamada one-time a clientes por colocaciones de los últimos 6–12 meses | ⚠️ Baseline a construir; meta de **mantener rotación 90 d por debajo del baseline** una vez exista cohorte | F1 (instrumentar) → F2 (medir) |
| **CSAT del hiring manager** | Satisfacción del cliente con la calidad de la terna/colocación | % que responde 4–5 en escala 1–5 (+ n) | Encuesta de **1 pregunta** al cierre de cada proceso, desde Semana 1 | % satisfechos ≥ baseline; migrar a NPS con n≥30 | F1 |

> **Nota sobre "calidad":** ningún proxy aislado define calidad. Se reporta el **conjunto** de los cuatro. La rotación a 90 días es el más valioso comercialmente, pero **depende de que el cliente devuelva el dato** (P4): sin cláusula, este indicador no nace.

### 4.3 Experiencia (el diferenciador "cercanía al candidato", hecho medible)

| KPI | Definición | Fórmula | Cómo capturar la línea base HOY | Meta realista | Fase |
|-----|------------|---------|----------------------------------|---------------|------|
| **CSAT cliente** | Satisfacción del cliente con el servicio/proceso | % respuestas 4–5 (1–5) + n | 1 pregunta al cierre de cada mandato, **desde Semana 1** | ⚠️ Baseline a establecer; sostener ≥ baseline | F1 |
| **CSAT candidato** | Experiencia del candidato con el proceso | % respuestas 4–5 (1–5) + n | 1 pregunta al cierre del proceso — **SOLO tras arreglar el SLA de comunicación** (ver F0). Lanzar antes = más backlash | ⚠️ Baseline a establecer; mejorar conforme se cierra el loop | F1 (post-SLA) |
| **NPS candidato / cliente** | Recomendación neta | `% promotores − % detractores` | **Diferido**: no se calcula hasta n≥30 acumulado; a volumen boutique un detractor mueve el índice ±10–20 pts | Reportar con n explícito cuando haya muestra; nunca como tendencia con n bajo | F2+ |
| **SLA de 1er contacto** | % de candidatos contactados dentro del SLA definido (ej. 48 h) | `# contactos ≤SLA / # candidatos en proceso` | Definir SLA en F0; medir manualmente desde Semana 1 | ≥90% dentro de SLA tras desplegar plantillas | F0 (definir) → F1 |
| **Ghosting rate** | % de candidatos que quedan sin respuesta/cierre | `# candidatos sin notificación de cierre / total en proceso` | Auditoría manual de procesos abiertos en el ATS | Tender a ~0% con plantillas de "sigues en proceso" / "cierre cordial" | F1 |

### 4.4 La base como activo (apalancamiento de velocidad)

| KPI | Definición | Fórmula | Cómo capturar la línea base HOY | Meta realista | Fase |
|-----|------------|---------|----------------------------------|---------------|------|
| **Salud / vigencia de la base** | Qué porción de los ~4.000 es realmente útil | Conjunto: `% con email/teléfono válido`, `% con CV parseable`, `% con última actividad <12 m`, `% duplicados` | **Auditoría one-time**: export de la base ⚠️ P2 + validación de contactabilidad + resolución de identidad (email/teléfono/cédula). Convierte "4.000" en un número honesto de vigentes (probablemente 1.500–2.500 ⚠️) | Establecer el denominador real; luego ≥50% vigente vía protocolo de actualización | F0 (auditar) → F1 |
| **% base etiquetada** | % de candidatos clasificados por skill/sector (buscables) | `# perfiles etiquetados / # vigentes` | Piloto: etiquetar 300–500 CVs de **un** sector y medir cobertura | Escalonado; priorizar familias de puesto del Pareto | F1 → F2 |
| **% de cobertura desde base interna (internal-fill rate)** | % de colocaciones servidas desde la base existente vs. sourcing nuevo | `# colocaciones desde base interna / # colocaciones totales` | **Denominador hoy desconocido.** Arranque: campo obligatorio "fuente del candidato" en cada mandato desde Semana 1 + estimación retroactiva preguntando al equipo por colocaciones recientes | ⚠️ Baseline desconocido → **30–40% en 6–9 meses** una vez la base esté etiquetada y vigente | F1 (instrumentar fuente) → F2 (meta) |

### 4.5 Riesgo y control

| KPI | Definición | Fórmula | Cómo capturar la línea base HOY | Meta realista | Fase |
|-----|------------|---------|----------------------------------|---------------|------|
| **Incidentes de candidato duplicado** | Veces que el mismo candidato se presenta 2× al mismo cliente | `# incidentes / trimestre` | Línea base = el incidente ya ocurrido (≥1). Implementar check de dedup pre-terna (hoja o campo ATS) desde Semana 1 | **0 incidentes/trimestre** | F0 |
| **% de rechazos con revisión humana** | % de comunicaciones de rechazo validadas por un humano antes de enviarse | `# rechazos revisados / # rechazos enviados` | Definir en F0; medir al activar el flujo | **100%** (HITL obligatorio; nunca auto-rechazo en rank 30+ sin revisión) | F2 |

---

## 5. Tablero de arranque mínimo (Semana 1)

> Objetivo: **empezar a medir el lunes**, sin esperar a verificar la API, sin construir infraestructura y sin sobrecargar a un equipo a 60 h/semana. Una sola hoja de cálculo compartida + dos campos en el ATS. Todo lo demás espera.

### 5.1 Qué se instrumenta en Semana 1 (y nada más)

**A. Hoja "Mandatos" — captura prospectiva (una fila por mandato nuevo):**

| Campo | Para qué KPI alimenta |
|-------|------------------------|
| Fecha apertura del mandato | Time-to-submit / time-to-fill |
| Cliente / hiring manager | Aceptación de terna, CSAT, dedup |
| Familia de rol y sector | Segmentación, base etiquetada |
| Fecha de entrega de terna | Time-to-submit |
| Fecha de oferta aceptada | Time-to-fill |
| Fuente del candidato colocado (base interna / sourcing nuevo) | % cobertura interna |
| Resultado de terna (avanzó ≥1 a entrevista S/N) | Aceptación de terna |

**B. Check de dedup pre-terna (regla obligatoria):** antes de enviar cualquier terna, verificar contra el ATS si el candidato ya fue presentado a ese cliente. Contador de incidentes en la misma hoja. → *Quick win reputacional de esfuerzo casi nulo.*

**C. CSAT cliente — 1 pregunta:** al cierre de cada proceso, "¿Qué tan satisfecho está con la terna/colocación? (1–5)". Registrar respuesta + fecha.

**D. Definición del SLA de 1er contacto** (ej. acuse ≤48 h) y plantillas mínimas de comunicación al candidato. → *Habilita lanzar el CSAT al candidato más adelante sin generar backlash.*

### 5.2 Qué NO va en Semana 1 (deliberadamente)

- ❌ CSAT/encuesta al **candidato** → hasta tener el SLA y las plantillas desplegadas.
- ❌ NPS → hasta n≥30.
- ❌ Extracción por API, Postgres, parseo de 4.000 CVs, embeddings → dependen del spike y de fases posteriores.
- ❌ Tiempos por etapa intermedia → hasta estandarizar stage-gates (F1).

### 5.3 Vista del tablero (lo que ve Virginia)

| Indicador | Esta semana | Acumulado | n | Notas |
|-----------|-------------|-----------|---|-------|
| Time-to-submit (p50, días) | — | — | — | Solo extremos confiables |
| Aceptación de terna (%) | — | — | — | |
| CSAT cliente (% 4–5) | — | — | — | Mostrar siempre n |
| Incidentes de duplicado | — | — | — | Meta: 0 |
| % colocaciones desde base interna | — | — | — | Baseline en construcción |
| Salud de base (% vigente) | one-time | — | — | De la auditoría F0 |

> Un dashboard de **una página** con estos seis renglones es lo que convierte, por primera vez, la operación de Conexión Talento en números — y es el ancla de credibilidad del primer proyecto.

---

## 6. Gobernanza de la medición

| Elemento | Definición |
|----------|------------|
| **Cadencia** | Revisión semanal de 15 min (ritual de equipo); reporte ejecutivo mensual a Virginia |
| **Dueño del dato (data steward)** | ⚠️ A nombrar. Candidata: la **asistente temporal**, redirigida de "tapar fuegos" a capturar métricas y mantener la base bajo nuestro método — así el presupuesto deja un activo permanente. **Condición:** no debe restarle a Lilian el alivio operativo que pidió |
| **Definición operativa por KPI** | Cada métrica tiene dueño, fuente y definición única (ej. *terna = exactamente 3 finalistas validados*). Sin definiciones comunes, 4 personas miden de 4 formas |
| **Anti-gaming** | Nunca premiar velocidad aislada. Time-to-submit se balancea con quality gates (aceptación de terna, rotación 90 d, CSAT). Atar bonos solo a velocidad incentiva ternas flojas |
| **Validez estadística** | A volumen boutique, reportar siempre el **n**; usar percentiles; tratar variaciones de bajo n como ruido, no como tendencia |
| **Caveats de datos sucios** | La línea base retrospectiva se entrega etiquetada "indicativo" en tiempos intermedios; declarar el margen antes de fijar baselines que luego sean vara de éxito |

---

## 7. Amarre a fases y criterios go/no-go

| Fase | KPIs que se activan | Criterio de éxito (go/no-go) — *números a calibrar tras spike* |
|------|---------------------|------------------------------------------------------------------|
| **Spike (Fase −1)** | Verificación de P1–P5 | API/export de TT confirmado · % vigencia muestreado · país y consentimiento confirmados · existe (o no) historial para golden set |
| **F0 — Diagnóstico + Quick Win** | Baseline time-to-submit/fill (extremos); incidentes de duplicado; salud de base (auditoría); SLA definido | **Éxito = ** baseline de ≥3 KPIs entregado + check de dedup operando (0 nuevos incidentes) + plantilla de CV adoptada por los 4. *Si no se cumple, se detiene antes de F1.* |
| **F1 — Estandarización + Líneas base** | Stage-gates estandarizados; campos obligatorios de intake; CSAT cliente; submit-to-interview; aceptación de terna; instrumentación de rotación 90 d; SLA de contacto; CSAT candidato (post-SLA) | **Éxito = ** etapas únicas en uso por los 4 · time-to-submit p50 **−30%** vs baseline propio · CSAT cliente con n acumulado |
| **F2 — IA asistida (piloto)** | Rotación 90 d (cohorte); % base etiquetada; internal-fill rate; % rechazos con revisión humana (100%); concordancia IA vs. "ojo clínico" | **Éxito = ** internal-fill ≥30% · concordancia del ranker validada · HITL al 100% en rechazos |
| **F3 — Base como producto** | Cobertura/representatividad del benchmark (n mínimo por celda); métricas de monetización | **Condicionado a base legal** (consentimiento granular, anonimización, validación por país). No se mide ni se vende sin esto |

---

## 8. Supuestos y banderas (a validar)

- ⚠️ **Volumen** (~20–60 colocaciones/año): condiciona qué KPIs tienen significancia. **Sin confirmar.**
- ⚠️ **API/export de Team Tailor:** toda la línea base *retrospectiva* (semanas, no meses) cuelga de esto. **No verificado** → fallback de captura prospectiva manual ya contemplado en el tablero de arranque.
- ⚠️ **Devolución de retención a 90 días por el cliente:** sin cláusula, el KPI de calidad de contratación no existe.
- ⚠️ **% de base vigente:** denominador desconocido de salud de base e internal-fill. **A muestrear en el spike.**
- ⚠️ **Golden set / historial de ternas:** asumido como insumo del futuro ranker (F2); con cero documentación puede **no existir**. Construirlo consume tiempo escaso de Virginia. No es prerequisito de este cuadro de mando, pero sí del KPI de concordancia en F2.
- ⚠️ **Métricas de monetización (benchmark):** fuera del camino crítico; bandera legal abierta. No se promete como línea de ingreso medible hasta resolver consentimiento y anonimización por país.

> **Lo que entregamos el viernes no son metas absolutas: es el marco de medición, el tablero de arranque de Semana 1 y las precondiciones que cerramos en el spike.** Prometer cifras de éxito antes de tener línea base propia sería repetir, en nuestro primer proyecto, el mismo error que le señalamos al cliente.
