


import sys

import telegram

try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
except ImportError:
    print('pip install python-telegram-bot --upgrade')
    sys.exit()

if telegram.__version__ !='20.0':
    print('pip install python-telegram-bot --upgrade')
    sys.exit()

try:
    from never_share import BOT_KEY
except ImportError:
    print("токен придётся взять свой :( :)")
    sys.exit()

from backend import reset, new_game, help_, move

app = ApplicationBuilder().token(BOT_KEY).build()

# app.add_handler(CommandHandler("start", help_))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CommandHandler("begin", new_game))
app.add_handler("/take <int>",move)
app.run_polling()
