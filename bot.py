import logging
import os
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pytz

# Configuración básica
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Configuración del token
TOKEN = os.getenv('7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM')

# Configurar zona horaria de Costa Rica
TIMEZONE = pytz.timezone('America/Costa_Rica')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot.")

def main():
    # Crear la aplicación con el token directamente
    application = Application.builder().token=TOKEN
    
    # Configurar APScheduler con la zona horaria
    application.job_queue.scheduler.configure({
        'timezone': TIMEZONE
    })
    
    # Agregar comandos
    application.add_handler(CommandHandler("start", start))
    
    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
