# Arquitectura de la Solución
## Conexión Talento — Sistema de Reclutamiento Asistido por IA

> **En una frase:** la IA acelera el reclutamiento de 5 días a horas sin perder el "ojo clínico" de Virginia, porque siempre decide una persona; lo que entregamos es un copiloto, no un piloto automático.

> **Documento de diseño.** Describe cómo será el sistema, sus piezas de IA, los controles de seguridad y cuánta libertad tiene cada pieza para actuar sola. Es un documento de diseño funcional; el calendario, el precio y el plan de recursos están en los entregables de *Roadmap por Fases* y *Propuesta Comercial*. Todo supuesto que el cliente aún no ha confirmado se marca con ⚠️ y se lista en §10 como condición que hay que resolver antes de avanzar.

---

## 1. Principios de diseño (las cinco reglas que gobiernan toda decisión)

**Para el negocio:** estas cinco reglas evitan que el proyecto se desvíe. Cuando dos caminos técnicos compiten, gana el que las respeta. No partimos de la tecnología; partimos de resolver las tensiones que detectamos en el análisis.

1. **El proceso antes que la tecnología.** Ninguna pieza de IA se construye sobre una etapa que no tenga su procedimiento escrito, sus criterios de evaluación claros y su punto de partida medido. La IA solo digitaliza un procedimiento ya documentado; sin procedimiento no hay nada que programar. *Esto es el filtro "Listo para IA".*
2. **Siempre una persona validando donde se decide sobre personas.** La IA pre-ordena, muestra evidencia y redacta borradores; el reclutador decide. Toda comunicación negativa a un candidato (un rechazo) pasa por revisión humana. No es por cumplir la ley: es el diferenciador de "cercanía" de la firma convertido en diseño.
3. **Reglas fijas donde se pueda, IA solo donde aporte.** Quitar duplicados, decidir a quién pasa según un umbral y maquetar el CV son reglas fijas, no IA. La IA se reserva para lo que ninguna regla resuelve: leer, extraer datos, ordenar y resumir.
4. **Comprar antes que construir.** A escala boutique (~20-60 colocaciones/año ⚠️), construir infraestructura propia rara vez se paga. Primero exprimir lo que el sistema actual (Team Tailor) **ya cobra**; construir a medida solo donde los datos demuestren que vale la pena. *Declaramos el conflicto de interés: nuestro ingreso crece cuanto más construimos a medida; por eso esta regla está escrita como principio, no como excepción.*
5. **El dato nunca lo inventa la IA.** Salarios, competencias y experiencia se citan siempre a su fuente (el CV, una encuesta licenciada, el sistema de candidatos). La IA jamás muestra un número que no pueda rastrear. Prohíbe que invente con tono de autoridad.

---

## 2. Reencuadre honesto: no son "6 agentes autónomos"

**Para el negocio:** vender "seis robots que trabajan solos" a un equipo de 10 personas, sin métricas ni procesos escritos, infla el costo, el riesgo y crea un sistema imposible de controlar. Hay que retar esa visión con rigor, no comprarla.

El cliente imagina seis agentes de IA. De los seis, solo uno (el Sourcer) es de verdad *autónomo* —es decir, decide solo, paso a paso, qué hacer a continuación. Los otros cinco son **herramientas que leen, extraen, puntúan o redactan contra un formato fijo y devuelven el control a la persona.**

La distinción no es de palabras: cambia el costo, el riesgo legal y cuánta libertad damos a la máquina. La arquitectura correcta para la fase temprana es:

> **3 herramientas de reglas fijas confiables + 1 orquestador con reglas + 1 capa de IA asistida** — y la autonomía real reservada para cuando el proceso esté probado.

Mantenemos la palabra "agente" en la conversación con el cliente por continuidad con su visión, pero la **ficha de cada uno declara qué es de verdad y cuánta libertad tiene** (§3).

---

## 3. Los seis componentes de IA

Cada componente se describe con su función, qué recibe, qué entrega, sus controles de seguridad, su nivel de libertad para actuar y —lo crítico— **qué entrega asistido (con persona aprobando) frente a qué haría solo**. La libertad se mide en tres niveles:

- **N1 – La IA sugiere:** produce un borrador o un orden; la persona edita y aprueba todo antes de cualquier acción hacia afuera.
- **N2 – La IA actúa con excepciones:** trabaja dentro de un rango ya aprobado; la persona revisa por muestreo o solo los casos raros.
- **N3 – Autónomo acotado:** ejecuta sin revisión caso por caso, con registro y auditoría posterior. **Ningún componente que decida sobre una persona o que se comunique con un candidato o cliente llega a N3.**

### 3.1 Cuadro maestro de componentes

| # | Componente (visión cliente) | Qué es de verdad | Función | Libertad objetivo | Fase |
|---|---|---|---|---|---|
| 1 | **Perfilador** | Herramienta que consulta fuentes + plantilla | Genera borrador de competencias, preguntas y rango salarial **citado a su fuente** | N1 | 2 |
| 2 | **Redactor de perfil** | Herramienta (cadena de instrucciones) | Redacta el perfil del puesto ajustado al tamaño y contexto de la empresa | N1 | 2 |
| 3 | **Sourcer** | Agente (el único de verdad autónomo) | Itera búsquedas y genera preguntas para revelar el perfil real | N2 | 3 |
| 4 | **Asistente que ordena candidatos** (Screener / Ranker) | Herramienta que puntúa + enruta con reglas | Lee ~200 CVs, puntúa contra una hoja de criterios, los ordena, propone top 10 | N1 → N2 (solo el tramo de rechazo, 30+) | 2 |
| 5 | **Entrevistador de pre-filtro** | Comprado (transcripción) + herramienta de resumen | Transcribe, resume por formato, detecta competencias con cita, sugiere preguntas | N1 | 2 |
| 6 | **Generador de CV con marca de la firma** | Herramienta (extrae a formato + plantilla fija) | Normaliza el CV y produce el documento con la marca de la firma | N2 | 0–1 (logro rápido) |

> **El componente "cero", el más importante y que el cliente no listó:** la **verificación de duplicados candidato-cliente** (§3.7). No es IA, y es el de mayor relación impacto/esfuerzo. Resuelve un riesgo de reputación que ya ocurrió ("mandé el mismo candidato dos veces").

A continuación, la ficha de cada uno.

---

### 3.2 Agente 1 — Perfilador

| Atributo | Detalle |
|---|---|
| **Función** | Producir un borrador ordenado de competencias críticas, banco de preguntas y referencia de salario de mercado para un puesto o sector. |
| **Qué recibe** | Sector, puesto, nivel, contexto de la reunión de arranque (§4); biblioteca curada de competencias; **fuente salarial con licencia o base propia con un mínimo de casos** ⚠️. |
| **Qué entrega** | Datos ordenados: 3-5 competencias, banco de preguntas de comportamiento por competencia, rango salarial **con fuente y fecha citadas**. |
| **Controles de seguridad** | (1) **Prohibido mostrar cifras salariales inventadas por la IA** — solo datos con fuente verificable, o el campo queda vacío con la nota "sin dato confiable". (2) No opina fuera del catálogo de competencias curado. (3) Toda salida es un borrador editable. |
| **Libertad** | **N1 – La IA sugiere.** El reclutador valida y ajusta antes de usar. |
| **Asistido vs. autónomo** | **Solo asistido, indefinidamente.** El estudio de salarios vendible es de Fase 3 y depende de tener base legal (ver *Documento de Datos y Legal*); aquí solo se usa adentro y citado. |

---

### 3.3 Agente 2 — Redactor de perfil de puesto

| Atributo | Detalle |
|---|---|
| **Función** | Redactar el perfil del puesto a partir de la reunión de arranque, ajustado al tamaño y contexto de la empresa-cliente. |
| **Qué recibe** | La hoja de arranque y de criterios completada (§4); la plantilla única de perfil de puesto de la firma. |
| **Qué entrega** | Borrador del perfil en la plantilla estándar, con requisitos obligatorios, deseables y la definición de éxito a 90 días. |
| **Controles de seguridad** | Estructura fija por plantilla (la IA redacta, no inventa requisitos); no agrega competencias fuera de la hoja de criterios. |
| **Libertad** | **N1 – La IA sugiere.** |
| **Asistido vs. autónomo** | Asistido. Es el paso 2 del proceso; depende al 100% de que el paso 1 (la reunión de arranque) esté estandarizado. |

---

### 3.4 Agente 3 — Sourcer *(el único de verdad autónomo)*

| Atributo | Detalle |
|---|---|
| **Función** | Iterar búsquedas sobre la base ya enriquecida y generar preguntas para revelar el perfil real del candidato. |
| **Qué recibe** | Hoja de criterios; base de talento enriquecida y vigente (condición previa: §3.8 ordenada); fuentes externas (LinkedIn ⚠️ según sus términos). |
| **Qué entrega** | Conjunto de candidatos vigentes con la justificación de por qué encajan; preguntas para revelar el perfil. |
| **Controles de seguridad** | Solo busca sobre candidatos **vigentes y con permiso válido**; no contacta solo; presenta resultados al reclutador. |
| **Libertad** | **N2 – La IA actúa con excepciones** (solo itera búsquedas; el contacto siempre es humano). |
| **Asistido vs. autónomo** | **Aspiracional, Fase 3.** Depende de que la base esté ordenada, sin duplicados y con una medida de vigencia. Sin eso, devuelve basura con tono seguro. No se promete en fase temprana. |

---

### 3.5 Agente 4 — Asistente que ordena candidatos (Screener / Ranker) *(el de mayor palanca y mayor riesgo)*

**Para el negocio:** aquí está el grueso del valor (el paso 4 concentra casi todo el trabajo manual) **y** el mayor riesgo legal y de reputación (filtrar candidatos de forma automática es decidir sobre personas, y un sesgo se multiplica al pasar 200 CVs por proceso).

| Atributo | Detalle |
|---|---|
| **Función** | Leer ~200 CVs, puntuar cada uno contra la hoja de criterios, ordenarlos y proponer top 10. |
| **Qué recibe** | CVs (texto extraído); **hoja de criterios con pesos construida CON Virginia**; set de decisiones de referencia con ternas históricas (los casos que enseñan a la IA a elegir como Virginia) ⚠️ (ver §10). |
| **Cómo procesa la información** | (1) **Borrar datos personales sensibles** (quitar foto, edad, estado civil, nacionalidad y nombre como criterios) → (2) extraer evidencia contra cada criterio → (3) puntuar **con la justificación citada al texto del CV** (sin inventar) → (4) ordenar. |
| **Qué entrega** | Orden con puntaje por criterio + cita de la evidencia; los tres tramos del semáforo de enrutamiento (§5). |
| **Controles de seguridad** | (1) **El orden NUNCA es decisión final automática.** (2) **Borrar datos personales sensibles obligatorio antes de puntuar** (equidad + poder defenderlo). (3) Justificación rastreable al CV; cero conclusiones sin respaldo. (4) **Revisión de sesgo antes de poner en producción** (tasa de selección por género/edad; excluir criterios prohibidos). (5) Registro de cada decisión. |
| **Libertad** | **N1 en el top 10 y la terna** (la persona aprueba). **N2 solo en el tramo de la posición 30 en adelante**, para *preparar* (no enviar) lotes de rechazo. |
| **Asistido vs. autónomo** | **Asistido siempre en lo que toca a una persona.** Se mide cuánto coincide con el "ojo clínico" de Virginia ("coincidió en X de 10") para construir confianza con evidencia. Los criterios le ganan a la IA; la persona le gana a los criterios mientras se calibra. |

---

### 3.6 Agente 5 — Entrevistador de pre-filtro

| Atributo | Detalle |
|---|---|
| **Función** | Escuchar y transcribir la llamada de pre-filtro, resumirla por formato, detectar competencias con evidencia y sugerir preguntas de seguimiento. |
| **Qué recibe** | Audio de la llamada **con permiso explícito de grabación**; guía de entrevista estructurada ligada a la hoja de criterios. |
| **Qué entrega** | Transcripción + resumen ordenado: competencias detectadas **con cita textual**, alertas, preguntas sugeridas. |
| **Controles de seguridad** | (1) **Pedir permiso de grabación al inicio de cada llamada** (guion obligatorio). (2) La IA **no concluye si la persona es apta** — detecta y resume; el reclutador evalúa. (3) Tiempo de retención de audios y transcripciones definido; la voz puede ser un dato biométrico. |
| **Libertad** | **N1 – La IA sugiere.** |
| **Asistido vs. autónomo** | Asistido. La transcripción se **compra** (no se construye), con calidad para el español de la región. |

---

### 3.7 Agente 6 — Generador de CV con marca de la firma *(el logro rápido visible)*

| Atributo | Detalle |
|---|---|
| **Función** | Tomar un CV crudo y producir el documento estandarizado con la marca de la firma, idéntico sin importar cuál de los 4 reclutadores lo opere. |
| **Qué recibe** | CV crudo (PDF o texto); las instrucciones de Virginia **formalizadas, con control de versiones y propiedad de la firma**; plantilla de marca de formato fijo. |
| **Qué entrega** | CV con la marca de la firma. **La IA solo extrae los datos a un formato fijo y redacta el resumen; el maquetado lo hace una plantilla fija, no lo decide la IA** (elimina la variabilidad). |
| **Controles de seguridad** | No decide nada sobre la persona (riesgo bajo); estructura forzada por el formato; no inventa experiencia. |
| **Libertad** | **N2 – La IA actúa con excepciones** (genera el documento; el reclutador revisa antes de enviarlo al cliente). |
| **Asistido vs. autónomo** | Logro rápido de **semana 1-2**. Entregable visible que demuestra el método sin riesgo. **Condición de cumplimiento previa:** dejar de meter datos personales de candidatos en el ChatGPT de consumo y migrar a una conexión empresarial con compromiso de no-entrenamiento y acuerdo de protección de datos firmado (el proveedor no usa ni entrena con los datos). Es una brecha activa hoy. |

---

### 3.8 Componente 0 — Verificación de duplicados candidato-cliente *(no es IA, es el más rentable)*

| Atributo | Detalle |
|---|---|
| **Función** | Antes de enviar una terna, verificar si el candidato ya fue presentado a ese cliente (y detectar si dijo falsamente que no había participado antes). |
| **Qué recibe** | Historial candidato × cliente × fecha (sacado del sistema de candidatos vía conexión técnica entre sistemas ⚠️ o, si no, de una hoja de cálculo o un campo del propio sistema). |
| **Qué entrega** | Alerta de duplicado + línea de tiempo del candidato. |
| **Tecnología** | **Cruce de identidad con reglas fijas** (correo/teléfono/cédula) + coincidencia aproximada de nombre. **Base de datos + regla, cero IA** (meterle IA introduciría errores de detección). |
| **Libertad** | **N2 – alerta dura** (bloquea el envío hasta que una persona confirme). |
| **Nota** | Es el embrión del "mercado interno" e historial. **No convertirlo en lista negra compartida ni en exclusión automática:** informa al reclutador, no decide. |

---

## 4. Condición transversal: la reunión de arranque estandarizada

**Para el negocio:** el verdadero cuello de botella no es el cribado, es la toma de requisitos al inicio (pasos 1-2). Ningún componente tiene criterios que aplicar sin esto.

El documento que alimenta a *todos* los agentes es la **hoja de arranque + criterios de 1 página por vacante**: contexto de la empresa, 3-5 competencias críticas, requisitos obligatorios frente a deseables con sus pesos, señales de descarte, rango salarial y definición de éxito a 90 días.

```
                 ┌──────────────────────────────────────┐
                 │  HOJA DE CRITERIOS / ARRANQUE (1 pág) │
                 │  (lo hace una persona, paso 1-2)      │
                 └──────────────────────────────────────┘
                        │ alimenta a TODOS los componentes
   ┌───────────┬────────┼────────┬───────────┬───────────┐
   ▼           ▼        ▼         ▼           ▼           ▼
Perfilador  Redactor  Sourcer  Screener  Entrevistador  GenCV
```

---

## 5. Cómo se coordinan las piezas (orquestación)

**Para el negocio:** el cliente ya definió los umbrales correctos. La arquitectura los **convierte en reglas fijas en código** (no en una instrucción a la IA, que la IA podría ignorar) y **corrige el punto ciego legal del rechazo automático**.

```
        El asistente puntúa 200 CVs contra la hoja de criterios
                              │
                   ┌──────────┴──────────┐
                   ▼                      ▼
       Borrar datos personales    Registro + justificación citada
                   │
                   ▼
         ┌─────────────────────────────────────────────┐
         │   ENRUTADOR DE REGLAS FIJAS (no IA)          │
         └─────────────────────────────────────────────┘
            │                  │                    │
        TOP 10            POSICIÓN 10-20         POSICIÓN 30+
            │                  │                    │
            ▼                  ▼                    ▼
   Reclutador valida   "Proceso sigue        Rechazo cordial
   → LLAMADA           abierto"              → ⚠️ REVISIÓN
   (N1: persona        (en espera,           HUMANA EN LOTE
    aprueba)           sin acción negativa)  antes de enviar
                                             (N2, nunca N3)
```

**Corrección crítica frente al diseño original del cliente:** el rechazo automático en la posición 30+ **no se envía solo**. Es el mayor pasivo legal y de reputación del diseño —en una empresa a la que *ya* atacan en LinkedIn por falta de seguimiento— y es una **decisión automatizada** (relevante si hay clientes o candidatos en la UE: el reglamento europeo trata el cribado como de alto riesgo). El rechazo se prepara en lote, lo revisa una persona y se envía con una plantilla **personalizada** (no el correo automático genérico a los 15 días). Esto protege a la vez el cumplimiento legal y el diferenciador de "cercanía".

---

## 6. Decisiones Comprar vs. Construir por componente

**Para el negocio:** a escala boutique, comprar o activar lo que ya existe casi siempre gana. Construir a medida solo donde no hay nada comprable que respete los controles de seguridad.

| Componente | Decisión | Justificación |
|---|---|---|
| **Funciones de IA del sistema actual** (emparejar, cribar, transcribir psicométricas) | **ACTIVAR** lo ya pagado | Team Tailor "tiene IA que no saben usar". Auditar y activar antes de comprar o construir nada. Valor inmediato a costo cero. |
| **Extraer datos del CV** | **Comprar** (conexión a IA externa) | Extracción a un formato con un modelo comercial; el cómputo cuesta poco (~US$0.01-0.03 por CV ⚠️). *El costo real no es el cómputo: es el control de calidad, quitar duplicados y mapear al vocabulario común.* |
| **Transcripción del pre-filtro** | **Comprar** | Comprar una transcripción de calidad para el español de la región. Construirla no diferencia. |
| **Modelos de IA** | **Comprar** (conexión técnica) | Familia Claude a través de una conexión técnica (ver §8). Nunca entrenar modelos propios. |
| **Vocabulario común de habilidades** | **Comprar/Adoptar** (ESCO) + capa local | ESCO es gratuita y multilingüe (en español). *No es "gratis": curar la capa de 15-30 sectores centroamericanos y ordenar el texto libre es trabajo real.* |
| **Base de datos para búsqueda semántica** | **Comprar gestionada** (pgvector) | No construir infraestructura. Y **solo en Fase 2+**, sobre una base ya limpia. |
| **Verificación de duplicados** | **Construir ligero** (base de datos + regla) | Trivial y sin alternativa exacta comprable; cuestión de horas. |
| **Generador de CV con marca** | **Construir ligero** (extraer + plantilla) | La marca es propia; el esfuerzo es formalizar las instrucciones que ya existen. |
| **Hoja de criterios / set de decisiones de referencia** | **Construir con el cliente** | Es el "ojo clínico" de Virginia; nadie lo vende. Es un artefacto humano, no de software. |
| **Almacén propio de datos** | **Posponer** | Solo si el caso de negocio lo justifica tras la prueba rápida de factibilidad. No migrar por impulso. |
| **Estudio de salarios de mercado** | **NO construir aún** | Bandera legal (competencia/datos) + riesgo de que la IA invente. Camino positivo: alianza con un proveedor con licencia, o un producto futuro con permiso explícito. |

---

## 7. Rol de Team Tailor

**Para el negocio: ampliar lo que tienen, no reemplazarlo.** Team Tailor es donde viven los candidatos hoy y ya trae acuerdo de protección de datos y funciones de cumplimiento. Migrar 4.000 registros sin orden replicaría el desorden en un sistema más caro, le trasladaría a una empresa de 10 personas toda la responsabilidad de seguridad, brechas y derechos de los datos, y pondría en riesgo la operación que genera el 63% de los ingresos.

| Función | Quién la cumple en la arquitectura objetivo |
|---|---|
| Registro de candidatos, vacantes, postulaciones y etapas | **Team Tailor** (se queda) |
| Integración con LinkedIn, envío de psicométricas, correos | **Team Tailor** (activar y afinar lo que ya tiene) |
| Etapas estandarizadas (requisito previo para medir) | **Team Tailor** (configurar 6-8 etapas únicas) |
| Capa de coordinación, puntaje, duplicados, enriquecimiento | **Capa propia delgada vía conexión técnica** ⚠️, *por encima* del sistema actual |
| Punto de partida medido de las métricas | **Análisis del registro de actividad del sistema** ⚠️ |

> **Supuesto que bloquea todo ⚠️:** toda la capa propia depende de que **el plan contratado de Team Tailor permita una conexión técnica de lectura/escritura y extraer la información en bloque sin un límite de uso prohibitivo.** No verificado. Es la dependencia que más peso carga del diseño. **Plan B si falla:** operar la capa de duplicados y puntaje sobre extracciones manuales periódicas + exprimir al máximo las funciones nativas del sistema. La decisión de "dejar Team Tailor o no" se pospone hasta tener evidencia de los límites de la conexión técnica y un caso de negocio con datos.

---

## 8. Tecnología recomendada (a alto nivel)

| Capa | Recomendación | Nota |
|---|---|---|
| **Modelos de IA** | Familia **Claude vía conexión técnica** ⚠️ *(validar los identificadores y precios vigentes contra la documentación oficial al momento de construir)*. Modelo de **razonamiento** para el asistente que ordena candidatos y el resumen de entrevistas (donde se exige fidelidad y poder rastrear todo); modelo **rápido y económico** para extraer datos de muchos CVs y ordenarlos. Configurado con **salida forzada a un formato fijo** para que la IA no pueda "opinar fuera de su rango". | Sin compromiso de no-entrenamiento + acuerdo de protección de datos, no se procesan datos personales. |
| **Extraer datos del CV** | IA → datos en formato estricto (experiencia, habilidades, sector, ubicación, idiomas, educación, pretensión salarial) + **una capa de validación** (detección de inconsistencias + revisión humana del 5-10%). | Nunca tratar el dato extraído como verdad sin rastrearlo al CV original. |
| **Búsqueda** | **Mixta**: filtros por dato exacto (sector, habilidad, vigencia, ubicación) + similitud por significado (búsqueda semántica en **pgvector**). | **Es la última milla, no la primera.** Orden obligatorio: identidad → orden → vigencia → vocabulario común → *recién entonces* similitud por significado. Buscar por significado sobre la base sucia de hoy devuelve basura con tono seguro. |
| **Almacén** | Postgres + almacenamiento de archivos para los PDFs. | Solo si se justifica; cifrado, control de acceso, acuerdo de protección de datos cliente-consultora, borrado al cierre. |
| **Vocabulario común de habilidades** | ESCO (esqueleto) + capa local de 15-30 sectores. | Ordena el texto libre de "4 personas, 4 criterios". |
| **Borrar datos personales** | Capa que quita los datos personales antes de puntuar. | Equidad + poder defenderlo. |
| **Integración** | Conexión técnica con Team Tailor ⚠️; sincronización incremental. | Capa propia portable por diseño. |

---

## 9. Diagrama del flujo de punta a punta

```
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 1-2  ARRANQUE + HOJA DE CRITERIOS (persona, consultivo)           │
│   Reclutador + cliente → hoja 1 pág.  ──►  Redactor (N1) borrador      │
│   de perfil de puesto                                                  │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 3  BÚSQUEDA DE CANDIDATOS                                         │
│   Sourcer (N2, Fase 3) busca sobre BASE ENRIQUECIDA + fuentes externas │
│   ── hoy: búsqueda manual / por habilidad sobre piloto de base ordenada│
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
        ┌────────────── VERIFICACIÓN DE DUPLICADOS (no IA, N2) ─────────┐
        │  ¿candidato ya presentado a este cliente?  → ALERTA DURA      │
        └───────────────────────────┬──────────────────────────────────┘
                                     ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 4  CRIBADO                                                        │
│   CVs ─► EXTRAER DATOS (IA→formato) ─► BORRAR DATOS PERSONALES ─►      │
│   ASISTENTE QUE ORDENA (N1) puntúa vs. criterios, cita evidencia ─►    │
│   ENRUTADOR DE REGLAS FIJAS:                                          │
│       top10 → llamada (persona aprueba)                               │
│       10-20 → en espera, sin acción negativa                         │
│       30+   → rechazo en LOTE con REVISIÓN HUMANA (jamás auto-envío)  │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 5  PRE-FILTRO                                                     │
│   Permiso de grabación ─► TRANSCRIPCIÓN (comprada) ─► RESUMEN ORDENADO │
│   (N1): competencias con cita, alertas, preguntas. La persona evalúa. │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 6-7  TERNA + CIERRE (persona: "ojo clínico", negociación, arte)   │
│   ── ZONA SIN AUTOMATIZAR: aquí vive el diferenciador.                │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ PASO 8  CV CON MARCA DE LA FIRMA                                       │
│   GENERADOR (N2): extrae a formato + plantilla fija. La persona        │
│   revisa antes de enviar.                                             │
└──────────────────────────────────────────────────────────────────────┘

  ◄── Transversal: punto de partida medido de métricas (análisis del
      registro del sistema) + registro de toda decisión de IA +
      compromiso de tiempo de respuesta al candidato
```

---

## 10. Honestidad sobre fases: copiloto vs. autónomo

**Para el negocio:** en el horizonte de este proyecto, el sistema es un copiloto, no un piloto automático. Esta tabla deja claro qué entregamos asistido hoy y qué NO dejamos correr solo (y por qué).

| Hoy entregamos (asistido, con persona) | NO entregamos autónomo (y por qué) |
|---|---|
| CV con marca de la firma estandarizado (N2) | Nada que decida sobre una persona corre sin persona |
| Verificación de duplicados con alerta dura (N2) | El rechazo nunca se auto-envía (sesgo no auditable + daño reputacional) |
| Asistente que pre-ordena, la persona aprueba (N1) | El orden nunca es decisión final automática |
| Resumen del pre-filtro con cita (N1) | La IA no concluye si la persona es apta |
| Perfilador/Redactor que hacen borradores (N1) | Cifras salariales inventadas por la IA |

**La verdad para el cliente:** en este proyecto, **el sistema es un copiloto, no un piloto automático.** La autonomía real (el Sourcer autónomo, monetizar la base, el estudio de salarios) es un "empezar pequeño y crecer": depende de tener la base ordenada y de cerrar las banderas legales, y **no se promete en fase temprana.** No es una limitación que haya que disculpar: es la decisión correcta. En una boutique que vive del "ojo clínico" y la cercanía, automatizar el juicio destruiría justo lo que la hace premium. La IA acelera de 5 días a horas **sin escalar la inconsistencia**; el "mismo día" solo aplica a coincidencias ya emparejadas de la base interna, no como métrica estrella.

---

## 11. Condiciones que bloquean (resolver antes de comprometer la arquitectura)

**Para el negocio:** estos supuestos sostienen todo lo anterior. Se resuelven en una **prueba rápida de factibilidad técnica y legal de ~1 semana antes de fijar el alcance**, no como "preguntas abiertas" que flotan.

| # | Supuesto ⚠️ | Si falla… | Dueño / acción |
|---|---|---|---|
| 1 | **País: El Salvador + Guatemala ✅** (confirmado). Falta validar el permiso de la base y la posible exposición a la UE | Define el alcance legal (Decreto 144/2024 SV vigente) y la viabilidad del estudio de salarios | Validar permiso/registro con Virginia |
| 2 | **Conexión técnica / extracción / plan de Team Tailor** | Se cae la verificación automática de duplicados, la extracción de datos y el punto de partida histórico | Verificar el plan real + plan B (extracciones manuales) |
| 3 | **Que exista el set de decisiones de referencia** (historial de ternas recuperable) | El asistente no replica el "ojo clínico"; construirlo exige el tiempo escaso de Virginia | Muestrear el historial; si no existe, financiar su construcción de forma explícita |
| 4 | **Vigencia y permiso de la base de 4.000** | El "60% del valor" se sobreestima; riesgo regulatorio | Auditar la vigencia (por muestreo) antes de invertir en enriquecerla |
| 5 | **Brecha activa: datos personales en el ChatGPT de consumo** | Transferencia de datos / posible entrenamiento con ellos | Cortar y migrar a una conexión empresarial con no-entrenamiento + acuerdo de protección de datos — **inmediato** |
| 6 | **Rol de la consultora como manejadora de datos personales** | Nuevo punto de brecha al exportar los 4.000 | Definir dónde viven los datos, cifrado, acuerdo de protección de datos cliente-consultora, borrado al cierre |

> **Sin esa prueba rápida, no se promete ningún logro rápido inicial.** Es la diferencia entre una presentación bonita de arquitectura y una arquitectura que aguanta el primer proyecto —que es de vida o muerte para la firma.
