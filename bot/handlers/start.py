from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_usn = update.effective_user.username
    message_user = (
        f"Halo, {user_usn}! \n"
        "Selamat datang di *Bot Laporan Harian* \n\n"
        "Ketik /help untuk mengetahui apa saja yang bisa dijalankan dari bot ini!"
    )

    await update.message.reply_text(
        message_user,
        parse_mode="Markdown"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_user = (
        f"*=== Daftar Perintah Bot ===* \n"
        "1. /start   : Memulai Perbincangan \n"
        "2. /help    : Menampilkan Daftar Perintah \n"
    )

    await update.message.reply_text(
        message_user,
        parse_mode="Markdown"
    )