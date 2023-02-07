"""здесь вся магия"""
import asyncio
from collections import defaultdict
import math
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

sessions = defaultdict(lambda:  BASKET)

async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('\n'.join(['/start: help',
    "reset: forfeit", "begin: start new game"]))


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ok! {str(BASKET)} candies now.')
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
    "/rules - rules", "/take<int>, as in /take1 or /take19 - take candy(-ies)"]))



async def move_bot(update_: Update, context: ContextTypes.DEFAULT_TYPE, killer:bool=False):
    await asyncio.sleep(0.00001)
    # print(killer)
    if sessions[update_.effective_user.id] <= 0:
        return
    if killer:
        await asyncio.sleep(0.00001)
        if sessions[update_.effective_user.id] <= MAX_TURN:
            pick = MAX_TURN
        elif sessions[update_.effective_user.id]%MAX_TURN == 0:
            pick = MAX_TURN-1
        elif sessions[update_.effective_user.id]%MAX_TURN !=1:
            pick = sessions[update_.effective_user.id]%MAX_TURN -1 
        else:
            pick = random.choice(range(1,MAX_TURN+1))# если уже нет победных ходов           
    else:
        await asyncio.sleep(0.00001)
        pick = random.choice(range(1,MAX_TURN+1))

    sessions[update_.effective_user.id] -= pick
    prompt = f"Bot took {str(pick)} candies.\n"+\
        f"{str(sessions[update_.effective_user.id])} left!" if\
        sessions[update_.effective_user.id] > 0 else\
            "Bot keeps the candy!"
    await update_.message.reply_text(prompt)
    if sessions[update_.effective_user.id] <= 0:
        await update_.message.reply_text(f"{RESULT[False]}")


async def move (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await asyncio.sleep(0.00001)
    if sessions[update.effective_user.id] <= 0:
        return
    digits_mask = re.compile("\d+")
    try:
        take = int(re.findall(digits_mask,update.message['text'])[0])
    except TypeError:
        return
    borders = range(1,MAX_TURN+1)
    if take not in borders:
        await update.message.reply_text(
            f"between {str(min(borders))} and {str(MAX_TURN)} expected!")
        return
    await asyncio.sleep(0.001)
    sessions[update.effective_user.id] -= take
    prompt = f'{str(sessions[update.effective_user.id])} left!' if\
        sessions[update.effective_user.id] > 0 else\
            "You got it!"
    await update.message.reply_text(prompt)
    if sessions[update.effective_user.id] <= 0:
        await update.message.reply_text(f"{RESULT[True]}")
    else :
        
        if sessions[update.effective_user.id] > 0:
            await move_bot(update_=update,context=context,killer=
            True)
    
