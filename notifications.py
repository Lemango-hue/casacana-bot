import httpx
from config import settings


async def notify_team(
    client_id: str,
    client_name: str | None,
    first_message: str,
    platform: str,
) -> None:
    text = (
        f"\U0001f514 *Nuevo cliente — Casa Cana*\n\n"
        f"\U0001f4f1 Canal: {platform.capitalize()}\n"
        f"\U0001f464 Cliente: {client_name or 'Desconocido'}\n"
        f"\U0001f194 ID: `{client_id}`\n"
        f"\U0001f4ac Mensaje: _{first_message[:120]}_\n\n"
        f"Para tomar control manual:\n"
        f"`POST /handoff/{client_id}?mode=human`"
    )

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as http:
        await http.post(url, json={
            "chat_id": settings.TELEGRAM_GROUP_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown",
        })
