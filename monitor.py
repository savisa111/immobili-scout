import os
import json
import requests

TOKEN = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
CHAT_ID = os.getenv("681440652")

with open("ricerche.json", "r", encoding="utf-8") as f:
    ricerche = json.load(f)

messaggio = f"""
🏠 IMMOBILI SCOUT ONLINE

✅ GitHub Actions OK
✅ Telegram OK
✅ File configurazione OK

📊 Numero ricerche:
{len(ricerche)}

🚀 Pronto per scansione immobiliare
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": messaggio
    }
)

print("MESSAGGIO INVIATO")
