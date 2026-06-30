# Investigación — índice y verificación

## En lenguaje ejecutivo (lo que importa para el negocio)

- **El valor está en construir lo que el sistema actual no hace.** El sistema donde guardan los candidatos (Team Tailor) tiene ~4.000 candidatos con CV, pero su IA solo filtra por palabras clave. El proyecto crea el motor de búsqueda por habilidades que hoy no existe: activa una base que está parada.
- **Antes de la IA, hay que ordenar los datos.** Estandarizar los campos y las etiquetas de habilidades en el sistema es el primer entregable de valor. Sin esto, la IA no rinde. Es la Fase 1.
- **El Salvador ya obliga a cumplir la ley de datos hoy.** Hay ley vigente (Decreto 144/2024) y Conexión Talento es sujeto obligado. Toca consentimiento por finalidad, política de retención, registro de datos y protocolo de brechas a 72 horas. Guatemala aún no tiene ley general; conviene aplicar el mismo estándar como anticipación y argumento de venta.
- **El benchmark de salarios se puede vender, pero solo con anonimización irreversible y auditada.** Es a la vez requisito legal y diferenciador de calidad. Antes de lanzarlo se necesita dictamen de un abogado salvadoreño.
- **Vender por fases con precio cerrado, no por hora.** Arranque realista de ~USD 14.000–36.000 para las primeras fases. El precio se ancla al retorno (activar base muerta + acelerar la entrega de candidatos), no a las horas ni a "comprar software".
- **La IA apoya, nunca decide — y eso se vende.** Siempre con una persona validando, con auditoría de sesgo y trazabilidad. Es mitigación legal, propuesta de valor del headhunting boutique y blindaje frente a clientes multinacionales.
- **Cuidado con lo que aún no está confirmado.** Varias afirmaciones clave (descarga masiva de CVs, articulado exacto de la ley, cifras de precios y de retorno) son inferidas o vienen de marketing de proveedores. Verificarlas antes de prometerlas al cliente (ver "Verificación crítica").

---

Cuatro briefs sustentan la propuesta para Conexión Talento: capacidades del sistema donde guardan los candidatos (Team Tailor), marco legal de datos en SV/GT, precios del proyecto y comparativa de IA en reclutamiento. Este índice resume el hallazgo clave de cada uno, marca lo que hay que confirmar antes de usarlo con el cliente y consolida las implicaciones accionables.

## Hallazgos por brief

- **Team Tailor — capacidades, IA, datos e integraciones** ([team-tailor.md](./team-tailor.md)): la base de ~4.000 candidatos + CVs **se puede extraer mediante la conexión técnica entre sistemas (API REST, formato JSON:API) con una clave de Administrador/Lectura**, y la IA nativa ("Co-pilot") **no hace búsqueda por significado de forma transversal** (solo filtra por criterios y por coincidencia de palabras clave). Conclusión: **potenciar**, no reemplazar — construimos el motor de búsqueda por habilidades que el sistema actual no tiene.

- **Marco legal — El Salvador y Guatemala** ([marco-legal-datos-sv-gt.md](./marco-legal-datos-sv-gt.md)): **El Salvador ya tiene ley vigente (Decreto 144/2024, regulador ACE)** y Conexión Talento es sujeto obligado hoy; Guatemala aún no tiene ley general. La comparativa de salarios **solo es comercializable sobre datos anonimizados de forma irreversible y agregada**.

- **Precios y modelos del proyecto** ([pricing-engagement.md](./pricing-engagement.md)): **estructurar el primer proyecto en fases con precio cerrado (fixed-fee)** (no por hora), con un arranque realista de **~USD 14.000–36.000** (Fases 0–2) para una PYME centroamericana, anclando el precio al retorno del sistema y no a las horas.

- **Comparativa — IA aplicada a reclutamiento y RRHH** ([benchmark-ia-rrhh.md](./benchmark-ia-rrhh.md)): el patrón de mayor retorno replicable a escala boutique es el **cribado/búsqueda por significado con varios asistentes de IA (LLM, Claude) que consultan la base propia (RAG)** (~11x más rápido que manual), siempre con una persona validando como mitigación legal y propuesta de valor.

## Verificación crítica

Afirmaciones que requieren confirmación, parecen poco soportadas o pueden desactualizarse antes de usarlas con el cliente:

- **Descarga masiva de CVs vía conexión técnica (Team Tailor): NO confirmada.** La forma de bajar los archivos (atributo `resume`/adjuntos) es inferida, no documentada. *Acción: probar con la cuenta y la clave de Administrador reales antes de prometer el proceso de extracción.*
- **"La conexión técnica requiere plan Enterprise": probablemente falso.** Proviene de un blog de terceros (pin.com) y contradice la evidencia oficial de que cualquier Company Admin puede crear claves. *Confirmar con un Account Executive de Team Tailor.* No bloquear la propuesta por este supuesto.
- **Stack regional y alcance de la clave actual (EU/NA/AU): sin verificar.** Define el punto de conexión y el acceso a datos de candidato. *Validar en la cuenta real.*
- **Articulado exacto de la Ley salvadoreña (Arts. 26-27, 37, 40/44, 57, 64): fuente secundaria.** El texto provino de una transcripción (informatica-juridica.com), no del Diario Oficial. *Cotejar contra el PDF oficial antes de citarlo en propuesta o contrato.* No es opinión legal vinculante: se requiere dictamen de abogado salvadoreño antes de lanzar el benchmark.
- **Reglamento/lineamientos de la ACE posteriores a mayo-2025: no verificado.** Es el punto legal más importante a actualizar, porque ahí estarían reglas concretas de retención, registro y posibles disposiciones sobre decisiones automatizadas.
- **Estatus de las iniciativas de Guatemala (6103/6572) a junio-2026: no verificado en detalle.** El panorama legislativo pudo cambiar.
- **Cifras de precios para Centroamérica: inferidas, no observadas.** No existe ninguna tarifa pública verificable para consultores de IA en SV/GT; las bandas se extrapolan de LATAM-Sur ajustadas a la baja. *Validar con cotizaciones locales reales.* Los rangos de "desarrollo de agentes de IA" (de <USD 10K a USD 300K+) son orden de magnitud, no cotización.
- **Métricas de retorno de la comparativa (Unilever, Emirates NBD, micro1, Paradox): provienen de marketing de los propios proveedores**, no auditadas y de implementaciones enterprise de alto volumen. *Usar como referencias aspiracionales, nunca como garantías a una boutique de ~10 personas.* No hay caso público de una boutique de este tamaño replicando esos números.
- **Precios de plataformas (SeekOut ~USD 833/asiento) y validez final del caso Workday: secundario/en litigio.** Citar con cautela.
- **Aplicabilidad del GDPR / EU AI Act: condicional.** Solo si hay candidatos o clientes en la UE. *Hacer una pregunta de alcance temprana antes de asumir obligaciones o de venderlas como diferenciador.*

## Implicaciones consolidadas para la propuesta

1. **El diferenciador es construir, no comprar.** El núcleo del proyecto —búsqueda por significado por habilidades/seniority/idioma con ordenamiento sobre los 4.000 candidatos— es justo la brecha de Team Tailor; se resuelve con extracción por la conexión técnica + procesamiento de CVs + búsqueda por significado que consulta la base propia (RAG, Claude). Potenciar el sistema actual, no reemplazarlo.

2. **Estructurar la data es el prerrequisito de todo.** Estandarizar los campos personalizados, las etiquetas de habilidades y la estructura de candidato en Team Tailor habilita tanto el Co-pilot como nuestro motor; sin esto, el RAG no rinde. Es la Fase 1 y el primer entregable de valor.

3. **Cumplimiento legal por diseño desde el día uno.** El Salvador exige cumplir ya: consentimiento por finalidad (selección / base futura / benchmark anonimizado), política de retención, registro de tratamientos, responsable de datos y protocolo de brechas a 72h. Aplicar el mismo estándar en Guatemala como anticipación y argumento comercial.

4. **El benchmark de salarios es un producto vendible, pero solo como proceso de anonimización auditado** (irreversible —k-anónima—, separado del sistema, con pruebas de que no se puede volver a identificar a la persona). Es a la vez el habilitador legal y un diferenciador de calidad; requiere validación legal local antes de lanzarse.

5. **Vender por fases con precio cerrado anclado al retorno del sistema.** Diagnóstico → Estandarización/Datos → Piloto de IA acotado (cribado/ordenamiento o generación de CV, 6-8 semanas) → Operación/cuota mensual. Arranque ~USD 14.000–36.000, con un reductor de riesgo (Fase 0 a precio reducido con crédito a Fase 1) en lugar de descuento general. El argumento es "activar base muerta + acelerar la entrega de candidatos", no "comprar software".

6. **IA como apoyo, nunca decisor — y convertirlo en argumento comercial.** Siempre con una persona validando, auditoría de sesgo y trazabilidad (instrucciones a la IA, criterios, puntuaciones), con cuidado especial en el filtrado por voz por variantes salvadoreña/guatemalteca y accesibilidad. Es mitigación legal, propuesta de valor del headhunting boutique y blindaje frente a clientes multinacionales sujetos a EU AI Act / LL144.
