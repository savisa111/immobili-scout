import os
import requests

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

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
