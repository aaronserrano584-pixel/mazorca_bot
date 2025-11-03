# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue
import pytz

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = 7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM
COSTA_RICA_TZ = pytz.timezone("America/Costa_Rica")

# Comando de ejemplo
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot corriendo correctamente en hora de Costa Rica.")

def main():
    # Crear JobQueue con zona horaria compatible
    job_queue = JobQueue(timezone=COSTA_RICA_TZ)
    job_queue.start()  # Inicia el JobQueue

    # Crear la aplicación y pasarle el JobQueue
   app = ApplicationBuilder().token(7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM).build()
   app.job_queue._scheduler.timezone = COSTA_RICA_TZ

    # Registrar handlers
    app.add_handler(CommandHandler("start", start))

    # Ejecutar bot
    app.run_polling()

if __name__ == "__main__":
    main()

