# Voz gratis (Piper)

Genera audios en español sin gastar créditos. Usa [Piper](https://github.com/OHF-Voice/piper1-gpl), un motor de voz de código abierto que corre en la propia máquina: el texto no sale a ningún servicio.

- **Probado el 24 de noviembre de 2026** en la sesión en la nube, con `piper-tts` 1.8.0: se instaló, descargó las voces y generó los audios de prueba.
- **Voces probadas:** `es_MX-claude-high` y `es_MX-ald-medium`, las dos en español de México. Hay más: `es_AR-daniela-high`, `es_ES-davefx-medium`, `es_ES-sharvard-medium`.
- **Calidad:** se entiende bien, pero suena más plana y sintética que ElevenLabs. Quien la probó no puede oír: comprobó que el archivo se genera y tiene sonido, no cómo suena.

## Uso

```bash
herramientas/voz-gratis/hablar.sh "Texto que se va a leer" salida.mp3
```

Con otra voz:

```bash
herramientas/voz-gratis/hablar.sh "Texto que se va a leer" salida.mp3 es_MX-ald-medium
```

La primera vez instala Piper y descarga la voz (unos 63 MB). Necesita `python3` y `ffmpeg`.

## Cuándo usar cada una

- **Piper (esto):** preguntas, resúmenes y avisos del día a día. Gratis e ilimitado.
- **ElevenLabs** (conector del autor): cuando importe que suene bien, por ejemplo para escuchar un capítulo narrado. Gasta créditos de su cuenta.

## En la nube

La máquina de una sesión en la nube es temporal: en cada sesión nueva hay que volver a instalar Piper, cosa que este script hace solo la primera vez que se usa. La instalación puede quedar bloqueada por el sistema de permisos si el autor no la ha pedido en esa sesión.

## Licencias

Piper se distribuye bajo GPL-3.0. Cada voz tiene su propia licencia, indicada en su ficha del repositorio de voces de Piper. Aquí se usa solo para escuchar textos propios.
