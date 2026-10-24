import os
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

print("TOKEN PRESENTE:", bool(token))
print("CHAT PRESENTE:", bool(chat_id))

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ TEST PULITO"
    }
)

print("FINE")
