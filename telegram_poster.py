import asyncio
import os
from telegram import Bot
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use the environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')  # Still necessary for background operation

bot = Bot(token=TOKEN)

async def send_message(text):
    """Sends a message to the specified Telegram chat."""
    await bot.send_message(chat_id=CHAT_ID, text=text)

def tail_f(filename, interval=0.2):
    """Implements tail -f like functionality using polling."""
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        position = f.tell()
        while True:
            time.sleep(interval)
            f.seek(0, os.SEEK_END)
            current_position = f.tell()
            if current_position <= position:
                continue
            f.seek(position, os.SEEK_SET)
            new_lines = f.readlines()
            position = current_position
            return new_lines

async def file_listener(filename="logs/game.log", interval=0.5):
    """Monitors the specified file for new lines and sends them to the Telegram group."""
    while True:
        new_lines = tail_f(filename, interval)
        if new_lines:
            message = ''.join(new_lines)
            await send_message(message)

if __name__ == '__main__':
    asyncio.run(file_listener())
