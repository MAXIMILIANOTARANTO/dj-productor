#!/usr/bin/env python3
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path("/home/workdir/artifacts/temas")

def slugify(s):
    s = s.strip().lower()
    trans = str.maketrans("áéíóúüñ", "aeiouun")
    s = s.translate(trans)
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "tema"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--bpm", default="118")
    p.add_argument("--key", default="Dm")
    p.add_argument("--corriente", default="tech", choices=["limpia", "tech", "organica", "constante"])
    p.add_argument("--voz", default="si", choices=["si", "no"])
    p.add_argument("--titulo", default="")
    args = p.parse_args()
    slug = slugify(args.slug)
    base = ROOT / slug
    for sub in ("02_toma", "03_piso", "04_mezcla", "05_master"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    titulo = args.titulo or slug.replace("-", " ")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    brief = base / "00_brief.md"
    if not brief.exists():
        brief.write_text(
            f"# {titulo}\n\n- slug: {slug}\n- bpm: {args.bpm}\n- key: {args.key}\n- corriente: {args.corriente}\n- voz: {args.voz}\n- creado: {now}\n- objetivo: FINAL.wav + FINAL.mp3\n",
            encoding="utf-8",
        )
    letra = base / "01_letra.md"
    if not letra.exists():
        letra.write_text(f"# Letra — {titulo}\n\n[Intro]\n\n[Verse]\n\n[Chorus]\n\n[Outro]\n", encoding="utf-8")
    print(base)

if __name__ == "__main__":
    main()
