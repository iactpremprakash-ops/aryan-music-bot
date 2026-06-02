from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

app = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("🎵 Music Bot is alive!\nUse /play to play music in voice chat.")

@app.on_message(filters.command("help"))
def help_cmd(_, message):
    message.reply_text("Commands:\n/start - Start bot\n/play - Play music (setup needed)")

print("Bot is running...")
app.run()
