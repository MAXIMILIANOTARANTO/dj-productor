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

## Tiempo

- Tiempo = beat. Compas = 4 tiempos (4/4).
- Frase = 8 compases = 32 tiempos. Unidad de cruce.
- Blend house/tech: 16 compases. Minimo club: 8. Largo: 32.
- A 118 BPM: 8 compases ≈ 16.3 s. 16 ≈ 32.5 s.
- Cue del incoming: conta hacia atras desde el 1 del swap.
- Si el incoming necesita 16 de intro sin grave, arrancalo 16 antes del 1 de salida del A.

Tres cues por track: mix-in, mix-point, mix-out. Cue de practica: 2 compases antes del mix-point.

## Flujo de un tema

1. Brief: slug, BPM, clave, corriente (limpia / tech / organica / constante), voz si/no, cama stems o stereo residual.
2. Letra en 01_letra.md con [Intro] [Verse] [Chorus] [Outro] si hay texto.
3. Toma a 02_toma/. Generador: letra en recuadro de letra, produccion en style. Variety Off.
4. Piso a 03_piso/. Con habla: 118-122 BPM. Kick y bajo en la tonica.
5. Mezcla: HPF de voz 160-180 Hz. Duck 2-4 dB del grave bajo la voz. True peak ≤ -1 dB. Con habla ≈ -11 a -9 LUFS.
6. Cerrar siempre a FINAL.wav + FINAL.mp3.

## EQ de cabina

- LOW  < ~150 Hz — kick y sub. Un dueño.
- MID  150–2000 Hz — cuerpo, fundamental de voz.
- HIGH > 2 kHz — hats, aire, sibilancia.

Incoming entra con LOW en kill (o HPF 180+). MID/HIGH primero.
Swap de LOW en el 1, uno o dos beats. No fade largo de sub.
Dos voces: dueño de MID. La otra –3 a –6 dB en 1–4 kHz o mute.
HPF voz 160–180 no es el LOW del piso.
Gain con EQ en 12. Despues se corta LOW.
Incoming: MID/HIGH a las 10 hasta que el fader esta arriba. Fader al 100% en el 1.

## Swap de grave

1. Beatmatch o phrase-align. EQ incoming plana en auricular.
2. Kill LOW del incoming.
3. Fader incoming: solo MID/HIGH sobre el grave del A.
4. En el 1: LOW A down, LOW B up. Un movimiento.
5. MID/HIGH del A afuera en la frase siguiente. Fader out.

Si A o B no tienen kick (poema), el dueño del LOW es el piso. Swap de voz, no de grave.

Tres modos: duro (mismo 1), demorado (4 beats sin grave), lento (a lo largo de 8). Cama constante = no hay swap A↔B de LOW.

Filtro: HPF del outgoing en los ultimos 4–8. Si tapa el kick dueño, fuera.

## Mezcla de tracks (DJ)

- Alinear frases de 8/16, no el beat suelto.
- Incoming con grave cortado. Swap en el 1.
- No dos subs. No dos voces lead.
- FX corto (echo de una frase, filter, loop ≤ 1 compas). Si tapa el kick, fuera.
- Intro B sobre outro A — blend largo. Intro B sobre coro A — mas corto.
- Habla: cruzar en puerta o silencio escrito. No a mitad de oracion.
- Dos leads vocales: blend 8, no 32.
- Drop contra drop: cut o drop-swap.

## Habla / poema

- No estirar el habla si distorsiona la frase.
- Alinear la oracion al 1, no cada silaba.
- Un lead. Acentos del piso (IT/EN, una palabra) mas bajos, nunca coro lleno.
- Si el piso canta la misma frase que el lead: mute o HPF 1–4 kHz de esa voz.
- Corriente con habla: limpia o constante.

## Tercer deck / cama / loop

- Loop de piso puede ser cama constante. Brief: tool, no tema.
- Cama no suma un segundo kick.
- Voz del loop = ondulacion, no lead.
- Costura ≥ 8 s o cue de intro/outro sin letra. Prohibido reiniciar un verso a mitad de frase del lead.
- Loop FX ≤ 1. Loop de mezcla 4 u 8. Loop de cama: multiplo de 8 o 16.

## Stems

Si el piso tiene voz y hay lead, separar.

1. Demucs / Stemroller (drums, bass, vocals, other).
2. Cama = drums + bass. Vocals del piso mute o –8/–12 dB.
3. Spleeter solo si Demucs no corre.
4. VirtualDJ stems: cabina humana. El skill no depende de esa GUI.
5. Automix no mezcla el set.

`other` a –3/–6 si no tapa MID del lead.
Stem no lava licencia.
Sin stem: declarar `cama: stereo residual`, HPF 1–4 kHz o cama ≤ 0.25.
Separar antes de loopear.

```
03_piso/
  piso.wav
  stems/drums.wav
  stems/bass.wav
  stems/vocals.wav
  stems/other.wav
  cama.wav
```

## Corrientes de piso

- limpia — prioriza que se oiga la voz
- tech — graves y medios, hats regulares
- organica — percusion de piel, mas aire
- constante — tool 4/4 sin quiebres, para mezclar encima

Un FINAL es tool o es tema compuesto. Declaralo en el brief.

## Set

Antes de mezclar, decir: BPM del piso, Camelot, quien manda LOW, quien manda voz en cada bloque, compas de entrada del B, blend 8/16/32, tercer deck si/no y si su voz esta muteada.

Viaje: entrada → medio → tension → cruce → pico → salida. No playlist.

Despues del bounce: una pasada solo graves, una solo voz. Si el loop reinicia letra a mitad del lead: no cerrado.

## Limites

- No pidas ni guardes API keys.
- Un bounce no convierte un sample ajeno en propio.
- Radio edit = otro archivo. No pisar el FINAL de club.
- Si no podes generar audio, entrega brief + estructura en compases + instrucciones de cierre.
- Historia del DJ, marketing, mapeo de software y SYNC no son ley de este skill.
