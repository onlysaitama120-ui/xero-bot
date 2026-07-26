<div align="center">

# ⚡ XERO BOT

**Your all-in-one Discord bot — moderation, fun, utility & more**

[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1530862362807443576&permissions=8&scope=bot)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

---

</div>

## Features

| Category | Commands |
|----------|----------|
| **Moderation** | `!ban` `!kick` `!unban` `!mute` `!unmute` `!warn` `!slowmode` `!clear` `!lock` `!unlock` |
| **Fun** | `!8ball` `!coinflip` `!dice` `!poll` `!say` |
| **Utility** | `!userinfo` `!serverinfo` `!membercount` `!avatar` `!remind` `!calc` `!ping` `!hello` |
| **Admin** | `!announce` `!giveaway` `!giverole` `!removerole` |
| **Welcome** | Auto greet & farewell messages with embeds |

## Preview

![Dashboard](https://onlysaitama120-ui.github.io/xero-bot/)

## Setup

### Prerequisites
- Python 3.10+
- A Discord bot token from the [Developer Portal](https://discord.com/developers/applications)

### Installation

```bash
git clone https://github.com/onlysaitama120-ui/xero-bot.git
cd xero-bot
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:
```env
TOKEN=your_bot_token_here
```

### Run

```bash
python bot.py
```

### Host 24/7

Deploy on [Viirless](https://hosting.viirless.net) — free Discord bot hosting.

1. Fork/push this repo to GitHub
2. Connect your GitHub to Viirless
3. Set start command to `python bot.py`
4. Add `TOKEN` env variable in the dashboard
5. Deploy

## Tech Stack

- **discord.py 2.0+** — Discord API wrapper
- **Python 3.10+** — Runtime
- **Viirless** — Hosting

## License

MIT
