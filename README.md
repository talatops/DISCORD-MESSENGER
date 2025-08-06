<h1 align="center">
  <br>
   ⏲️ Message Scheduler Bot ⏲️
  <br>
</h1>
<p align="center">A discord bot to assist you with scheduling messages. Supports loop functionality, embed customization, etc.</p>

## ❗ Features
* ➿ Loop schedules 
* 🔁 Endless loop available
* ⏲️ Supports time input as **minutes**, **hours**, **days** and **weeks**
* 👍 Easy functionality
* ♾️ Set unlimited schedules 
* 🔒 Usable by server administrators only
* 🤖 Supports prefix commands only
* 💬 Supports choice between a normal message and an embed
* 🆗 Confirm your schedule with overview command
* ✏️ Edit your schedule
* 🗑️ Remove your schedule


## 🚀 Quick Start

### 1. Clone and Configure
- Clone this repo to your server or local machine.
- In `config.py`, set your Discord bot token:
  ```python
  Token = "YOUR_DISCORD_BOT_TOKEN"
  ```

### 2. Run Locally (Python 3.12+)
```sh
pip install -r requirements.txt
python main.py
```

### 3. Run with Docker (Recommended for EC2/Cloud)
Build and run with Docker Compose:
```sh
docker-compose up --build -d
```

### 4. Environment
- All schedules are stored in `assets/data.sqlite` (persistent).
- The bot requires the Message Content Intent enabled in the Discord Developer Portal.

---

## ⚙️ Features
- Schedule messages and embeds to any channel
- Loop and infinite scheduling
- Supports time input: minutes (m), hours (h), days (d), weeks (w)
- Interactive dropdowns for editing/removing schedules
- SQLite database for persistence
- Admin-only commands
- Docker-ready for easy cloud deployment

---

## 📝 Commands
- `.ping` - Check bot latency
- `.schedule add message <#channel> <duration> <message>` - Schedule a text message
- `.schedule add embed <#channel> <duration> <description>` - Schedule an embed
- `.schedule overview` - View all active schedules
- `.schedule remove` - Remove a schedule (interactive dropdown)
- `.schedule edit message <#channel/None> <content>` - Edit scheduled messages
- `.schedule edit embed <#channel/None> <description>` - Edit scheduled embeds
- `.help` - Show help menu
- `.help schedule` - Show detailed schedule commands

---

## 🐳 Docker/Cloud Deployment
1. Edit your `config.py` and add your bot token.
2. Deploy to any server/EC2 with Docker:
   ```sh
   docker-compose up --build -d
   ```
3. The bot will auto-restart and keep running in the background.

---

## 📖 License
Released under the [Apache License 2.0](https://github.com/DorianAarno/SchedulerBot/blob/main/LICENSE) license.

