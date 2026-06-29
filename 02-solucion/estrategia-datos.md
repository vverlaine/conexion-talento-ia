# Estrategia de datos — Conexión Talento

**Documento entregable · Memoria del proyecto · Fase: Descubrimiento**
*De cómo convertir 4.000 registros estáticos en un activo de talento vivo, buscable y defendible — sin precipitarse, sin sobre-construir, y sin tocar el 63% de los ingresos que financian todo.*

---

## 1. Síntesis ejecutiva

**Tesis central (que retamos al cliente y a nosotros mismos):** la base de 4.000 candidatos **no es "oro" todavía**. Hoy es un activo de bajo rendimiento: sin clave de identidad única, con duplicados, vencido en un **30–50% ⚠️ (a medir, no a suponer)** y sin estructura. El "~60% del valor" que intuye Virginia es **potencial condicionado**, no un hecho. Su valor no está en el volumen ni en ponerle embeddings encima (lo vistoso); está condicionado a tres cosas aburridas y baratas: **(1) una clave de identidad única, (2) deduplicación con línea de tiempo candidato–cliente, y (3) un score de frescura.** Hasta que eso exista, comprar búsqueda vectorial es ponerle un motor de Fórmula 1 a un carro sin ruedas.

Cuatro decisiones de gobierno que estructuran esta estrategia:

1. **Secuencia no negociable:** `identidad → estructura → frescura → taxonomía → embeddings`. Saltar a lo semántico primero devuelve basura con alta confianza.
2. **No migrar del ATS todavía.** Se **extrae por API** y se enriquece en una capa propia *por encima* de Team Tailor. Abandonar el ATS hoy es resolver el problema equivocado y arriesgar la operación que genera el 63% de los ingresos.
3. **Nada se promete sin un Spike de Factibilidad pagado (Fase −1).** Los quick wins de datos cuelgan de una API de Team Tailor **que nadie ha verificado** y de un *golden set* **que probablemente no existe**. Eso se confirma o se apaga *antes* de cotizar alcance.
4. **BUY antes de BUILD, y lo declaramos abiertamente.** A volumen boutique (⚠️ ~20–60 colocaciones/año a confirmar), construir infraestructura custom puede tener **ROI negativo por años**. Nuestro ingreso crece cuanto más construimos: por eso declaramos el conflicto de interés y la recomendación por defecto es **exprimir lo que Team Tailor ya cobra** + capa mínima propia, reservando el *build* solo si la economía lo justifica con datos.

> **Corrección explícita a la crítica adversarial:** este documento incorpora costo/asequibilidad, plan de recursos de la consultora, el rol de la consultora como **nuevo procesador de PII**, umbrales go/no-go concretos, y la **reparación de reputación ANTES de medir CSAT**. Donde un dato del cliente falta, se marca **⚠️ supuesto a validar**.

---

## 2. Diagnóstico honesto del activo

| Mito del cliente | Realidad | Implicación |
|---|---|---|
| "Tenemos 4.000 candidatos = big data" | 4.000 filas caben en una hoja de cálculo o pocos MB de Postgres. El problema **nunca fue el tamaño** | No es un reto de datos masivos; encuadrarlo así infla el esfuerzo percibido y el costo |
| "Es oro" | Oro **sin refinar e ilíquido**: sin clave única, duplicados, ~30–50% vencido ⚠️ | El KPI real no es "4.000", es **"candidatos vigentes y contactables por skill/sector"** (probablemente 1.500–2.500 ⚠️) |
| "Hay que salir de Team Tailor para explotarla" | TT expone API REST/JSON (candidatos, aplicaciones, vacantes, tags, custom fields) ⚠️ *sujeto a verificación de tier* | Se extrae por API y se enriquece encima. Migrar es decisión de Fase 3 **con datos**, no con entusiasmo |
| "El mismo candidato enviado 2 veces es mala suerte" | Es un fallo de **resolución de identidad + ausencia de timeline**, no de IA | Se corrige con un *lookup*, barato, en Fase 0 |

**"4.000 candidatos" es hoy una *vanity metric*.** El primer entregable de datos es convertir esa cifra en un número honesto de vigentes.

---

## 3. La cadena crítica (resolviendo la tensión entre lentes)

La crítica adversarial señaló —con razón— que las distintas perspectivas se contradicen en la secuencia: *datos* quería parsear/extraer en paralelo en Fase 1; *proceso* quería documentar primero; *métricas* exigía etapas estandarizadas antes de medir. **Resolución acordada en una sola ruta crítica:**

```
Fase -1  SPIKE         Verificar API/export TT · muestrear vigencia · confirmar país+consentimiento · ver si existe golden set
   │
Fase 0   IDENTIDAD     Extracción read-only por API · resolución de identidad · dedup · timeline candidato-cliente · auditoría de vigencia
   │      (paralelo)   Diccionario de datos v0 (vocabulario) — NO etiquetar aún
   │
Fase 1   ESTRUCTURA    Modelo canónico · parsing de CV a esquema · taxonomía ESCO+overlay · gobernanza/consentimiento/retención
   │      FRESCURA      Score de vigencia · protocolo de actualización · (reparar SLA de comunicación ANTES de encuestar)
   │
Fase 2   BÚSQUEDA      Filtros estructurados → recién aquí embeddings + búsqueda híbrida sobre base ya limpia
   │
Fase 3   PRODUCTO      Portal de auto-actualización (mercado interno) · monetización condicionada a base legal
```

**Regla de oro contra el círculo vicioso:** el diccionario de datos (**vocabulario**) se define *antes* de enriquecer; la **identidad** se resuelve *antes* de la estructura; la **estructura** *antes* de los embeddings. Etiquetar sin vocabulario estándar solo amplifica la inconsistencia de "4 personas, 4 criterios".

---

## 4. Fase −1 — Spike de factibilidad técnica y legal (1 semana, pagada)

**Antes de prometer un solo quick win de datos.** Apaga o confirma todos los supuestos *load-bearing*. Sin esto, no comprometemos ningún P0.

| Pregunta bloqueante | Cómo se resuelve | Dueño | Si la respuesta es "no"… |
|---|---|---|---|
| ¿País exacto de operación? (CR/Panamá/Nicaragua = ley integral; Guatemala = solo habeas data ⚠️) | **Email de 5 min a Virginia — cerrar HOY, no "antes del viernes"** | Víctor | Bloquea scoping legal, retención y benchmark |
| ¿TT expone API/export masivo en el tier contratado? ¿Rate limits? | Prueba real contra la API con credenciales del cliente | Víctor | Plan B: export manual/CSV; se reescalan tiempos de Fase 0 |
| ¿Cuántos de los 4.000 están realmente vigentes? | Muestreo de 200–300 registros: email/teléfono válido, última actividad | Víctor + temp | Dimensiona el esfuerzo a la base vigente, no a 4.000 nominales |
| ¿Existe identificador único confiable (cédula/DPI) o solo email/teléfono? | Inspección de campos en TT | Víctor | Define estrategia de resolución de identidad |
| ¿Existe historial recuperable (quién entró a terna vs no) para un *golden set*? | Revisión con Virginia/Lili | Lili | Si no existe, el *golden set* hay que **construirlo** — costo no trivial, depende del tiempo escaso de Virginia |
| ¿Qué consentimiento aceptan hoy los candidatos al aplicar? | Revisar formulario de TT + link LinkedIn | Víctor | Define qué usos secundarios son lícitos |

**Entregable del spike:** un semáforo de 1 página (verde/ámbar/rojo por supuesto) que habilita —o reescala— el resto del programa. **Go/no-go:** si API y vigencia salen en rojo, la estrategia de datos se replantea hacia "exprimir TT" sin capa propia.

---

## 5. Arquitectura de datos objetivo

**Principio: augmentar, no reemplazar.** Team Tailor sigue siendo el sistema de registro operativo (mantiene LinkedIn, psicométricas, rechazos). Construimos una **capa de análisis/enriquecimiento de solo-lectura por encima**.

```
┌─────────────────────────────────────────────────────────┐
│  Team Tailor (ATS, sistema de registro) — NO SE TOCA     │
│  candidatos · aplicaciones · vacantes · tags · CV (PDF)  │
└───────────────┬─────────────────────────────────────────┘
                │  Sync incremental (API REST, read-only)
                ▼
┌─────────────────────────────────────────────────────────┐
│  Capa propia de talento (gestionada, no infra a medida)  │
│  • Postgres (modelo canónico) + pgvector                 │
│  • Object storage (PDFs de CV, cifrado)                  │
│  • Pipeline de parsing/enriquecimiento (LLM API)         │
└─────────────────────────────────────────────────────────┘
```

**Build-vs-buy — postura honesta (conflicto de interés declarado):**

| Componente | Recomendación por defecto | Por qué |
|---|---|---|
| Almacén/DB vectorial | **Gestionado** (Postgres+pgvector administrado), no infra propia | Boutique no debe operar infra |
| ASR (transcripción ES regional) | **Comprar**, no construir | Madurez del mercado |
| IA de matching/screening | **Activar primero lo que TT ya cobra** y no usan | El ROI de construir custom puede ser negativo a 20–60 colocaciones/año ⚠️ |
| Taxonomía | **Adoptar ESCO** (gratuita), no inventar | Reinventar la rueda quema semanas |
| Parsing de CV | LLM por API (no fine-tuning) | Costo de cómputo marginal |

> **Declaración de integridad:** nuestro encargo crece cuanto más custom construyamos. Por eso la recomendación por defecto —*exprimir el ATS que ya pagan*— es la que **encoge** nuestro contrato. La integridad en el primer proyecto vale más que su tamaño.

---

## 6. Modelo de datos canónico de talento

Esquema mínimo viable, con **gobernanza embebida desde el diseño** (no como parche posterior).

**Entidades y relaciones:**

| Entidad | Campos clave | Notas de gobernanza |
|---|---|---|
| **Candidato** (golden record) | `id_único`, identidad resuelta, aliases/CVs históricos enlazados | Fuente, fecha de consentimiento, base legal, `score_vigencia` |
| **Aplicación** | candidato → vacante, etapa, timestamps | Origen del dato (aplicó vs sourced ⚠️) |
| **Proceso/Vacante** | cliente, familia de puesto, sector, rango salarial | Confidencialidad por contrato/NDA |
| **Cliente** | empresa, hiring manager | Consentimiento para uso de datos de compensación |
| **Skill** (N:N con Candidato) | código ESCO + label local | Normalizado, no texto libre |
| **Sector/Ocupación** | ESCO + overlay CA | — |
| **Evento** (log/timeline) | candidato × proceso × cliente × fecha × resultado | **Núcleo del mercado interno** |

**Campos de gobernanza obligatorios en Candidato:** `fuente`, `consentimiento` (sí/no + finalidades), `fecha_última_verificación`, `score_vigencia (0–100)`, `estado_ciclo_vida` (vigente / en proceso / no vigente / no contactar).

Este es el **contrato de datos** sobre el que se apoyan parsing, búsqueda e IA. Sin él, se automatiza el desorden.

---

## 7. Resolución de identidad y deduplicación

El "mismo candidato enviado 2 veces" es **entity resolution + timeline**, no IA.

**Pipeline:**
1. **Match determinista** por email + teléfono + cédula/DPI (si existe).
2. **Match fuzzy** por nombre + atributos (fecha nacimiento, empleador) con umbral conservador.
3. **Golden record reversible:** se **enlazan** aliases/CVs, **no se borran**.

**Calibración de umbrales — el balance crítico:**

| Error | Consecuencia | Mitigación |
|---|---|---|
| **Falso positivo** (fusionar 2 personas distintas) | Brecha de privacidad: se muestra el historial de una persona a otra | Umbrales conservadores + revisión humana de *matches* dudosos |
| **Falso negativo** (no detectar duplicado) | Reaparece "el enviado dos veces" | Alerta blanda + revisión en el gate de terna |

**Quick win (Fase 0):** dedup + alerta "este candidato ya fue presentado a este cliente hace X meses". Mata un riesgo reputacional **ya materializado** con un *lookup*. Embrión del mercado interno.

---

## 8. Historial candidato–cliente ("mercado interno") — anti-duplicados y anti-mentira

**Qué es:** una línea de tiempo que, por cada candidato, registra **a qué procesos y clientes fue presentado, en qué fecha y con qué resultado** (terna / colocado / rechazado / declinó).

**Dos dolores que resuelve con un *lookup*, no con intuición:**
- **"Mandé al mismo dos veces":** gate obligatorio de verificación **antes de enviar cualquier terna**.
- **"Los candidatos mienten sobre participación previa":** si el sistema sabe a qué procesos fue cada persona, la mentira se detecta automáticamente.

**Límites de uso (corrección legal/ética — innegociable):**
- El historial **informa al reclutador; NO excluye automáticamente** al candidato.
- **No** se convierte en lista negra compartida entre clientes.
- **No** alimenta decisiones adversas automatizadas sin base legal y revisión humana.

**Implementación escalonada:** Fase 0 como tabla/campo derivado del ATS con regla manual → Fase 1 integrado al modelo canónico con alerta automática.

---

## 9. Parsing y enriquecimiento de CV

**Objetivo:** extraer JSON estructurado de cada CV (experiencia, empleadores, skills, sector, ubicación, idiomas, educación, pretensión salarial) y mapearlo al modelo canónico + taxonomía.

**Costo real (corrección a la sobrepromesa "$40–150"):**

| Componente | Costo | Realidad |
|---|---|---|
| Cómputo LLM (~$0.01–0.03/CV) | **USD 40–150 one-time** | Cierto, pero **es la parte barata** |
| **QA con muestreo humano 5–10%** | 200–400 revisiones manuales | El **verdadero cuello de botella** |
| PDFs escaneados, con foto, multi-idioma | Horas de trabajo calificado | Subestimado por un orden de magnitud |
| Mapeo a modelo canónico + ESCO + dedup | Semanas, no centavos | El titular "$150" oculta cientos de horas |

**El esfuerzo está en la validación y el mapeo, no en el cómputo.** Se dimensiona contra la **base vigente**, no contra 4.000.

**Controles obligatorios:**
- **Des-identificación de PII antes de cualquier scoring:** retirar foto, edad, estado civil, nacionalidad (los CV en CA suelen incluirlos). Inyectar eso a un ranker introduce sesgo medible y responsabilidad legal.
- **Esquema de salida estricto** + validación de consistencia para mitigar alucinación; nunca usar el dato parseado como verdad absoluta sin trazar al CV fuente.
- **Cortar YA la inyección de PII en ChatGPT de consumo** (brecha activa: el prompt de Virginia probablemente envía CVs completos a ChatGPT personal). Migrar a Enterprise/Team o API con no-entrenamiento + DPA. Costo casi nulo, cierra riesgo inmediato.

---

## 10. Taxonomía de skills y sectores

**Adoptar ESCO** (clasificación europea, gratuita, multilingüe con español; ~3.000 ocupaciones, ~13.900 skills, ya jerarquizadas) como **columna vertebral**, en lugar de construir una ontología desde cero.

**Pero "adoptar" no es "gratis" (corrección):** ESCO es europea. El trabajo real es:
- **Overlay local:** curar 15–30 sectores/títulos/competencias propios de Centroamérica y del nicho de Conexión Talento (incluidos títulos informales).
- **Normalización:** mapear el texto libre de 4 reclutadores con 4 criterios contra la taxonomía.
- **Medir tasa de no-match** por cohorte como métrica de calidad de la normalización.

**Resultado:** la base se vuelve **buscable por skill y sector de forma consistente**, no por texto libre. Habilita el mercado interno y (condicionado a legal) el cross-sell.

---

## 11. Protocolo de actualización continua y score de vigencia

Convierte la base de un cementerio estático en un activo vivo.

**Score de vigencia (0–100):** decae con el tiempo, se refresca con cada interacción (aplicación, actualización, respuesta a campaña). La búsqueda **prioriza candidatos vigentes**. Mantiene honesto el conteo de "cuántos vigentes".

**Ciclo de vida del dato:**
1. Campaña de re-engagement por email a candidatos "dormidos".
2. Verificación de empleo/contacto.
3. **Portal de auto-actualización** (Fase 3): el candidato actualiza CV, disponibilidad y pretensiones, y opta por alertas. Refresca vigencia **sin trabajo manual del equipo saturado** y mejora la candidate experience.

> **Secuencia crítica (corrección a la crítica):** **reparar el SLA de comunicación al candidato ANTES de lanzar cualquier CSAT o campaña de re-engagement.** Encuestar a candidatos ya enojados y *ghosteados* puede provocar **más** backlash en LinkedIn ("me ignoraron y ahora me preguntan cómo me sentí"). Primero se cierra el loop de comunicación; luego se mide.

> **Supuesto frágil que NO aceptamos:** que el equipo de 4 personas saturadas etiquetará/mantendrá la base manualmente. Cualquier proceso que dependa de captura manual fracasa. Por eso: **automatizar** enriquecimiento (parsing/taxonomía) y frescura (portal), no añadir trabajo manual.

---

## 12. Búsqueda: estructurada primero, semántica al final

Embeddings y búsqueda vectorial son la **última milla, no la primera**. Sobre una base sucia devuelven basura con alta confianza.

**Orden de implementación:**
1. **Filtros estructurados** (sector, skill ESCO, vigencia, ubicación, disponibilidad) — esto ya resuelve la mayoría de las consultas ("búscame backend semi-senior en banca, disponible").
2. **Recién entonces:** embeddings de CV+perfil estructurado en pgvector + **búsqueda híbrida** (filtros + similitud semántica).

**Piloto de validación (Fase 2, <30 días):** parsear 300–500 CVs de **un solo sector**, normalizar contra ESCO, y demostrar la búsqueda funcionando en vivo. Prueba tangible del valor del activo antes de procesar los 4.000.

---

## 13. Gobernanza, calidad y cumplimiento de datos

**Marco mínimo (barato de redactar, caro de omitir):**

| Pieza | Qué incluye | Fase |
|---|---|---|
| **Confirmar país + ley aplicable** | Ley 8968 CR / Ley 81 Panamá / Ley 787 Nicaragua / habeas data Guatemala ⚠️; ¿registro de base ante regulador? | −1/0 |
| **Designar responsable de datos** | Punto único de responsabilidad (Virginia o Lili) | 0 |
| **Aviso de privacidad en el punto de aplicación** | Finalidades separadas (reclutamiento vs benchmark vs capacitación), base legal, retención, derechos ARCO | 1 |
| **Inventario de datos (RoPA-lite)** | Qué datos, de dónde, base legal, dónde, con quién, cuánto | 1 |
| **Política de retención + purga** | Plazos; purgar/anonimizar caducos. Retener 4.000 indefinidamente es pasivo legal | 1 |
| **Consentimiento granular (opt-in)** | Casillas separadas: reclutamiento / capacitación / estudios de compensación anonimizados | 1 |
| **DPAs con proveedores** | Team Tailor, OpenAI/LLM, ASR, psicométricas | 1–2 |

**Punto omitido por todas las lentes y exigido por la crítica — la consultora se vuelve PROCESADORA de PII:** al exportar los 4.000 a un almacén propio, nuestra boutique pasa a ser **sub-procesadora de datos personales**. Esto exige:
- **DPA cliente–consultora** (no solo cliente–proveedor).
- **Dónde viven los 4.000 durante el proyecto**, cifrado en reposo, control de accesos por rol.
- **Borrado/devolución al cierre** del engagement.
- Reconocer que introducimos un **nuevo vector de brecha** en nuestro primer proyecto: se cierra **antes** de tocar la base, no después.

**Monetización — CONGELADA hasta cerrar base legal (decisión de gobierno inmediata):**
- **Benchmark de compensaciones:** ⚠️ posible bandera roja legal. Datos salariales provienen de negociaciones con clientes, probablemente bajo NDA. En mercados pequeños son **re-identificables aun agregados** ("el salario del CFO de la empresa X"). *Camino positivo, no solo "no":* explorar **alianza con un proveedor licenciado de comp-data**, o producto futuro con k-anonimato (N mínimo por celda) **y** verificación contractual de derecho de reúso. No entra al camino crítico ni se promete el viernes.
- **Cross-sell de capacitaciones:** viola limitación de finalidad sin consentimiento separado + opt-out. Bloqueado hasta Fase 1.

---

## 14. Métricas de salud de la base

**Reportar siempre con `n` al lado y caveats** (a volumen boutique, casi toda métrica de funnel tiene n limitado; no presentar ruido como tendencia).

| Métrica | Definición | Hoy | Meta escalonada ⚠️ |
|---|---|---|---|
| **% vigente** | candidatos con datos/consentimiento < 12 meses | Desconocido | medir en Spike → ≥50% en 6–9 meses |
| **% contactable** | email/teléfono válido | Desconocido | ≥70% de los vigentes |
| **% parseable** | CV con extracción exitosa | Desconocido | medir por cohorte |
| **% etiquetado** | con skill/sector normalizado a ESCO | ~0% | 100% de la base vigente |
| **Tasa de duplicados** | registros fusionados / total | Desconocido | medir → mantener |
| **Tasa de no-match taxonómico** | skills sin mapear a ESCO | — | < umbral a definir |
| **Incidentes de duplicado** (candidato reenviado) | # por trimestre | ≥1 (ya ocurrió) | **→ 0** |
| **Internal-fill rate** | colocaciones servidas desde la base vs sourcing nuevo | Desconocido (¡ni el denominador!) | baseline → 30–40% en 6–9 meses |

**El North Star del activo de datos:** `candidatos vigentes y contactables, etiquetados por skill/sector` + `internal-fill rate`. Eso convierte "tenemos oro" en una línea base medible y desarma o confirma el "60% del valor" **con datos**.

> **Dashboard de auditoría de vigencia** (Fase 0): el primer entregable de datos. Convierte "4.000" en un número honesto.

---

## 15. Secuenciación por fases con go/no-go concretos

| Fase | Entregables de datos | Esfuerzo agregado ⚠️ | Go/No-Go (cifras, no adjetivos) |
|---|---|---|---|
| **−1 Spike** | Semáforo de factibilidad API + vigencia + país + golden set | 1 sem | **GO si** API permite export Y vigencia muestral ≥40%. Si no → replantear a "exprimir TT" |
| **0 Identidad** | Extracción read-only · dedup · timeline candidato-cliente · dashboard de vigencia · diccionario v0 | 2–4 sem | **GO si** ≥X% duplicados detectados + dashboard de vigencia entregado + alerta anti-reenvío operando |
| **1 Estructura+Frescura** | Modelo canónico · parsing+QA · ESCO+overlay · gobernanza/consentimiento/retención · score de vigencia | (programa de varios meses — **no "esfuerzo bajo"**) | **GO si** ≥80% base vigente etiquetada + marco legal cerrado + DPA cliente-consultora firmado |
| **2 Búsqueda** | Filtros estructurados → embeddings → búsqueda híbrida · piloto 1 sector | Medio | **GO si** piloto demuestra recuperación útil en 1 sector con precisión validada por reclutador |
| **3 Producto** | Portal auto-actualización · monetización (solo si base legal lo permite) | Alto | **GO solo si** legal valida finalidad + consentimiento granular acumulado |

**Kill-criteria explícito:** si al cierre de Fase 0 la vigencia real resulta < 25% o la API no soporta sincronización viable, **se detiene el build de datos** y se pivotea a "exprimir Team Tailor + dedup en hoja/campo", sin capa propia.

---

## 16. Costo, asequibilidad y recurso (lo que la crítica exigió y faltaba)

**Realidad económica:** el cliente ancla en **~US$1.5k–2.7k** (3 meses de asistente temporal ⚠️). El programa completo de datos (capa propia + parsing + ESCO + entity resolution + score de vigencia + gobernanza + legal) es **fácilmente un esfuerzo de varios meses de trabajo senior**. **El build completo probablemente excede lo que una PYME de 10 personas puede financiar.**

**Recomendación por defecto — "camino BUY suficientemente bueno":**
1. Activar la IA y funciones que **Team Tailor ya cobra** y no usan.
2. **Dedup + timeline** en campo del ATS / hoja controlada (Fase 0, bajo costo).
3. SOPs livianos y diccionario de datos (vocabulario) — barato, alto valor.
4. **Reservar el build custom** (pgvector, parsing masivo, portal) **solo si** el internal-fill rate y la economía unitaria lo justifican con datos del Spike.

**Recurso (capacidad de NUESTRA consultora):** Víctor es experto en data/IA pero **no en RRHH ni en compliance**. La parte legal (RoPA, retención, antitrust del benchmark, DPA) **se subcontrata a un abogado de datos local** — no se promete in-house. El parsing/QA masivo y la curaduría de ESCO requieren manos calificadas que hoy no tenemos asignadas; se dimensionan en la propuesta, no se ocultan tras etiquetas de "esfuerzo bajo".

**La asistente temporal:** su tiempo va a **descargar la operación de Lili** (su pedido real, evita quemar a la champion) y, en lo posible, a apoyo de etiquetado supervisado — **no** a las dos cosas a la vez ni a documentar el "ojo clínico" (eso requiere a Virginia/Lili).

---

## 17. Supuestos a validar (⚠️) y precondiciones bloqueantes

| # | Supuesto | Tipo | Dueño |
|---|---|---|---|
| 1 | País de operación y ley aplicable | **Precondición bloqueante** — cerrar HOY | Virginia |
| 2 | Team Tailor expone API/export en el tier contratado | **Precondición bloqueante** | Víctor (Spike) |
| 3 | 30–50% de la base está vencida | Supuesto a medir en Spike | Víctor |
| 4 | Existe golden set / historial recuperable | Supuesto frágil — probablemente **NO existe** | Lili |
| 5 | Existe identificador único (cédula/DPI) | A verificar | Víctor |
| 6 | Origen de los 4.000: ¿aplicaron o fueron *sourced* de LinkedIn? | Determina base legal para monetizar | Virginia |
| 7 | Volumen real (vacantes/mes, colocaciones/año) | Determina ROI y validez estadística | Virginia |
| 8 | Idioma de los CV (solo ES o mixto) | Afecta parsing/embeddings | Spike |

---

## 18. Riesgos clave y mitigaciones

| Riesgo | Sev. | Mitigación |
|---|---|---|
| **Legal:** monetizar/reutilizar datos sin base legal ni anonimización | Alto | Congelar toda monetización hasta cerrar gobernanza; confirmar país; k-anonimato + N mínimo |
| **Decay subestimado:** "oro" sobrevalorado si 30–50% vencido | Alto | Auditoría de vigencia en Spike **antes** de invertir en enriquecer |
| **Errores de identidad:** fusionar 2 personas = brecha de privacidad | Alto | Umbrales conservadores, revisión humana, fusión **reversible** |
| **API de TT no verificada** soporta media estrategia | Alto | Spike pagado la confirma antes de prometer P0 |
| **Consultora como nuevo vector de brecha de PII** | Alto | DPA cliente-consultora, cifrado, accesos por rol, borrado al cierre |
| **Migración prematura del ATS** replica el desorden en sistema más caro y rompe la operación (63% ingresos) | Alto | NO migrar hasta tener estructura + caso de negocio; agotar funciones que ya pagan |
| **ROI negativo a escala boutique** por sobre-construir | Medio | BUY antes de BUILD; build solo si la economía lo justifica con datos |
| **Costo real del parsing** subestimado (QA, ESCO, dedup) | Medio | Presupuestar el trabajo calificado, no solo el cómputo |
| **Captura manual fracasa** con equipo saturado | Medio | Automatizar enriquecimiento y frescura; portal de auto-actualización |

---

### Cierre

La estrategia de datos de Conexión Talento no es un proyecto de big data ni de búsqueda vectorial vistosa. Es **plomería disciplinada**: identidad única, deduplicación con memoria, frescura medida y un vocabulario común — todo construido **sobre** el ATS que ya pagan, **bajo** un marco de gobernanza que hoy no existe, y **solo hasta donde la economía de una boutique lo justifique**. Hecho en ese orden, los 4.000 registros dejan de ser una *vanity metric* y se vuelven, por primera vez, un activo vivo, buscable y defendible. Hecho al revés, le ponemos un motor de Fórmula 1 a un carro sin ruedas.
