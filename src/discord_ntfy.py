import os
import requests
from dotenv import load_dotenv


def notify_discord(message: str, webhook_url: str = None) -> bool:
    load_dotenv()

    if webhook_url is None:
        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Discord webhook URL not found. Unable to send notification.")
        return False

    payload = {"content": message}

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Discord notification: {e}")
        return False
