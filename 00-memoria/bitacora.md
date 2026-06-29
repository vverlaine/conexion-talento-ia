# Bitácora del proyecto — Conexión Talento

Registro vivo de sesiones, decisiones y pendientes. La entrada más reciente va arriba.

---

## Sesión 01 — 2026-06-29 — Descubrimiento y diagnóstico inicial

**Participaron:** Víctor (consultor). Fuente: transcripción de la llamada de descubrimiento con Virginia (CEO).

**Qué se hizo:**
- Se creó el repositorio de la memoria del proyecto (`conexion-talento-ia`).
- Se guardó la transcripción verbatim y la extracción de datos clave (`01-descubrimiento/`).
- Se ejecutó un análisis multi-experto (8 lentes + crítica adversarial + síntesis) que generó los
  documentos base de diagnóstico, dolores, oportunidades, solución, datos, riesgos, métricas, roadmap y propuesta.

**Decisiones tomadas:**
- **Tesis central:** *estandarizar y documentar antes de automatizar* + *activar el "oro" de la base de 4000 candidatos*.
- Estructura del engagement por **fases flexibles** (Fase 0 quick win → 1 procesos+datos → 2 IA asistida → 3 escala/monetización).
- Establecer **líneas base de métricas desde la semana 1** (el cliente hoy no mide nada).

**Hallazgos de investigación (deep-research, integrados):**
- **Jurisdicción confirmada:** El Salvador (primario) + Guatemala (secundario). **El Salvador YA tiene Ley de Protección de Datos Personales vigente (Decreto 144/2024)** → Conexión Talento es sujeto obligado hoy. Guatemala sin ley general aún.
- **Team Tailor:** base extraíble por **API REST (key Admin/Read)**; el "Co-pilot" de IA **no hace búsqueda semántica transversal** → estrategia **augmentar, no reemplazar**. *Descarga masiva de CVs por API NO confirmada — probar con cuenta real.*
- **Pricing:** fixed-fee por fase; arranque Fases 0–2 **~USD 13–33k** (alineado a benchmark LATAM USD 14–36k).
- **Benchmark IA-RRHH:** patrón replicable = cribado/matching semántico (Claude + RAG) con humano-en-el-bucle.
- Detalle y fuentes en [`99-research/`](../99-research/README.md). La **crítica adversarial interna** quedó en [`critica-adversarial.md`](./critica-adversarial.md).

**Reconciliación hecha:** propuesta actualizada con jurisdicción + hecho legal SV + **3 modelos de pricing con cifras**; `riesgos §5.1` corregido (el dato viejo "El Salvador laxo" era falso); README con carpetas marcadas completas.

**Banderas vivas (para no perder de vista):**
- ⚠️ Benchmark de compensaciones: solo lícito **anonimizado irreversible + agregado (k-anonimato)** y con **dictamen de abogado salvadoreño**. Congelado hasta entonces.
- ⚠️ No precipitar la salida de Team Tailor; augmentar por API primero.
- ⚠️ Riesgo de adopción: reclutadora que insiste en leer 200 CVs; cada quien con su método.
- ⚠️ Economía vs ancla del cliente (~USD 1.5–2.7k de la temporal): vender por fases autofinanciadas; declarar conflicto de interés build-vs-buy.

**Pendientes / próximos pasos:**
- [ ] Pedir a Virginia **acceso de solo-lectura / export de muestra de Team Tailor** → probar API + mini-demo de búsqueda semántica para el viernes.
- [ ] Conseguir **fee por colocación + volumen de mandatos/mes** (para el caso de ROI). Conversación del martes.
- [ ] Validar oficialmente **consentimiento de la base** y posible exposición UE.
- [ ] **Dictamen de abogado salvadoreño** antes de cualquier benchmark.
- [ ] Pulir cifras de pricing con tarifa local; **propuesta final el viernes**.
- [ ] Preparar el **kit para la reunión del martes** con Lili (JD "Embajador de Marca", "día de Lili antes/después", mapa de proceso co-autorable) — listo el lunes.

---
