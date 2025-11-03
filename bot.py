# bot.py
import os
import pytz
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Cargar el token desde variable de entorno
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Debes configurar la variable de entorno TELEGRAM_BOT_TOKEN con tu token.")

# Zona horaria de Costa Rica
COSTA_RICA_TZ = pytz.timezone("America/Costa_Rica")

# Comando de prueba /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot funcionando con zona horaria de Costa Rica ✅")

# Función que ejecutará el job programado
async def tarea_programada(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    await context.bot.send_message(chat_id=chat_id, text="¡Recordatorio diario desde tu bot!")

async def main():
    # Crear la aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Registrar comando /start
    app.add_handler(CommandHandler("start", start))

    # Configurar el JobQueue para usar la zona horaria de Costa Rica
    app.job_queue.scheduler.configure(timezone=COSTA_RICA_TZ)

    # Agregar un job diario a las 08:00 AM Costa Rica
    app.job_queue.run_daily(
        tarea_programada,
        time=pytz.datetime.time(hour=8, minute=0, tzinfo=COSTA_RICA_TZ),
        days=(0, 1, 2, 3, 4, 5, 6)  # Lunes a domingo
    )

    # Ejecutar el bot
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
