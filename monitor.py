import os
import json
import requests

TOKEN = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
CHAT_ID = os.getenv("681440652")

with open("ricerche.json", "r", encoding="utf-8") as f:
    ricerche = json.load(f)

url = ricerche[0]["url"]

try:

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    messaggio = f"""
🏠 IMMOBILI SCOUT

STATUS:
{r.status_code}

URL:
{url}

HTML:
{len(r.text)} caratteri
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": messaggio
        }
    )

    print("OK")

except Exception as e:

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": f"ERRORE:\n{e}"
        }
    )

    print(e)
