import os
import asyncio
from datetime import datetime
import pytz

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# -----------------------------
# Configuración del TOKEN
# -----------------------------
TOKEN = os.getenv("7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM")
if not TOKEN:
    raise ValueError("7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM")

# -----------------------------
# Funciones de comandos
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot activo y listo.")

# Ejemplo de tarea programada
async def tarea_programada(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    now = datetime.now(pytz.timezone("America/Costa_Rica"))
    await context.bot.send_message(chat_id=chat_id, text=f"Recordatorio automático: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# -----------------------------
# Función principal
# -----------------------------
async def main():
    # Construimos la aplicación del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Agregamos manejadores de comandos
    app.add_handler(CommandHandler("start", start))

    # Configuración de JobQueue con timezone de Costa Rica
    job_queue = app.job_queue

    # Creamos un trabajo recurrente: todos los días a las 8:00 am hora Costa Rica
    job_queue.run_daily(
        tarea_programada,
        time=datetime.strptime("08:00:00", "%H:%M:%S").time(),
        days=(0,1,2,3,4,5,6),  # lunes a domingo
        context=None
    )

    # Iniciamos el bot
    await app.run_polling()

# -----------------------------
# Ejecutamos la función principal
# -----------------------------
if __name__ == "__main__":
    asyncio.run(main())
