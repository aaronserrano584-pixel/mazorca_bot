import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytz
from tzlocal import get_localzone_name  # Detecta la zona horaria local

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "TU_TOKEN_AQUI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Bot funcionando correctamente con zona horaria local.")

def main():
    # Crear la aplicación
    app = ApplicationBuilder().token(TOKEN).build()

    # Detectar zona horaria local compatible con pytz
    local_timezone_name = get_localzone_name()  # Ej: "America/Mexico_City"
    local_timezone = pytz.timezone(local_timezone_name)

    # Configurar JobQueue con zona horaria local
    app.job_queue._scheduler.timezone = local_timezone

    # Agregar comandos
    app.add_handler(CommandHandler("start", start))

    # Ejecutar bot
    app.run_polling()

if __name__ == "__main__":
    main()
