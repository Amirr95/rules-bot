import logging
# from logging.handlers import RotatingFileHandler
# from telegram import Bot, Location, KeyboardButton, Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext, \
#     BasePersistence, ConversationHandler, PicklePersistence, Dispatcher
# from telegram.error import BadRequest, Unauthorized, NetworkError
# import os
# import warnings
# from telegram.ext import ChatJoinRequestHandler 

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ChatJoinRequestHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

TOKEN = "6293821023:AAFNkUKZO5paCCnKPdiG-6DS_zIA9j0lClQ"
PROXY_URL = "http://127.0.0.1:8889"
CHANNEL_ID = '1001956851590'

# Define the message to send
RULES_MESSAGE = 'Welcome to the channel! Please follow the rules: ...'

# Function to handle new members joining the channel
async def handle_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=RULES_MESSAGE
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, you just pressed start"
    )

if __name__ == '__main__':
    # application = ApplicationBuilder().token(TOKEN).proxy_url(PROXY_URL).get_updates_proxy_url(PROXY_URL).build()
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    join_handler = ChatJoinRequestHandler(handle_new_member, chat_id=CHANNEL_ID)

    application.add_handler(start_handler)
    application.add_handler(join_handler)

    application.run_polling()

