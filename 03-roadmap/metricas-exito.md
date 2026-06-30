# Cómo medimos el éxito — Conexión Talento

**Proyecto:** Estandarización → Digitalización → IA para Reclutamiento y Selección
**Entregable:** Tablero de indicadores + Hoja de arranque (Semana 1)
**Preparado por:** [Consultora] · **Versión:** 1.0 · **Estado:** Borrador para validar con Virginia y Lilian

> **En una frase:** Pasamos de "no tenemos métricas" a un tablero honesto que mide la operación desde el primer lunes y se convierte en la prueba del retorno de cada fase. Lo que entregamos el viernes es el marco para medir, no promesas de cifras.

---

## 1. Para qué sirve y cómo está pensado

**El beneficio para el negocio:** este tablero convierte la operación de Conexión Talento en números por primera vez. Es la vara con la que demostraremos, fase por fase, que el dinero invertido rinde. No es un cuadro aspiracional: es honesto, accionable y defendible ante un cliente.

Está construido sobre seis principios. Varios **corrigen errores que detectó nuestra propia revisión crítica interna**:

1. **Medimos lo que sí controlamos.** Nuestro indicador estrella de velocidad es el **tiempo hasta entregar la terna** (los días desde que se abre la búsqueda hasta que el cliente recibe los 3 finalistas). El **tiempo hasta cubrir la vacante** (cierre) lo reportamos, pero **no lo prometemos**: depende de la decisión del cliente y del preaviso del candidato. El eslogan "5 días → mismo día" **sale del tablero**: sirve para vender, no es una meta medible que esté en nuestras manos.
2. **Metas sobre nuestro propio punto de partida, nunca cifras de industria.** Comprometemos *mejoras relativas* sobre el punto de partida que midamos nosotros, no números de mercado que no controlamos. Es la lógica de empezar pequeño y crecer: "medimos antes, mejoramos, lo demostramos".
3. **A volumen de boutique, la estadística manda.** Con ~20–60 colocaciones/año (⚠️ **dato a confirmar**), encuestas de recomendación y muchas tasas de embudo son puro ruido. Arrancamos con **satisfacción del cliente** (% de satisfechos + el número absoluto) y dejamos la métrica de recomendación para cuando haya 30 casos o más acumulados. **Siempre se reporta cuántos casos hay (el "n") al lado del número.**
4. **Medianas, no promedios.** Los tiempos se reportan como mediana y como el caso "casi peor" (el 90% de los casos por debajo de cierto valor). Con pocos casos, un promedio engaña.
5. **Reparar antes de medir.** La encuesta de satisfacción al **candidato** se lanza **después** de arreglar el compromiso de tiempo de respuesta. Encuestar a candidatos ya molestos (los que atacan en LinkedIn) generaría más reacción negativa, no información útil.
6. **Punto de partida con advertencias explícitas.** Los datos del sistema donde guardan los candidatos (Team Tailor) están contaminados: las etapas del proceso se usan de 4 formas distintas. Solo los **extremos** del proceso (apertura → terna → cierre) son confiables; los tiempos intermedios se marcan como "indicativos" hasta estandarizar etapas.

---

## 2. Condiciones que hay que cerrar ANTES de prometer cualquier indicador

> **El riesgo:** prometer metas sin estas condiciones cerradas sería repetir, en nuestro primer proyecto, el error que le señalamos al cliente. No son "preguntas abiertas": son **condiciones con responsable y fecha**. La mitad del valor de medir cuelga de ellas. Recomendamos una **prueba de factibilidad pagada de 1 semana** antes de comprometer metas.

| # | Condición | Por qué bloquea la medición | Responsable | Estado |
|---|-----------|------------------------------|-------------|--------|
| P1 | **País de operación** | Define qué ley de datos aplica y si es viable medir/almacenar datos personales y armar el comparativo de mercado | Virginia (email, 5 min) | ⚠️ Pendiente |
| P2 | **¿Team Tailor deja extraer su información? (plan contratado)** | Si no podemos descargar el historial de eventos, no hay punto de partida con datos pasados en semanas; habría que medir solo de hoy en adelante | Consultora (prueba) | ⚠️ Sin verificar |
| P3 | **Volumen real** (búsquedas/mes, colocaciones/año, clientes activos) | Define qué métricas tienen suficientes casos y cuáles son ruido | Virginia | ⚠️ Pendiente |
| P4 | **¿El cliente devuelve si el contratado siguió y rindió a los 90 días?** | Sin ese dato, el indicador de calidad de la contratación no existe; debe **quedar por escrito** en el plan a 90 días que ya entregan | Virginia + Legal | ⚠️ Pendiente |
| P5 | **% de la base con permiso y datos de menos de 12 meses** | Es la **base de cálculo** de la salud de la base y del % de vacantes cubiertas con base propia; hoy nadie lo sabe | Prueba (muestreo) | ⚠️ Pendiente |

**Regla de oro:** ningún indicador de este tablero se "promete" como meta firme el viernes hasta cerrar P1–P5. Lo que se entrega el viernes es **el marco de medición y la hoja de arranque**, no las metas absolutas.

---

## 3. Mapa de indicadores (1 página)

```
                    MÉTRICA GUÍA
   % de búsquedas cerradas dentro del tiempo comprometido
                            +
              Colocaciones por reclutador / mes
                            │
   ┌──────────────┬─────────┴───────┬──────────────┬──────────────┐
VELOCIDAD       CALIDAD         EXPERIENCIA      LA BASE COMO     RIESGO/
(la controlas)  (cruzada)       (diferenciador)  ACTIVO           CONTROL
   │              │                 │                │              │
- Tiempo a      - % terna →       - Satisfacción  - % base        - Candidatos
  entregar        entrevista        cliente          vigente         duplicados
  terna         - Aceptación      - Satisfacción  - % etiquetada  - % rechazos
- Tiempo a        de terna          candidato      - % vacantes      con revisión
  cubrir vac.   - Rotación 90d    - Tiempo 1er      cubiertas con    humana
  (reportar,    - Satisfacción      contacto         base propia
  no prometer)    cliente que     - Sin respuesta
                  contrata          (ghosting)
```

**Métrica guía:** combina volumen (colocaciones por reclutador) con cumplir lo prometido (% de búsquedas cerradas a tiempo). Evita premiar solo la velocidad, que empujaría a entregar ternas flojas.

---

## 4. Tablero detallado de indicadores

> **Fases:** **F0** Diagnóstico + Victoria rápida · **F1** Estandarización + Puntos de partida + Filtros de avance entre etapas · **F2** IA asistida (piloto) · **F3** La base como producto.
> Las metas son **rangos ilustrativos y conservadores sobre nuestro propio punto de partida**; se ajustan tras la prueba de factibilidad. ⚠️ = dato a confirmar.

### 4.1 Velocidad

| Indicador | Qué mide | Cómo se calcula | Cómo medir el punto de partida HOY (sin histórico) | Meta realista | Fase |
|-----------|----------|-----------------|-----------------------------------------------------|---------------|------|
| **Tiempo hasta entregar la terna** *(indicador estrella)* | Días hábiles desde que se abre la búsqueda hasta que el cliente recibe la terna | `fecha_entrega_terna − fecha_apertura` (mediana y caso casi peor) | **Con datos pasados (preferido):** descargar las fechas de las últimas 10–15 búsquedas cerradas del sistema — extremos confiables ⚠️ depende de P2. **Plan B:** registro manual en una hoja desde la Semana 1, anotando fecha de apertura y de terna por cada búsqueda nueva | Reducir la mediana propia **entre −30% y −50%** al cerrar F1 (ej. de 5 d → 48–72 h); meta ambiciosa porque la controlamos | F0 (medir) → F1 (meta) |
| **Tiempo hasta cubrir la vacante** *(reportar, no prometer)* | Días desde la apertura hasta la oferta aceptada | `fecha_oferta_aceptada − fecha_apertura` (mediana / caso casi peor) | Misma descarga de datos pasados (extremos confiables) o registro manual | **No se compromete meta** (depende del cliente y del candidato); se reporta la tendencia | F0 (medir) |
| **Tiempo hasta el primer candidato** | Días hasta presentar el **primer** candidato (señal temprana de que la búsqueda avanza) | `fecha_primer_candidato − fecha_apertura` | Registro manual desde la Semana 1 | Indicativo en F1, tras estandarizar etapas | F1 |

### 4.2 Calidad del candidato (no se mide directo: se cruza con 4 señales)

| Indicador | Qué mide | Cómo se calcula | Cómo medir el punto de partida HOY | Meta realista | Fase |
|-----------|----------|-----------------|-------------------------------------|---------------|------|
| **% terna → entrevista** | % de candidatos presentados que el cliente decide entrevistar | `# entrevistados por el cliente / # presentados` | Conteo con datos pasados del sistema ⚠️ P2; o registro manual por terna | Subir frente al punto de partida al introducir la hoja de criterios de arranque (F1) | F1 |
| **Aceptación de terna** | % de ternas en que el cliente avanza ≥1 finalista a entrevista/oferta | `# ternas con ≥1 avance / # ternas presentadas` | Conteo manual de las últimas 10–15 ternas (preguntando al equipo) + registro desde la Semana 1 | ⚠️ Punto de partida desconocido; subir tras estandarizar criterios | F1 |
| **Rotación / permanencia a 90 días** *(el indicador más vendible)* | % de colocados que dejan el puesto (o son reemplazados) en 90 días | `# bajas ≤90 d / # colocaciones` | **No hay histórico de seguimiento.** Arranque: (a) **dejar por escrito** la devolución del dato en el plan a 90 días que ya entregan (P4); (b) seguir desde la próxima colocación; (c) una llamada única a clientes por colocaciones de los últimos 6–12 meses | ⚠️ Punto de partida por construir; meta de **mantener la rotación a 90 días por debajo del punto de partida** una vez exista seguimiento | F1 (montar) → F2 (medir) |
| **Satisfacción del cliente que contrata** | Satisfacción con la calidad de la terna/colocación | % que responde 4–5 en escala 1–5 (+ n) | Encuesta de **1 pregunta** al cierre de cada proceso, desde la Semana 1 | % satisfechos ≥ punto de partida; pasar a métrica de recomendación con n≥30 | F1 |

> **Sobre "calidad":** ninguna señal aislada define la calidad. Se reporta el **conjunto** de las cuatro. La rotación a 90 días es la más valiosa para vender, pero **depende de que el cliente devuelva el dato** (P4): sin cláusula, este indicador no nace.

### 4.3 Experiencia (el diferenciador "cercanía al candidato", hecho medible)

| Indicador | Qué mide | Cómo se calcula | Cómo medir el punto de partida HOY | Meta realista | Fase |
|-----------|----------|-----------------|-------------------------------------|---------------|------|
| **Satisfacción del cliente** | Satisfacción con el servicio/proceso | % respuestas 4–5 (1–5) + n | 1 pregunta al cierre de cada búsqueda, **desde la Semana 1** | ⚠️ Punto de partida a establecer; sostener ≥ punto de partida | F1 |
| **Satisfacción del candidato** | Experiencia del candidato con el proceso | % respuestas 4–5 (1–5) + n | 1 pregunta al cierre del proceso — **SOLO tras arreglar el compromiso de tiempo de respuesta** (ver F0). Lanzarla antes = más reacción negativa | ⚠️ Punto de partida a establecer; mejorar a medida que se cierra el círculo de comunicación | F1 (tras el compromiso de respuesta) |
| **Recomendación (candidato / cliente)** | Recomendación neta | `% que recomienda − % que critica` | **Aplazado**: no se calcula hasta tener 30 casos o más acumulados; a volumen boutique un solo crítico mueve el índice ±10–20 puntos | Reportar con el n explícito cuando haya muestra; nunca como tendencia con pocos casos | F2+ |
| **Tiempo de primer contacto** | % de candidatos contactados dentro del plazo comprometido (ej. 48 h) | `# contactos ≤plazo / # candidatos en proceso` | Definir el plazo en F0; medir manualmente desde la Semana 1 | ≥90% dentro del plazo tras desplegar plantillas | F0 (definir) → F1 |
| **Candidatos sin respuesta (ghosting)** | % de candidatos que quedan sin respuesta ni cierre | `# candidatos sin aviso de cierre / total en proceso` | Revisión manual de procesos abiertos en el sistema | Tender a ~0% con plantillas de "sigues en proceso" / "cierre cordial" | F1 |

### 4.4 La base como activo (lo que multiplica la velocidad)

| Indicador | Qué mide | Cómo se calcula | Cómo medir el punto de partida HOY | Meta realista | Fase |
|-----------|----------|-----------------|-------------------------------------|---------------|------|
| **Salud / vigencia de la base** | Qué parte de los ~4.000 contactos es realmente útil | Conjunto: `% con email/teléfono válido`, `% con CV legible por máquina`, `% con actividad <12 m`, `% duplicados` | **Auditoría única**: descargar la base ⚠️ P2 + verificar que se puede contactar + cruzar identidades (email/teléfono/cédula) para **quitar duplicados**. Convierte el "4.000" en un número honesto de contactos vigentes (probablemente 1.500–2.500 ⚠️) | Fijar el número real de vigentes; luego ≥50% vigente con un protocolo de actualización | F0 (auditar) → F1 |
| **% base etiquetada** | % de candidatos clasificados por habilidad/sector (es decir, buscables) | `# perfiles etiquetados / # vigentes` | Piloto: etiquetar 300–500 CVs de **un** sector y medir cobertura | Por etapas; priorizar las familias de puesto más frecuentes | F1 → F2 |
| **% de vacantes cubiertas con base propia** | % de colocaciones servidas desde la base existente vs. buscar de cero | `# colocaciones desde base propia / # colocaciones totales` | **Hoy no se sabe la base de cálculo.** Arranque: campo obligatorio "fuente del candidato" en cada búsqueda desde la Semana 1 + estimación retroactiva preguntando al equipo por colocaciones recientes | ⚠️ Punto de partida desconocido → **30–40% en 6–9 meses** una vez la base esté etiquetada y vigente | F1 (registrar fuente) → F2 (meta) |

### 4.5 Riesgo y control

| Indicador | Qué mide | Cómo se calcula | Cómo medir el punto de partida HOY | Meta realista | Fase |
|-----------|----------|-----------------|-------------------------------------|---------------|------|
| **Candidatos duplicados** | Veces que el mismo candidato se presenta 2× al mismo cliente | `# incidentes / trimestre` | Punto de partida = el incidente que ya ocurrió (≥1). Poner un chequeo de duplicados antes de cada terna (hoja o campo en el sistema) desde la Semana 1 | **0 incidentes/trimestre** | F0 |
| **% de rechazos con revisión humana** | % de mensajes de rechazo validados por una persona antes de enviarse | `# rechazos revisados / # rechazos enviados` | Definir en F0; medir al activar el flujo | **100%** (siempre con una persona validando; nunca rechazo automático de los últimos de la lista sin revisión) | F2 |

---

## 5. Hoja de arranque mínima (Semana 1)

> **El beneficio:** empezar a medir el lunes, sin esperar a verificar la conexión técnica entre sistemas, sin construir infraestructura y sin recargar a un equipo que ya trabaja 60 h/semana. Una sola hoja de cálculo compartida + dos campos en el sistema. Todo lo demás espera.

### 5.1 Qué se monta en Semana 1 (y nada más)

**A. Hoja "Búsquedas" — una fila por cada búsqueda nueva:**

| Campo | A qué indicador alimenta |
|-------|---------------------------|
| Fecha de apertura de la búsqueda | Tiempo a entregar terna / a cubrir vacante |
| Cliente / persona que contrata | Aceptación de terna, satisfacción, duplicados |
| Familia de puesto y sector | Segmentación, base etiquetada |
| Fecha de entrega de la terna | Tiempo a entregar terna |
| Fecha de oferta aceptada | Tiempo a cubrir vacante |
| Fuente del candidato colocado (base propia / búsqueda nueva) | % vacantes cubiertas con base propia |
| Resultado de la terna (avanzó ≥1 a entrevista S/N) | Aceptación de terna |

**B. Chequeo de duplicados antes de la terna (regla obligatoria):** antes de enviar cualquier terna, verificar en el sistema si el candidato ya fue presentado a ese cliente. Contador de incidentes en la misma hoja. → *Victoria rápida de reputación, casi sin esfuerzo.*

**C. Satisfacción del cliente — 1 pregunta:** al cierre de cada proceso, "¿Qué tan satisfecho está con la terna/colocación? (1–5)". Anotar respuesta + fecha.

**D. Definir el compromiso de tiempo de primer contacto** (ej. acuse ≤48 h) y plantillas mínimas de comunicación al candidato. → *Habilita lanzar la encuesta al candidato más adelante sin generar reacción negativa.*

### 5.2 Qué NO va en Semana 1 (a propósito)

- ❌ Encuesta al **candidato** → hasta tener el compromiso de respuesta y las plantillas en marcha.
- ❌ Métrica de recomendación → hasta tener 30 casos o más.
- ❌ Extraer la información por conexión técnica, base de datos, procesar 4.000 CVs, búsqueda por significado → dependen de la prueba de factibilidad y de fases posteriores.
- ❌ Tiempos por etapa intermedia → hasta estandarizar los filtros de avance entre etapas (F1).

### 5.3 Lo que ve Virginia (vista del tablero)

| Indicador | Esta semana | Acumulado | n | Notas |
|-----------|-------------|-----------|---|-------|
| Tiempo a entregar terna (mediana, días) | — | — | — | Solo extremos confiables |
| Aceptación de terna (%) | — | — | — | |
| Satisfacción cliente (% 4–5) | — | — | — | Mostrar siempre el n |
| Incidentes de duplicado | — | — | — | Meta: 0 |
| % colocaciones desde base propia | — | — | — | Punto de partida en construcción |
| Salud de base (% vigente) | única vez | — | — | De la auditoría F0 |

> Un tablero de **una página** con estas seis líneas es lo que convierte, por primera vez, la operación de Conexión Talento en números — y es el ancla de credibilidad del primer proyecto.

---

## 6. Cómo se gobierna la medición

| Elemento | Definición |
|----------|------------|
| **Frecuencia** | Revisión semanal de 15 min (ritual de equipo); reporte ejecutivo mensual a Virginia |
| **Responsable del dato** | ⚠️ A nombrar. Candidata: la **asistente temporal**, reorientada de "apagar fuegos" a capturar métricas y mantener la base con nuestro método — así el presupuesto deja un activo permanente. **Condición:** no debe quitarle a Lilian el alivio operativo que pidió |
| **Definición única por indicador** | Cada métrica tiene responsable, fuente y una sola definición (ej. *terna = exactamente 3 finalistas validados*). Sin definiciones comunes, 4 personas miden de 4 formas |
| **Evitar trampas** | Nunca premiar solo la velocidad. El tiempo a entregar terna se equilibra con filtros de calidad (aceptación de terna, rotación 90 d, satisfacción). Atar bonos solo a velocidad empuja a ternas flojas |
| **Validez estadística** | A volumen boutique, reportar siempre el **n**; usar medianas; tratar las variaciones con pocos casos como ruido, no como tendencia |
| **Advertencia de datos sucios** | El punto de partida con datos pasados se entrega marcado "indicativo" en los tiempos intermedios; declarar el margen antes de fijar puntos de partida que luego serán vara de éxito |

---

## 7. Amarre a fases y criterios de seguir / no seguir

| Fase | Indicadores que se activan | Criterio de éxito (seguir / no seguir) — *números a ajustar tras la prueba* |
|------|----------------------------|------------------------------------------------------------------------------|
| **Prueba de factibilidad (Fase −1)** | Verificar P1–P5 | Confirmado que Team Tailor deja extraer la información · % de vigencia muestreado · país y permiso de datos confirmados · existe (o no) historial para el set de decisiones de referencia (los casos que enseñan a la IA a elegir como Virginia) |
| **F0 — Diagnóstico + Victoria rápida** | Punto de partida de tiempos a entregar/cubrir (extremos); duplicados; salud de base (auditoría); compromiso de respuesta definido | **Éxito =** punto de partida de ≥3 indicadores entregado + chequeo de duplicados operando (0 incidentes nuevos) + plantilla de CV adoptada por los 4. *Si no se cumple, se detiene antes de F1.* |
| **F1 — Estandarización + Puntos de partida** | Etapas estandarizadas; campos obligatorios de arranque; satisfacción cliente; % terna→entrevista; aceptación de terna; montaje del seguimiento de rotación 90 d; compromiso de contacto; satisfacción candidato (tras el compromiso) | **Éxito =** etapas únicas en uso por los 4 · mediana de tiempo a entregar terna **−30%** vs punto de partida propio · satisfacción cliente con n acumulado |
| **F2 — IA asistida (piloto)** | Rotación 90 d (seguimiento); % base etiquetada; % vacantes con base propia; % rechazos con revisión humana (100%); concordancia IA vs. "ojo clínico" | **Éxito =** vacantes cubiertas con base propia ≥30% · validada la concordancia del asistente que ordena candidatos · siempre una persona validando, al 100% en rechazos |
| **F3 — La base como producto** | Cobertura/representatividad del comparativo de mercado (mínimo de casos por celda); métricas de ingresos | **Condicionado a la base legal** (permiso detallado, anonimización irreversible, validación por país). No se mide ni se vende sin esto |

---

## 8. Supuestos y banderas (a confirmar)

- ⚠️ **Volumen** (~20–60 colocaciones/año): condiciona qué indicadores tienen significado estadístico. **Sin confirmar.**
- ⚠️ **Team Tailor deja extraer la información:** todo el punto de partida *con datos pasados* (semanas, no meses) cuelga de esto. **Sin verificar** → ya tenemos el plan B de registro manual en la hoja de arranque.
- ⚠️ **El cliente devuelve la permanencia a 90 días:** sin cláusula, el indicador de calidad de la contratación no existe.
- ⚠️ **% de base vigente:** base de cálculo desconocida de la salud de base y de las vacantes con base propia. **A muestrear en la prueba.**
- ⚠️ **Set de decisiones de referencia / historial de ternas:** se asume como insumo del futuro asistente que ordena candidatos (F2); sin documentación puede **no existir**. Construirlo consume tiempo escaso de Virginia. No es requisito de este tablero, pero sí del indicador de concordancia en F2.
- ⚠️ **Métricas de ingresos (comparativo de mercado):** fuera del camino crítico; con bandera legal abierta. No se promete como línea de ingreso medible hasta resolver permiso y anonimización por país.

> **Lo que entregamos el viernes no son metas absolutas: es el marco de medición, la hoja de arranque de la Semana 1 y las condiciones que cerramos en la prueba de factibilidad.** Prometer cifras de éxito antes de tener nuestro propio punto de partida sería repetir, en nuestro primer proyecto, el mismo error que le señalamos al cliente.
