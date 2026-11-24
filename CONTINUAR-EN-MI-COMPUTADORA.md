# Cómo continuar en tu computadora

Este paquete contiene todo el proyecto de la historia de Rem tal como quedó el 24 de noviembre de 2026, después de trabajarlo en una sesión de Claude en la nube. Está pensado para que sigas desde tu computadora sin perder nada.

## Qué hacer (tres pasos)

1. **Descomprime el zip** en una carpeta que no vayas a borrar, por ejemplo en Documentos.
2. **Abre la app de escritorio de Claude** y empieza una sesión que trabaje **en esa carpeta de tu computadora** (no en la nube).
3. **Pégale este mensaje:**

```text
Este es el proyecto de la historia de Rem, mi personaje de la campaña de Novarkan. Venimos de una sesión en la nube.

Lee primero CLAUDE.md, luego CONTINUAR-EN-MI-COMPUTADORA.md y registro/decisiones.md. Después lee novela/story.md, novela/style-sheet.md, las fichas de novela/characters/ y registro/propuesta-rework.md.

El plan de la Parte I y el esquema del capítulo 1 ya están aprobados. Lo siguiente es escribir el capítulo 1. Antes de escribir, dime en pocas líneas qué entendiste y qué te falta.

Prefiero escuchar a leer: háblame corto y, cuando puedas, dame las preguntas y los resúmenes en audio.
```

## Qué hay en el paquete

| Carpeta o archivo | Qué es |
|---|---|
| `CLAUDE.md` | Las reglas de trabajo y el estado del proyecto. Claude lo lee solo al empezar. |
| `registro/decisiones.md` | Todo lo que has decidido, con fecha y motivo, y lo que sigue pendiente. |
| `registro/propuesta-rework.md` | La historia nueva: las tres partes, el plan de la Parte I y el esquema del capítulo 1. |
| `registro/critica-borrador.md` | La crítica completa de tu borrador, con la nota. |
| `registro/procedencia.md` | Registro de quién escribe qué (todavía vacío). |
| `novela/` | El proyecto del libro: biblia, hoja de estilo y fichas de Rem, Kani, Stark, Rico, Aldis, Varo y Polybius. |
| `mundo/notas/` | El mundo de Novarkan: 15 archivos de notas de la wiki. |
| `mundo/master/` | Lo que te dio tu máster: el texto del patrón y el resumen de Discord. |
| `borrador-anterior/` | Tu historia original, en Word y en texto. |
| `docs/investigacion/` | El informe sobre skills y herramientas para escritores, y sus notas. |
| `herramientas/pagina-de-voz/` | Las páginas que leen en voz alta, por si quieres reutilizarlas. |
| `.claude/skills/` | Las 25 skills: las 24 de story-skills y `estilo-es`. Se cargan solas al abrir la carpeta con Claude Code. |
| `.git/` | El historial de cambios y el enlace con tu repositorio de GitHub (`Lemango-hue/casacana-bot`). |

Las carpetas que empiezan por punto (`.claude`, `.git`) están ocultas en algunos sistemas; es normal no verlas.

## Agentes, skills y plugins

- **Skills del proyecto:** van dentro del paquete, en `.claude/skills/`.
- **Skills y plugins de tu cuenta de Claude** (documentos, PDF, investigación y demás): no van en el zip porque no son archivos del proyecto. Viven en tu cuenta y, según la documentación de Claude Code, se sincronizan también a tu computadora.
- **Agentes:** en la nube no se creó ningún agente propio. Se usaron los que Claude trae de serie.
- **Plugin Apodictic** (editor que diagnostica sin reescribir): se te sugirió y no aparecía instalado. Es opcional; se añade desde `claude.ai/customize/plugins`.

## Lo que en la nube no se pudo y en tu computadora sí

- **Leer World Anvil y Discord directamente.** Una sesión local puede usar tu navegador con tus cuentas. Sirve para traer las páginas nuevas de tu máster (él anunció artículos sobre los Kalashtar, la Tierra de los Sueños y la Orden de la Muerte Verdadera) y para copiar el texto exacto en lugar de notas resumidas.
- **Audio de verdad.** En la nube se bloqueó la instalación de un programa de voz. En tu computadora, Claude puede usar la voz del sistema.
- **La herramienta `story`** de story-skills, que cuenta palabras y revisa la continuidad. En la nube el sistema de permisos no dejó ejecutarla. Está en `.claude/skills/story-maintenance/scripts/story.js`; es código de terceros, así que Claude debe pedirte permiso antes de usarla.

## Dónde quedamos

- **Aprobado:** la historia en tres partes (el orfanato; la calle y Varo; Polybius), Varo como paladín del Juramento de Somnia, el español neutro, el plan de seis capítulos de la Parte I y el esquema del capítulo 1.
- **Siguiente paso:** escribir el capítulo 1, «La cuna en la niebla».
- **Después:** una guía de una página para interpretar a Rem en la mesa.

## Preguntas que siguen abiertas

Para tu máster:

- Por qué la gente de Él quiere secuestrar a Rem.
- Si le parece bien que Varo sea un Paladín del Juramento de Somnia.
- Qué correcciones pide tu historia tras sus artículos de la Orden de la Muerte Verdadera.
- Cómo es el barrio de Rem en Darkopolis y cómo funcionan allí los orfanatos.
- Qué relación hay entre Rico y Pollyana Conagher.

Para ti:

- El título definitivo.
- Qué fue de Varo entre el entrenamiento y el presente.
- Si Rem tiene las orejas parecidas a las de elfo que le propusiste al máster.

## GitHub

Todo esto está también en tu repositorio `Lemango-hue/casacana-bot`, que sigue **público**. Dijiste que lo pasarías a privado: en GitHub, Settings, Danger Zone, «Change repository visibility». Desde tu computadora, Claude puede seguir subiendo los cambios ahí si tienes tu cuenta de GitHub conectada; si no, el proyecto funciona igual solo con la carpeta.

Una advertencia: no trabajes el proyecto a la vez en la nube y en tu computadora sin subir y bajar los cambios, porque las dos copias se separarían.
