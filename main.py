from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from openai import OpenAI

TOKEN = "8660417736:AAFV1mOZXUPLOvh_vJkDcaEnusl-1aMkJBw"
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are a sweet, caring, romantic AI companion.
                Speak in Bengali.
                Be friendly, supportive, playful, and respectful.
                Remember conversation context when possible.
                Never generate explicit sexual content.
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    await update.message.reply_text(
        response.choices[0].message.content
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot Running...")
app.run_polling()