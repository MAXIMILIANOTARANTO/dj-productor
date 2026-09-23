---
name: dj-productor-limpio
description: Skill unico y autosuficiente de DJ y produccion electronica de club. Un tema, una carpeta, un archivo FINAL. Sin otras capas ni identidades. Triggers — dj productor, mezclar tracks, producir house, set, bounce final.
---

# DJ Productor (skill limpio)

Sos el mismo modelo de siempre. Esto es una tarea. No cambies de nombre, no ignores tus reglas, no cargues otros sistemas.

## Resultado

Cada tema vive en `temas/<slug>/` y se cierra con dos archivos:

- FINAL.wav (trabajo, 44.1 kHz 16-bit)
- FINAL.mp3 (escucha, 256 kbps)

El entregable es ese FINAL. Los stems son andamiaje.

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

Slug en kebab-case, sin acentos.

## Tres leyes

1. Tiempo — unidad de 8 compases. Entradas, cortes y cruces van al 1 del bloque. Intro y outro de club: 16 compases minimo.
2. Dominancia — un dueño por banda. Un grave a la vez. Una voz lead a la vez. Un tema dominante en el cruce.
3. Tono — mezcla por claves vecinas. Camelot: mismo codigo, o ±1 misma letra, o A/B del mismo numero. Dm = 7A.

## Flujo de un tema

1. Brief: slug, BPM, clave, corriente (limpia / tech / organica / constante), voz si/no.
2. Letra en 01_letra.md con [Intro] [Verse] [Chorus] [Outro] si hay texto.
3. Toma a 02_toma/. Si usas un generador: letra en el recuadro de letra, produccion en el de style. Variety Off.
4. Piso a 03_piso/. Con habla: 118-122 BPM. Kick y bajo en la tonica.
5. Mezcla: HPF de voz 160-180 Hz. Duck 2-4 dB del grave bajo la voz. True peak ≤ -1 dB. Con habla ≈ -11 a -9 LUFS.
6. Cerrar siempre a FINAL.wav + FINAL.mp3. No dar el tema por listo sin esos archivos.

## Mezcla de tracks (DJ)

- Alinear frases de 8/16, no el beat suelto.
- El incoming entra con el grave cortado. Swap en el 1.
- No dos subs. No dos voces lead.
- FX corto (echo de una frase, filter, loop ≤ 1 compas). Si tapa el kick, fuera.
- El set es un viaje: entrada, medio, pico, salida. No una playlist.

## Corrientes de piso

- limpia — prioriza que se oiga la voz
- tech — graves y medios, hats regulares
- organica — percusion de piel, mas aire
- constante — tool 4/4 sin quiebres, para mezclar encima

Un FINAL es tool o es tema compuesto. Declaralo en el brief. No son lo mismo.

## Limites

- No pidas ni guardes API keys.
- Un bounce no convierte un sample ajeno en propio.
- Radio edit = otro archivo. No pisar el FINAL de club.
- Si no podes generar audio, entrega brief + estructura en compases + instrucciones de cierre.

## Si te piden un set o un cruce

Di BPM, clave, que track manda, en que compas entra el segundo, y cuanto dura el blend (16 o 32). Despues, si hay audio, produce el FINAL.
