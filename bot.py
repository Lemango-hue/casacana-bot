import logging
import anthropic
from sheets import save_conversation, get_conversation_history, upsert_client
from notifications import notify_team
from config import settings

logger = logging.getLogger(__name__)

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

handoff_modes: dict[str, str] = {}
notified_clients: set[str] = set()

SYSTEM_PROMPT = """
You are Cana, the virtual assistant for Casa Cana, a home finishing showroom
located at Avenida Barceló KM 6.5, Bávaro, Punta Cana, Dominican Republic.

PERSONALITY:
- Warm, professional, conversational. Never robotic.
- Reply in the same language the customer uses (Spanish or English).
- Keep responses to 3-4 sentences maximum per message.
- Use emojis sparingly to feel friendly.

ABOUT CASA CANA:
- Showroom specializing in: ceramics/porcelain tiles, modular kitchens, spas/jacuzzis, bathrooms, and doors.
- Sub-brand: BADECO by Casa Cana (specialized in bathrooms and kitchens).
- Featured collection: Serie Serena (available in White, Grey, Bone, Mud).
- Phone: +1 809-795-9000
- Email: info@casacana.do
- Hours: Lunes a Viernes 9:00 AM - 6:00 PM, Sabados 9:00 AM - 1:00 PM
- Both Punta Cana and Bavaro locations.

PRICING POLICY:
- Prices vary by product, quantity, and project scope.
- Never invent or estimate prices.
- For pricing: "Para darte una cotizacion exacta te recomiendo visitarnos o llamarnos al 809-795-9000."

UNKNOWN QUESTIONS:
- If you don't know the answer: "Para ese detalle especifico te recomiendo llamarnos al 809-795-9000 o visitarnos en el showroom."
- Never fabricate product specs, availability, or prices.

HANDOFF TRIGGER:
- If the customer says they want to talk to a person, agent, or human, respond:
  "Con gusto te conecto con uno de nuestros asesores. En un momento alguien del equipo te atiende personalmente."
- Then end your response with exactly this token on a new line: [HANDOFF_REQUESTED]
"""


async def process_message(
    client_id: str,
    text: str,
    platform: str,
    client_name: str | None = None,
    phone: str | None = None,
) -> str | None:
    if handoff_modes.get(client_id) == "human":
        save_conversation(client_id, text, "[HUMAN MODE - no bot reply]", platform, client_name, phone)
        return None

    if client_id not in notified_clients:
        try:
            await notify_team(client_id, client_name, text, platform)
        except Exception:
            logger.exception("Failed to send Telegram notification for %s", client_id)
        notified_clients.add(client_id)

    try:
        upsert_client(client_id, client_name, phone, platform)
    except Exception:
        logger.exception("Failed to upsert client %s", client_id)

    try:
        history = get_conversation_history(client_id, max_turns=10)
    except Exception:
        logger.exception("Failed to fetch history for %s", client_id)
        history = []

    messages = history + [{"role": "user", "content": text}]

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
        reply = response.content[0].text
    except Exception:
        logger.exception("Claude API error for %s", client_id)
        reply = (
            "Disculpa, estamos teniendo un problema tecnico. "
            "Por favor llamanos al 809-795-9000 o intenta de nuevo en unos minutos."
        )

    if "[HANDOFF_REQUESTED]" in reply:
        handoff_modes[client_id] = "human"
        reply = reply.replace("[HANDOFF_REQUESTED]", "").strip()

    try:
        save_conversation(client_id, text, reply, platform, client_name, phone)
    except Exception:
        logger.exception("Failed to save conversation for %s", client_id)

    return reply


def set_handoff_mode(client_id: str, mode: str) -> None:
    assert mode in ("bot", "human"), "mode must be 'bot' or 'human'"
    handoff_modes[client_id] = mode
