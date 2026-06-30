# Riesgos, privacidad y cumplimiento
### Memoria del proyecto Conexión Talento — Entregable de gobierno

> **En una frase:** El mayor peligro del proyecto no es la tecnología, es la ley. Antes de vender datos o automatizar el descarte de candidatos hay que cerrar permisos legales y consentimiento; saltarse esto puede costar el cliente y la reputación.

> **Propósito.** Este documento reúne los riesgos del programa y fija las reglas de cumplimiento legal que deciden qué se puede construir, vender y automatizar —y en qué orden—. Es **directo y sin rodeos** en protección de datos de candidatos, porque ahí está la mayor distancia entre lo que el cliente *quiere hacer* y lo que *puede hacer dentro de la ley*. Priorizamos hacer las cosas bien por encima del tamaño del contrato: en nuestro primer proyecto, un problema legal mal manejado no es un riesgo de negocio, es de vida o muerte.

---

## 1. Resumen ejecutivo

**Lo que importa para el negocio:** la mayor amenaza no es técnica, es legal y de orden de los pasos. El cliente quiere ganar dinero con su base de ~4.000 candidatos (vender un estudio de salarios de mercado y ofrecer capacitaciones) y automatizar el descarte de CVs con rechazo automático. Esos son justo los dos frentes con más exposición legal y reputacional, y donde tenemos menos margen de error.

**Los cinco riesgos que pueden hundir el proyecto, del más grave al menos grave:**

| # | Riesgo | Por qué es crítico |
|---|--------|--------------------|
| 1 | **Vender datos de candidatos sin permiso legal** (estudio de salarios + ofrecer capacitaciones sin base legal) | Usar datos recogidos para reclutar con fines comerciales viola la regla de "solo para el fin que se pidió". El estudio de salarios suma riesgo de volver a identificar a personas, de prácticas anticompetitivas y de romper acuerdos de confidencialidad con los clientes que aportan el 63% de los ingresos. |
| 2 | **Discriminación por culpa del algoritmo en el descarte** | Ordenar candidatos usando datos del pasado repite el sesgo (género, edad, foto, origen). El rechazo automático del puesto 30 en adelante sin que lo revise una persona convierte ese sesgo en sistema, a escala de 200 CVs por proceso. |
| 3 | **Fuga de datos personales que está ocurriendo HOY** (CVs pegados en el ChatGPT gratuito) | No es un riesgo futuro: es envío de datos personales al extranjero y posible uso de esos datos para entrenar el modelo, ahora mismo. |
| 4 | **Prometer resultados rápidos sobre supuestos sin verificar** (conexión técnica con el sistema de candidatos, set de decisiones de referencia, país) | Toda la Fase 0 depende de capacidades que nadie ha confirmado. Prometer y no cumplir quema al primer cliente. |
| 5 | **Que Lili renuncie (riesgo de fuga)** | Es punto único de falla, impulsora del cambio y cuello de botella, de 7am a 7pm. Si se va antes de documentar lo que sabe, se va con ella la operación, la memoria y la adopción de golpe. |

**Postura de gobierno (decisiones que tomamos HOY, no en la Fase 3):**
- **CONGELAR** toda venta del estudio de salarios y toda oferta de capacitaciones a la base hasta cerrar permiso legal, consentimiento y anonimización. No cuesta esfuerzo y evita el peor riesgo.
- **UNA PERSONA OBLIGATORIA** antes de comunicar cualquier rechazo. La IA pre-ordena; nunca decide ni comunica sola.
- **CORTAR** esta semana el uso del ChatGPT gratuito con datos de candidatos.
- **NO PROMETER** ningún entregable que dependa de la conexión técnica con el sistema de candidatos (Team Tailor) antes de hacer una *prueba rápida de factibilidad* que la verifique (ver §3).

---

## 2. Cómo leer este registro (metodología)

- **Probabilidad** e **Impacto** en escala Alta / Media / Baja. **Severidad** = la combinación de las dos (🔴 crítico / 🟠 alto / 🟡 medio).
- Cada riesgo tiene **un responsable con nombre** y un **disparador de la acción correctiva**. Sin responsable, un riesgo es solo un deseo.
- Los supuestos no confirmados se marcan **⚠️ a validar**. No los disfrazamos de hechos: son condiciones previas.
- Este documento **resuelve** las tensiones entre las tres miradas del análisis (datos vs. proceso vs. indicadores) que, sin resolver, dejan el camino crítico en el aire (ver §3 y §8).

---

## 3. Condiciones previas que bloquean (resolver antes de cotizar)

La crítica fue certera: varios "resultados rápidos prioritarios" descansan sobre supuestos que **nadie verificó**. Los pasamos de "preguntas abiertas" a **condiciones previas con responsable y plan B**. Recomendamos una **Fase −1: Prueba rápida de factibilidad técnica y legal (1 semana, pagada)** antes de comprometer alcance o precio.

| Condición previa | Por qué bloquea | Responsable | Plan B si falla |
|---|---|---|---|
| **País donde opera y dónde residen candidatos/clientes** ⚠️ | Define qué ley aplica, el registro de la base ante la autoridad, los plazos, las multas y la **viabilidad del estudio de salarios**. Es un correo de 5 min a Virginia; resolverlo HOY. | Virginia / Consultor líder | Sin país no hay análisis legal: no se cotiza Fase 1 ni siguientes. |
| **Conexión técnica / forma de extraer datos / plan contratado de Team Tailor** ⚠️ | Sostiene la extracción de datos, la medición del punto de partida, el quitar duplicados y la búsqueda inteligente sobre la base. | Consultor líder + soporte de Team Tailor | Si no se puede descargar la información en bloque: trabajar dentro de Team Tailor (campos/vistas) y posponer el almacén propio. |
| **Que exista un set de decisiones de referencia** (historial recuperable de quién entró a la terna y quién no) ⚠️ | Sin él no se puede ajustar ni auditar el asistente que ordena candidatos. Con CERO documentación, probablemente **no existe**, y crearlo exige tiempo de Virginia (el recurso más escaso y más resistente). | Virginia | Sin set de referencia: el descarte con IA se pospone; no se promete en Fase 2. |
| **Origen y consentimiento de los 4.000** ⚠️ (¿aplicaron por voluntad propia o fueron buscados/extraídos de LinkedIn?) | Cambia por completo el permiso legal para cualquier uso secundario. | Virginia | Si el origen no se puede rastrear: la base es un pasivo legal, no un activo para vender. |
| **¿Hay candidatos o clientes en la Unión Europea?** ⚠️ | Activa la ley europea de datos (GDPR Art. 22, decisión automatizada) y la ley europea de IA (el descarte de candidatos cuenta como alto riesgo, Anexo III). | Virginia | Si hay exposición a la UE: revisión obligatoria de brechas antes de operar IA de selección. |

> **Regla de oro:** no prometemos ningún resultado rápido que dependa de una capacidad sin confirmar. La prueba rápida descarta o confirma estos supuestos; recién entonces se fija precio y alcance.

---

## 4. Registro de riesgos

### 4.1 Riesgos legales y de cumplimiento

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Responsable |
|----|--------|:---:|:---:|:---:|------------|-------|
| L1 | **Vender el estudio de salarios sin permiso legal** (volver a identificar personas en un mercado pequeño, prácticas anticompetitivas por intercambiar datos salariales entre empresas, romper acuerdos de confidencialidad con clientes) | Alta | Alto | 🔴 | Congelar el producto. Reconstruirlo solo en Fase 3 con: consentimiento por cada fin, anonimización irreversible (mínimo de personas por celda puesto×sector×país para que nadie pueda ser identificado), validación legal local y verificación contractual del derecho a reutilizar datos de salarios. | Consultor + abogado local ⚠️ |
| L2 | **Ofrecer capacitaciones a la base = usar los datos para un fin distinto al que se pidió** | Alta | Alto | 🔴 | Bloquear hasta tener un permiso aparte para ese fin. Datos de reclutamiento ≠ datos de marketing. | Consultor + Virginia |
| L3 | **Meter datos personales en el ChatGPT gratuito** (fuga activa) | Alta (en curso) | Alto | 🔴 | Prohibir hoy. Pasar el uso a ChatGPT Enterprise/Team o a la conexión técnica con el proveedor, con compromiso de no entrenar con los datos + acuerdo de protección de datos (el proveedor no usa ni entrena con los datos). | Consultor líder |
| L4 | **Operar sin aviso de privacidad ni consentimiento rastreable** en el punto donde el candidato aplica | Alta | Alto | 🟠 | Publicar un aviso de privacidad en el formulario (LinkedIn/Team Tailor): para qué se usan los datos, base legal, plazos y derechos del candidato. | Virginia |
| L5 | **No registrar la base de datos ante la autoridad** (PRODHAB en Costa Rica / ANTAI en Panamá, según país ⚠️) | Media | Alto | 🟠 | Lista de verificación legal de 1 página por país; registrar si aplica. | Abogado local ⚠️ |
| L6 | **Sin política de cuánto tiempo se guardan los datos** (4.000 guardados sin límite, "no saben cuántos siguen vigentes") | Alta | Medio | 🟠 | Definir plazos, rastrear el origen del consentimiento, borrar/anonimizar los caducados. Llevar el registro de datos que exige la ley en versión ligera (qué datos usan, para qué y con qué permiso). | Consultor + Virginia |
| L7 | **Grabar la entrevista previa sin consentimiento explícito** (la voz puede ser dato biométrico; transcribirla + detectar competencias = perfilado) | Media | Alto | 🟠 | Texto de consentimiento al inicio de cada llamada; definir dónde se guardan los audios/transcripciones y por cuánto tiempo. | Lili / reclutadores |
| L8 | **La consultora pasa a manejar datos personales de terceros** al copiar la base a un almacén propio | Media | Alto | 🟠 | Acuerdo de protección de datos entre cliente y consultora (no usar ni entrenar con los datos), cifrado, control de quién accede, ubicación definida de los datos y borrado al terminar el proyecto. | Consultor líder |
| L9 | **Decisión automatizada sin que la revise una persona** (rechazo automático del puesto 30 en adelante, correo a los 15 días) — incumple la ley europea (GDPR Art. 22) si hay exposición a la UE | Media | Alto | 🟠 | Una persona validando siempre (ver §6). Dejar registro de cada decisión con su justificación citada. | Consultor + Lili |

### 4.2 Riesgos técnicos

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Responsable |
|----|--------|:---:|:---:|:---:|------------|-------|
| T1 | **La conexión técnica o la descarga de Team Tailor está limitada o tope de uso por minuto** ⚠️ | Media | Alto | 🟠 | Verificar en la prueba rápida (§3). Diseñar una capa que se pueda mover de sistema; plan B dentro de Team Tailor. | Consultor líder |
| T2 | **Búsqueda inteligente sobre una base sucia** → devuelve basura con apariencia de certeza | Alta | Alto | 🟠 | Orden obligatorio: identidad → estructura → datos al día → vocabulario común de habilidades y sectores → *recién ahí* la búsqueda inteligente. No saltar primero a lo inteligente. | Consultor de datos |
| T3 | **Cifras de salarios/mercado inventadas por la IA** presentadas como si fueran ciertas | Alta | Alto | 🔴 | Prohibir cifras generadas por el modelo. Solo fuentes con licencia o un set de datos propio con un mínimo de registros, citadas con fuente y fecha. | Consultor de datos |
| T4 | **Errores al unir identidades**: fusionar a dos personas distintas expone el historial ajeno (fuga de privacidad); no fusionar deja pasar duplicados | Media | Alto | 🟠 | Umbrales conservadores, revisión humana de las uniones dudosas, fusión **reversible** (enlazar, no borrar). | Consultor de datos |
| T5 | **Datos inventados al procesar el CV** (habilidades/fechas que no estaban) | Media | Medio | 🟡 | Formato de salida estricto, validación de consistencia, revisión humana del 5–10% de los casos, rastrear siempre al CV original. | Consultor de datos |
| T6 | **Mudarse de Team Tailor a la carrera** rompe las integraciones (LinkedIn, pruebas psicométricas, rechazos) y traslada la seguridad y el riesgo de fugas a una PYME de 10 personas | Media | Alto | 🟠 | NO mudarse. Primero potenciar vía la conexión técnica; decidir con datos y análisis de seguridad, no por entusiasmo. | Consultor + Virginia |
| T7 | **Sobre-ingeniería "con agentes autónomos"** (6 agentes sueltos sin proceso ni indicadores = imposible de controlar) | Media | Medio | 🟡 | Replantear: 3 herramientas predecibles + 1 coordinador que decide con reglas fijas y siempre con una persona validando. Autonomía solo donde aporta (búsqueda de candidatos). Las reglas de seguridad van escritas en el código (formato de salida estricto), no como una instrucción de texto a la IA. | Consultor de IA |

### 4.3 Riesgos de adopción y capacidad de entrega

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Responsable |
|----|--------|:---:|:---:|:---:|------------|-------|
| A1 | **Que Lili renuncie (agotamiento, 7am–7pm)** — punto único de falla, impulsora del cambio y cuello de botella | Media | Alto | 🔴 | Liberar su tiempo PRIMERO. Documentar lo que sabe en las semanas 2–3 (no al final de la Fase 1). Enmarcar la persona temporal como **seguro contra su fuga**, no solo como alivio. | Virginia |
| A2 | **Resistencia por identidad profesional** (ven la IA como pérdida de su "ojo clínico") | Alta | Alto | 🟠 | Mensaje "la IA potencia tu criterio, tú decides". Diseñar juntos la hoja de criterios para evaluar candidatos (ellos son los autores). La regla "la IA no opina" es el mensaje central de adopción, no una restricción técnica. | Consultor de cambio |
| A3 | **Choque entre quien patrocina y quien usa**: Virginia decide el cambio y a la vez es reclutadora con método propio | Media | Alto | 🟠 | Pacto de que ella adopta primero y en público (su prompt de CV como prueba). Acompañamiento a la patrocinadora, 30 min/semana. | Consultor de cambio |
| A4 | **Gastar el presupuesto de la persona temporal en tapar huecos operativos** → cero capacidad instalada, la dependencia vuelve en el mes 4 | Media | Medio | 🟡 | Usar a la persona temporal para **descargar la operación de Lili** (lo que ella realmente pide) y proteger las horas de ella y de Virginia para el diseño. No poner a la persona temporal a etiquetar contra el vocabulario común de habilidades (es trabajo calificado). | Virginia |
| A5 | **Capacidad de NUESTRA consultora**: boutique, primer proyecto, líder sin RRHH ni área de cumplimiento propia | Alta | Alto | 🟠 | Plan de equipo explícito: qué hace el consultor, qué se **subcontrata** (legal de datos, transcripción de voz) y qué se co-escribe con Lili (cubre el vacío de conocimiento de RRHH). No prometer "McKinsey/BCG" en frentes donde no tenemos capacidad declarada. | Consultor líder |
| A6 | **Dependencia en círculo en el camino crítico**, sin responsable: estandarizar etapas ← liberar a Lili ← IA de descarte ← set de decisiones de referencia ← tiempo de Virginia | Alta | Alto | 🟠 | **Romper el círculo** así: (1) la persona temporal descarga la operación de Lili → le libera 4–6h/semana; (2) Lili y Virginia documentan juntas, *a mano*, la hoja de criterios y el set de referencia, en sesiones cronometradas de 45 min; (3) recién entonces se construye el asistente que ordena candidatos. Ver §8. | Consultor líder |

### 4.4 Riesgos reputacionales

| ID | Riesgo | Prob. | Impacto | Sev. | Mitigación | Responsable |
|----|--------|:---:|:---:|:---:|------------|-------|
| R1 | **Reenviar el mismo candidato 2 veces al mismo cliente** (ya pasó) | Alta | Alto | 🟠 | Registro de presentaciones candidato×cliente×fecha + regla de no reenvío + alerta de duplicado. Verificación con **reglas fijas** (consulta directa al sistema), no con IA. Resultado rápido de horas. | Consultor de datos |
| R2 | **Ataques en LinkedIn por mala experiencia del candidato** — la "cercanía" que venden como diferenciador es hoy su mayor pasivo | Alta | Alto | 🟠 | Compromiso de tiempo de respuesta en la comunicación (acuse en 48h, actualización de estado, rechazo personalizado) **antes** de medir la satisfacción del candidato. Rol de "embajador de marca". | Consultor + Lili |
| R3 | **Encuestar a candidatos enojados antes de arreglar el tiempo de respuesta** → más reacción negativa ("me ignoraron y ahora preguntan cómo me sentí") | Media | Medio | 🟡 | Ordenar los pasos: arreglar la comunicación PRIMERO, lanzar la encuesta de satisfacción después. | Consultor de cambio |
| R4 | **Rechazo automático por IA sin una persona** amplifica el daño reputacional que ya existe y expone a un sesgo que nadie puede auditar | Media | Alto | 🔴 | Una persona validando siempre (§6). Rechazos en lote revisado antes de enviar. | Lili |
| R5 | **Primer proyecto fallido = anti-referencia** (en vez de caso de éxito), por la brecha entre presupuesto y recursos | Media | Alto | 🟠 | Criterios de "cuándo cancelar" y puntos de seguir/no seguir con cifras (§7). Alcance quirúrgico. No "casi regalar" la Fase 0 dando el éxito por hecho sin verificar las condiciones previas. | Consultor líder |
| R6 | **Sobreprometer "el mismo día"** a una CEO enamorada del concepto | Media | Medio | 🟡 | Enterrar el "mismo día", no posponerlo a la Fase 3. Prometer el tiempo hasta entregar la terna (que sí controlamos) y mejoras sobre el propio punto de partida medido. | Consultor comercial |

---

## 5. Protección de datos de candidatos — la sección directa

> Esta es la sección que el cliente menos quiere oír y más necesita. La base de 4.000 candidatos **todavía no es "oro"**: una parte importante es **pasivo legal** —consentimiento dudoso, origen que no se puede rastrear, datos caducados, sin un fin de venta declarado—. Venderla tal cual dispararía justo el daño reputacional que el cliente teme, **más** una exposición legal real. El valor aparece *después* de arreglar la capa de permisos legales, no antes.

### 5.1 Qué ley aplica — El Salvador (vigente) + Guatemala ✅

**Jurisdicción confirmada:** El Salvador (operación principal) y Guatemala (secundaria). Esto cambia el tono: **El Salvador YA regula** —no es un marco laxo como se asumía—, así que cumplir es obligación de hoy, no opción de mañana. Lo convertimos en argumento de venta ("cumplimiento desde el diseño"). Detalle y fuentes en [`99-research/marco-legal-datos-sv-gt.md`](../99-research/marco-legal-datos-sv-gt.md).

| País | Ley / Autoridad | Qué implica para Conexión Talento |
|------|-----------------|-------------|
| **El Salvador** (principal) | **Ley de Protección de Datos Personales — Decreto 144/2024, VIGENTE**, con autoridad propia | **Está obligado HOY:** consentimiento por cada fin, derechos del titular, plazos de conservación, registro de los tratamientos, responsable de datos y protocolo ante fugas. El estudio de salarios **solo es legal si está anonimizado de forma irreversible y agregada** (mínimo de personas por celda para que nadie pueda ser identificado). |
| **Guatemala** (secundaria) | Sin ley general aún (habeas data en la Constitución; iniciativas en trámite) | Menos obligaciones formales, pero **no exime** de responsabilidad civil/contractual. Aplicamos el estándar salvadoreño por anticipación y como diferenciador. |
| **UE** (solo si aplica) ⚠️ | Ley europea de datos (GDPR) + ley europea de IA (EU AI Act) | Solo si hay candidatos/clientes en la UE. *Pregunta a resolver temprano.* |

> ⚠️ **A validar antes de citarlo en contrato o lanzar el estudio de salarios:** el texto exacto del Decreto 144/2024 vino de una fuente secundaria; **se requiere dictamen de un abogado salvadoreño** y cotejo contra el Diario Oficial, además de revisar el reglamento y los lineamientos de la autoridad posteriores a su entrada en vigor (ahí estarían las reglas concretas de conservación, registro y decisiones automatizadas).

Y si hay **candidatos o clientes en la UE** ⚠️: la ley europea de datos (GDPR Art. 22, la decisión automatizada exige intervención humana, explicación y derecho a reclamar) + la ley europea de IA (el descarte de candidatos cuenta como **alto riesgo**, Anexo III, con gestión de riesgo, gobierno de datos, supervisión humana, transparencia y registro obligatorios). Es también un blindaje frente a clientes multinacionales.

### 5.2 Permiso legal y "solo para el fin que se pidió" — el principio que el cliente está a punto de violar

Los datos se recogieron para **un solo fin: postular a una vacante**. Cualquier uso secundario (estudio de salarios comercial, marketing de capacitaciones) **excede ese fin** y exige una de dos cosas:
1. **Consentimiento aparte y específico** para el nuevo fin, o
2. **Interés legítimo documentado** + un mecanismo real para darse de baja (y aun así, no aplica a datos sensibles ni a la venta de datos).

**Sin esto, no hay permiso legal.** "Tenemos sus datos" no es lo mismo que "podemos usarlos para lo que queramos".

### 5.3 Consentimiento por cada fin — el diseño correcto

Pedir el **permiso por cada fin, por separado**, desde el formulario de aplicación:

- ☐ Tratar mis datos para **procesos de reclutamiento** (la base del servicio).
- ☐ Recibir **ofertas de capacitación / formación** (oferta de capacitaciones — fin aparte).
- ☐ Inclusión **anonimizada** en **estudios de salarios** (estudio de mercado — fin aparte).

Más: gestión de preferencias, baja real y funcional, y **guardar la fecha y el origen del consentimiento como un campo de datos**. Esto **habilita** la venta de forma legal, en vez de bloquearla.

### 5.4 Por qué VENDER el estudio de salarios es la bandera roja #1

Es, a la vez, la mayor oportunidad de ingresos **y** el mayor riesgo. Vendido "en crudo" es una **factura legal con tono de autoridad**, no un producto. Cuatro razones que se suman:

1. **El origen de los datos es confidencial.** Las cifras de salarios vienen de las expectativas de los candidatos y de las **negociaciones con clientes**, casi seguro cubiertas por acuerdos de confidencialidad. Venderlas puede **romper contratos con los propios clientes que aportan el 63% de los ingresos** → pleito con quien más te importa.
2. **Re-identificación en un mercado pequeño.** En Centroamérica, "el salario del CFO de la empresa X" se puede atribuir a una persona **aun con los datos agregados**. **Anonimizado ≠ libre de usar.** Sin un mínimo de empresas/registros por celda, es un incidente esperando a pasar.
3. **Riesgo de prácticas anticompetitivas (antitrust).** Intercambiar datos de salarios entre empresas puede contar como colusión según el país. Requiere validación legal local explícita.
4. **Cifras inventadas si las genera la IA.** Sin una fuente con licencia (Mercer/Korn Ferry/encuestas locales) o un set de datos propio estadísticamente válido (con un mínimo por celda), las cifras son inventadas con apariencia de rigor.

**Decisión de gobierno: CONGELAR la venta del estudio de salarios.** No se promete en la propuesta del viernes. Camino positivo (para honrar la ambición de Virginia, no solo decir "no"): explorar una **alianza con un proveedor con licencia de datos de salarios**, o construir el producto en Fase 3 con consentimiento por cada fin + anonimización desde el diseño + validación contractual y legal. **Bien, no rápido.**

### 5.5 Ofrecer capacitaciones sin el consentimiento adecuado — la otra bandera roja

Es **exactamente la misma vía** que ya les genera ataques en LinkedIn (contacto no deseado / falta de seguimiento). Venderles mal **amplifica el daño reputacional que dicen temer**. No se ofrecen capacitaciones a la base sin el permiso específico de §5.3. Punto.

### 5.6 Fuga activa HOY — el prompt de Virginia en ChatGPT

El "prompt" para estandarizar CVs casi seguro **mete los datos personales completos de los candidatos en el ChatGPT gratuito**: envío de datos al extranjero y posible uso para entrenar el modelo. **Es una fuga en curso, no un riesgo futuro.** Cortar esta semana: prohibir pegar CVs en el ChatGPT personal; pasar a Enterprise/Team o a la conexión técnica con compromiso de no entrenar + acuerdo de protección de datos. Costo casi nulo, cierra el riesgo de inmediato.

### 5.7 Conservación, inventario y la consultora como encargada de datos

- **Registro de datos que exige la ley, versión ligera:** qué datos se usan, de dónde vienen, con qué permiso, dónde se guardan, con quién se comparten y cuánto se conservan.
- **Política de conservación:** plazos definidos, borrado/anonimización de los caducados. Una base guardada sin límite viola la regla de "no conservar más de lo necesario".
- **La consultora pasa a manejar datos de terceros** al copiar los 4.000 a un almacén propio: exige un **acuerdo de protección de datos entre cliente y consultora** (no usar ni entrenar con los datos), cifrado, control de accesos, ubicación definida y **borrado al cierre**. Esto abre una nueva vía de fuga; hay que cerrarla *antes* de tocar la base.

### 5.8 Historial del candidato — legítimo, pero con límites

Llevar el historial candidato×cliente para evitar el reenvío duplicado es **legítimo y resuelve un riesgo reputacional real**. PERO: **no** convertirlo en una lista negra compartida entre clientes, **ni** en una decisión en contra automática. El historial **informa al reclutador**; no excluye solo.

---

## 6. Sesgo en el descarte automático, explicabilidad y decisión humana

### 6.1 El riesgo: discriminación a gran escala

Puntuar/ordenar candidatos usando datos del pasado **repite la discriminación del pasado** —género, edad, nombre, foto u origen como atajos—. El caso emblemático es la herramienta de reclutamiento **descartada por Amazon** por sesgo de género. Sin auditoría, el asistente que ordena candidatos convierte la discriminación en sistema sobre **200 CVs por proceso**, con responsabilidad legal-laboral directa para la consultora **y** para el cliente final.

Agravante centroamericano: los CVs suelen incluir **foto, edad, estado civil y nacionalidad**. Meter eso directo al evaluador **inyecta un sesgo medible**.

### 6.2 Controles obligatorios antes de poner cualquier IA de descarte en producción

1. **Quitar los datos personales** antes de evaluar: borrar foto, edad, estado civil, nacionalidad, nombre y señales de maternidad. Por equidad y para poder defender el proceso.
2. **Excluir de forma explícita las variables atajo prohibidas** de los criterios del modelo.
3. **Auditoría de sesgo:** medir el porcentaje de selección por grupo (género/edad) y la diferencia entre grupos; documentar el resultado.
4. **Set de decisiones de referencia + hoja de criterios, hechos CON Virginia** ⚠️: convertir su "ojo clínico" en una matriz explícita (criterios, pesos, escalas, ejemplos) anclada en decisiones del pasado. Sin esto, el evaluador no replica su criterio, el cliente lo rechaza y no hay forma de medir aciertos ni sesgo. **Es el entregable más crítico del proyecto** y no debe definirlo solo un equipo ajeno a RRHH.
5. **Advertencia estadística de boutique** ⚠️: con ~20–60 colocaciones al año, la auditoría de sesgo y la medición de aciertos tienen **muy pocos casos** para ser robustas. Reportar siempre cuántos casos hay; tratar los resultados como indicativos, no como prueba. Esto refuerza por qué el descarte con IA es Fase 2 o posterior, no un resultado rápido.

### 6.3 Explicabilidad y decisión humana (siempre con una persona validando)

| Principio | Cómo se implementa |
|-----------|----------------|
| **La IA pre-ordena; la persona decide.** | El orden **nunca** es la decisión final automática. El reclutador valida el top 10 y la terna. |
| **Eliminar el rechazo automático (puesto 30+, correo a los 15 días) como decisión final sin revisión.** | Rechazos en **lote revisado** antes de enviar, o con una persona validando caso por caso. Protege el cumplimiento (ley europea, GDPR Art. 22) **y** el diferenciador de "cercanía". |
| **Cada puntaje con su justificación citada al CV.** | Sin inventar: la IA extrae la evidencia frente a los criterios del perfil y cita el texto fuente. Registro de cada decisión. |
| **Protocolo cuando hay desacuerdo.** | Cuando la IA y la persona difieren: **gana la persona** y se ajusta la hoja de criterios. La confianza se construye mostrando "la IA coincidió en X de 10", no por fe. |
| **Reglas de seguridad escritas en el código.** | Los umbrales (top10 / 10–20 / 30+) disparan acciones por reglas fijas, con **revisión humana obligatoria** en rechazos y terna. "La IA no opina fuera de su alcance" se fuerza con formato de salida estricto, no con una instrucción de texto a la IA. |

---

## 7. Recomendaciones: qué hacer / qué NO hacer

### ✅ HACER (acciones de bajo esfuerzo y alto valor, en orden)

1. **Confirmar el país HOY** ⚠️ y armar una lista de verificación legal de 1 página (ley aplicable, registro, plazos, multas). Nombrar a un **responsable de datos** interno (Virginia o Lili).
2. **Cortar el ChatGPT gratuito** con datos personales de candidatos esta semana (Enterprise/conexión técnica + acuerdo de protección de datos + no entrenar con los datos).
3. **Poner el registro de presentaciones** candidato×cliente×fecha con alerta de duplicado (reglas fijas, consulta directa al sistema). Cierra R1 en días.
4. **Publicar el aviso de privacidad** en el formulario de aplicación (para qué se usan los datos, base legal, plazos, derechos).
5. **Arreglar el tiempo de respuesta al candidato** *antes* de lanzar cualquier encuesta de satisfacción (evita R3).
6. **Una persona validando obligatoria** en todos los rechazos, desde ya.
7. **Levantar el inventario de datos** (registro ligero de qué datos, para qué y con qué permiso) y la política de conservación; muestrear cuántos datos de la base siguen vigentes antes de invertir en enriquecerla.
8. **Firmar acuerdos de protección de datos** con Team Tailor, el proveedor de IA/transcripción de voz y OpenAI; más un **acuerdo cliente–consultora** por nuestro rol de encargados de datos.
9. **Ejecutar la prueba rápida de factibilidad (Fase −1)** que descarta o confirma los supuestos frágiles (§3) antes de cotizar.
10. **Construir la hoja de criterios y el set de decisiones de referencia CON Virginia** antes de escribir una sola línea de código del asistente.

### ⛔ NO HACER (líneas rojas del programa)

1. **NO vender el estudio de salarios** hasta tener permiso legal, anonimización irreversible, validación de prácticas anticompetitivas y verificación contractual. No prometerlo el viernes.
2. **NO ofrecer capacitaciones** a la base sin un permiso específico y por separado.
3. **NO dejar que la IA rechace ni comunique** a un candidato sin revisión humana.
4. **NO alimentar el evaluador con datos personales sensibles** (foto, edad, estado civil, origen, nombre).
5. **NO mostrar cifras de salarios generadas por la IA** como si fueran datos.
6. **NO mudarse de Team Tailor** ni extraer la base antes de tener vocabulario común de habilidades, protocolo de vigencia y un caso de negocio con datos.
7. **NO tratar "anonimizado" como sinónimo de "libre de regulación"**, ni dar por hecho que los 4.000 tienen consentimiento válido para venderlos.
8. **NO poner a la persona temporal a hacer ingeniería de datos** mientras Lili sigue ahogada: se quema a la impulsora del cambio (A1/A4).
9. **NO construir los 6 "agentes"** sobre un proceso sin estandarizar: escala la inconsistencia a velocidad de máquina.
10. **NO sobreprometer** "el mismo día" ni retorno sin un punto de partida medido propio.

### Seguir / No seguir y criterios para cancelar (cifras, no adjetivos) ⚠️

Estos umbrales hay que calibrarlos con el cliente; se proponen como ancla:

- **La Fase −1 (prueba rápida) pasa el filtro si:** se confirma la conexión técnica/descarga de Team Tailor **o** se define un plan B viable **+** se confirman país y consentimiento **+** hay evidencia de un set de decisiones de referencia usable (o un plan financiado para crearlo). **Si no → no se cotiza Fase 1; se replantea.**
- **La Fase 0 es exitosa si:** se detecta ≥X% de duplicados al quitar duplicados **+** los 4 reclutadores adoptan la plantilla de CV **+** se entrega el punto de partida medido de 3 indicadores. **Si no → se detiene antes de la Fase 1.**
- **Criterio absoluto para cancelar por cumplimiento:** si no se puede establecer permiso legal/consentimiento para tratar la base, **se detiene toda iniciativa de venta**, sin excepción.

---

## 8. Resolución del camino crítico (cómo zanjamos la tensión entre análisis)

Las tres miradas del análisis se contradicen en el orden de los pasos, y dejarlo sin resolver es un riesgo en sí mismo. Lo zanjamos:

- **Datos** quiere extraer/procesar la base en la Fase 1. **Proceso** quiere documentar primero. **Indicadores** exige etapas estandarizadas antes de medir.
- **Camino crítico acordado:** (1) **prueba rápida de factibilidad** (descarta supuestos) → (2) **liberar a Lili** con la persona temporal que descarga su operación → (3) **estandarizar etapas + extraer la hoja de criterios y el set de referencia** (proceso e indicadores en paralelo, a mano) → (4) **punto de partida honesto** (solo los extremos confiables: tiempo hasta entregar la terna, tiempo hasta cubrir la vacante; los intermedios con advertencia por etapas inconsistentes) → (5) **extracción/enriquecimiento de datos** sobre una base limpia → (6) **IA asistida, siempre con una persona validando**, sobre un proceso ya estandarizado.
- Esto **rompe la dependencia en círculo** (A6): el conocimiento de Virginia se documenta *a mano* primero; la IA viene después, no antes.

---

## 9. Supuestos a validar ⚠️ (consolidado)

| Supuesto | Por qué importa | Cómo confirmarlo |
|----------|-----------------|------------------|
| País donde opera y dónde residen los datos | Define todo el marco legal y la viabilidad del estudio de salarios | Correo a Virginia (HOY) |
| Conexión técnica/descarga/plan de Team Tailor | Sostiene la extracción, el punto de partida y el quitar duplicados | Prueba técnica rápida |
| Que exista un set de decisiones de referencia recuperable | Ajuste y auditoría del asistente que ordena candidatos | Revisión con Virginia |
| Origen y consentimiento de los 4.000 | Permiso legal para cualquier uso secundario | Auditoría de origen |
| Exposición a la UE (candidatos/clientes) | Activa la ley europea (GDPR Art. 22) + ley europea de IA | Confirmar con Virginia |
| Qué consentimiento muestra hoy Team Tailor al aplicar | Determina qué usos secundarios son válidos | Revisar la configuración de Team Tailor |
| Si los contratos con clientes permiten reutilizar datos de salarios | Viabilidad legal del estudio de salarios | Revisión de los acuerdos de confidencialidad |
| Costo total del programa vs. capacidad de pago del cliente | Que sea asequible para una PYME (techo mental ~US$2.7k ⚠️) | Modelo de costo por unidad |
| Capacidad de entrega de la consultora (legal/transcripción de voz subcontratados) | Que podamos cumplir el estándar prometido | Plan de equipo |

---

*Documento de gobierno. La postura de cumplimiento aquí descrita es obligatoria para el diseño de las fases: ninguna iniciativa de automatización o venta avanza sin cerrar antes las condiciones legales y de consentimiento que le corresponden.*
