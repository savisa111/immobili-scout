import os
import json
import requests

TOKEN = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
CHAT_ID = os.getenv("681440652")

with open("ricerche.json", "r", encoding="utf-8") as f:
    searches = json.load(f)

msg = f"""
🏠 IMMOBILI SCOUT

✅ GitHub attivo

✅ Telegram attivo

✅ Configurazione corretta

📊 Ricerche caricate:
{len(searches)}

🚀 Pronto per Playwright
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": msg
    }
)

print("MESSAGGIO INVIATO")
