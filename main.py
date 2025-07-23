import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from googletrans import Translator

# Конфигурация
TOKEN = os.getenv("TELEGRAM_TOKEN")
translator = Translator()

# Обработчики команд
async def start(update: Update, context):
    await update.message.reply_text("🔠 Привет! Я бот-переводчик. Просто отправь мне текст!")

async def translate(update: Update, context):
    text = update.message.text
    try:
        # Переводим на английский (можно изменить)
        result = translator.translate(text, dest='en')
        await update.message.reply_text(f"🌍 Перевод:\n{result.text}")
    except Exception as e:
        await update.message.reply_text("❌ Ошибка перевода")

async def meme_translate(update: Update, context):
    text = update.message.text.replace("/meme", "").strip()
    if not text:
        await update.message.reply_text("Пример: /meme Привет")
        return
    
    # Простейшая реализация мем-перевода
    memes = {
        "cat": f"🐱 Мяу! {text} *мур-мур*",
        "pirate": f"☠️ Йо-хо-хо! {text}, собака!",
        "academic": f"Согласно исследованиям, '{text}' представляет собой..."
    }
    
    await update.message.reply_text(memes["cat"])  # По умолчанию кот

# Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("meme", meme_translate))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))
    
    app.run_polling()

if __name__ == "__main__":
    main()