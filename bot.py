import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")  # Render tomará la variable de su panel

def start(update: Update, context: CallbackContext):
    update.message.reply_text("¡Bot iniciado correctamente!")

def main():
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

