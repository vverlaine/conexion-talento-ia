# Investigación — índice y verificación

Cuatro briefs sustentan la propuesta para Conexión Talento: capacidades del ATS Team Tailor, marco legal de datos en SV/GT, pricing del engagement y benchmark de IA en reclutamiento. Este índice resume el hallazgo clave de cada uno, marca lo que hay que confirmar antes de usarlo con el cliente y consolida las implicaciones accionables.

## Hallazgos por brief

- **Team Tailor — capacidades, IA, datos e integraciones** ([team-tailor.md](./team-tailor.md)): la base de ~4.000 candidatos + CVs **es extraíble vía API REST (JSON:API) con key Admin/Read**, y la IA nativa ("Co-pilot") **no hace matching semántico transversal** (es screening por criterios y keyword matching). Conclusión: **augmentar**, no reemplazar — construimos el motor de búsqueda por skills que el ATS no tiene.

- **Marco legal — El Salvador y Guatemala** ([marco-legal-datos-sv-gt.md](./marco-legal-datos-sv-gt.md)): **El Salvador ya tiene ley vigente (Decreto 144/2024, regulador ACE)** y Conexión Talento es sujeto obligado hoy; Guatemala aún no tiene ley general. El benchmark de compensaciones **solo es comercializable sobre datos anonimizados de forma irreversible y agregada**.

- **Pricing y modelos de engagement** ([pricing-engagement.md](./pricing-engagement.md)): **estructurar el primer proyecto en fases con fixed-fee** (no por hora), con un arranque realista de **~USD 14.000–36.000** (Fases 0–2) para una PYME centroamericana, anclando el precio al ROI del ATS y no a las horas.

- **Benchmark — IA aplicada a reclutamiento y RRHH** ([benchmark-ia-rrhh.md](./benchmark-ia-rrhh.md)): el patrón de mayor ROI replicable a escala boutique es el **cribado/matching semántico multi-agente con LLM (Claude) + RAG** sobre la base propia (~11x más rápido que manual), con humano-en-el-bucle como mitigación legal y propuesta de valor.

## Verificación crítica

Afirmaciones que requieren confirmación, parecen poco soportadas o pueden desactualizarse antes de usarlas con el cliente:

- **Descarga masiva de CVs vía API (Team Tailor): NO confirmada.** El endpoint/forma de bajar los archivos (atributo `resume`/adjuntos) es inferido, no documentado. *Acción: probar con la cuenta y key Admin reales antes de prometer el pipeline de extracción.*
- **"La API requiere plan Enterprise": probablemente falso.** Proviene de un blog de terceros (pin.com) y contradice la evidencia oficial de que cualquier Company Admin puede crear keys. *Confirmar con un Account Executive de Team Tailor.* No bloquear la propuesta por este supuesto.
- **Stack regional y scope de la key actual (EU/NA/AU): sin verificar.** Define el endpoint y el acceso a datos de candidato. *Validar en la cuenta real.*
- **Articulado exacto de la Ley salvadoreña (Arts. 26-27, 37, 40/44, 57, 64): fuente secundaria.** El texto provino de una transcripción (informatica-juridica.com), no del Diario Oficial. *Cotejar contra el PDF oficial antes de citarlo en propuesta o contrato.* No es opinión legal vinculante: se requiere dictamen de abogado salvadoreño antes de lanzar el benchmark.
- **Reglamento/lineamientos de la ACE posteriores a mayo-2025: no verificado.** Es el punto legal más importante a actualizar, porque ahí estarían reglas concretas de retención, registro y posibles disposiciones sobre decisiones automatizadas.
- **Estatus de las iniciativas de Guatemala (6103/6572) a junio-2026: no verificado en detalle.** El panorama legislativo pudo cambiar.
- **Cifras de pricing para Centroamérica: inferidas, no observadas.** No existe ninguna tarifa pública verificable para consultores de IA en SV/GT; las bandas se extrapolan de LATAM-Sur ajustadas a la baja. *Validar con cotizaciones locales reales.* Los rangos de "desarrollo de agentes de IA" (de <USD 10K a USD 300K+) son orden de magnitud, no cotización.
- **Métricas de ROI del benchmark (Unilever, Emirates NBD, micro1, Paradox): provienen de marketing de los propios proveedores**, no auditadas y de implementaciones enterprise de alto volumen. *Usar como benchmarks aspiracionales, nunca como garantías a una boutique de ~10 personas.* No hay caso público de una boutique de este tamaño replicando esos números.
- **Pricing de plataformas (SeekOut ~USD 833/asiento) y validez final del caso Workday: secundario/en litigio.** Citar con cautela.
- **Aplicabilidad del GDPR / EU AI Act: condicional.** Solo si hay candidatos o clientes en la UE. *Hacer una pregunta de scoping temprana antes de asumir obligaciones o de venderlas como diferenciador.*

## Implicaciones consolidadas para la propuesta

1. **El diferenciador es construir, no comprar.** El núcleo del proyecto —búsqueda semántica por skills/seniority/idioma con ranking sobre los 4.000 candidatos— es justo la brecha de Team Tailor; se resuelve con extracción por API + parsing de CVs + embeddings + RAG (Claude). Augmentar el ATS, no reemplazarlo.

2. **Estructurar la data es el prerrequisito de todo.** Estandarizar custom fields, tags de skills y estructura de candidato en Team Tailor habilita tanto el Co-pilot como nuestro motor; sin esto, el RAG no rinde. Es la Fase 1 y el primer entregable de valor.

3. **Cumplimiento legal por diseño desde el día uno.** El Salvador exige cumplir ya: consentimiento por finalidad (selección / base futura / benchmark anonimizado), política de retención, registro de tratamientos, responsable de datos y protocolo de brechas a 72h. Aplicar el mismo estándar en Guatemala como anticipación y argumento comercial.

4. **El benchmark de compensaciones es un producto vendible, pero solo como pipeline de anonimización auditado** (irreversible, k-anónimo, separado del ATS, con pruebas de reidentificación). Es a la vez el habilitador legal y un diferenciador de calidad; requiere validación legal local antes de lanzarse.

5. **Vender por fases con fixed-fee anclado al ROI del ATS.** Diagnóstico → Estandarización/Datos → Piloto de IA acotado (cribado/ranking o generación de CV, 6-8 semanas) → Operación/retainer. Arranque ~USD 14.000–36.000, con un reductor de riesgo (Fase 0 a precio reducido con crédito a Fase 1) en lugar de descuento general. El argumento es "activar base muerta + acelerar shortlist", no "comprar software".

6. **IA como apoyo, nunca decisor — y convertirlo en argumento comercial.** Humano-en-el-bucle obligatorio, auditoría de sesgo y trazabilidad (prompts, criterios, scores), con cuidado especial en el screening por voz por variantes salvadoreña/guatemalteca y accesibilidad. Es mitigación legal, propuesta de valor del headhunting boutique y blindaje frente a clientes multinacionales sujetos a EU AI Act / LL144.
