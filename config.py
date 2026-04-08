import json
import base64
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ANTHROPIC_API_KEY: str
    WHATSAPP_API_KEY: str = ""
    WHATSAPP_PHONE_NUMBER_ID: str = ""
    META_VERIFY_TOKEN: str = "casacana_webhook_2024"
    META_APP_SECRET: str = ""
    INSTAGRAM_PAGE_ACCESS_TOKEN: str = ""
    GOOGLE_SHEET_ID: str
    GOOGLE_CREDENTIALS_FILE: str = "credentials.json"
    GOOGLE_CREDENTIALS_B64: str = ""
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_GROUP_CHAT_ID: str

    class Config:
        env_file = ".env"


# Decode base64 credentials for cloud deployment (Render/Railway)
creds_b64 = os.getenv("GOOGLE_CREDENTIALS_B64")
if creds_b64 and not os.path.exists("credentials.json"):
    with open("credentials.json", "w") as f:
        json.dump(json.loads(base64.b64decode(creds_b64)), f)

settings = Settings()
