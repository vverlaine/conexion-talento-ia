# Conexión Talento — Memoria del Proyecto

**Ordenar antes de automatizar · Sacar provecho a la base de candidatos · Demostrar valor con números**

> **En una frase:** Antes de poner inteligencia artificial, ponemos orden: estandarizamos el proceso, sacamos provecho a la base de ~4.000 candidatos y medimos para probar el valor con cifras, no con promesas.

> Este es el repositorio de trabajo del proyecto de Datos, Inteligencia Artificial y Transformación Digital para **Conexión Talento**. Este archivo es la puerta de entrada: en 3 minutos resume el reto, nuestra recomendación central, las apuestas grandes y dónde está cada documento.
>
> Estándar de calidad tipo McKinsey/BCG. Es un documento vivo — la versión oficial del diagnóstico está en [`01-descubrimiento/datos-clave.md`](./01-descubrimiento/datos-clave.md).

---

## 1. Resumen ejecutivo (léelo en 1 minuto)

**El reto.** Conexión Talento es una consultora boutique de headhunting (~10 personas, El Salvador como mercado principal y Guatemala como secundario). Su motor es Reclutamiento y Selección: **63% de los ingresos**. Aspira a ser "consultora de clase mundial", con la **cercanía al candidato** como su sello distintivo. Hoy opera con **cero estandarización** (4 reclutadores, 4 formas distintas de trabajar), **cero documentación**, **cero métricas**, y con el sistema donde se guardan los candidatos (Team Tailor) y una base de **~4.000 candidatos** desaprovechados. La contradicción: vende "cercanía" mientras la critican en LinkedIn por falta de seguimiento, y ya presentó dos veces el mismo candidato al mismo cliente. La CEO (Virginia, 20 años de oficio, "ojo clínico") imagina **6 "agentes" de inteligencia artificial** y velocidad "el mismo día"; pidió de forma explícita que la **retemos**.

**Nuestra recomendación central.** **No automatizar el desorden.** En una boutique que vive del criterio humano y de la cercanía, el sello distintivo **no es la inteligencia artificial, es la disciplina de proceso**. Por eso: **(1) estandarizar → digitalizar → DOCUMENTAR antes de automatizar**, y **(2) sacar provecho al "oro" de la base** — que hoy **no es oro, es oro sin refinar**: sin un identificador único por persona, sin etiquetas y sin protocolo de vigencia (probable 30–50% desactualizado ⚠️). El valor real está en la "plomería aburrida" (estándar, quitar duplicados, métricas, hoja de criterios para evaluar candidatos), no en la automatización vistosa.

**Las 4 apuestas mayores.**

| # | Apuesta | Por qué gana |
|---|---------|--------------|
| **A** | **Estandarizar el criterio antes que el software** — hoja de criterios para tomar el pedido del cliente, criterios explícitos del "ojo clínico" de Virginia y plantilla única de CV con la marca | Sin criterios escritos, ninguna herramienta de IA sabe qué aplicar; automatizar antes solo multiplica la inconsistencia a velocidad de máquina. Es lo que ningún competidor con IA copia sin la artesanía detrás. |
| **B** | **Métricas y punto de partida medido desde la semana 1** — reconstruidos del registro de actividad de Team Tailor, no inventados | "Cero métricas" es falso: el sistema ya guarda fechas y horas de cada paso. Sin un **punto de partida propio** no hay forma de probar el retorno ni de defender un precio premium. Es el argumento para **empezar pequeño y crecer**. |
| **C** | **Aprovechar la base SIN cambiar de sistema todavía** — quitar duplicados, reconstruir el historial candidato-cliente, auditar vigencia y estructura; **ampliar las capacidades de Team Tailor mediante conexiones técnicas entre sistemas antes de reemplazarlo** | Cierra el riesgo de reputación que ya ocurrió y convierte el "tenemos oro" en un número honesto. Cambiar de sistema sin ordenar primero solo copia el desorden a un sistema más caro y pone en riesgo el 63% de los ingresos. |
| **D** | **IA asistida, siempre con una persona validando, sobre un proceso ya ordenado** — empezar por el asistente que ordena candidatos según tus criterios y el generador de CV; **congelar la venta del comparativo de salarios** | 5 de los 6 "agentes" son en realidad herramientas que entregan un resultado ordenado, no agentes autónomos. El rechazo automático de candidatos y el comparativo salarial son las dos bombas legales y de reputación: requieren validación humana y revisión legal. |

**El camino (fases flexibles, con puntos de decisión seguir/no seguir).**

```
Fase -1  Prueba rápida de factibilidad (1 sem, pagada) → despeja los supuestos frágiles ANTES de cotizar
Fase 0   Quick win + diagnóstico (2-3 sem)             → CV estándar, quitar duplicados, primeras métricas, credibilidad
Fase 1   Estandarización + datos + métricas           → manuales de proceso, hojas de criterios, punto de partida medido, extracción de datos vía conexión técnica
Fase 2   IA asistida (piloto 1-2 módulos)             → asistente que ordena candidatos + generador de CV, siempre con persona validando y con frenos de seguridad
Fase 3   Escala y monetización (condicionada)         → enriquecer la base, mercado interno de talento, comparativo salarial (si la ley lo permite)
```

**Orden obligatorio (resuelve la tensión entre las distintas disciplinas):** estandarizar etapas y criterios → punto de partida medido y limpio → ordenar los datos → recién entonces IA. No se automatiza ninguna etapa sin su estándar documentado y su punto de partida medido. Para romper el círculo "se necesita el ojo clínico documentado para construir la herramienta que lo documenta", el **set de decisiones de referencia (los casos que enseñan a la IA a elegir como Virginia) se extrae en las primeras 2-3 semanas** con tiempo protegido de Virginia.

---

## 2. Lo que NO vamos a hacer (y por qué — el reto que pediste)

| Lo que el cliente quiere ya | Nuestra postura | Razón |
|---|---|---|
| Los **6 agentes** de IA | Pilotar **1-2** sobre un proceso ya ordenado | Vender 6 agentes sin métricas ni documentación es vender humo en el primer proyecto. |
| Velocidad **"el mismo día"** | Comprometer el **tiempo hasta entregar la terna** (lo que sí controlamos); enterrar el "mismo día" | El cierre depende del cliente y del preaviso del candidato. Prometerlo siembra decepción. |
| **Vender el comparativo** de salarios | **Congelado** hasta validar la base legal | Riesgo de prácticas anticompetitivas + protección de datos + posibilidad de re-identificar personas en un mercado pequeño + posible incumplimiento de los acuerdos de confidencialidad con los clientes que pagan el 63%. Salida positiva: alianza con un proveedor que ya tenga licencia. |
| **Salir de Team Tailor** | **No cambiar** de sistema aún; ampliar sus capacidades vía conexión técnica | Es una decisión de la Fase 3, con datos, no por impulso. |
| **+1 persona** (pedido de Lili) | Redirigir el presupuesto de la persona temporal a **ordenar y documentar**, y reposicionar el puesto como **"Embajador de Marca / Experiencia del Candidato"** | El problema no es falta de manos, es falta de proceso. Un 5º reclutador sin estándar añade una 5ª forma de hacer las cosas. |

---

## 3. Guía de navegación del repositorio

| Carpeta | Qué contiene | Estado |
|---|---|---|
| [`00-memoria/`](./00-memoria) | **Bitácora viva** del proyecto: sesiones, decisiones, alertas y pendientes. La entrada más reciente va arriba. Empezar aquí para ponerse al día. | Activa |
| [`01-descubrimiento/`](./01-descubrimiento) | Información cruda y su interpretación: `transcripcion-llamada-01-raw.md` (la llamada palabra por palabra) y **`datos-clave.md` (la versión oficial** del diagnóstico, con supuestos marcados ⚠️). | Completa (Sesión 01) |
| [`02-solucion/`](./02-solucion) | Diseño de la solución: `arquitectura-solucion.md`, `estrategia-datos.md`, `riesgos-y-cumplimiento.md`. Los "6 agentes" replanteados, el modelo de datos, y el registro de datos que exige la ley (El Salvador / Decreto 144/2024). | Completa (v1) |
| [`03-roadmap/`](./03-roadmap) | `roadmap-fases.md` (fases, entregables, puntos de decisión seguir/no seguir, condiciones para abortar) y `metricas-exito.md` (cuadro de indicadores + cómo medir el punto de partida). | Completa (v1) |
| [`04-propuesta/`](./04-propuesta) | **Entregables del viernes:** `Propuesta-Conexion-Talento.pdf` (propuesta detallada, 16 pp.) + `Presentacion-Conexion-Talento.pptx` (presentación ejecutiva, 17 láminas). Origen: `*.md` + `assets/` (estilos y generador). También `propuesta-comercial.md` (versión larga, de uso interno). | **PDF + PPTX listos** |
| [`99-research/`](./99-research) | Investigación de apoyo. Ver [`99-research/README.md`](./99-research/README.md). Incluye: `team-tailor.md` (qué hace el sistema y su conexión técnica entre sistemas), `marco-legal-datos-sv-gt.md` (El Salvador + Guatemala), `benchmark-ia-rrhh.md` y `pricing-engagement.md`. | Completa (v1) |

**Convención:** las carpetas siguen el orden del proyecto (`00`→`04`), con `99-research` como anexo transversal. Todo dato no confirmado se marca `⚠️ a validar`.

---

## 4. Estado del proyecto

**Sesión actual:** 01 — Descubrimiento y diagnóstico (2026-06-29). Ver [`00-memoria/bitacora.md`](./00-memoria/bitacora.md).

**Hecho:** repositorio creado · transcripción y datos clave capturados · análisis desde múltiples ángulos (8 enfoques + crítica adversarial) · investigación de apoyo (Team Tailor, marco legal SV/GT, comparativo de IA en RRHH, precios).

**Compromisos próximos:**

| Hito | Fecha | Entregable |
|---|---|---|
| **Reunión Virginia–Lili** | **Martes** | Kit de adopción listo el **lunes**: descripción del puesto "Embajador de Marca", "el día de Lili antes y después", mapa de proceso que Lili pueda co-escribir. |
| **Propuesta al cliente** | **Viernes** | Documento breve por fases + opciones de precio + cuadro de alternativas + **1 ejemplo tangible** (un CV real con la marca + el concepto de quitar duplicados). Mostrar, no prometer. |

**Condiciones que deben cerrarse antes de avanzar (resolver en la Prueba rápida / Fase -1, no dejarlas "flotando"):**

| # | Condición | Impacto si falla | Responsable |
|---|---|---|---|
| 1 | **País/jurisdicción** — confirmado El Salvador + Guatemala; falta validar el consentimiento y el registro | Define todo el marco legal y si el comparativo salarial es viable | Víctor → Virginia |
| 2 | **Conexión técnica / extracción de datos / nivel de plan de Team Tailor** sin verificar | Sostiene los primeros quick wins (extraer datos, quitar duplicados, punto de partida medido). Sin plan B, se cae media Fase 0 | Prueba técnica |
| 3 | **¿Existe el set de decisiones de referencia** (historial de quién entró a terna)? | El asistente que ordena candidatos no replica el "ojo clínico" sin él | Víctor + Virginia |
| 4 | **Comisión por colocación y volumen por mes** | Sin esto no hay caso de retorno ni precio defendible | Virginia |
| 5 | **Vigencia/consentimiento real** de los 4.000 | Mide cuánto vale realmente la base — el "~60% del valor" que se mencionó en la llamada es hoy solo un supuesto | Muestreo en la Prueba rápida |

**Alertas abiertas (autocrítica honesta):**
- ⚠️ **Economía y capacidad de pago.** La referencia mental del cliente son ~3 meses de una persona temporal (**~US$1.5k–2.7k ⚠️**); el plan completo es un programa de varios meses. **Antes de cotizar las fases hay que sumar el costo total y verificar que el cliente pueda pagarlo y que el retorno lo justifique.** Si construir todo a medida excede lo que una PYME de 10 personas puede financiar, por defecto recomendamos el **camino "comprar algo suficientemente bueno"** (activar la IA que Team Tailor ya cobra + manuales de proceso ligeros + quitar duplicados en una hoja de cálculo) y dejar la construcción a medida solo si el volumen lo justifica con datos. Declaramos nuestro **conflicto de interés**: ganamos más cuanto más se construya a medida; la integridad en el primer proyecto vale más que el tamaño del contrato.
- ⚠️ **Quién entrega.** Boutique, primer proyecto, líder no técnica en RRHH ni en cumplimiento legal. Falta un plan de capacidad y de subcontratación (legal local, transcripción de audio) y nombrar un dueño interno del cambio.
- ⚠️ **Continuidad de la operación.** Ninguna intervención de la Fase 1 toca un proceso en marcha: el 63% de los ingresos debe seguir fluyendo. **Riesgo de fuga de Lili** (trabaja de 7am a 7pm) tratado como amenaza de renuncia; la persona temporal también funciona como seguro para retenerla.
- ⚠️ **Validez estadística.** Con 20–60 colocaciones al año, las encuestas de recomendación y las auditorías de sesgo tienen pocos casos para ser confiables: usar satisfacción del cliente (% de satisfechos + el conteo) y reportar siempre el número de casos.

---

*Última actualización: 2026-06-29 · Sesión 01. Mantener este README sincronizado con la bitácora.*
