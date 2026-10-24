import os
import json
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

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
🏠 TEST RICERCA IMMOBILIARE

STATUS:
{r.status_code}

HTML:
{len(r.text)}

URL:
{url[:100]}
"""

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": messaggio
        }
    )

except Exception as e:

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": f"ERRORE:\n{e}"
        }
    )
