"""Convierte un texto en un WAV con Kokoro, un motor de voz gratuito y local.

Uso: python kokoro_hablar.py CARPETA_DEL_MODELO VOZ SALIDA.wav [VELOCIDAD] < texto

Lo llama hablar.sh; no hace falta usarlo a mano.
"""
import sys

import soundfile as sf
from kokoro_onnx import Kokoro


def main() -> None:
    carpeta, voz, salida = sys.argv[1], sys.argv[2], sys.argv[3]
    velocidad = float(sys.argv[4]) if len(sys.argv) > 4 else 0.95
    texto = sys.stdin.read().strip()
    if not texto:
        sys.exit("No hay texto que leer.")
    motor = Kokoro(f"{carpeta}/kokoro-v1.0.onnx", f"{carpeta}/voices-v1.0.bin")
    audio, frecuencia = motor.create(texto, voice=voz, speed=velocidad, lang="es")
    sf.write(salida, audio, frecuencia)


if __name__ == "__main__":
    main()
