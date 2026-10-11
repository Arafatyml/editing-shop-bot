
import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not configured")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🔥 Welcome to Editing Shop!\n\n"
        "🛍️ Packages\n"
        "🎬 Editing Materials & XML\n"
        "💎 Premium Apps\n"
        "🤝 Referral & Earnings\n"
        "📞 Official Contact\n\n"
        "Use /shop to browse packages."
    )

@bot.message_handler(commands=["shop"])
def shop(message):
    bot.reply_to(
        message,
        "🛍️ Editing Shop\n\n"
        "📦 Packages are being prepared.\n"
        "Please check back soon!"
    )

bot.infinity_polling()
