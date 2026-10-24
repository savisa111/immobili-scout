import os
import requests

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU ")
chat_id = os.getenv("681440652")

print("TOKEN:", bool(token))
print("CHAT:", bool(chat_id))

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ IMMOBILI SCOUT FUNZIONANTE"
    }
)

print(r.status_code)
print(r.text)import os
import json
import requests
from bs4 import BeautifulSoup

with open("ricerche.json", "r", encoding="utf-8") as f:
    ricerche = json.load(f)

ricerca = ricerche[0]

url = ricerca["url"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("STATUS:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

links = set()

for a in soup.find_all("a", href=True):

    href = a["href"]

    if "/annunci/" in href:
        links.add(href)

token = os.getenv("8712672793:AAEqJg5tPNX6lw8-AzqDU5ej1s-hB_z_qGU")
chat_id = os.getenv("681440652")

msg = f"""
🏠 IMMOBILI SCOUT

STATUS:
{r.status_code}

HTML:
{len(r.text)}

LINK ANNUNCI TROVATI:
{len(links)}
"""

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": msg
    }
)

for link in list(links)[:10]:

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": link
        }
    )
