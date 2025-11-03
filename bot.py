import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytz
from datetime import datetime

TOKEN = "7436710622:AAHZyaEt6HSIP5MNKNFJbAZVZXLx36VPlbM"
COSTA_RICA_TZ = pytz.timezone("America/Costa_Rica")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bot corriendo en Costa Rica")

async def job():
    while True:
        now = datetime.now(COSTA_RICA_TZ)
        if now.hour == 9 and now.minute == 0:
            print("¡Ejecutando job diario!")
        await asyncio.sleep(60)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    asyncio.create_task(job())
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
