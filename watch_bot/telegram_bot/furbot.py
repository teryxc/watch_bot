'''
Created on Jul 15, 2018

@author: teryx
'''
import telegram
from telegram_bot import TELEGRAM_TOKEN, USER_ID

bot = telegram.Bot(token=TELEGRAM_TOKEN)

updates = bot.get_updates()
print([[u.message.chat_id,u.message.text] for u in updates])

bot.send_message(USER_ID, str(bot.get_me()) + ' is alive.' )