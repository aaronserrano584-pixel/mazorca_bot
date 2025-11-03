import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytz  # Importamos pytz para la zona horaria

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
    # Crear la aplicación
    app = ApplicationBuilder().token(TOKEN).build()

    # --- CORRECCIÓN DEL ERROR DE ZONA HORARIA ---
    # Forzamos que JobQueue use una zona horaria compatible con pytz
    app.job_queue._scheduler.timezone = pytz.timezone("UTC")
    # ---------------------------------------------

    # Agregar comandos
    app.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
