

import sys


import telegram
if telegram.__version__ !='20.0':
    print('pip install python-telegram-bot --upgrade')
    sys.exit

try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
except ImportError:
    print('pip install python-telegram-bot --upgrade')
    sys.exit()

try:
    from never_share import BOT_KEY
except ImportError:
    print("токен придётся взять свой :( :)")
    sys.exit()

from backend import reset, rules, move, notation
from constants import MAX_TURN



app = ApplicationBuilder().token(BOT_KEY).build()
app.add_handler(CommandHandler("start", notation))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CommandHandler("rules", rules))
for i in range(MAX_TURN+1):
    app.add_handler(CommandHandler(f"take{str(i)}",move))
app.run_polling()
