import os
import pytz
import asyncio
from datetime import datetime
from telegram.ext import ApplicationBuilder, CommandHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Obtener token desde variable de entorno
TOKEN = os.getenv("7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM")
if not TOKEN:
    os.getenv ValueError("7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM")

# Configurar zona horaria de Costa Rica
COSTA_RICA_TZ = pytz.timezone("America/Costa_Rica")

# Función de ejemplo para /start
async def start(update, context):
    await update.message.reply_text("¡Hola! Soy tu bot.")

# Función de ejemplo para un job programado
def scheduled_job(context):
    print(f"Job ejecutado en {datetime.now(COSTA_RICA_TZ)}")

async def main():
    # Crear aplicación del bot
    app = ApplicationBuilder().token("7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM").build()

    # Agregar comando /start
    app.add_handler(CommandHandler("start", start))

    # Configurar scheduler con zona horaria correcta
    scheduler = AsyncIOScheduler(timezone=COSTA_RICA_TZ)
    scheduler.add_job(scheduled_job, "interval", seconds=60)  # Job cada 60 segundos
    scheduler.start()

    # Iniciar bot
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())

