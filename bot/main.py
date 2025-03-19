from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
from config.setting import BOT_TOKEN
from handlers import start, create

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("help", start.help))

    create_conv = ConversationHandler(
        entry_points=[CommandHandler("tambahdata", create.create_data)],
        states={
            create.AWAITING_CODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, create.submiting_data)
            ]
        },
        fallbacks=[CommandHandler("cancel", create.cancel_handler)],
    )
    app.add_handler(create_conv)

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()