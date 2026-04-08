import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from config import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def _get_sheet(tab_name: str):
    creds = Credentials.from_service_account_file(settings.GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
    gc = gspread.authorize(creds)
    spreadsheet = gc.open_by_key(settings.GOOGLE_SHEET_ID)
    return spreadsheet.worksheet(tab_name)


def save_conversation(client_id, user_message, bot_reply, platform, client_name=None, phone=None):
    sheet = _get_sheet("Conversaciones")
    now = datetime.now()
    sheet.append_row([
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        platform,
        client_id,
        client_name or "",
        phone or "",
        user_message,
        bot_reply,
        "human" if "[HUMAN" in bot_reply else "bot",
    ])


def get_conversation_history(client_id: str, max_turns: int = 10) -> list[dict]:
    sheet = _get_sheet("Conversaciones")
    all_rows = sheet.get_all_records()
    client_rows = [r for r in all_rows if str(r.get("cliente_id")) == str(client_id)]
    recent = client_rows[-max_turns:]
    history = []
    for row in recent:
        if row.get("mensaje_cliente"):
            history.append({"role": "user", "content": str(row["mensaje_cliente"])})
        if row.get("respuesta_bot") and "[HUMAN MODE" not in str(row["respuesta_bot"]):
            history.append({"role": "assistant", "content": str(row["respuesta_bot"])})
    return history


def upsert_client(client_id, client_name, phone, platform):
    sheet = _get_sheet("Clientes")
    all_records = sheet.get_all_records()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    existing = next((i for i, r in enumerate(all_records) if str(r.get("cliente_id")) == str(client_id)), None)
    if existing is None:
        sheet.append_row([now, platform, client_id, client_name or "", phone or "", 1, now])
    else:
        row_index = existing + 2
        total = int(sheet.cell(row_index, 6).value or 0) + 1
        sheet.update_cell(row_index, 6, total)
        sheet.update_cell(row_index, 7, now)
        if client_name:
            sheet.update_cell(row_index, 4, client_name)
