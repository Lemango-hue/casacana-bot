#!/usr/bin/env bash
# Convierte un texto en un audio mp3 con Piper, un motor de voz gratuito que
# corre en la propia máquina. No gasta créditos ni envía el texto a ningún servicio.
#
# Uso:
#   herramientas/voz-gratis/hablar.sh "Texto que se va a leer" salida.mp3 [voz]
#   herramientas/voz-gratis/hablar.sh - salida.mp3 [voz]   (lee el texto de la entrada estándar)
#
# Voces en español probadas: es_MX-claude-high (por defecto) y es_MX-ald-medium.
# La primera vez instala Piper y descarga la voz (unos 63 MB); después es inmediato.
# Requiere python3 y ffmpeg.
set -euo pipefail

texto="${1:?Falta el texto (o - para leerlo de la entrada estándar)}"
salida="${2:?Falta el archivo mp3 de salida}"
voz="${3:-es_MX-claude-high}"
base="${VOZ_GRATIS_DIR:-$HOME/.cache/voz-gratis}"

mkdir -p "$base/voces"
if [ ! -x "$base/venv/bin/python" ]; then
  python3 -m venv --system-site-packages "$base/venv"
  "$base/venv/bin/pip" install -q piper-tts
fi
if [ ! -f "$base/voces/$voz.onnx" ]; then
  "$base/venv/bin/python" -m piper.download_voices --download-dir "$base/voces" "$voz"
fi

wav="$(mktemp --suffix=.wav)"
trap 'rm -f "$wav"' EXIT
if [ "$texto" = "-" ]; then
  "$base/venv/bin/python" -m piper -m "$base/voces/$voz.onnx" -f "$wav"
else
  printf '%s\n' "$texto" | "$base/venv/bin/python" -m piper -m "$base/voces/$voz.onnx" -f "$wav"
fi
ffmpeg -v error -y -i "$wav" -codec:a libmp3lame -q:a 4 "$salida"
echo "Audio guardado en $salida"
