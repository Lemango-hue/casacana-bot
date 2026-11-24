# Página de voz

El autor prefiere escuchar a leer. En la sesión en la nube no se pudo instalar un programa de voz, así que las preguntas y los resúmenes se le entregaron en una página HTML que los lee en voz alta con la voz del navegador (Web Speech API).

- `ejemplo-preguntas.html`: cuatro preguntas con botón «Escuchar todo» y un botón por pregunta.
- `ejemplo-resumen-capitulo-1.html`: el mismo molde con el resumen de un capítulo.

## Cómo reutilizarla

Copia uno de los ejemplos y cambia solo tres cosas dentro del `<script>`: el texto de `intro`, la lista `preguntas` (cada elemento tiene `texto`, que se ve; `rec`, la línea pequeña; y `voz`, lo que se lee en voz alta) y los títulos del `<h1>` y del `<title>`. Escribe el campo `voz` para el oído: frases completas, números con letra, sin signos raros.

## En una sesión local

Con Claude trabajando en la computadora del autor hay opciones mejores que esta página: la voz del sistema (por ejemplo `say` en macOS o el narrador de Windows) o un programa de voz instalado, que sí permiten generar un archivo de audio de verdad. Esta página queda como alternativa que funciona en cualquier navegador.
