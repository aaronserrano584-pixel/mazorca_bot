import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "TU_TOKEN_AQUI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Bot funcionando correctamente.")

def main():
    # Crear la aplicación sin tocar el JobQueue
    app = ApplicationBuilder().token(TOKEN).build()

    # Agregar comandos
    app.add_handler(CommandHandler("start", start))

    # Ejecutar bot
    app.run_polling()

if __name__ == "__main__":
    main()
