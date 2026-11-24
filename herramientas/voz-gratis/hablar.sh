#!/usr/bin/env bash
# Convierte un texto en un audio mp3 con un motor de voz gratuito que corre en
# la propia máquina. No gasta créditos ni envía el texto a ningún servicio.
#
# Uso:
#   herramientas/voz-gratis/hablar.sh "Texto que se va a leer" salida.mp3 [voz]
#   herramientas/voz-gratis/hablar.sh - salida.mp3 [voz]   (lee el texto de la entrada estándar)
#
# Voces:
#   em_alex (por defecto), em_santa, ef_dora   -> motor Kokoro, el que prefiere el autor
#   es_MX-claude-high, es_MX-ald-medium ...     -> motor Piper
#
# La primera vez instala el motor y descarga la voz (Kokoro, unos 350 MB; Piper,
# unos 63 MB por voz); después es inmediato. Requiere python3, curl y ffmpeg.
set -euo pipefail

texto="${1:?Falta el texto (o - para leerlo de la entrada estándar)}"
salida="${2:?Falta el archivo mp3 de salida}"
voz="${3:-em_alex}"
base="${VOZ_GRATIS_DIR:-$HOME/.cache/voz-gratis}"
aqui="$(cd "$(dirname "$0")" && pwd)"
py="$base/venv/bin/python"

mkdir -p "$base"
[ -x "$py" ] || python3 -m venv --system-site-packages "$base/venv"

wav="$(mktemp --suffix=.wav)"
entrada="$(mktemp)"
trap 'rm -f "$wav" "$entrada"' EXIT
if [ "$texto" = "-" ]; then cat > "$entrada"; else printf '%s\n' "$texto" > "$entrada"; fi

case "$voz" in
  em_*|ef_*)
    "$py" -c "import kokoro_onnx, soundfile" 2>/dev/null || "$base/venv/bin/pip" install -q kokoro-onnx soundfile
    mkdir -p "$base/kokoro"
    for f in kokoro-v1.0.onnx voices-v1.0.bin; do
      [ -f "$base/kokoro/$f" ] || curl -sS -L -o "$base/kokoro/$f" \
        "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
    done
    "$py" "$aqui/kokoro_hablar.py" "$base/kokoro" "$voz" "$wav" < "$entrada"
    ;;
  *)
    "$py" -c "import piper" 2>/dev/null || "$base/venv/bin/pip" install -q piper-tts
    mkdir -p "$base/voces"
    [ -f "$base/voces/$voz.onnx" ] || "$py" -m piper.download_voices --download-dir "$base/voces" "$voz"
    "$py" -m piper -m "$base/voces/$voz.onnx" -f "$wav" < "$entrada"
    ;;
esac

# Iguala el volumen para que todas las voces suenen igual de fuerte.
ffmpeg -v error -y -i "$wav" -af loudnorm=I=-16:TP=-1.5:LRA=11 -codec:a libmp3lame -q:a 3 "$salida"
echo "Audio guardado en $salida"
