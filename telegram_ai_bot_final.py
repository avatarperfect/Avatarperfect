
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# OpenAI API Key
openai.api_key = "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"

# Respond function
async def respond(update: Update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Человек спрашивает: {user_message}. Ответь как его идеальная версия.",
        max_tokens=100
    )
    await update.message.reply_text(response['choices'][0]['text'].strip())

# Creating the application
app = ApplicationBuilder().token('7825988457:AAHe3UmlYsChzGnUEnlJ6u4MXRiv989cV4c').build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

# Run polling
app.run_polling()
