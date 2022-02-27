import telegram, logging
from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler

## token
token = "5224120947:AAH8J6SzRjiafxnAQJMKwRz-zDs14Qs6Dq4"

## Creating an instance of the bot
bot = telegram.Bot(token=token)

## continuously fetches new updates from telegram and passes them on to the Dispatcher class
updater = Updater(token=token, use_context=True)
dp = updater.dispatcher

##logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

##func
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
start_handler = CommandHandler('start', start)
dp.add_handler(start_handler)
updater.start_polling()