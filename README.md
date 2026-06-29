# Conexión Talento — Memoria del Proyecto

**Estandarizar antes de automatizar · Activar el oro de la base · Demostrar valor con métricas**

> Repositorio de trabajo del engagement de Data & Analítica, IA y Transformación Digital para **Conexión Talento**. Este README es el punto de entrada: en 3 minutos da el reto, nuestra tesis, las apuestas y dónde está cada cosa.
>
> Estándar de calidad McKinsey/BCG. Documento vivo — la fuente de verdad del diagnóstico es [`01-descubrimiento/datos-clave.md`](./01-descubrimiento/datos-clave.md).

---

## 1. Resumen ejecutivo (léelo en 1 minuto)

**El reto.** Conexión Talento es una consultora boutique de headhunting (~10 personas, El Salvador primario + Guatemala secundario) cuyo motor es Reclutamiento y Selección (**63% de los ingresos**). Aspira a ser "consultora de clase mundial" con **cercanía al candidato** como diferenciador. Hoy opera con **cero estandarización** (4 reclutadores, 4 métodos), **cero documentación**, **cero métricas** y un ATS (Team Tailor) y una base de **~4.000 candidatos** subexplotados. La paradoja: vende "cercanía" mientras la atacan en LinkedIn por falta de seguimiento, y ya presentó dos veces el mismo candidato al mismo cliente. La CEO (Virginia, 20 años, "ojo clínico") visualiza **6 "agentes" de IA** y velocidad "mismo día"; pidió explícitamente que la **retemos**.

**Nuestra tesis central.** **No automatizar el desorden.** En una boutique que vive del criterio humano y la cercanía, el diferenciador **no es la IA, es la disciplina de proceso**. Por eso: **(1) estandarizar → digitalizar → DOCUMENTAR antes de automatizar**, y **(2) activar el "oro" de la base** — que hoy **no es oro, es oro sin refinar**: sin identidad única, sin etiquetas, sin protocolo de vigencia (probable 30–50% caduco ⚠️). El valor se materializa en la "plomería aburrida" (estándar, dedup, métricas, rúbrica), no en la autonomía vistosa.

**Las 4 apuestas mayores.**

| # | Apuesta | Por qué gana |
|---|---------|--------------|
| **A** | **Estandarizar el criterio antes que el código** — scorecard de intake, rúbrica explícita del "ojo clínico" de Virginia y plantilla única de CV con branding | Sin scorecard, ningún agente tiene criterio que aplicar; automatizar escala la inconsistencia a velocidad de máquina. Es lo que ningún competidor con IA copia sin la artesanía detrás. |
| **B** | **Métricas y líneas base desde la semana 1** — reconstruidas del event-log de Team Tailor, no inventadas | "Cero métricas" es falso: el ATS ya registra timestamps. Sin línea base **propia** no hay ROI demostrable ni precio premium defendible. Es el argumento *land-and-expand*. |
| **C** | **Activar la base SIN migrar el ATS todavía** — dedup + historial candidato-cliente, auditoría de vigencia y estructura; **augmentar Team Tailor por API antes de reemplazarlo** | Cierra el riesgo reputacional ya materializado y convierte "tenemos oro" en un número honesto. Migrar sin estructura replica el desorden en un sistema más caro y arriesga el 63% de los ingresos. |
| **D** | **IA asistida con humano-en-el-loop, sobre proceso ya estandarizado** — empezar por Screener/Ranker y Generador de CV; **congelar la venta del benchmark de compensaciones** | 5 de los 6 "agentes" son herramientas con salida estructurada, no agentes. El auto-rechazo (rank 30+) y el benchmark salarial son las dos bombas legales/reputacionales: requieren gate humano y validación legal. |

**El camino (fases flexibles, con puertas go/no-go).**

```
Fase -1  Spike de factibilidad (1 sem, pagado)  → apaga los supuestos frágiles ANTES de cotizar
Fase 0   Quick win + diagnóstico (2-3 sem)       → CV estándar, dedup, primeras métricas, credibilidad
Fase 1   Estandarización + datos + métricas      → SOPs, scorecards, líneas base, extracción por API
Fase 2   IA asistida (piloto 1-2 módulos)        → Screener/Ranker + Generador CV, con HITL y guardarraíles
Fase 3   Escala y monetización (condicionada)    → enriquecimiento de base, mercado interno, benchmark (si la ley lo permite)
```

**Cadena crítica (resuelve la tensión entre disciplinas):** estandarizar etapas y criterios → líneas base limpias → estructura de datos → recién entonces IA. No se automatiza ninguna etapa sin su estándar documentado y su línea base. Para romper el círculo "se necesita el ojo clínico documentado para construir la herramienta que lo documenta", el **golden set se extrae en las primeras 2-3 semanas** con tiempo protegido de Virginia.

---

## 2. Lo que NO vamos a hacer (y por qué — el reto que pediste)

| Lo que el cliente quiere ya | Nuestra postura | Razón |
|---|---|---|
| Los **6 agentes** de IA | Pilotar **1-2** sobre proceso estandarizado | Vender 6 agentes sin métricas ni documentación es vender humo en el primer proyecto. |
| Velocidad **"mismo día"** | Comprometer **time-to-submit** (lo que sí controlamos); enterrar "mismo día" | El cierre depende del cliente y del preaviso del candidato. Prometerlo siembra decepción. |
| **Vender el benchmark** de compensaciones | **Congelado** hasta validar base legal | Riesgo antitrust + protección de datos + re-identificación en mercado pequeño + posible violación de NDAs con los clientes que pagan el 63%. Camino positivo: alianza con proveedor licenciado. |
| **Salir del ATS** | **No migrar** aún; augmentar por API | Decisión de Fase 3 con datos, no por impulso. |
| **+1 persona** (pedido de Lili) | Redirigir el presupuesto de la temporal a **estructurar y documentar**, y reposicionar el rol como **"Embajador de Marca / Candidate Experience"** | El problema no es falta de manos, es falta de proceso. Un 5º reclutador sin estándar añade una 5ª forma de hacer las cosas. |

---

## 3. Guía de navegación del repositorio

| Carpeta | Qué contiene | Estado |
|---|---|---|
| [`00-memoria/`](./00-memoria) | **Bitácora viva** del proyecto: sesiones, decisiones, banderas y pendientes. La entrada más reciente va arriba. Empezar aquí para ponerse al día. | Activa |
| [`01-descubrimiento/`](./01-descubrimiento) | Insumos crudos y su interpretación: `transcripcion-llamada-01-raw.md` (verbatim) y **`datos-clave.md` (fuente de verdad** del diagnóstico, con supuestos marcados ⚠️). | Completa (Sesión 01) |
| [`02-solucion/`](./02-solucion) | Diseño de la solución: `arquitectura-solucion.md`, `estrategia-datos.md`, `riesgos-y-cumplimiento.md`. Los "6 agentes" reencuadrados, modelo de datos, y el registro legal (El Salvador / Decreto 144/2024). | Completa (v1) |
| [`03-roadmap/`](./03-roadmap) | `roadmap-fases.md` (fases, entregables, puertas go/no-go, kill-criteria) y `metricas-exito.md` (cuadro de KPIs + cómo capturar líneas base). | Completa (v1) |
| [`04-propuesta/`](./04-propuesta) | **Entregables del viernes:** `Propuesta-Conexion-Talento.pdf` (propuesta detallada, 16 pp.) + `Presentacion-Conexion-Talento.pptx` (deck ejecutivo, 17 slides). Fuente: `*.md` + `assets/` (CSS y generador). También `propuesta-comercial.md` (versión larga interna). | **PDF + PPTX listos** |
| [`99-research/`](./99-research) | Investigación de soporte. Ver [`99-research/README.md`](./99-research/README.md). Incluye: `team-tailor.md` (capacidades/API), `marco-legal-datos-sv-gt.md` (El Salvador + Guatemala), `benchmark-ia-rrhh.md` y `pricing-engagement.md`. | Completa (v1) |

**Convención:** las carpetas siguen el flujo del engagement (`00`→`04`), con `99-research` como anexo transversal. Todo dato no confirmado se marca `⚠️ a validar`.

---

## 4. Estado del proyecto

**Sesión actual:** 01 — Descubrimiento y diagnóstico (2026-06-29). Ver [`00-memoria/bitacora.md`](./00-memoria/bitacora.md).

**Hecho:** repositorio creado · transcripción y datos clave capturados · análisis multi-experto (8 lentes + crítica adversarial) · investigación de soporte (Team Tailor, marco legal SV/GT, benchmark IA-RRHH, pricing).

**Compromisos próximos:**

| Hito | Fecha | Entregable |
|---|---|---|
| **Reunión Virginia–Lili** | **Martes** | Kit de adopción listo el **lunes**: job description "Embajador de Marca", "día de Lili antes/después", mapa de proceso co-autorable con Lili. |
| **Propuesta al cliente** | **Viernes** | Documento *lean* por fases + opciones de pricing + cuadro de alternativas + **1 teaser tangible** (un CV real con branding + concepto de dedup). Mostrar, no prometer. |

**Precondiciones bloqueantes (cerrar en el Spike / Fase -1, no dejar "flotando"):**

| # | Precondición | Impacto si falla | Dueño |
|---|---|---|---|
| 1 | **País/jurisdicción** — confirmado El Salvador + Guatemala; falta validar consentimiento y registro | Define todo el marco legal y la viabilidad del benchmark | Víctor → Virginia |
| 2 | **API / export / tier de Team Tailor** sin verificar | Sostiene los quick wins P0 (extracción, dedup, baseline). Sin plan B, colapsa media Fase 0 | Spike técnico |
| 3 | **¿Existe golden set** (historial de quién entró a terna)? | El Screener no replica el "ojo clínico" sin él | Víctor + Virginia |
| 4 | **Fee por colocación y volumen/mes** | Sin esto no hay caso de ROI ni pricing defendible | Virginia |
| 5 | **Vigencia/consentimiento real** de los 4.000 | Dimensiona el "60% del valor" — hoy es supuesto | Muestreo en Spike |

**Banderas abiertas (autocrítica honesta):**
- ⚠️ **Economía y capacidad.** El ancla mental del cliente es ~3 meses de temporal (**~US$1.5k–2.7k ⚠️**); el roadmap completo es un programa de varios meses. **Antes de cotizar fases hay que sumar el costo total y hacer un chequeo de asequibilidad/ROI.** Si el *build* completo excede lo que una PYME de 10 personas puede financiar, recomendamos por defecto el **camino "BUY suficientemente bueno"** (activar la IA que Team Tailor ya cobra + SOPs livianos + dedup en hoja) y reservar el *build* custom solo si el volumen lo justifica con datos. Declaramos nuestro **conflicto de interés**: nuestro ingreso crece con cuanto más custom se construya; la integridad en el primer proyecto vale más que el tamaño del encargo.
- ⚠️ **Quién entrega.** Boutique, primer proyecto, líder no-RRHH y no-compliance. Falta plan de capacidad/subcontratación (legal local, ASR) y nombrar dueño interno del cambio.
- ⚠️ **Continuidad operativa.** Ninguna intervención de Fase 1 toca un mandato en vuelo: el 63% de los ingresos debe seguir fluyendo. **Riesgo de fuga de Lili** (7am–7pm) tratado como amenaza de attrition; la temporal es también seguro de retención.
- ⚠️ **Validez estadística.** A 20–60 colocaciones/año, NPS y auditorías de sesgo tienen *n* limitado: usar CSAT (% satisfechos + conteo) y reportar siempre el *n*.

---

*Última actualización: 2026-06-29 · Sesión 01. Mantener este README sincronizado con la bitácora.*
