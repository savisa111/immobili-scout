import os
import json
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

with open("ricerche.json", "r", encoding="utf-8") as f:
    ricerche = json.load(f)

url = ricerche[0]["url"]

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

msg = f"""
🏠 TEST RICERCA IMMOBILIARE

STATUS:
{r.status_code}

HTML:
{len(r.text)} caratteri

URL:
{url[:150]}...
"""

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": msg
    }
)import os
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

print("TOKEN PRESENTE:", bool(token))
print("CHAT PRESENTE:", bool(chat_id))

if not token:
    raise Exception("TELEGRAM_TOKEN NON TROVATO")

if not chat_id:
    raise Exception("TELEGRAM_CHAT_ID NON TROVATO")

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ TEST GITHUB OK"
    }
)

print("STATUS:", r.status_code)
print(r.text)
