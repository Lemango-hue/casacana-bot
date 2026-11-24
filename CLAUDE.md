# Novela (título pendiente)

Este repositorio contiene una novela en español escrita en colaboración entre el autor y Claude. Aquí vive todo lo que el libro necesita recordar: cada sesión empieza sin memoria, así que lo que no esté en un archivo no existe para la siguiente.

## Reparto de trabajo

- Claude redacta los borradores; el autor edita y decide. La última palabra sobre trama, personajes y voz es del autor.
- Antes de que exista prosa de un capítulo, presenta el esquema escena por escena y espera la aprobación del autor (flujo de la skill `chapter-writing`).
- Lo que no esté decidido en los archivos del proyecto (un rasgo de un personaje, una regla del mundo, un hecho del pasado) se pregunta al autor antes de fijarlo; si lo propones tú, márcalo como propuesta hasta que lo apruebe.
- Cuando opines sobre el texto, diagnostica con franqueza y señala lo que no funciona aunque no te lo pregunten. El autor quiere mejorar el libro y un elogio sin fundamento no le sirve.
- Verifica antes de afirmar: si algo depende de lo ya escrito, léelo en los archivos en lugar de fiarte de la conversación.

## Idioma y estilo

- Todo el libro y toda la conversación van en español.
- Variedad: español neutro latinoamericano, con tuteo, sin regionalismos marcados (decisión del autor, 23-11-2026).
- Sigue la skill `estilo-es` para raya de diálogo, comillas, signos y tratamiento. Las skills de `story-skills` están pensadas primero para el inglés: conserva su intención y aplica las convenciones del español.
- La voz sale de los textos del autor en `voz/muestras/` y de `novela/style-sheet.md`.

## Dónde está cada cosa

| Ruta | Contenido |
|---|---|
| `novela/` | El proyecto del libro en formato story-skills: `story.md` (biblia), `style-sheet.md`, `characters/`, `worldbuilding/`, `plot/`, `chapters/`, `scenes/`, `continuity/`. Creado a mano el 23-11-2026; sus índices `_index.md` se mantienen a mano mientras la herramienta `story` no pueda ejecutarse. El mundo no se duplica ahí: está en `mundo/`. |
| `mundo/` | El mundo de la historia (Novarkan). `mundo/README.md` explica su origen y sus límites; `mundo/notas/INDICE.md` es la puerta de entrada. Son notas, no el texto original del máster. |
| `mundo/master/` | Lo que el máster le dio al autor para Rem: `patron-de-rem.md` (texto literal) y `discord-con-el-master.md` (resumen de sus mensajes privados, con la ficha de Rem: dote, objetos, raza). Son la fuente de más autoridad. |
| `borrador-anterior/` | La historia original del autor (`Rem.docx` y su conversión a texto). Sus hechos están aprobados por el máster, salvo lo que el autor cambió después. No es el texto que se edita: la versión nueva se escribe en `novela/chapters/`. |
| `registro/critica-borrador.md` | La crítica completa de ese borrador, con conteos y errores de continuidad. Léela antes de redactar: dice qué no repetir. |
| `registro/propuesta-rework.md` | La historia nueva: las tres partes, el plan de la Parte I y el esquema del capítulo 1. |
| `herramientas/pagina-de-voz/` | Páginas HTML que leen en voz alta, para entregar preguntas y resúmenes al autor. |
| `CONTINUAR-EN-MI-COMPUTADORA.md` | Guía para el autor al pasar de la nube a una sesión local, con el estado y las preguntas abiertas. |
| `voz/muestras/` | Textos del autor para captar su voz. |
| `registro/procedencia.md` | Qué redactó Claude y qué cambió el autor, por capítulo. |
| `registro/decisiones.md` | Decisiones del autor que afectan a todo el libro. |
| `docs/investigacion/` | Informe sobre herramientas, flujo de trabajo y contexto legal, y las notas de investigación en `notas/`. |
| `.claude/skills/` | Las 24 skills de story-skills y la skill propia `estilo-es`. |
| `.claude/terceros/` | Licencia y origen de lo copiado de terceros. |

## Ritual por capítulo

Una sesión por capítulo: el contexto limpio evita arrastrar versiones viejas de la historia.

1. Reúne el contexto del capítulo con la skill `chapter-writing` (personajes en escena, estado de continuidad, promesas y preguntas abiertas).
2. Presenta el esquema y espera aprobación.
3. Redacta en `novela/chapters/` siguiendo `estilo-es` y la voz del autor.
4. Repasa el borrador con la lista final de `estilo-es` y di al autor qué encontraste.
5. Actualiza escenas, estado de continuidad y registros como indica `chapter-writing`.
6. Anota el capítulo en `registro/procedencia.md`.
7. Haz commit y push, para que nada dependa de la máquina de la sesión.

Cuando el autor devuelva un capítulo editado, trata su versión como la buena: actualiza la continuidad a partir de ella y anota en `registro/procedencia.md` que la editó.

## La herramienta `story`

Las skills usan un programa de comprobación incluido en `.claude/skills/story-maintenance/scripts/story.js` (cuenta palabras, reconstruye índices y detecta fallos de continuidad). Es código de terceros: ejecútalo solo si el autor lo ha autorizado en la sesión. Si no puede ejecutarse, haz esas comprobaciones leyendo los archivos y crea el proyecto con `story-init/references/manual-setup.md`, y avisa al autor de que la comprobación fue manual.

## Publicación

El texto es para la mesa de la campaña de rol del autor y no se va a publicar (decisión del 23-11-2026). Por eso se usa el mundo del máster y el material de D&D tal cual. `registro/procedencia.md` se mantiene igualmente al día: si el autor cambiara de idea y quisiera publicar, haría falta el permiso del máster, retirar lo que pertenece a D&D y declarar el texto generado por IA.

El repositorio está público por ahora. El autor autorizó el 23-11-2026 subir los cambios así y dijo que lo pasará a privado cuando pueda: haz push con normalidad y no vuelvas a preguntarlo. No subas nada que no sea de este proyecto.

## Estado del proyecto

La historia sigue a Rem, el personaje de un borrador anterior del autor (unas 30 000 palabras, en `borrador-anterior/`; criticado el 23-11-2026 en `registro/critica-borrador.md`), y transcurre en Novarkan. Lee `mundo/README.md` y `registro/decisiones.md` antes de proponer nada: hay contradicciones entre ese borrador y el mundo, y decisiones que dependen del máster de la campaña.

Ya se sabe que Rem es brujo y que su patrón es Polybius, de la orden de la Muerte Verdadera: el texto del máster está en `mundo/master/patron-de-rem.md` y manda sobre las notas y sobre el borrador anterior.

Rem es un Kalashtar del tipo Nightmare, tiene 19 años en el 56 PSM (nació hacia el 37 PSM), es huérfano sin familia conocida y no tiene elemento asignado. El ritual del orfanato y sus llamas negras son obra de Él y los Sentinels, no de la orden de su patrón. El máster aprobó los hechos del borrador anterior, así que son canon de la mesa.

El ritual del orfanato ocurre la noche del día 7 del mes 7 del 48 PSM, con Rem de 11 años; Varo lo encuentra un año después. La cronología completa está en `registro/decisiones.md`.

Rem ya juega en la campaña (Guerrero 1 / Brujo 8) y de adulto es duro y activo: ha matado a unos 38 del culto de Él. El rework debe tender el puente entre el niño del orfanato y ese adulto, y sirve además para que el autor practique cómo interpretarlo en la mesa. Carácter fijado: se aleja y guarda rencor; primero culpa y después rabia. Tono: oscuro y serio, con terror lovecraftiano cuando aparece Él.

De niño, lo que Rem más quiere es pertenecer. Los elementos de Kani y Stark no se mencionan.

La estructura en tres partes está aprobada (`registro/propuesta-rework.md`): el orfanato, la calle y Varo, y Polybius. Varo es un Paladín del Juramento de Somnia. «El Sello» está eliminado: no lo uses. Los ojos de Rem son los del borrador (dos anillos, turquesa y naranja). Habrá una guía de interpretación para la mesa.

El plan de la Parte I y el esquema del capítulo 1 están aprobados (`registro/propuesta-rework.md`). Se escribe capítulo a capítulo: el autor lee cada uno antes de seguir. Siguiente paso: redactar el capítulo 1.

El autor prefiere escuchar a leer: además del texto en el chat, entrégale las preguntas y los resúmenes en audio. Desde el 24-11-2026 el autor tiene conectado ElevenLabs: usa su herramienta de generar voz, descarga el mp3 y envíaselo como archivo. Voz probada: «Miguel - Voz Profunda Latino Neutro» (voice_id `eA1KGxXkPw301wzoKzzz`), modelo `eleven_v4`; el autor aún no ha confirmado si le gusta. Gasta créditos de su cuenta, así que escribe los audios breves y no repitas una generación para reintentar. Si ElevenLabs no está disponible, queda la página HTML que lee con la voz del navegador (molde en `herramientas/pagina-de-voz/`). Mensajes cortos. No uses ventanas de preguntas con opciones: las ha rechazado dos veces.

No hay muestras de voz del autor: la voz se rige por `novela/style-sheet.md`.

El 24-11-2026 el autor decidió seguir trabajando en una sesión local, en su computadora, porque en la nube no se podía usar su navegador ni generar audio. Si estás en esa sesión local: puedes leer World Anvil y Discord con su navegador para traer el texto exacto del máster, y puedes pedirle permiso para ejecutar la herramienta `story`.
