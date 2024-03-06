from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import os
from dotenv import load_dotenv
from read_and_write import add_new_line

# Load environment variables from .env file
load_dotenv()

# Use the environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Define a function to log messages to a file
async def log_message(update: Update, context: CallbackContext) -> None:
    # Extract the message text
    message_text = update.message.text
    add_new_line("logs/telegram.log", message_text.lower())

def main():
    # Create the application using the bot token
    application = Application.builder().token(TOKEN).build()

    # Add a message handler for all text messages
    application.add_handler(MessageHandler(filters.TEXT, log_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
