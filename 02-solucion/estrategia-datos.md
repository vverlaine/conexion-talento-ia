# Estrategia de datos — Conexión Talento

**Documento entregable · Memoria del proyecto · Fase: Descubrimiento**
*Cómo convertir 4.000 registros estáticos en una base de talento viva, buscable y defendible — sin precipitarse, sin construir de más, y sin tocar el 63% de los ingresos que financian todo.*

---

> **En una frase:** los 4.000 candidatos todavía no son "oro"; primero hay que limpiarlos y ordenarlos (barato), y solo después invertir en búsqueda inteligente — exprimiendo lo que ya pagan a su sistema actual antes de construir nada nuevo.

---

## 1. Síntesis ejecutiva

**Para el negocio:** Virginia cree que la base de 4.000 candidatos vale ~60% del valor del proyecto. Es un potencial real, pero todavía no es un hecho. Hoy esa base rinde poco y, hasta arreglarla, gastar en tecnología vistosa es tirar dinero.

**La tesis que retamos al cliente y a nosotros mismos:** la base **no es "oro" todavía**. Hoy es un activo de bajo rendimiento: sin una forma única de identificar a cada persona, con duplicados, con un **30–50% de la información vencida ⚠️ (a medir, no a suponer)** y sin orden. El valor no está en el volumen ni en ponerle encima búsqueda inteligente (lo vistoso); está condicionado a tres cosas aburridas y baratas: **(1) una forma única de identificar a cada candidato, (2) quitar duplicados y registrar a qué clientes se le presentó y cuándo, y (3) una nota de qué tan actualizado está cada dato.** Hasta que eso exista, comprar búsqueda avanzada es ponerle un motor de Fórmula 1 a un carro sin ruedas.

Cuatro decisiones de gobierno que estructuran esta estrategia:

1. **Orden no negociable:** primero `identidad`, luego `estructura`, luego `frescura`, luego `vocabulario común de habilidades y sectores`, y solo al final `búsqueda inteligente`. Saltar a la búsqueda avanzada primero devuelve basura que *parece* confiable.
2. **No mudarse del sistema actual todavía.** Se **extrae la información por conexión técnica entre sistemas (API)** y se enriquece en una capa propia *por encima* de Team Tailor (el sistema donde guardan los candidatos). Abandonarlo hoy resuelve el problema equivocado y pone en riesgo la operación que genera el 63% de los ingresos.
3. **Nada se promete sin una prueba rápida pagada (Fase −1).** Las mejoras rápidas de datos dependen de una conexión técnica de Team Tailor **que nadie ha verificado** y de un set de decisiones de referencia (los casos que enseñan a la IA a elegir como Virginia) **que probablemente no existe**. Eso se confirma o se descarta *antes* de cotizar alcance.
4. **Comprar antes que construir, y lo declaramos abiertamente.** A volumen boutique (⚠️ ~20–60 colocaciones/año a confirmar), construir sistemas a medida puede **no recuperar la inversión durante años**. Nuestro ingreso crece cuanto más construimos: por eso declaramos el conflicto de interés y la recomendación por defecto es **exprimir lo que Team Tailor ya cobra** y no usan, más una capa propia mínima, dejando la construcción a medida solo si los números la justifican.

> **Corrección explícita a la crítica recibida:** este documento incorpora costo y asequibilidad, el plan de personal de la consultora, el hecho de que la consultora pasa a manejar datos personales sensibles, criterios concretos de seguir/parar, y la **reparación de la relación con los candidatos ANTES de medir su satisfacción**. Donde falta un dato del cliente, se marca **⚠️ supuesto a validar**.

---

## 2. Diagnóstico honesto del activo

**Para el negocio:** lo que el cliente cree de su base no coincide con la realidad. Reencuadrar estos mitos baja el esfuerzo percibido y el costo.

| Mito del cliente | Realidad | Implicación |
|---|---|---|
| "Tenemos 4.000 candidatos = muchísimos datos" | 4.000 filas caben en una hoja de cálculo. El problema **nunca fue el tamaño** | No es un reto de datos masivos; verlo así infla el esfuerzo percibido y el costo |
| "Es oro" | Oro **sin refinar y difícil de usar**: sin forma única de identificar a cada persona, con duplicados, ~30–50% vencido ⚠️ | El indicador real no es "4.000", es **"candidatos vigentes y contactables por habilidad/sector"** (probablemente 1.500–2.500 ⚠️) |
| "Hay que salir de Team Tailor para explotarla" | Team Tailor permite extraer la información por conexión técnica (candidatos, postulaciones, vacantes, etiquetas, campos propios) ⚠️ *sujeto a verificar el plan contratado* | Se extrae y se enriquece encima. Mudarse es decisión de Fase 3 **con datos**, no con entusiasmo |
| "El mismo candidato enviado 2 veces es mala suerte" | Es un fallo de **identificación de personas y de no tener una línea de tiempo**, no de IA | Se corrige con una consulta simple, barata, en Fase 0 |

**"4.000 candidatos" es hoy una cifra de vanidad** (impresiona pero no significa valor). El primer entregable de datos es convertir esa cifra en un número honesto de vigentes.

---

## 3. La ruta crítica (resolviendo la tensión entre enfoques)

**Para el negocio:** las distintas miradas del equipo se contradecían en el orden. Aquí se unifican en una sola ruta para no rehacer trabajo ni amplificar el desorden.

La crítica señaló —con razón— que las perspectivas se contradicen: la mirada de *datos* quería procesar y extraer en paralelo en Fase 1; la de *proceso* quería documentar primero; la de *métricas* exigía etapas estandarizadas antes de medir. **Resolución acordada en una sola ruta:**

```
Fase -1  PRUEBA RÁPIDA   Verificar la conexión técnica/extracción de Team Tailor · muestrear vigencia · confirmar país+consentimiento · ver si existe el set de decisiones de referencia
   │
Fase 0   IDENTIDAD       Extracción de solo lectura por conexión técnica · identificar personas · quitar duplicados · línea de tiempo candidato-cliente · auditoría de vigencia
   │      (paralelo)     Diccionario de datos v0 (vocabulario común) — NO etiquetar aún
   │
Fase 1   ESTRUCTURA      Modelo de datos único · ordenar el CV en un formato estándar · vocabulario común (ESCO) + ajuste local · gobernanza/consentimiento/retención
   │      FRESCURA        Nota de vigencia · protocolo de actualización · (reparar el compromiso de respuesta al candidato ANTES de encuestar)
   │
Fase 2   BÚSQUEDA        Filtros estructurados → recién aquí búsqueda inteligente sobre una base ya limpia
   │
Fase 3   PRODUCTO        Portal de auto-actualización (mercado interno) · monetización condicionada a permiso legal
```

**Regla de oro contra el círculo vicioso:** el diccionario de datos (**vocabulario común**) se define *antes* de enriquecer; la **identidad** se resuelve *antes* de la estructura; la **estructura** *antes* de la búsqueda inteligente. Etiquetar sin vocabulario estándar solo amplifica la inconsistencia de "4 personas, 4 criterios".

---

## 4. Fase −1 — Prueba rápida de factibilidad técnica y legal (1 semana, pagada)

**Para el negocio:** antes de prometer una sola mejora, confirmamos que los supuestos que sostienen el plan son reales. Una semana barata evita comprometer meses de trabajo sobre arena.

| Pregunta bloqueante | Cómo se resuelve | Dueño | Si la respuesta es "no"… |
|---|---|---|---|
| ¿País exacto de operación? (CR/Panamá/Nicaragua = ley integral de datos; Guatemala = solo derecho a acceder/corregir datos ⚠️) | **Correo de 5 min a Virginia — cerrar HOY, no "antes del viernes"** | Víctor | Bloquea el análisis legal, la retención y la comparación de mercado |
| ¿Team Tailor permite extraer la información en el plan contratado? ¿Hay límites de velocidad? | Prueba real contra la conexión técnica con credenciales del cliente | Víctor | Plan B: descarga manual/CSV; se reajustan los tiempos de Fase 0 |
| ¿Cuántos de los 4.000 están realmente vigentes? | Muestreo de 200–300 registros: correo/teléfono válido, última actividad | Víctor + temporal | Dimensiona el esfuerzo a la base vigente, no a 4.000 nominales |
| ¿Existe un identificador único confiable (cédula/DPI) o solo correo/teléfono? | Inspección de campos en Team Tailor | Víctor | Define cómo identificar a cada persona |
| ¿Existe historial recuperable (quién entró a terna y quién no) para armar el set de decisiones de referencia? | Revisión con Virginia/Lili | Lili | Si no existe, hay que **construirlo** — costo no trivial, depende del tiempo escaso de Virginia |
| ¿Qué consentimiento aceptan hoy los candidatos al postularse? | Revisar el formulario de Team Tailor + enlace de LinkedIn | Víctor | Define qué otros usos de los datos son legales |

**Entregable de la prueba:** un semáforo de 1 página (verde/ámbar/rojo por cada supuesto) que habilita —o reajusta— el resto del programa. **Seguir o parar:** si la conexión técnica y la vigencia salen en rojo, la estrategia de datos se replantea hacia "exprimir Team Tailor" sin capa propia.

---

## 5. Arquitectura de datos objetivo

**Para el negocio:** no reemplazamos el sistema que ya usan; le ponemos encima una capa de análisis que no lo toca. Cero riesgo para la operación que paga las facturas.

**Principio: sumar, no reemplazar.** Team Tailor sigue siendo el sistema oficial donde vive todo (LinkedIn, pruebas psicométricas, rechazos). Construimos una **capa de análisis y enriquecimiento de solo lectura por encima**.

```
┌─────────────────────────────────────────────────────────┐
│  Team Tailor (sistema oficial de registro) — NO SE TOCA  │
│  candidatos · postulaciones · vacantes · etiquetas · CV  │
└───────────────┬─────────────────────────────────────────┘
                │  Sincronización gradual (conexión técnica, solo lectura)
                ▼
┌─────────────────────────────────────────────────────────┐
│  Capa propia de talento (gestionada, no a medida)        │
│  • Base de datos única + motor de búsqueda inteligente   │
│  • Almacenamiento de CV (PDF), cifrado                   │
│  • Proceso de ordenado y enriquecimiento con IA          │
└─────────────────────────────────────────────────────────┘
```

**Comprar o construir — postura honesta (conflicto de interés declarado):**

| Componente | Recomendación por defecto | Por qué |
|---|---|---|
| Base de datos y motor de búsqueda | **Gestionado por un proveedor**, no infraestructura propia | Una boutique no debe operar infraestructura |
| Transcripción de audio (español regional) | **Comprar**, no construir | El mercado ya está maduro |
| IA de selección/ordenamiento de candidatos | **Activar primero lo que Team Tailor ya cobra** y no usan | Construir a medida puede no recuperar la inversión a 20–60 colocaciones/año ⚠️ |
| Vocabulario de habilidades y sectores | **Adoptar ESCO** (gratuito), no inventar | Reinventar la rueda quema semanas |
| Ordenado de CV | IA por conexión técnica (sin entrenar un modelo propio) | El costo de cómputo es marginal |

> **Declaración de integridad:** nuestro encargo crece cuanto más construyamos a medida. Por eso la recomendación por defecto —*exprimir el sistema que ya pagan*— es la que **encoge** nuestro contrato. La integridad en el primer proyecto vale más que su tamaño.

---

## 6. Modelo de datos único de talento

**Para el negocio:** sin un esquema común con reglas de privacidad incorporadas, automatizar solo multiplica el desorden. Esto es el cimiento sobre el que todo lo demás se apoya.

Esquema mínimo viable, con **reglas de privacidad incorporadas desde el diseño** (no como parche posterior).

**Entidades y relaciones:**

| Entidad | Campos clave | Notas de privacidad |
|---|---|---|
| **Candidato** (ficha maestra) | `id_único`, identidad resuelta, CVs antiguos enlazados | Fuente, fecha de consentimiento, permiso legal, `nota_de_vigencia` |
| **Postulación** | candidato → vacante, etapa, fechas | Origen del dato (se postuló vs lo buscamos ⚠️) |
| **Proceso/Vacante** | cliente, tipo de puesto, sector, rango salarial | Confidencialidad por contrato/acuerdo |
| **Cliente** | empresa, responsable de contratación | Consentimiento para usar datos de salarios |
| **Habilidad** (varias por candidato) | código ESCO + nombre local | Normalizado, no texto libre |
| **Sector/Ocupación** | ESCO + ajuste para Centroamérica | — |
| **Evento** (registro/línea de tiempo) | candidato × proceso × cliente × fecha × resultado | **Corazón del mercado interno** |

**Campos de privacidad obligatorios en cada Candidato:** `fuente`, `consentimiento` (sí/no + para qué usos), `fecha_última_verificación`, `nota_de_vigencia (0–100)`, `estado` (vigente / en proceso / no vigente / no contactar).

Este es el **acuerdo de datos** sobre el que se apoyan el ordenado, la búsqueda y la IA. Sin él, se automatiza el desorden.

---

## 7. Identificar personas y quitar duplicados

**Para el negocio:** el "mismo candidato enviado 2 veces" no se arregla con IA, sino con una consulta que cruza datos. Es barato y mata un riesgo de reputación ya ocurrido.

El problema es **identificar correctamente a cada persona y tener su línea de tiempo**, no IA.

**Proceso:**
1. **Coincidencia exacta** por correo + teléfono + cédula/DPI (si existe).
2. **Coincidencia aproximada** por nombre + atributos (fecha de nacimiento, empleador) con un umbral conservador.
3. **Ficha maestra reversible:** los CVs y nombres alternativos se **enlazan**, **no se borran**.

**Calibración de umbrales — el balance crítico:**

| Error | Consecuencia | Mitigación |
|---|---|---|
| **Falso positivo** (fusionar 2 personas distintas) | Brecha de privacidad: se le muestra el historial de una persona a otra | Umbrales conservadores + revisión humana de los casos dudosos |
| **Falso negativo** (no detectar un duplicado) | Reaparece "el enviado dos veces" | Alerta suave + revisión justo antes de entregar la terna |

**Mejora rápida (Fase 0):** quitar duplicados + alerta "este candidato ya fue presentado a este cliente hace X meses". Mata con una consulta simple un riesgo de reputación **ya materializado**. Es la semilla del mercado interno.

---

## 8. Historial candidato–cliente ("mercado interno") — anti-duplicados y anti-mentira

**Para el negocio:** una memoria de a quién se presentó dónde y cuándo. Resuelve dos dolores reales (mandar al mismo dos veces y candidatos que mienten sobre su participación previa) con una consulta, no con intuición.

**Qué es:** una línea de tiempo que, por cada candidato, registra **a qué procesos y clientes fue presentado, en qué fecha y con qué resultado** (terna / colocado / rechazado / declinó).

**Dos dolores que resuelve con una consulta, no con intuición:**
- **"Mandé al mismo dos veces":** verificación obligatoria **antes de enviar cualquier terna**.
- **"Los candidatos mienten sobre participación previa":** si el sistema sabe a qué procesos fue cada persona, la mentira se detecta sola.

**Límites de uso (corrección legal/ética — innegociable):**
- El historial **informa al reclutador; NO excluye automáticamente** al candidato.
- **No** se convierte en lista negra compartida entre clientes.
- **No** alimenta decisiones en contra del candidato de forma automática sin permiso legal y revisión humana.

**Implementación escalonada:** Fase 0 como tabla/campo derivado del sistema actual con regla manual → Fase 1 integrado al modelo único con alerta automática.

---

## 9. Ordenar y enriquecer los CV

**Para el negocio:** sacar de cada CV los datos clave en un formato uniforme. Lo barato es el cómputo; lo caro y lo que de verdad cuesta es revisar que esté bien. No se subestima.

**Objetivo:** sacar de cada CV un formato estructurado (experiencia, empleadores, habilidades, sector, ubicación, idiomas, educación, pretensión salarial) y conectarlo al modelo único + vocabulario común.

**Costo real (corrección a la promesa exagerada de "$40–150"):**

| Componente | Costo | Realidad |
|---|---|---|
| Cómputo de IA (~$0.01–0.03/CV) | **USD 40–150 una sola vez** | Cierto, pero **es la parte barata** |
| **Control de calidad revisando a mano 5–10%** | 200–400 revisiones manuales | El **verdadero cuello de botella** |
| PDFs escaneados, con foto, en varios idiomas | Horas de trabajo calificado | Subestimado por mucho |
| Conexión al modelo único + ESCO + quitar duplicados | Semanas, no centavos | El titular "$150" oculta cientos de horas |

**El esfuerzo está en validar y conectar, no en el cómputo.** Se dimensiona contra la **base vigente**, no contra 4.000.

**Controles obligatorios:**
- **Quitar datos personales sensibles antes de cualquier evaluación automática:** retirar foto, edad, estado civil, nacionalidad (los CV en Centroamérica suelen incluirlos). Meter eso a un asistente que ordena candidatos introduce sesgo medible y responsabilidad legal.
- **Formato de salida estricto** + validación de consistencia para evitar que la IA invente datos; nunca usar el dato extraído como verdad absoluta sin poder rastrearlo al CV original.
- **Cortar YA el envío de datos personales a ChatGPT de consumo** (brecha activa: el uso actual de Virginia probablemente envía CVs completos a su ChatGPT personal). Migrar a una versión empresarial o por conexión técnica con compromiso de no entrenar con los datos + acuerdo de protección de datos (el proveedor no usa ni entrena con los datos). Costo casi nulo, cierra un riesgo inmediato.

---

## 10. Vocabulario común de habilidades y sectores

**Para el negocio:** que la base se pueda buscar por habilidad y sector de forma consistente, no por texto libre. Adoptar un estándar gratuito ahorra semanas, pero hay que adaptarlo a la región.

**Adoptar ESCO** (clasificación europea, gratuita, multilingüe con español; ~3.000 ocupaciones, ~13.900 habilidades, ya jerarquizadas) como **columna vertebral**, en lugar de construir un vocabulario desde cero.

**Pero "adoptar" no es "gratis" (corrección):** ESCO es europea. El trabajo real es:
- **Ajuste local:** curar 15–30 sectores/títulos/competencias propios de Centroamérica y del nicho de Conexión Talento (incluidos títulos informales).
- **Normalización:** mapear el texto libre de 4 reclutadores con 4 criterios contra el vocabulario común.
- **Medir cuántos casos no encajan** por grupo, como indicador de calidad de la normalización.

**Resultado:** la base se vuelve **buscable por habilidad y sector de forma consistente**, no por texto libre. Habilita el mercado interno y (sujeto a permiso legal) la venta cruzada.

---

## 11. Protocolo de actualización continua y nota de vigencia

**Para el negocio:** convierte un cementerio de datos viejos en una base viva. Sin esto, la base envejece sola y vuelve al punto de partida.

**Nota de vigencia (0–100):** baja con el tiempo, sube con cada interacción (postulación, actualización, respuesta a una campaña). La búsqueda **prioriza a los candidatos vigentes**. Mantiene honesto el conteo de "cuántos vigentes".

**Ciclo de vida del dato:**
1. Campaña de reconexión por correo a candidatos "dormidos".
2. Verificación de empleo/contacto.
3. **Portal de auto-actualización** (Fase 3): el candidato actualiza su CV, disponibilidad y pretensiones, y elige recibir alertas. Refresca la vigencia **sin trabajo manual del equipo saturado** y mejora la experiencia del candidato.

> **Orden crítico (corrección a la crítica):** **reparar el compromiso de respuesta al candidato ANTES de lanzar cualquier encuesta de satisfacción o campaña de reconexión.** Encuestar a candidatos ya enojados e ignorados puede provocar **más** reacción negativa en LinkedIn ("me ignoraron y ahora me preguntan cómo me sentí"). Primero se cierra el círculo de comunicación; luego se mide.

> **Supuesto frágil que NO aceptamos:** que el equipo de 4 personas saturadas etiquetará/mantendrá la base a mano. Cualquier proceso que dependa de captura manual fracasa. Por eso: **automatizar** el enriquecimiento (ordenado/vocabulario) y la frescura (portal), no añadir trabajo manual.

---

## 12. Búsqueda: estructurada primero, inteligente al final

**Para el negocio:** la búsqueda inteligente es lo último, no lo primero. Sobre una base sucia devuelve basura que parece confiable. Los filtros simples ya resuelven la mayoría de las consultas.

La búsqueda inteligente (que entiende el significado, no solo palabras exactas) es la **última milla, no la primera**.

**Orden de implementación:**
1. **Filtros estructurados** (sector, habilidad ESCO, vigencia, ubicación, disponibilidad) — esto ya resuelve la mayoría de las consultas ("búscame un programador de back-end semi-senior en banca, disponible").
2. **Recién entonces:** búsqueda inteligente sobre el CV + perfil estructurado + **búsqueda combinada** (filtros + similitud de significado).

**Prueba piloto de validación (Fase 2, <30 días):** ordenar 300–500 CVs de **un solo sector**, normalizar contra ESCO y demostrar la búsqueda funcionando en vivo. Prueba tangible del valor del activo antes de procesar los 4.000.

---

## 13. Gobernanza, calidad y cumplimiento de datos

**Para el negocio:** un marco legal mínimo es barato de redactar y caro de omitir. Y hay un punto que nadie había visto: al copiar los 4.000 a una base propia, la consultora pasa a manejar datos personales y se vuelve un nuevo riesgo de brecha. Se cierra antes de tocar nada.

**Marco mínimo (barato de redactar, caro de omitir):**

| Pieza | Qué incluye | Fase |
|---|---|---|
| **Confirmar país + ley aplicable** | Ley 8968 CR / Ley 81 Panamá / Ley 787 Nicaragua / derecho a acceder y corregir datos en Guatemala ⚠️; ¿hay que registrar la base ante el regulador? | −1/0 |
| **Designar responsable de datos** | Un único punto de responsabilidad (Virginia o Lili) | 0 |
| **Aviso de privacidad al momento de postularse** | Usos separados (reclutamiento vs comparación de mercado vs capacitación), permiso legal, retención, derechos del candidato | 1 |
| **Inventario de datos (registro de datos que exige la ley: qué datos usan, para qué y con qué permiso)** | Qué datos, de dónde, con qué permiso, dónde, con quién, por cuánto tiempo | 1 |
| **Política de retención + borrado** | Plazos; borrar/anonimizar los caducos. Guardar 4.000 indefinidamente es un pasivo legal | 1 |
| **Consentimiento detallado (opt-in)** | Casillas separadas: reclutamiento / capacitación / estudios de salarios anonimizados | 1 |
| **Acuerdos de protección de datos con proveedores** (el proveedor no usa ni entrena con los datos) | Team Tailor, proveedor de IA, transcripción, psicométricas | 1–2 |

**Punto omitido por todos los enfoques y exigido por la crítica — la consultora pasa a MANEJAR datos personales:** al copiar los 4.000 a una base propia, nuestra boutique pasa a **procesar datos personales por cuenta del cliente**. Esto exige:
- **Acuerdo de protección de datos entre cliente y consultora** (no solo entre cliente y proveedor).
- **Dónde viven los 4.000 durante el proyecto**, cifrados, con acceso controlado por rol.
- **Borrado o devolución al cierre** del trabajo.
- Reconocer que introducimos un **nuevo punto de riesgo de brecha** en nuestro primer proyecto: se cierra **antes** de tocar la base, no después.

**Monetización — CONGELADA hasta cerrar el permiso legal (decisión de gobierno inmediata):**
- **Estudios de salarios:** ⚠️ posible bandera roja legal. Los datos salariales vienen de negociaciones con clientes, probablemente bajo acuerdo de confidencialidad. En mercados pequeños se pueden **volver a identificar aun estando agregados** ("el salario del director financiero de la empresa X"). *Camino positivo, no solo "no":* explorar **una alianza con un proveedor licenciado de datos salariales**, o un producto futuro con anonimización irreversible (no se puede volver a identificar a la persona; con un mínimo de personas por grupo) **y** verificación contractual de que se tiene derecho a reutilizar el dato. No entra a la ruta crítica ni se promete el viernes.
- **Venta cruzada de capacitaciones:** usa los datos para un fin distinto al consentido; bloqueado hasta tener consentimiento separado y opción de salida. Hasta Fase 1.

---

## 14. Indicadores de salud de la base

**Para el negocio:** estos indicadores convierten "tenemos oro" en un punto de partida medido. Sin ellos, el "60% del valor" es una corazonada; con ellos, se confirma o se desarma con datos.

**Reportar siempre con el `n` al lado y sus salvedades** (a volumen boutique, casi todo indicador de embudo tiene pocos casos; no presentar ruido como tendencia).

| Indicador | Definición | Hoy | Meta escalonada ⚠️ |
|---|---|---|---|
| **% vigente** | candidatos con datos/consentimiento de menos de 12 meses | Desconocido | medir en la prueba → ≥50% en 6–9 meses |
| **% contactable** | correo/teléfono válido | Desconocido | ≥70% de los vigentes |
| **% que se puede ordenar** | CV con extracción exitosa | Desconocido | medir por grupo |
| **% etiquetado** | con habilidad/sector normalizado a ESCO | ~0% | 100% de la base vigente |
| **Tasa de duplicados** | registros fusionados / total | Desconocido | medir → mantener bajo |
| **Tasa de casos sin encajar en el vocabulario** | habilidades sin mapear a ESCO | — | < umbral a definir |
| **Incidentes de duplicado** (candidato reenviado) | número por trimestre | ≥1 (ya ocurrió) | **→ 0** |
| **% de vacantes cubiertas con la propia base** | colocaciones servidas desde la base vs buscar de nuevo | Desconocido (¡ni el total!) | punto de partida → 30–40% en 6–9 meses |

**La métrica guía del activo de datos:** `candidatos vigentes y contactables, etiquetados por habilidad/sector` + `% de vacantes cubiertas con la propia base`. Eso convierte "tenemos oro" en un punto de partida medido y desarma o confirma el "60% del valor" **con datos**.

> **Tablero de auditoría de vigencia** (Fase 0): el primer entregable de datos. Convierte "4.000" en un número honesto.

---

## 15. Secuencia por fases con criterios concretos de seguir/parar

**Para el negocio:** cada fase tiene una puerta con números, no adjetivos. Si los números no dan, se para y se cambia de rumbo. Esto evita gastar de más persiguiendo un activo que no rinde.

| Fase | Entregables de datos | Esfuerzo agregado ⚠️ | Seguir/Parar (cifras, no adjetivos) |
|---|---|---|---|
| **−1 Prueba rápida** | Semáforo de factibilidad: conexión técnica + vigencia + país + set de decisiones de referencia | 1 sem | **SEGUIR si** la conexión técnica permite extraer Y la vigencia muestral es ≥40%. Si no → replantear a "exprimir Team Tailor" |
| **0 Identidad** | Extracción de solo lectura · quitar duplicados · línea de tiempo candidato-cliente · tablero de vigencia · diccionario v0 | 2–4 sem | **SEGUIR si** se detecta ≥X% de duplicados + se entrega el tablero de vigencia + funciona la alerta anti-reenvío |
| **1 Estructura+Frescura** | Modelo único · ordenado+control de calidad · ESCO+ajuste local · gobernanza/consentimiento/retención · nota de vigencia | (programa de varios meses — **no "esfuerzo bajo"**) | **SEGUIR si** ≥80% de la base vigente está etiquetada + marco legal cerrado + acuerdo de protección de datos cliente-consultora firmado |
| **2 Búsqueda** | Filtros estructurados → búsqueda inteligente → búsqueda combinada · piloto 1 sector | Medio | **SEGUIR si** el piloto demuestra resultados útiles en 1 sector con precisión validada por el reclutador |
| **3 Producto** | Portal de auto-actualización · monetización (solo si el permiso legal lo permite) | Alto | **SEGUIR solo si** legal valida el uso + consentimiento detallado acumulado |

**Criterio de paro explícito:** si al cierre de Fase 0 la vigencia real resulta < 25% o la conexión técnica no soporta una sincronización viable, **se detiene la construcción de datos** y se cambia a "exprimir Team Tailor + quitar duplicados en hoja/campo", sin capa propia.

---

## 16. Costo, asequibilidad y personal (lo que la crítica exigió y faltaba)

**Para el negocio:** el cliente puede pagar ~US$1.5k–2.7k; el programa completo cuesta mucho más. La recomendación honesta es empezar barato exprimiendo lo que ya pagan, y solo construir si los números lo justifican.

**Realidad económica:** el cliente ancla en **~US$1.5k–2.7k** (3 meses de una asistente temporal ⚠️). El programa completo de datos (capa propia + ordenado + ESCO + identificación de personas + nota de vigencia + gobernanza + legal) es **fácilmente un esfuerzo de varios meses de trabajo senior**. **El proyecto completo probablemente supera lo que una PYME de 10 personas puede financiar.**

**Recomendación por defecto — "camino de compra suficientemente bueno":**
1. Activar la IA y funciones que **Team Tailor ya cobra** y no usan.
2. **Quitar duplicados + línea de tiempo** en un campo del sistema actual / hoja controlada (Fase 0, bajo costo).
3. Procedimientos simples y diccionario de datos (vocabulario común) — barato, alto valor.
4. **Reservar la construcción a medida** (base de búsqueda, ordenado masivo, portal) **solo si** el % de vacantes cubiertas con la propia base y los números lo justifican con datos de la prueba.

**Personal (capacidad de NUESTRA consultora):** Víctor es experto en datos/IA pero **no en RRHH ni en cumplimiento legal**. La parte legal (registro de datos que exige la ley, retención, riesgo de competencia desleal en los estudios de salarios, acuerdos de protección de datos) **se subcontrata a un abogado de datos local** — no se promete hacerla en casa. El ordenado/control de calidad masivo y la curaduría de ESCO requieren manos calificadas que hoy no tenemos asignadas; se dimensionan en la propuesta, no se ocultan tras etiquetas de "esfuerzo bajo".

**La asistente temporal:** su tiempo va a **descargar la operación de Lili** (su pedido real, evita quemar a la persona clave) y, en lo posible, a apoyo de etiquetado supervisado — **no** a las dos cosas a la vez ni a documentar el "ojo clínico" (eso requiere a Virginia/Lili).

---

## 17. Supuestos a validar (⚠️) y condiciones bloqueantes

**Para el negocio:** estos son los puntos que, si no se cierran, frenan todo. Los dos primeros se cierran hoy.

| # | Supuesto | Tipo | Dueño |
|---|---|---|---|
| 1 | País de operación y ley aplicable | **Condición bloqueante** — cerrar HOY | Virginia |
| 2 | Team Tailor permite extraer la información en el plan contratado | **Condición bloqueante** | Víctor (prueba) |
| 3 | 30–50% de la base está vencida | Supuesto a medir en la prueba | Víctor |
| 4 | Existe set de decisiones de referencia / historial recuperable | Supuesto frágil — probablemente **NO existe** | Lili |
| 5 | Existe identificador único (cédula/DPI) | A verificar | Víctor |
| 6 | Origen de los 4.000: ¿se postularon o los buscamos en LinkedIn? | Determina el permiso legal para monetizar | Virginia |
| 7 | Volumen real (vacantes/mes, colocaciones/año) | Determina el retorno y la validez estadística | Virginia |
| 8 | Idioma de los CV (solo español o mixto) | Afecta el ordenado y la búsqueda inteligente | Prueba |

---

## 18. Riesgos clave y mitigaciones

**Para el negocio:** los riesgos altos son legales, de reputación y de gastar de más. Todos tienen una mitigación concreta y barata si se hacen en orden.

| Riesgo | Sev. | Mitigación |
|---|---|---|
| **Legal:** monetizar/reutilizar datos sin permiso legal ni anonimización | Alto | Congelar toda monetización hasta cerrar gobernanza; confirmar país; anonimización irreversible + mínimo de personas por grupo |
| **Vencimiento subestimado:** "oro" sobrevalorado si 30–50% está vencido | Alto | Auditoría de vigencia en la prueba **antes** de invertir en enriquecer |
| **Errores de identidad:** fusionar 2 personas = brecha de privacidad | Alto | Umbrales conservadores, revisión humana, fusión **reversible** |
| **Conexión técnica de Team Tailor no verificada** sostiene media estrategia | Alto | Prueba pagada que la confirma antes de prometer nada |
| **Consultora como nuevo punto de riesgo de brecha de datos personales** | Alto | Acuerdo de protección de datos cliente-consultora, cifrado, acceso por rol, borrado al cierre |
| **Mudarse del sistema actual demasiado pronto** replica el desorden en un sistema más caro y rompe la operación (63% de ingresos) | Alto | NO mudarse hasta tener estructura + caso de negocio; agotar las funciones que ya pagan |
| **No recuperar la inversión a escala boutique** por construir de más | Medio | Comprar antes que construir; construir solo si los números lo justifican |
| **Costo real del ordenado** subestimado (control de calidad, ESCO, duplicados) | Medio | Presupuestar el trabajo calificado, no solo el cómputo |
| **La captura manual fracasa** con el equipo saturado | Medio | Automatizar enriquecimiento y frescura; portal de auto-actualización |

---

### Cierre

La estrategia de datos de Conexión Talento no es un proyecto de datos masivos ni de búsqueda inteligente vistosa. Es **plomería disciplinada**: una forma única de identificar a cada persona, quitar duplicados con memoria, frescura medida y un vocabulario común — todo construido **sobre** el sistema que ya pagan, **bajo** un marco de gobernanza que hoy no existe, y **solo hasta donde la economía de una boutique lo justifique**. Hecho en ese orden, los 4.000 registros dejan de ser una cifra de vanidad y se vuelven, por primera vez, un activo vivo, buscable y defendible. Hecho al revés, le ponemos un motor de Fórmula 1 a un carro sin ruedas.
