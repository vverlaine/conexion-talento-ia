#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renderiza la propuesta PDF: Markdown -> (pandoc) HTML -> (weasyprint) PDF.

Uso:  python3 assets/render_pdf.py     (desde 04-propuesta/)
Requiere: pandoc, weasyprint.
"""
import subprocess, pathlib, sys

HERE   = pathlib.Path(__file__).resolve().parent          # .../04-propuesta/assets
ROOT   = HERE.parent                                       # .../04-propuesta
MD     = ROOT / "Propuesta-Conexion-Talento.md"
CSS    = HERE / "estilo-pdf.css"
OUT    = ROOT / "Propuesta-Conexion-Talento.pdf"
FULL   = HERE / "_full.html"

FIRM = "Vértice"   # nombre de la firma

COVER = f"""<div class="cover">
  <div class="band"></div>
  <div class="inner">
    <div class="eyebrow">Propuesta de arranque · Confidencial</div>
    <h1>Tu ojo clínico,<br>vuelto un sistema que escala</h1>
    <div class="sub">Ordenar y medir el motor de Reclutamiento &amp; Selección y —con tu criterio—
      activar la IA y tu base de talento. Empezamos por una victoria concreta en 3 semanas,
      no por un gran compromiso.</div>
    <div class="meta">
      <span><strong>Preparado para</strong><br>Virginia — CEO, Conexión Talento</span>
      <span><strong>Preparado por</strong><br>{FIRM} · Data, IA &amp; Transf. Digital</span>
      <span><strong>Fecha</strong><br>Julio 2026</span>
    </div>
  </div>
</div>"""

def main():
    body = subprocess.run(
        ["pandoc", str(MD), "-f", "markdown", "-t", "html5"],
        capture_output=True, text=True, check=True).stdout
    css = CSS.read_text(encoding="utf-8")
    html = (f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
            f"<style>\n{css}\n</style></head><body>\n{COVER}\n{body}\n</body></html>")
    FULL.write_text(html, encoding="utf-8")
    subprocess.run(["weasyprint", str(FULL), str(OUT)], check=True)
    print("PDF guardado:", OUT)

if __name__ == "__main__":
    sys.exit(main())
