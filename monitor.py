import os
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

print("TOKEN:", token is not None)
print("CHAT:", chat_id is not None)

if not token:
    raise Exception("TELEGRAM_TOKEN non trovato")

if not chat_id:
    raise Exception("TELEGRAM_CHAT_ID non trovato")

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ TEST GITHUB CORRETTO"
    }
)

print("STATUS:", r.status_code)
print(r.text)import os
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU ")
chat_id = os.getenv("681440652")

print("TOKEN PRESENTE:", bool(token))
print("CHAT_ID PRESENTE:", bool(chat_id))

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ NUOVA VERSIONE MONITOR"
    }
)

print("STATUS:", r.status_code)
print(r.text)
