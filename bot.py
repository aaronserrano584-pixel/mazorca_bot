from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "TU_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Bot funcionando.")

def main():
    # Crear la aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Registrar comandos
    app.add_handler(CommandHandler("start", start))

    # Ejecutar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
