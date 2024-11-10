import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, CallbackContext, filters, CommandHandler
from bot.openai_api import get_gemini_response  
from bot.database import create_table
from bot.database import store_query  
import re

def split_message(text, max_length=4096):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]


async def start(update: Update, context: CallbackContext) -> None:
    username = update.effective_user.username
    welcome_message = (
        f"Hello! @{username} I'm your artificial intelligence assistant."
        "You can ask me questions and I'll answer you to the best of my ability. 😊 \n\n"
        "To start, just write something and I'll respond. Let's go!\n"
    )
    
    keyboard = [[
        InlineKeyboardButton("Channel", url="https://t.me/+KQkliYhDy_U1N2Ex"),
        InlineKeyboardButton("Developer", url="https://t.me/Gh0stDeveloper")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


async def handle_message(update: Update, context: CallbackContext) -> None:
    user_query = update.message.text
    user_id = update.message.from_user.id

    ai_response = await get_gemini_response(user_query)

    messages = split_message(ai_response)

    for message in messages:
        try:
            await update.message.reply_text(message, parse_mode='Markdown')
        except telegram.error.BadRequest as e:
            print(f"Error: {e}")

    store_query(user_id, user_query, ai_response)


async def help(update: Update, context: CallbackContext) -> None:
    help_message = (
        "Hello! Here are the available commands:\n\n"
        "/start - Begins the interaction with the bot.\n"
        "/help - Displays this message with the available commands.\n"
        "/info - Provides detailed information about my abilities and limitations."
        "/privacy - Displays the bot's privacy policy.\n\n"
        "You can ask me questions and I'll answer as best I can. 😊"
    )
    
    await update.message.reply_text(help_message)

async def info(update: Update, context: CallbackContext) -> None:
    info_message = (
        "I'm an artificial intelligence assistant created to help you with various tasks. "
        "I can answer questions, provide information, and help you with basic programming tasks,"
        "But I have some limitations:\n\n"
        "- I do not have access to private information or external databases (except those provided in this bot).\n"
        "- My knowledge is limited until September 2021, so I have no information about subsequent events or developments."
        "- I cannot perform illegal or malicious tasks.\n\n"
        "If you have any questions or need help, don't hesitate to ask me!"
    )
    
    await update.message.reply_text(info_message)


async def privacy(update: Update, context: CallbackContext) -> None:
    privacy_message = (
        "Bot Privacy Policy:\n\n"
        "This bot respects your privacy and does not collect or store personal information without your consent. "
        "The queries you send will be processed to generate responses, and that data can be stored in a database."
        "to improve the service and for safety and maintenance purposes."
        "However, we do not share your information with third parties without your explicit consent.\n\n"
        "If you have any questions about privacy, please contact us."
    )
    
    await update.message.reply_text(privacy_message)


def main():
    from bot.config import TELEGRAM_TOKEN

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("help", help))

    application.add_handler(CommandHandler("info", info))

    application.add_handler(CommandHandler("privacy", privacy))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == "__main__":
    main()
