# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytz

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token de tu bot
TOKEN = "TU_TOKEN_AQUI"

# Zona horaria de Costa Rica
COSTA_RICA_TZ = pytz.timezone("America/Costa_Rica")

# Comando de ejemplo
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot corriendo correctamente en hora de Costa Rica.")

def main():
    # Construir la aplicación
    app = ApplicationBuilder().token(TOKEN).build()

    # --- CORRECCIÓN APSCHEDULER ---
    # Forzar que el job_queue use la zona horaria de Costa Rica
    app.job_queue._scheduler.timezone = COSTA_RICA_TZ

    # Registrar handlers
    app.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
