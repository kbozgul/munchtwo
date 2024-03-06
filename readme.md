Welcome to the Telegram Version of Munchkin Bot!

Dependencies:

pip install python-dotenv
pip install python-telegram-bot
pip install matplotlib (for plotting the results)

.env needs to be filled with:
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID

There needs to be 3 things running at the same time:
telegram_poster.py
telegram_logger.py
main.py

Commands:
k1 z-2 :Adds a level to k, reduces 2 levels from z
. :Next turn
cancel :cancel last command
end :end the game without reaching level 10 and save

