import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue
import pytz  # Necesario para zonas horarias compatibles con APScheduler

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token de tu bot
TOKEN = "TU_TOKEN_AQUI"

# Comando de prueba /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Bot funcionando correctamente.")

def main():
    # Crear JobQueue con timezone de pytz
    job_queue = JobQueue(timezone=pytz.timezone("UTC"))

    # Crear la aplicación pasándole la JobQueue ya configurada
    app = ApplicationBuilder().token(TOKEN).job_queue(job_queue).build()

    # Agregar comandos
    app.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
