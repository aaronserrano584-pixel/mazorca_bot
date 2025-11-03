import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Cargar token desde variables de entorno
TOKEN = os.environ.get("BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot funcionando correctamente.")

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Lista de comandos disponibles:\n/start - iniciar el bot\n/help - ayuda")

# Echo de mensajes de texto
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Recibido: {update.message.text}")

def main():
    # Crear aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Registrar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Registrar handler para mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Ejecutar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
