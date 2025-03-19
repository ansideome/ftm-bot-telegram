from telegram.ext import ApplicationBuilder, CommandHandler
from config.setting import BOT_TOKEN
from handlers import start

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("help", start.help))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()