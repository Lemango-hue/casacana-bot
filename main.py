import json
import hmac
import hashlib
import logging
import httpx
from fastapi import FastAPI, Request, HTTPException, Query
from bot import process_message, set_handoff_mode
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Casa Cana Bot")


@app.get("/webhook")
async def verify_webhook(request: Request):
    params = dict(request.query_params)
    if params.get("hub.verify_token") == settings.META_VERIFY_TOKEN:
        return int(params["hub.challenge"])
    raise HTTPException(status_code=403, detail="Invalid verify token")


@app.post("/webhook")
async def receive_message(request: Request):
    raw_body = await request.body()
    body = json.loads(raw_body)

    # Validate Meta signature (skip if META_APP_SECRET not configured)
    if settings.META_APP_SECRET:
        signature = request.headers.get("X-Hub-Signature-256", "")
        expected = "sha256=" + hmac.new(
            settings.META_APP_SECRET.encode(), raw_body, hashlib.sha256
        ).hexdigest()
        if not hmac.compare_digest(signature, expected):
            raise HTTPException(status_code=403, detail="Invalid signature")

    entry = body.get("entry", [{}])[0]
    changes = entry.get("changes", [{}])[0]
    value = changes.get("value", {})

    try:
        # WhatsApp
        if "messages" in value and "contacts" in value:
            for msg, contact in zip(value["messages"], value["contacts"]):
                if msg.get("type") != "text":
                    continue
                client_id = msg["from"]
                text = msg["text"]["body"]
                client_name = contact.get("profile", {}).get("name")
                reply = await process_message(client_id, text, "whatsapp", client_name, client_id)
                if reply:
                    await send_whatsapp(client_id, reply)

        # Instagram
        messaging_list = entry.get("messaging", [])
        if messaging_list:
            messaging = messaging_list[0]
            if "message" in messaging and "text" in messaging.get("message", {}):
                client_id = messaging["sender"]["id"]
                text = messaging["message"]["text"]
                reply = await process_message(client_id, text, "instagram")
                if reply:
                    await send_instagram(client_id, reply)
    except Exception:
        logger.exception("Error processing webhook")

    return {"status": "ok"}


# Telegram test endpoint - send a message to test the bot without Meta
@app.post("/test")
async def test_message(request: Request):
    body = await request.json()
    client_id = body.get("client_id", "test_user")
    text = body.get("text", "Hola")
    client_name = body.get("name", "Test User")

    reply = await process_message(client_id, text, "test", client_name)
    return {"reply": reply}


@app.post("/handoff/{client_id}")
async def handoff(client_id: str, mode: str = Query(..., pattern="^(bot|human)$")):
    set_handoff_mode(client_id, mode)
    return {"client_id": client_id, "mode": mode, "status": "updated"}


@app.get("/health")
async def health():
    return {"status": "ok"}


async def send_whatsapp(to: str, text: str) -> None:
    if not settings.WHATSAPP_PHONE_NUMBER_ID:
        logger.warning("WhatsApp not configured, skipping send")
        return
    url = f"https://graph.facebook.com/v19.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {settings.WHATSAPP_API_KEY}"}
    payload = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": text}}
    async with httpx.AsyncClient() as http:
        response = await http.post(url, json=payload, headers=headers)
        response.raise_for_status()


async def send_instagram(recipient_id: str, text: str) -> None:
    if not settings.INSTAGRAM_PAGE_ACCESS_TOKEN:
        logger.warning("Instagram not configured, skipping send")
        return
    url = "https://graph.facebook.com/v19.0/me/messages"
    params = {"access_token": settings.INSTAGRAM_PAGE_ACCESS_TOKEN}
    payload = {"recipient": {"id": recipient_id}, "message": {"text": text}}
    async with httpx.AsyncClient() as http:
        response = await http.post(url, params=params, json=payload)
        response.raise_for_status()
