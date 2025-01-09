
import openai
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Respond function
async def respond(update: Update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Человек спрашивает: {user_message}. Ответь как его идеальная версия.",
        max_tokens=100
    )
    await update.message.reply_text(response['choices'][0]['text'].strip())

# Telegram API Token from environment variable
app = ApplicationBuilder().token(os.getenv("TELEGRAM_API_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

# Run polling
app.run_polling()
