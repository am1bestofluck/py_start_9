"""здесь вся магия"""
from collections import defaultdict
import telegram
import sys

try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
except ImportError:
    print('pip install python-telegram-bot --upgrade')
    sys.exit()

from constants import BASKET, MAX_TURN

sessions = defaultdict(lambda:  None)
import asyncio # :(
import webbrowser

class Game():
    
    def __init__(self,user:Update):
        self.user = user.effective_user.id
    
    async def flow_fork(self):
        return
    
    async def flow_easy(self):
        return
    
    async def flow_hard(self):
        return

    async def result(self):
        if True:
            return
        return


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('\n'.join(['/start: help',
    "reset: forfeit", "begin: start new game"]))


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ok!')

async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(' '.join(['Hello! We start again!\n\t',
    "Imagine basket, full of candies.\n",
    "You can have on of them.", "The last one! That is, if You are shrewd.",
    "\n\t", "Rules are simple!", "One to grab the last candy, keeps it!",
    "Real nice candy, I can tell! Hf."]))
    sessions[update.effective_user.id] = BASKET
    
async def move (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("int expected")

    

# async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')