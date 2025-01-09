import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токены из переменных окружения
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Устанавливаем ключ для OpenAI
openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я ваш AI-бот!")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_question = " ".join(context.args)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_question,
        max_tokens=1000
    )
    await update.message.reply_text(response["choices"][0]["text"])

app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ask", ask))

app.run_polling()