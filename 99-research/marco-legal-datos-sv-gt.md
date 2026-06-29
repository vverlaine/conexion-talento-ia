# Marco legal de protección de datos personales — El Salvador y Guatemala

*Brief de investigación para Conexión Talento (RRHH/headhunting) · Tratamiento de datos de candidatos · Junio 2026*

---

## Resumen ejecutivo

- **El Salvador YA tiene ley general vigente.** El Decreto Legislativo N.º 144, *Ley de Protección de Datos Personales*, fue aprobado el 12 de noviembre de 2024, publicado en el Diario Oficial el 15 de noviembre de 2024 y entró en vigencia ocho días después (≈23/24 de noviembre de 2024, Art. 64). El regulador es la **Agencia de Ciberseguridad del Estado (ACE)**, con potestad sancionadora. Hubo un período de adecuación de ~6 meses (hasta mayo de 2025). **Conexión Talento, al operar en El Salvador y tratar ~4000 candidatos, es sujeto obligado y debe cumplir ya.**

- **Guatemala NO tiene ley general vigente.** Solo existen iniciativas en trámite (la 6103 "Ley Integral de Protección de Datos en Poder de Terceros" y la más reciente 6572, conocida por el Pleno el 5 de agosto de 2025). Hoy aplica protección fragmentaria vía *habeas data* constitucional y la Ley de Acceso a la Información Pública. Para Guatemala se recomienda adoptar voluntariamente el estándar salvadoreño/GDPR como buena práctica y anticipación regulatoria.

- **Consentimiento reforzado para reclutamiento.** En El Salvador el consentimiento debe ser libre, específico, informado, expreso e individualizado (Arts. 26-27); para **datos sensibles** (salud, biométricos, orientación sexual, origen étnico, creencias) se exige consentimiento **expreso y por escrito** (Art. 37). El consentimiento para reclutar **no cubre automáticamente** otros usos como construir un benchmark comercial: rige la **limitación de finalidad** (Art. 5).

- **El cribado/ranking con IA es admisible pero con cautelas.** La LPDP salvadoreña **no regula explícitamente** las decisiones automatizadas ni el "derecho a explicación" (vacío normativo relevante). Recomendación: mantener **humano en el ciclo**, no rechazar candidatos de forma 100% automática, documentar criterios y auditar sesgos. Si hay nexo con la UE, esto pasa de buena práctica a obligación legal estricta.

- **CRÍTICO — Monetizar un benchmark de compensaciones SÍ es viable, pero solo con datos verdaderamente anonimizados/agregados.** La LPDP **excluye de su ámbito** los datos disociados/anonimizados (anonimización = procedimiento **irreversible**, Art. 4(h); exclusión en Art. 3). Un benchmark construido sobre datos **anonimizados e irreversiblemente agregados** (sin posibilidad de reidentificación) cae fuera de la ley y **sí puede comercializarse**. Vender datos **identificables** de candidatos, o datos pseudonimizados reidentificables, **sin consentimiento específico para esa finalidad, NO es legal.**

- **Si hay candidatos/clientes en la UE, cambia todo.** Aplica el **GDPR** (alcance extraterritorial, Art. 3: hasta €20M o 4% de facturación global) y el **EU AI Act**, que clasifica la IA de reclutamiento como **alto riesgo** (Anexo III.4); obligaciones core desde el **2 de agosto de 2026** (gestión de riesgos, gobernanza de datos, pruebas de sesgo, supervisión humana, transparencia; sanciones hasta €15M/3%). El reconocimiento de emociones en el ámbito laboral está **prohibido** desde febrero de 2025.

- **Acciones inmediatas:** (1) cláusulas de consentimiento por finalidad en el ATS (Team Tailor); (2) política de retención; (3) registro de tratamientos y designación de responsable de datos; (4) protocolo de brechas a 72h; (5) pipeline de anonimización auditada antes de cualquier producto de datos; (6) mantener decisión humana en el cribado.

---

## Hallazgos detallados

### 1. El Salvador — Ley vigente (Decreto 144 de 2024)

**Estatus y autoridad.** Ley aprobada 12-nov-2024, publicada 15-nov-2024, vigente ~8 días después (Art. 64). Aprobada en paquete con la Ley de Ciberseguridad y Seguridad de la Información. El regulador es la **Agencia de Ciberseguridad del Estado (ACE)**, encargada de controlar, inspeccionar, supervisar y sancionar; debía emitir lineamientos en ~3 meses, con un período de adecuación total de ~6 meses para los sujetos obligados.

**Ámbito territorial (Art. 2).** Aplica a personas naturales y jurídicas, públicas o privadas, que traten datos **dentro o fuera** del territorio salvadoreño — alcance amplio que claramente cubre a una consultora local con base de candidatos salvadoreños.

**Consentimiento.** General (Arts. 26-27): libre, específico, informado, expreso e individualizado; pueden admitirse formas verbales, escritas o por signos inequívocos, pero **se prohíben las casillas pre-marcadas**. Datos sensibles (Art. 37): consentimiento **expreso e inequívoco por escrito**, salvo emergencia vital.

**Datos sensibles (Art. 4(g)).** Información sobre características físicas/morales, vida privada, creencias religiosas, origen étnico, orientación sexual, salud, datos biométricos y genéticos. *Relevante para RRHH: fotos, datos de salud en exámenes médicos, y cualquier inferencia de etnia/religión/orientación caen aquí.*

**Derechos del titular (ARCO-POL, Arts. 6-14).** Acceso, Rectificación, Cancelación, Oposición, Portabilidad, Olvido y Limitación. Plazo de respuesta: **20 días hábiles**, prorrogables otros 20 (Art. 20).

**Retención (Art. 5(h)).** Principio de temporalidad: conservación limitada al período necesario para los fines del tratamiento. *No hay un plazo fijo en años; la empresa debe definir y justificar su propia política.*

**Transferencias.** Locales/a terceros (Art. 40): requieren consentimiento previo e informado. Internacionales (Art. 44): solo a países con nivel de protección equivalente, con consentimiento previo salvo excepciones (p. ej. tratados regionales).

**Brechas de seguridad.** Notificación a la ACE y a los titulares afectados en un **plazo máximo de 72 horas**.

**Sanciones (Art. 57).** Leves: 1-10 salarios mínimos; graves: 11-25; muy graves: 26-40 salarios mínimos. *Con el salario mínimo del sector comercio/servicios (~US$408/mes), el rango aproximado va de ~US$408 a ~US$16,320 por infracción — sanciones moderadas comparadas con GDPR, pero con riesgo reputacional alto en un negocio de confianza como el headhunting.*

**Decisiones automatizadas.** La ley **no contiene** un régimen específico de decisiones automatizadas/perfilamiento ni un "derecho a explicación" equivalente al Art. 22 del GDPR. Existe protección indirecta vía principios (calidad, finalidad) y jurisprudencia constitucional sobre no discriminación, pero es un **vacío relevante**.

**Anonimización (Art. 4(h) + exclusión Art. 3).** La disociación/anonimización es un **procedimiento irreversible** tras el cual el dato deja de asociarse a su titular. Los datos anonimizados/disociados están **excluidos del ámbito de aplicación de la ley** (junto con datos crediticios, periodísticos y de seguridad nacional). *Este es el fundamento legal clave para el producto de benchmark.*

> Nota: El Salvador tuvo un intento previo de ley (2021) con una "Autoridad Nacional Digital"; la norma **vigente y aplicable hoy es el Decreto 144 de 2024** con la ACE como regulador.

**Crítica de sociedad civil.** Organizaciones (p. ej. IPANDETEC) han cuestionado la **independencia del regulador**, dado que la ACE está adscrita al Ejecutivo/Presidencia, y han señalado riesgos en figuras como el "derecho al olvido" para retirar contenidos. Esto importa para evaluar previsibilidad regulatoria.

### 2. Guatemala — Sin ley general (solo iniciativas)

No existe ley general de protección de datos en vigor. Iniciativas relevantes: **6103** ("Ley Integral de Protección de Datos Personales en Poder de Terceros", avanzada a segundo debate) y la más reciente **6572** (presentada/conocida por el Pleno el 5-ago-2025), la más adelantada. No hay autoridad de control establecida. Marco vigente fragmentario: *habeas data* (garantía constitucional) y disposiciones de la Ley de Acceso a la Información Pública (Decreto 57-2008) para datos en poder de entes públicos. **Implicación:** menor exigencia legal formal hoy, pero alta probabilidad de ley en el corto/mediano plazo; conviene operar ya bajo estándar salvadoreño/GDPR.

### 3. Cribado/ranking con IA — implicaciones

- **El Salvador:** legal, sin prohibición específica. Riesgo principal = sesgo discriminatorio (la discriminación sí está proscrita constitucionalmente) y falta de transparencia. Buenas prácticas exigibles de facto: supervisión humana, no rechazo totalmente automatizado, documentación de criterios, evaluaciones de impacto cuando hay tratamiento a gran escala o basado en IA.
- **UE (si aplica):** GDPR Art. 22 da derecho a no ser objeto de decisiones **únicamente** automatizadas con efectos significativos, e impone derecho a información/explicación e intervención humana. El EU AI Act lo refuerza (ver §4).
- **Recomendación transversal:** tratar el modelo como **apoyo a la decisión**, nunca como decisor final.

### 4. Si hay candidatos o clientes en la UE

**GDPR (Art. 3, alcance extraterritorial).** Aplica a una empresa fuera de la UE si **ofrece servicios** a personas en la UE o **monitorea su comportamiento** en la UE. El mero acceso a un sitio web no basta; debe haber intención de dirigirse a residentes de la UE (idioma, moneda, etc.). Si Conexión Talento recluta deliberadamente candidatos en la UE o presta servicio a clientes que tratan datos de personas en la UE, queda sujeta. Sanciones hasta **€20M o 4%** de facturación global. Datos anonimizados quedan fuera (Recital 26), pero los **pseudonimizados siguen dentro**.

**EU AI Act.** La IA usada para reclutamiento/selección — incluido **filtrar postulaciones y evaluar/rankear candidatos** — es **alto riesgo** (Anexo III, punto 4). Calendario: prácticas prohibidas (reconocimiento de emociones en el trabajo, categorización biométrica) desde **feb-2025**; obligaciones core de alto riesgo desde **2-ago-2026**: gestión de riesgos, gobernanza/calidad de datos, documentación técnica, pruebas de **sesgo**, **supervisión humana**, transparencia (informar a candidatos del uso de IA y su rol), monitoreo continuo y, para proveedores, marcado CE. Sanciones hasta **€35M/7%** (prácticas prohibidas) y **€15M/3%** (incumplimiento alto riesgo).

### 5. CRÍTICO — Monetizar/vender un benchmark de compensaciones

**Conclusión:** es **viable y legalmente defendible SOLO si** el benchmark se construye sobre datos **anonimizados, agregados e irreversiblemente desidentificados**.

**Por qué (El Salvador):** la LPDP excluye de su ámbito los datos anonimizados/disociados (Art. 3 + Art. 4(h)). Un producto que reporte, por ejemplo, "rango salarial mediano para Gerente de Finanzas en San Salvador, sector retail" — sin que ninguna cifra permita reidentificar a una persona — **no trata "datos personales"** y, por tanto, no requiere consentimiento individual ni cae bajo las restricciones de la ley.

**Condiciones de admisibilidad:**
1. **Anonimización irreversible y verificada** (la ley exige irreversibilidad). No basta con borrar el nombre: hay que evitar la reidentificación por combinación de atributos.
2. **Agregación con umbrales mínimos** (p. ej. no publicar celdas con menos de *k* registros — k-anonimato; típicamente k≥5/10) para impedir inferir el salario de un individuo concreto.
3. **Supresión de cuasi-identificadores** o su generalización (rangos de edad, no fecha exacta; sector, no empleador específico cuando el universo es pequeño).
4. **Gobernanza documentada**: política de anonimización, pruebas de reidentificación, y separación entre el dato fuente (identificable, en el ATS) y el dataset analítico.

**Lo que NO es admisible:**
- Vender o ceder **datos identificables o pseudonimizados reidentificables** de candidatos sin **consentimiento específico para la finalidad de comercialización** (la finalidad de "reclutar" no habilita "vender datos" — limitación de finalidad, Art. 5).
- Benchmarks tan granulares que permitan deducir la compensación de una persona o de una empresa-cliente individualizable.
- Incluir **datos sensibles** en el producto sin base reforzada.
- En el caso UE: incluso anónimos requieren rigor; si quedan pseudonimizados, sigue aplicando GDPR y se necesita base legal (consentimiento o interés legítimo bien fundado) y, posiblemente, evaluación de impacto.

**Refuerzo recomendado (cinturón y tirantes):** aunque la anonimización exime legalmente, conviene **informar a los candidatos** en la política de privacidad que datos agregados/anonimizados podrán usarse para análisis y benchmarks de mercado, y ofrecer transparencia. Esto reduce riesgo reputacional y blinda frente a una eventual interpretación estricta del regulador.

---

## Qué significa para Conexión Talento

1. **Cumplir YA en El Salvador.** No es opcional ni futuro: la ley está vigente y la empresa es sujeto obligado con ~4000 titulares. Priorizar: base legal/consentimiento, registro de tratamientos, política de retención, responsable de datos y protocolo de brechas (72h).

2. **Rediseñar el consentimiento en Team Tailor por finalidad.** Separar: (a) participar en procesos de selección; (b) permanecer en la base para futuras vacantes; (c) uso de datos anonimizados para análisis/benchmark de mercado. Eliminar casillas pre-marcadas. Guardar evidencia de consentimiento y fecha.

3. **Definir y aplicar una política de retención.** La ley exige temporalidad. Fijar plazos (p. ej. X años desde el último contacto), con renovación de consentimiento o supresión automatizada. Útil además para depurar y estructurar la base de datos del proyecto.

4. **El producto de benchmark es comercializable — pero conviértelo en un pipeline de anonimización auditado.** Construir el dataset analítico **separado** del ATS, con anonimización irreversible, umbrales k-anónimos y pruebas de reidentificación documentadas. Esto es a la vez el habilitador legal y un diferenciador de calidad del entregable.

5. **Cribado con IA = apoyo, no decisor.** Mantener revisión humana documentada, criterios explicables y auditoría periódica de sesgo (género, edad, origen). Aunque la ley salvadoreña no lo exige expresamente, protege frente a discriminación y prepara el terreno para la UE.

6. **Guatemala: anticiparse.** Sin ley vigente, pero aplicar el mismo estándar evita retrabajo cuando se apruebe (probable) y es argumento comercial de seriedad ante clientes.

7. **Mapear exposición a la UE antes de prometer nada.** Si algún cliente o candidato está en la UE, suben las obligaciones (GDPR + AI Act alto riesgo desde ago-2026). Conviene una pregunta de scoping temprana: ¿hay personas en la UE en el universo de datos? Si sí, diseñar para GDPR/AI Act desde el inicio.

8. **Designar un responsable/encargado de datos** (la práctica lo recomienda y la UE lo exigiría en varios escenarios) y documentar todo: el cumplimiento se prueba con registros.

---

## Nivel de confianza y vacíos

**Alta confianza:**
- Existencia, fecha y regulador (ACE) de la ley salvadoreña (Decreto 144, nov-2024): confirmado por múltiples fuentes concordantes, incluyendo el portal de la Asamblea Legislativa y firmas legales.
- Ausencia de ley general en Guatemala y existencia de iniciativas 6103/6572: confirmado por el Congreso de Guatemala y análisis legales regionales.
- Clasificación de la IA de reclutamiento como alto riesgo en el EU AI Act (Anexo III.4) y fechas clave (feb-2025 prohibiciones, 2-ago-2026 alto riesgo): confirmado por fuentes oficiales de la UE.
- Exclusión de datos anonimizados/disociados del ámbito de la LPDP salvadoreña (fundamento del benchmark): confirmado en el texto de la ley.

**Confianza media / a verificar con el texto oficial:**
- **Numeración exacta de artículos** (Arts. 26-27 consentimiento, 37 sensibles, 40/44 transferencias, 57 sanciones, 64 vigencia): provienen de una transcripción secundaria (informatica-juridica.com) y de análisis de firmas; **deben cotejarse contra el Diario Oficial / PDF oficial de la Asamblea** antes de citarlos en la propuesta o en un contrato.
- **Montos exactos de sanciones**: el rango en salarios mínimos parece consistente, pero el salario mínimo de referencia y la conversión a USD deben confirmarse con la tabla vigente.
- **Estado del reglamento de la ACE y lineamientos emitidos**: no se pudo verificar si la ACE ya publicó el reglamento/lineamientos operativos posteriores a mayo-2025. **Es el punto más importante a actualizar**, porque ahí estarían reglas concretas sobre retención, registro y posibles disposiciones sobre decisiones automatizadas.

**Vacíos / no verificado:**
- La LPDP salvadoreña **no regula explícitamente** decisiones automatizadas ni "derecho a explicación"; no se halló jurisprudencia o lineamiento específico que lo desarrolle (más allá de protección constitucional general anti-discriminación).
- Estatus legislativo exacto y probabilidad de aprobación de las iniciativas guatemaltecas 6103/6572 a junio-2026: no verificado en detalle; el panorama puede haber cambiado.
- No se consultó a un abogado salvadoreño colegiado: **este brief es insumo de investigación, no opinión legal vinculante.** Antes de lanzar el producto de benchmark se recomienda dictamen legal local que valide el método de anonimización.

---

## Fuentes

1. [Asamblea Legislativa de El Salvador — Decreto N.º 144 (PDF oficial)](https://www.asamblea.gob.sv/sites/default/files/documents/decretos/7A4FBD85-7E1B-46BE-9408-6FC549E53E00.pdf) — Texto oficial de la ley (no se pudo abrir por error de certificado en esta sesión; **fuente primaria a cotejar**).
2. [Informática Jurídica — Decreto N.º 144, Ley de Protección de Datos Personales (texto/artículos)](https://www.informatica-juridica.com/ley/decreto-no-144-ley-para-la-proteccion-de-datos-personales-de-12-de-noviembre-de-2024/) — Articulado detallado: consentimiento, sensibles, ARCO-POL, transferencias, anonimización, sanciones, vigencia. (Transcripción secundaria a verificar.)
3. [Central Law — Nueva Ley de Protección de Datos Personales de El Salvador](https://central-law.com/el-salvador-nueva-ley-de-proteccion-de-datos-personales-claves-para-su-cumplimiento-y-aplicacion/) — Plazos de adecuación, rol de la ACE, brechas 72h, transferencias, ARCO-POL.
4. [LatinAlliance — Guía LPDP El Salvador](https://latinalliance.co/2026/03/27/proteccion-datos-personales-el-salvador-lpdp-guia/) — Derechos, clasificación de datos, obligaciones empresariales, mención a supervisión humana en decisiones automatizadas.
5. [Consortium Legal — Implementación de la protección de datos en Centroamérica](https://consortiumlegal.com/2025/09/25/implementacion-efectiva-de-la-proteccion-de-datos-en-centroamerica/) — Comparativo: El Salvador con ley vigente vs. Guatemala solo con iniciativas.
6. [Congreso de Guatemala — Iniciativa de protección de datos personales (2025)](https://www.congreso.gob.gt/noticias_congreso/13884/2025/1) — Estatus de la iniciativa 6572 en el Pleno.
7. [Competitividad GT — Ficha técnica Iniciativa 6103 (Ley Integral de Protección de Datos)](https://competitividad.gt/wp-content/uploads/2024/05/Ficha-Tecnica-Iniciativa-6103-Ley-Integral-de-proteccion-de-datos.pdf) — Contenido de la iniciativa guatemalteca 6103.
8. [IPANDETEC — El Salvador aprueba su ley de datos personales](https://ipandetec.org/biometria/el-salvador-aprueba-su-ley-de-datos-personales/) — Perspectiva de sociedad civil; principios, exclusión de datos anonimizados, *habeas data*; cuestionamientos a la independencia del regulador.
9. [EU Artificial Intelligence Act — Annex III (sistemas de alto riesgo)](https://artificialintelligenceact.eu/annex/3/) — Clasificación de IA de reclutamiento/selección como alto riesgo (punto 4).
10. [artificialintelligenceact.eu — Qué significa el AI Act para empresas de staffing](https://artificialintelligenceact.eu/what-the-act-means-for-staffing-businesses/) — Obligaciones para reclutamiento, supervisión humana, transparencia, fechas (feb-2025, 2-ago-2026), sanciones.
11. [GDPR-info.eu — Art. 3 GDPR (alcance territorial)](https://gdpr-info.eu/art-3-gdpr/) — Aplicación extraterritorial a empresas fuera de la UE.
12. [GDPR.eu — ¿Aplica el GDPR a empresas fuera de la UE?](https://gdpr.eu/companies-outside-of-europe/) — Criterio de "targeting", umbral de aplicabilidad y sanciones (€20M/4%).

*Documento preparado como insumo de investigación; no constituye asesoría legal. Verificar el articulado contra el Diario Oficial y obtener dictamen de abogado salvadoreño antes de lanzar el producto de benchmark o cláusulas contractuales.*
