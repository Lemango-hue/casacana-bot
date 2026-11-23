# Origen de las skills de story-skills

Las 24 carpetas de `.claude/skills/` distintas de `estilo-es` son una copia sin modificar de la carpeta `skills/` del proyecto Story Skills.

- Proyecto: https://github.com/danjdewhurst/story-skills
- Autor: Daniel Dewhurst
- Versión: 0.25.0
- Commit copiado: `33085ccc3ceb94a6ff9362cf499091123cdfb30d` (14 de noviembre de 2026)
- Fecha de la copia: 23 de noviembre de 2026
- Licencia: MIT (ver `LICENSE` en esta misma carpeta)

## Qué se revisó antes de copiar

- Se leyeron la documentación de idiomas, la guía para escritores y las skills `chapter-writing` y `story-init`.
- La herramienta `story-maintenance/scripts/story.js` se examinó por búsqueda de patrones: no contiene llamadas de red; solo lanza `git` y, para generar PDF, un motor de PDF que ya esté instalado. No fue una auditoría línea a línea.
- La herramienta no se ha ejecutado todavía en este proyecto.

## Cómo actualizar

Sustituir las 24 carpetas por las de una versión nueva del proyecto, revisar su lista de cambios (`CHANGELOG.md` en el repositorio de origen) y actualizar la versión y el commit de este archivo.
