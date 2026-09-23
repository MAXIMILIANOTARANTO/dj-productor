#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil, subprocess, sys
from pathlib import Path
ROOT = Path("/home/workdir/artifacts/temas")

def newest_wav(folder):
    wavs = sorted(folder.glob("*.wav"), key=lambda p: p.stat().st_mtime, reverse=True)
    return wavs[0] if wavs else None

def longest_wav(folder):
    wavs = list(folder.glob("*.wav"))
    return max(wavs, key=lambda p: p.stat().st_size) if wavs else None

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(r.returncode)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--src", default="")
    args = p.parse_args()
    base = ROOT / args.slug
    if not base.is_dir():
        raise SystemExit(f"no existe {base}")
    src = Path(args.src) if args.src else None
    if src is None:
        for folder, pick in (
            (base / "05_master", newest_wav),
            (base / "04_mezcla", newest_wav),
            (base / "03_piso", longest_wav),
            (base / "02_toma", newest_wav),
        ):
            if folder.is_dir():
                src = pick(folder)
                if src:
                    break
    if src is None or not src.exists():
        raise SystemExit("no hay wav para cerrar")
    master_dir = base / "05_master"
    master_dir.mkdir(parents=True, exist_ok=True)
    staged = master_dir / "bounce.wav"
    if src.resolve() != staged.resolve():
        shutil.copy2(src, staged)
    final_wav = base / "FINAL.wav"
    final_mp3 = base / "FINAL.mp3"
    run(["ffmpeg", "-y", "-i", str(staged), "-ac", "2", "-ar", "44100", "-c:a", "pcm_s16le", str(final_wav)])
    run(["ffmpeg", "-y", "-i", str(final_wav), "-codec:a", "libmp3lame", "-b:a", "256k", str(final_mp3)])
    print(final_wav)
    print(final_mp3)

if __name__ == "__main__":
    main()
