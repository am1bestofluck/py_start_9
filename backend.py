"""здесь вся магия"""
from collections import defaultdict
import random
import re
import telegram
import sys

try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
except ImportError:
    print('pip install python-telegram-bot --upgrade')
    sys.exit()

from constants import BASKET, MAX_TURN, RESULT

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
    sessions[update.effective_user.id] = BASKET

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(' '.join(['Hello!\n\t',
    "Imagine basket, full of candies.\n",
    "You can have on of them.", "The last one! That is, if You are shrewd.",
    "\n\t", "Rules are simple!",f"Can take up to {str(MAX_TURN)} candies. ", "One to grab the last candy, keeps it!",
    "Real nice candy, I can tell! Hf."]))
    sessions[update.effective_user.id] = BASKET

async def notation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('\n'.join(["/start - info","/reset - retry",
    "/rules - rules", "/take <int> - take candy(-ies)"]))

async def move_bot(update_: Update, context: ContextTypes.DEFAULT_TYPE, killer:bool=False):
    if killer:
        pass # acts to win
    else:
        sessions[update_.effective_user.id] - random.choice(range(MAX_TURN+1)) 


async def move (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"between 0 and {str(MAX_TURN)} expected!")

    if sessions[update.effective_user.id> 0:]
        move_bot(update_=update,killer=False)
    if sessions[update.effective_user.id] < 1:
        print(RESULT[True])


# async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def parse_msg(update, context):
    if re.search("^(/take) \d+$", update.message.text, re.IGNORECASE | re.DOTALL):
        
       update.message.reply_text("send your content")