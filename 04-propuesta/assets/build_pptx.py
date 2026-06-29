#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la presentación ejecutiva (PPTX) para Conexión Talento."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---------- Paleta ----------
NAVY  = RGBColor(0x10,0x2A,0x43)
NAVY2 = RGBColor(0x0C,0x22,0x36)
TEAL  = RGBColor(0x1C,0x7C,0x8C)
TEALL = RGBColor(0x2E,0x9C,0xAD)
DEEP  = RGBColor(0x14,0x50,0x6B)
GOLD  = RGBColor(0xC9,0xA2,0x27)
INK   = RGBColor(0x1A,0x27,0x33)
MUTED = RGBColor(0x5B,0x6B,0x7B)
LINE  = RGBColor(0xD9,0xE2,0xEC)
SOFT  = RGBColor(0xF5,0xF7,0xFA)
WHITE = RGBColor(0xFF,0xFF,0xFF)
FONT  = "Arial"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]
ML = Inches(0.7)                      # margen izq
CW = Inches(13.333 - 1.4)            # ancho de contenido

def slide():
    return prs.slides.add_slide(BLANK)

def rect(s, l, t, w, h, fill=None, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE):
    sp = s.shapes.add_shape(shape, l, t, w, h)
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = line_w or Pt(1)
    return sp

def tb(s, l, t, w, h, anchor=MSO_ANCHOR.TOP):
    b = s.shapes.add_textbox(l, t, w, h); tf = b.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    return tf

def para(tf, runs, size=14, color=INK, bold=False, align=PP_ALIGN.LEFT,
         space_before=0, space_after=4, bullet=False, leading=1.08, first=False):
    p = tf.paragraphs[0] if first and not tf.paragraphs[0].runs else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before); p.space_after = Pt(space_after)
    try: p.line_spacing = leading
    except Exception: pass
    if isinstance(runs, str):
        runs = [(runs, bold, color, size)]
    if bullet:
        r = p.add_run(); r.text = "•  "
        r.font.size = Pt(size); r.font.color.rgb = TEAL; r.font.bold = True; r.font.name = FONT
    for item in runs:
        text, b, c, sz = (item + (bold, color, size))[:4] if isinstance(item, tuple) else (item, bold, color, size)
        r = p.add_run(); r.text = text
        r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = c; r.font.name = FONT
    return p

def footer(s, n, light=False):
    c = RGBColor(0x9F,0xB4,0xC6) if light else RGBColor(0xA8,0xB4,0xC0)
    tf = tb(s, ML, Inches(7.04), Inches(8), Inches(0.32))
    para(tf, "Confidencial · Conexión Talento", size=8, color=c, first=True)
    tf2 = tb(s, Inches(13.333-4.7), Inches(7.04), Inches(4), Inches(0.32))
    para(tf2, f"‹TU CONSULTORA›   ·   {n}", size=8, color=c, align=PP_ALIGN.RIGHT, first=True)

def title_bar(s, kicker, title, n):
    tf = tb(s, ML, Inches(0.42), CW, Inches(0.3))
    para(tf, kicker.upper(), size=10.5, color=TEAL, bold=True, first=True)
    tf2 = tb(s, ML, Inches(0.72), CW, Inches(0.7))
    para(tf2, title, size=25, color=NAVY, bold=True, first=True, leading=1.0)
    rect(s, ML, Inches(1.46), Inches(1.6), Pt(3), fill=TEAL)
    footer(s, n)
    return Inches(1.75)   # y de inicio de contenido

def style_table(tbl, header_fill=NAVY, header_color=WHITE, body_size=11.5,
                header_size=11.5, zebra=True, align_first_left=True):
    for ci, cell in enumerate(tbl.rows[0].cells):
        cell.fill.solid(); cell.fill.fore_color.rgb = header_fill
        cell.margin_top = Pt(3); cell.margin_bottom = Pt(3)
        cell.margin_left = Pt(6); cell.margin_right = Pt(6)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.size = Pt(header_size); r.font.bold = True
                r.font.color.rgb = header_color; r.font.name = FONT
    for ri in range(1, len(tbl.rows)):
        for ci, cell in enumerate(tbl.rows[ri].cells):
            cell.fill.solid()
            cell.fill.fore_color.rgb = SOFT if (zebra and ri % 2 == 0) else WHITE
            cell.margin_top = Pt(3); cell.margin_bottom = Pt(3)
            cell.margin_left = Pt(6); cell.margin_right = Pt(6)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            for p in cell.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(body_size); r.font.name = FONT
                    r.font.color.rgb = INK
                    if ci == 0 and align_first_left:
                        r.font.bold = True; r.font.color.rgb = NAVY

def add_table(s, data, l, t, w, col_w=None, header_fill=NAVY, body_size=11.5,
              header_size=11.5, row_h=None):
    rows, cols = len(data), len(data[0])
    gtbl = s.shapes.add_table(rows, cols, l, t, w, Inches(0.4*rows)).table
    # quitar estilo por defecto (banding) para controlar nosotros
    tblPr = gtbl._tbl.tblPr
    tblPr.set('firstRow', '0'); tblPr.set('bandRow', '0')
    for ri, row in enumerate(data):
        for ci, val in enumerate(row):
            cell = gtbl.cell(ri, ci)
            cell.text = ""
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            r = p.add_run(); r.text = str(val); r.font.name = FONT
    if col_w:
        for ci, cw in enumerate(col_w):
            gtbl.columns[ci].width = cw
    if row_h:
        for ri in range(rows):
            gtbl.rows[ri].height = row_h
    style_table(gtbl, header_fill=header_fill, body_size=body_size, header_size=header_size)
    return gtbl

# ============================================================== SLIDE 1 — PORTADA
s = slide()
rect(s, 0, 0, SW, SH, fill=NAVY)
rect(s, 0, 0, SW, Inches(0.16), fill=GOLD)
tf = tb(s, Inches(0.9), Inches(1.7), Inches(11), Inches(0.4))
para(tf, "PROPUESTA DE PROYECTO · CONFIDENCIAL", size=12, color=GOLD, bold=True, first=True)
tf = tb(s, Inches(0.9), Inches(2.25), Inches(11.2), Inches(2.0))
para(tf, "El sistema operativo de un", size=40, color=WHITE, bold=True, first=True, leading=1.05)
para(tf, "reclutamiento de clase mundial", size=40, color=WHITE, bold=True, leading=1.05)
tf = tb(s, Inches(0.9), Inches(4.25), Inches(10.6), Inches(1.2))
para(tf, "Estandarizar, medir y luego automatizar con IA el motor de Reclutamiento & Selección "
         "de Conexión Talento — y activar el valor de su base de talento.",
     size=16, color=RGBColor(0xC2,0xD4,0xE2), first=True, leading=1.3)
rect(s, Inches(0.9), Inches(6.25), Inches(11.5), Pt(1), fill=RGBColor(0x2A,0x44,0x5E))
for i,(a,b) in enumerate([("Preparado para","Virginia — CEO, Conexión Talento"),
                          ("Preparado por","‹TU CONSULTORA› · Data, IA & Transf. Digital"),
                          ("Fecha","Julio 2026")]):
    tf = tb(s, Inches(0.9+i*3.9), Inches(6.45), Inches(3.7), Inches(0.8))
    para(tf, a+":", size=10, color=RGBColor(0x9F,0xB4,0xC6), first=True, space_after=2)
    para(tf, b, size=11.5, color=WHITE, bold=True)

# ============================================================== SLIDE 2 — AGENDA
s = slide(); y = title_bar(s, "Hoja de ruta de hoy", "Agenda", 2)
items = [("01","El reto y el diagnóstico"),
         ("02","Nuestro enfoque: estandarizar antes de automatizar"),
         ("03","El proyecto en 4 fases (entregables, tiempos, esfuerzo)"),
         ("04","Roadmap"),
         ("05","Inversión y modelos de cobro"),
         ("06","Métricas de éxito, riesgos y próximos pasos")]
for i,(n,t) in enumerate(items):
    yy = Inches(2.0 + i*0.78)
    rect(s, ML, yy, Inches(0.62), Inches(0.62), fill=SOFT, line=TEAL, line_w=Pt(1.2))
    tf = tb(s, ML, yy, Inches(0.62), Inches(0.62), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, n, size=15, color=TEAL, bold=True, align=PP_ALIGN.CENTER, first=True)
    tf = tb(s, Inches(1.5), yy, Inches(10.5), Inches(0.62), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, t, size=16, color=INK, first=True)

# ============================================================== SLIDE 3 — EL RETO
s = slide(); y = title_bar(s, "01 · Entendimiento", "El reto", 3)
tf = tb(s, ML, y, CW, Inches(1.3))
para(tf, [("Conexión Talento vive de su motor de Reclutamiento & Selección — ", False, INK, 15),
          ("el 63% de los ingresos", True, NAVY, 15),
          (". Tiene activos poco comunes: el ojo clínico de Virginia, un ATS y ~4.000 candidatos. "
           "Lo que falta no son herramientas: es la ", False, INK, 15),
          ("columna vertebral", True, NAVY, 15),
          (" que vuelve ese talento escalable.", False, INK, 15)], first=True, leading=1.25)
# caja paradoja
box = rect(s, ML, Inches(3.05), CW, Inches(1.25), fill=RGBColor(0xEE,0xF5,0xF6))
rect(s, ML, Inches(3.05), Pt(4), Inches(1.25), fill=TEAL)
tf = tb(s, Inches(1.0), Inches(3.2), Inches(11.2), Inches(0.95), anchor=MSO_ANCHOR.MIDDLE)
para(tf, [("La paradoja: ", True, NAVY, 15),
          ("vende “cercanía al candidato” mientras la critican en LinkedIn por falta de seguimiento, "
           "y ya presentó dos veces el mismo candidato al mismo cliente. El cuello de botella no es de "
           "manos — es de proceso.", False, INK, 15)], first=True, leading=1.25)
tf = tb(s, ML, Inches(4.7), CW, Inches(2.0))
for t in ["4 reclutadores trabajan de 4 formas distintas, sin documentar ni estandarizar.",
          "Cero métricas: sin línea base no hay ROI demostrable ni precio premium.",
          "La base de ~4.000 candidatos no es buscable — “el oro” está sin refinar."]:
    para(tf, t, size=14.5, color=INK, bullet=True, space_after=7, first=(t.startswith("4 ")), leading=1.15)

# ============================================================== SLIDE 4 — DIAGNÓSTICO
s = slide(); y = title_bar(s, "01 · Diagnóstico", "Dónde estás hoy", 4)
data = [["Dimensión","Estado actual","Implicación"],
        ["Proceso","4 reclutadores, 4 métodos; sin documentar","El criterio no escala ni se transfiere"],
        ["Datos","~4.000 candidatos sin etiquetar ni vigencia","No buscable; ~30–50% probablemente caduco"],
        ["Tecnología","Team Tailor con IA sin explotar","Se paga capacidad que no se usa"],
        ["Métricas","Inexistentes (“no métricas”)","Sin línea base no hay ROI ni precio premium"],
        ["Experiencia","Sin seguimiento; críticas en LinkedIn","La marca dice “cercanía”, el candidato no la siente"]]
add_table(s, data, ML, y, CW, col_w=[Inches(2.3), Inches(5.0), Inches(4.63)],
          body_size=12.5, header_size=12.5, row_h=Inches(0.72))

# ============================================================== SLIDE 5 — TESIS
s = slide(); rect(s,0,0,SW,SH,fill=NAVY); footer(s,5,light=True)
rect(s, 0, 0, Inches(0.16), SH, fill=GOLD)
tf = tb(s, ML, Inches(0.6), CW, Inches(0.4))
para(tf, "02 · NUESTRO ENFOQUE", size=11, color=GOLD, bold=True, first=True)
tf = tb(s, ML, Inches(1.5), Inches(11.6), Inches(2.4))
para(tf, [("Estandarizar ", True, WHITE, 30),("antes de automatizar.", True, TEALL, 30)],
     first=True, leading=1.1)
para(tf, "Meter IA sobre el desorden solo produce malos resultados más rápido. "
         "El diferenciador no es la IA — es la disciplina de proceso que ningún "
         "competidor copia sin el criterio humano detrás.",
     size=16, color=RGBColor(0xC2,0xD4,0xE2), space_before=10, leading=1.3)
# secuencia
steps = ["Estandarizar el criterio","Medir líneas base","Estructurar los datos","IA asistida"]
x = ML
for i,stp in enumerate(steps):
    w = Inches(2.7)
    rect(s, x, Inches(4.7), w, Inches(0.95), fill=RGBColor(0x16,0x3A,0x55), line=TEAL, line_w=Pt(1))
    tf = tb(s, x, Inches(4.7), w, Inches(0.95), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, f"{i+1}. {stp}", size=13.5, color=WHITE, bold=True, align=PP_ALIGN.CENTER, first=True, leading=1.05)
    x = Emu(int(x) + int(w))
    if i < len(steps)-1:
        ar = tb(s, x, Inches(4.7), Inches(0.42), Inches(0.95), anchor=MSO_ANCHOR.MIDDLE)
        para(ar, "→", size=20, color=GOLD, bold=True, align=PP_ALIGN.CENTER, first=True)
        x = Emu(int(x) + int(Inches(0.42)))

# ============================================================== SLIDE 6 — SÍ / RETAMOS
s = slide(); y = title_bar(s, "02 · Honrar tu ambición y retarte", "Lo que decimos SÍ — y lo que te retamos", 6)
# columna SÍ
rect(s, ML, y, Inches(5.8), Inches(4.7), fill=RGBColor(0xEE,0xF5,0xF6))
rect(s, ML, y, Inches(5.8), Inches(0.5), fill=TEAL)
tf = tb(s, ML, y, Inches(5.8), Inches(0.5), anchor=MSO_ANCHOR.MIDDLE)
para(tf, "  SÍ (honra tu visión)", size=14, color=WHITE, bold=True, first=True)
tf = tb(s, Inches(0.95), Emu(int(y)+int(Inches(0.65))), Inches(5.3), Inches(3.9))
for t in ["Velocidad: time-to-terna de ~5 días a 48–72h, medible.",
          "Cercanía como proceso verificable (SLA al candidato).",
          "IA con criterio: pilotos de ROI claro y bajo riesgo.",
          "Monetizar la base — por un camino legal y bien hecho."]:
    para(tf, t, size=13, color=INK, bullet=True, space_after=8, first=(t.startswith("Velocidad")), leading=1.15)
# columna RETAMOS
rx = Inches(7.0)
rect(s, rx, y, Inches(5.63), Inches(4.7), fill=SOFT)
rect(s, rx, y, Inches(5.63), Inches(0.5), fill=GOLD)
tf = tb(s, rx, y, Inches(5.63), Inches(0.5), anchor=MSO_ANCHOR.MIDDLE)
para(tf, "  Te retamos a reconsiderar", size=14, color=NAVY, bold=True, first=True)
tf = tb(s, Emu(int(rx)+int(Inches(0.25))), Emu(int(y)+int(Inches(0.65))), Inches(5.1), Inches(3.9))
for a,b in [("“Una persona más”","el cuello de botella es de proceso, no de manos."),
            ("“6 agentes de IA”","hoy son 6 procesos sin escribir; 5 son herramientas."),
            ("“La base es oro”","es oro sin refinar; la medimos antes de invertir."),
            ("“Vender el benchmark”","bandera legal: solo anonimizado e irreversible."),
            ("“Salir del ATS”","no migrar aún; extraer por API primero.")]:
    para(tf, [(a+": ", True, NAVY, 12.5),(b, False, INK, 12.5)], bullet=True, space_after=7,
         first=(a.startswith("“Una")), leading=1.12)

# ============================================================== SLIDE 7 — FASES OVERVIEW
s = slide(); y = title_bar(s, "03 · El proyecto por fases", "Cuatro fases, con puertas de decisión", 7)
data = [["Fase","Nombre","Duración","Esfuerzo","Inversión","Resultado / Puerta"],
        ["0","Factibilidad + Quick Wins","2–3 sem","8–12 jorn.","US$2.500*","Semáforo de viabilidad + 2 quick wins"],
        ["1","Estandarizar, Documentar, Medir","4–6 sem","20–30 jorn.","US$9.500","La “columna vertebral”: SOPs, rúbrica, métricas"],
        ["2","IA asistida (modular)","6–8 sem","25–35 jorn.","US$12.000","Screener/Ranker + Generador de CV (con HITL)"],
        ["3","Activo de datos y escala","horizonte","a dimensionar","desde 15.000 /\nretainer 3.500/mes","Base buscable, mercado interno, benchmark"]]
add_table(s, data, ML, y, CW,
          col_w=[Inches(0.7),Inches(3.0),Inches(1.25),Inches(1.35),Inches(1.85),Inches(3.78)],
          body_size=11, header_size=11, row_h=Inches(0.82))
tf = tb(s, ML, Inches(6.55), CW, Inches(0.4))
para(tf, "* La Fase 0 acredita el 100% a la Fase 1. Cifras indicativas en USD, a calibrar con tarifa local y tu fee por colocación.",
     size=9.5, color=MUTED, first=True)

# ============================================================== SLIDES 8-11 — DETALLE FASES
def phase_slide(n, tag, meta, objetivo, entregables, puerta, color, idx):
    s = slide(); y = title_bar(s, f"03 · Fase {n}", tag, idx)
    rect(s, ML, y, Inches(2.0), Inches(0.42), fill=color)
    tf = tb(s, ML, y, Inches(2.0), Inches(0.42), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, f"  FASE {n}", size=13, color=WHITE, bold=True, first=True)
    tf = tb(s, Inches(2.9), y, Inches(9.7), Inches(0.42), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, meta, size=11.5, color=MUTED, align=PP_ALIGN.RIGHT, first=True)
    yy = Emu(int(y)+int(Inches(0.62)))
    tf = tb(s, ML, yy, CW, Inches(0.6))
    para(tf, [("Objetivo:  ", True, NAVY, 14),(objetivo, False, INK, 14)], first=True, leading=1.15)
    tf = tb(s, ML, Emu(int(yy)+int(Inches(0.62))), CW, Inches(3.0))
    para(tf, "Entregables", size=13, color=TEAL, bold=True, first=True, space_after=5)
    for i,e in enumerate(entregables):
        if isinstance(e, tuple):
            para(tf, [(e[0]+": ", True, NAVY, 12.5),(e[1], False, INK, 12.5)], bullet=True, space_after=5, leading=1.12)
        else:
            para(tf, e, size=12.5, color=INK, bullet=True, space_after=5, leading=1.12)
    # puerta
    by = Inches(6.05)
    rect(s, ML, by, CW, Inches(0.75), fill=SOFT, line=color, line_w=Pt(1))
    rect(s, ML, by, Pt(4), Inches(0.75), fill=color)
    tf = tb(s, Inches(0.95), by, Inches(11.5), Inches(0.75), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, [(f"Puerta {n} →  ", True, color, 12),(puerta, False, INK, 12)], first=True, leading=1.12)

phase_slide("0","Factibilidad + Quick Wins","2–3 semanas · 8–12 jornadas · US$2.500 (acredita a F1)",
    "apagar los supuestos frágiles y entregar valor visible de inmediato.",
    [("Spike de factibilidad","verificar la API/export de Team Tailor contra la cuenta real + muestreo de vigencia y marco legal"),
     ("Registro anti-duplicado","candidato × cliente × fecha — cierra el riesgo reputacional ya materializado"),
     ("Plantilla/SOP de CV con branding v1","formalizar tu prompt como activo versionado de la firma"),
     ("Cierre de brecha de privacidad","migrar el uso de IA a un entorno con DPA / no-entrenamiento"),
     ("Tablero de línea base","minado del historial del ATS (con caveats honestos)")],
    "API confirmada o plan B; vigencia medida; plantilla adoptada por los 4; ≥3 KPIs con línea base.",
    TEALL, 8)

phase_slide("1","Estandarizar, Documentar y Medir","4–6 semanas · 20–30 jornadas · US$9.500",
    "instalar la columna vertebral. Aquí vive el valor real y la capacidad que se queda.",
    [("Mapa de proceso “deber ser”","los 8 pasos con RACI, SLA por etapa y dueño nombrado"),
     ("SOP de cribado + rúbrica + golden set","tu ojo clínico hecho criterios y pesos — el entregable estrella"),
     ("Scorecard de intake","1 página por vacante: must/nice-to-have, pesos, éxito a 90 días"),
     ("Árbol de métricas + estandarización del ATS","1 North Star + ~10 KPIs; etapas y campos obligatorios"),
     ("Gobernanza de datos + taxonomía v1","RoPA-lite, base legal por finalidad, diccionario de skills (ESCO)")],
    "etapas estandarizadas; SOP + rúbrica firmados; golden set armado; baseline medido. La IA no arranca sin esto.",
    TEAL, 9)

phase_slide("2","IA asistida (modular)","6–8 semanas · 25–35 jornadas · US$12.000",
    "acelerar lo que ya probó su criterio. Solo módulos que pasen la “Puerta Listo para IA”.",
    [("Screener/Ranker asistido (~US$7.000)","des-identifica PII → puntúa vs scorecard con justificación → pre-ordena. El humano valida; la IA nunca rechaza sola"),
     ("Generador de CV con branding (~US$4.000)","extracción a esquema fijo + plantilla determinista"),
     ("Medición vs línea base + auditoría de sesgo","trazabilidad de prompts, criterios y scores"),
     ("Opcional: entrevistador de pre-screening","ASR comprado, con consentimiento de grabación")],
    "concordancia IA-vs-ojo clínico ≥ umbral en búsquedas reales; sin sesgo relevante; mejora medible de time-to-terna.",
    DEEP, 10)

phase_slide("3","Activo de datos y escala","horizonte · land-and-expand · desde US$15.000 o retainer US$3.500/mes",
    "convertir la base en activo líquido y abrir nuevas líneas. Condicionada a las fases previas.",
    [("Enriquecimiento de la base","parsing, golden record, score de vigencia → búsqueda por skill e internal-fill"),
     ("Mercado interno / historial de candidato","+ portal de auto-actualización"),
     ("Decisión augmentar-vs-migrar Team Tailor","con datos y caso de negocio"),
     ("Benchmark de compensaciones","solo con validación legal, k-anonimato y consentimiento — o alianza con proveedor licenciado"),
     ("Cross-sell de capacitaciones","a la base, con consentimiento separado")],
    "cada nueva línea se autofinancia con el valor demostrado en las fases previas.",
    GOLD, 11)

# ============================================================== SLIDE 12 — ROADMAP
s = slide(); y = title_bar(s, "04 · Roadmap", "Cómo se ve en el tiempo", 12)
chart_x = Inches(2.35); chart_w = Inches(10.0); weeks = 16
wk = Emu(int(chart_w) // weeks)
# rejilla de semanas
for i in range(0, weeks+1, 2):
    gx = Emu(int(chart_x) + i*int(wk))
    rect(s, gx, Inches(2.05), Pt(0.8), Inches(3.4), fill=LINE)
    lab = tb(s, Emu(gx-int(Inches(0.2))), Inches(1.78), Inches(0.4), Inches(0.25))
    para(lab, f"S{i if i>0 else 1}", size=8.5, color=MUTED, align=PP_ALIGN.CENTER, first=True)
bars = [("Fase 0", 0, 3, TEALL),("Fase 1", 2, 8, TEAL),
        ("Fase 2", 6, 13, DEEP),("Fase 3", 10, 16, GOLD)]
for i,(name, a, b, col) in enumerate(bars):
    ry = Inches(2.25 + i*0.78)
    lab = tb(s, ML, ry, Inches(1.6), Inches(0.5), anchor=MSO_ANCHOR.MIDDLE)
    para(lab, name, size=13, color=NAVY, bold=True, first=True)
    bx = Emu(int(chart_x) + a*int(wk)); bw = Emu((b-a)*int(wk))
    rect(s, bx, ry, bw, Inches(0.5), fill=col, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
# nota puertas
tf = tb(s, ML, Inches(5.7), CW, Inches(1.1))
for t,fr in [("Las fases se solapan: la extracción de datos corre en paralelo a la documentación.", True),
             ("Cada puerta go/no-go es una decisión explícita de continuar, reordenar o detener.", False),
             ("Arranque recomendado: Fases 0 + 1 (~7–9 semanas) para demostrar valor antes de invertir en IA.", False)]:
    para(tf, t, size=13, color=INK, bullet=True, space_after=6, first=fr, leading=1.15)

# ============================================================== SLIDE 13 — INVERSIÓN
s = slide(); y = title_bar(s, "05 · Inversión", "Paquetes y modelos de cobro", 13)
# paquetes (3 tarjetas)
pk = [("Arranque","Fase 0 + 1","~US$12.000", True),
      ("Sistema + piloto IA","Fases 0 + 1 + 2","~US$24.000", False),
      ("Programa completo","Fases 0–3","desde ~US$39.000", False)]
cw = Inches(3.83)
for i,(t,sub,price,rec) in enumerate(pk):
    x = Emu(int(ML) + i*int(Inches(4.05)))
    rect(s, x, y, cw, Inches(1.85), fill=(RGBColor(0xEE,0xF5,0xF6) if rec else SOFT),
         line=(TEAL if rec else LINE), line_w=Pt(1.5 if rec else 1))
    rect(s, x, y, cw, Inches(0.12), fill=(TEAL if rec else NAVY))
    tf = tb(s, Emu(int(x)+int(Inches(0.2))), Emu(int(y)+int(Inches(0.25))), Inches(3.4), Inches(1.5))
    para(tf, t + ("  ✓ recomendado" if rec else ""), size=13.5, color=NAVY, bold=True, first=True, space_after=2)
    para(tf, sub, size=11.5, color=MUTED, space_after=8)
    para(tf, price, size=20, color=(TEAL if rec else NAVY), bold=True)
# tabla modelos
tf = tb(s, ML, Inches(3.95), CW, Inches(0.35))
para(tf, "Tres modelos de cobro — tú eliges:", size=13, color=TEAL, bold=True, first=True)
data = [["Modelo","Cómo funciona","Cuándo encaja"],
        ["A · Fixed-fee por fase  ✓","Precio cerrado por entregables; pagas lo que apruebas en cada puerta","Fases 0–2 (recomendado para arrancar)"],
        ["B · Retainer mensual","Cuota fija (~US$2.500–5.000/mes) por acompañamiento y operación","Fase 3 / operación continua"],
        ["C · Híbrido base + éxito","Fee base reducido + kicker atado a una métrica","Solo Fase 3, con línea base limpia"]]
add_table(s, data, ML, Inches(4.35), CW, col_w=[Inches(3.0),Inches(5.6),Inches(3.33)],
          body_size=11, header_size=11, row_h=Inches(0.6))

# ============================================================== SLIDE 14 — MÉTRICAS
s = slide(); y = title_bar(s, "06 · Cómo medimos el éxito", "De “cero métricas” a un cuadro de mando", 14)
data = [["KPI","Qué mide","Línea base","Meta"],
        ["Time-to-terna","Días de apertura a terna entregada","~5 días","48–72h"],
        ["Aceptación de terna","% de ternas que el cliente aprueba","a medir","↑ sostenido"],
        ["Rotación a 90 días","% de colocados que salen <90 días","a medir","↓"],
        ["Cobertura base interna","% de mandatos cubiertos sin sourcing externo","~0% hoy","↑"],
        ["Salud de la base","% de candidatos vigentes y etiquetados","desconocida","↑"],
        ["Experiencia (CSAT)","% de candidatos satisfechos (con n)","a medir","≥ 80%"]]
add_table(s, data, ML, y, CW, col_w=[Inches(2.6),Inches(5.7),Inches(2.0),Inches(1.63)],
          body_size=11.5, header_size=11.5, row_h=Inches(0.6))
tf = tb(s, ML, Inches(6.5), CW, Inches(0.4))
para(tf, "Crear las líneas base (hoy inexistentes) es parte del valor de la Fase 1 — y la prueba de tu ROI.",
     size=11, color=MUTED, first=True)

# ============================================================== SLIDE 15 — RIESGOS
s = slide(); y = title_bar(s, "06 · Riesgos y cumplimiento", "Lo gestionamos por diseño", 15)
data = [["Riesgo","Mitigación"],
        ["Protección de datos — El Salvador ya regula (Decreto 144/2024, vigente)","Consentimiento por finalidad, registro, retención y responsable de datos desde la Fase 1. Cumplimiento por diseño = argumento de venta"],
        ["Vender el benchmark salarial = bandera roja","Congelado hasta dictamen de abogado salvadoreño + anonimización irreversible (k-anonimato)"],
        ["Sesgo en cribado automático","Humano-en-el-bucle obligatorio; la IA nunca rechaza sola; auditoría de sesgo y trazabilidad"],
        ["API de Team Tailor no verificada","Spike de factibilidad en semana 1; plan B de captura acotada"],
        ["Adopción del equipo","Co-diseño con los reclutadores; el rol extra como embajador de marca, no operativo"]]
add_table(s, data, ML, y, CW, col_w=[Inches(4.6),Inches(7.33)],
          body_size=11.5, header_size=12, row_h=Inches(0.8))

# ============================================================== SLIDE 16 — NECESITAMOS / PASOS
s = slide(); y = title_bar(s, "06 · Para arrancar", "Qué necesitamos de ti y próximos pasos", 16)
tf = tb(s, ML, y, Inches(6.0), Inches(0.4))
para(tf, "Qué necesitamos de Conexión Talento", size=14, color=TEAL, bold=True, first=True)
tf = tb(s, ML, Emu(int(y)+int(Inches(0.5))), Inches(6.0), Inches(3.8))
for t in ["Accesos a Team Tailor (lectura/export) — semana 1.",
          "Fee por colocación + volumen de mandatos/mes.",
          "Horas protegidas de Virginia (golden set).",
          "Confirmación del consentimiento de la base.",
          "Un dueño interno del estándar."]:
    para(tf, t, size=13, color=INK, bullet=True, space_after=8, first=(t.startswith("Accesos")), leading=1.15)
rx = Inches(7.1)
tf = tb(s, rx, y, Inches(5.5), Inches(0.4))
para(tf, "Próximos pasos", size=14, color=TEAL, bold=True, first=True)
for i,t in enumerate(["Validar la propuesta y elegir el paquete de arranque (Fase 0+1).",
                      "Habilitar accesos y compartir el fee por colocación.",
                      "Arrancar la Fase 0 — primer valor visible en 2–3 semanas."]):
    yy = Emu(int(y)+int(Inches(0.55)) + i*int(Inches(1.0)))
    rect(s, rx, yy, Inches(0.55), Inches(0.55), fill=TEAL)
    tf = tb(s, rx, yy, Inches(0.55), Inches(0.55), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, str(i+1), size=16, color=WHITE, bold=True, align=PP_ALIGN.CENTER, first=True)
    tf = tb(s, Emu(int(rx)+int(Inches(0.8))), yy, Inches(4.6), Inches(0.7), anchor=MSO_ANCHOR.MIDDLE)
    para(tf, t, size=13, color=INK, first=True, leading=1.15)

# ============================================================== SLIDE 17 — CIERRE
s = slide(); rect(s,0,0,SW,SH,fill=NAVY)
rect(s, 0, 0, SW, Inches(0.16), fill=GOLD)
tf = tb(s, Inches(0.9), Inches(2.7), Inches(11.5), Inches(2.0))
para(tf, "Instalamos el sistema operativo de tu firma —", size=28, color=WHITE, bold=True, first=True, leading=1.12)
para(tf, "no vendemos manos.", size=28, color=TEALL, bold=True, leading=1.12)
tf = tb(s, Inches(0.9), Inches(4.5), Inches(11), Inches(1.0))
para(tf, "Estándar + documentación + métricas + activos que se quedan y se componen. "
         "Empezamos pequeño, demostramos valor con datos, y escalamos solo lo que funciona.",
     size=15, color=RGBColor(0xC2,0xD4,0xE2), first=True, leading=1.3)
tf = tb(s, Inches(0.9), Inches(6.4), Inches(11), Inches(0.5))
para(tf, "Gracias, Virginia. — ‹TU CONSULTORA› · Data, IA & Transformación Digital",
     size=12, color=GOLD, bold=True, first=True)

prs.save("Presentacion-Conexion-Talento.pptx")
print("PPTX guardado:", len(prs.slides._sldIdLst), "slides")
