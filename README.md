# discord-ntfy

A simple Python library to send notifications to Discord via webhooks.

## Installation

```bash
pip install discord-ntfy
```

## Usage

1. Create a Discord webhook URL in your Discord server settings
2. Set the webhook URL in your `.env` file:

```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK_URL
```

3. Use the library:

```python
from discord_ntfy import notify_discord

# Send a notification
notify_discord("Hello, Discord!")

# Or provide webhook URL directly
notify_discord("Hello!", webhook_url="https://discord.com/api/webhooks/...")
```
