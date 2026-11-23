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
- Variedad regional del narrador y de los personajes: **pendiente de decidir con el autor**.
- Sigue la skill `estilo-es` para raya de diálogo, comillas, signos y tratamiento. Las skills de `story-skills` están pensadas primero para el inglés: conserva su intención y aplica las convenciones del español.
- La voz sale de los textos del autor en `voz/muestras/` y de `novela/style-sheet.md`.

## Dónde está cada cosa

| Ruta | Contenido |
|---|---|
| `novela/` | El proyecto del libro en formato story-skills: `story.md` (biblia), `style-sheet.md`, `characters/`, `worldbuilding/`, `plot/`, `chapters/`, `scenes/`, `continuity/`. **Todavía no existe**: se crea con la skill `story-init` cuando el autor dé la idea. |
| `voz/muestras/` | Textos del autor para captar su voz. |
| `registro/procedencia.md` | Qué redactó Claude y qué cambió el autor, por capítulo. |
| `registro/decisiones.md` | Decisiones del autor que afectan a todo el libro. |
| `docs/investigacion/` | Informe sobre herramientas, flujo de trabajo y contexto legal. |
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

Como Claude redacta los borradores, el libro cuenta como contenido generado por IA para Amazon KDP, que exige declararlo aunque se edite a fondo. `registro/procedencia.md` es lo que permitirá declararlo con exactitud y distinguir la aportación del autor. Mantenlo al día.

## Estado del proyecto

Pendiente de recibir del autor: la idea de la novela, la variedad de español y las muestras de voz (o una entrevista de voz). Con eso, el siguiente paso es `premise-workshop` o `story-init`.
