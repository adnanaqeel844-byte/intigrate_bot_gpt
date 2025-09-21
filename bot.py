import os
import sys
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

#Configure OpenAI
openai.api_key = OPENAI_KEY


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋 I'm your GPT-powered bot. Ask me anything!")


# Chat handler
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        # Send message to GPT
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",   # You can also use "gpt-4"
            messages=[{"role": "user", "content": user_message}]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        await update.message.reply_text(bot_reply)

    except Exception as e:
        await update.message.reply_text(f"⚠️ OpenAI Error: {str(e)}")


# Main function
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN is missing in environment variables")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":

    main()


