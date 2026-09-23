---
name: dj-productor
description: Skill final DJ PRODUCTOR. Engloba toma, piso, capas, master y entrega. Cada tema vive en su carpeta. El cierre es siempre un solo archivo FINAL.wav mas FINAL.mp3. Absorbe maestro-electronica-dj y sistema-toma-sonora. Triggers — dj productor, skill final musica, nuevo tema, carpeta de tema, cerrar tema, bounce final, producir track, set house tech, voz sobre piso.
metadata:
  version: "1.0"
  tipo: skill-final
---

# DJ Productor

Un tema. Una carpeta. Un archivo final.
Todo lo demas (stems, loops, tomas, partitura) es andamiaje.

Cuerpos absorbidos
- Toma — https://github.com/MAXIMILIANOTARANTO/sistema-toma-sonora
- Piso — https://github.com/MAXIMILIANOTARANTO/maestro-electronica-dj

## Proteccion

- No API keys en repo.
- No reverse de MakeSong.
- Voz / poema es lead si existe.
- Silencio escrito no se rellena.
- Licencias a la vista. El bounce no lava una licencia.

## Carpeta de tema (obligatoria)

Raiz — `/home/workdir/artifacts/temas/<slug>/`

```
<slug>/
  00_brief.md
  01_letra.md
  02_toma/
  03_piso/
  04_mezcla/
  05_master/
  FINAL.wav
  FINAL.mp3
```

Crear con `scripts/nuevo_tema.py`.
Cerrar con `scripts/cerrar_tema.py`.

## Flujo unico

1. Nucleo — slug, BPM, clave, corriente, voz.
2. Letra en 01_letra.md con etiquetas.
3. Toma en 02_toma/. Variety Off.
4. Piso 118-122 si hay habla. Stems en 03_piso/.
5. Mezcla HPF 160-180. 04_mezcla/pre.wav.
6. FINAL.wav 44.1 16-bit + FINAL.mp3 256k.
7. No cerrar sin FINAL.*.

## Eficiencia

No regenerar piso si no cambio el brief. No llamar generador si ya hay toma. GitHub lleva brief y letra, no wavs salvo pedido.
