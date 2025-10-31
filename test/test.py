r"""
uv run test/test.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from discord_ntfy import notify_discord


def test_notify_discord():
    message = "Hello from discord-ntfy test!"
    result = notify_discord(message)
    
    if result:
        print("✓ Notification sent successfully")
    else:
        print("✗ Failed to send notification")
    
    return result


if __name__ == "__main__":
    test_notify_discord()

