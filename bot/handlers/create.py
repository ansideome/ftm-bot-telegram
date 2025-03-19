from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from services.start_service import post_data

AWAITING_CODE = 1

async def create_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_user = (
        "📋 Silakan masukkan data dengan format berikut:\n\n"
        "`witel/sto/nama_lemari_ftm_eakses/no_panel_eakses/no_port_eakses/"
        "nama_lemari_ftm_oakses/no_panel_oakses/no_port_oakses/no_core_feeder/"
        "nama_segmen_feeder_utama/status_oa/kapasitas_kabel_feeder_utama/nama_ocd`\n\n"
        "_Contoh:_\n"
        "`MALANG/MLG/FTM-MLG-EA-XX/PANEL 1/8/FTM-MLG-OA-XX/PANEL 1/8/8/FE-MLG-XX/IDLE/98/IDLE`\n\n"
        "❗ Kosongkan data dengan `*` jika tidak ada."
    )

    await update.message.reply_text(message_user, parse_mode="Markdown")
    return AWAITING_CODE

async def submiting_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    fields = user_input.split('/')

    if len(fields) != 13:
        await update.message.reply_text(
            "Input tidak sesuai dengan format, cek kembali dan coba lagi"
        )
        return AWAITING_CODE
    
    fields = ["" if field.strip() == "*" else field for field in fields]

    payload = {
        "witel": fields[0],
        "sto": fields[1],
        "nama_lemari_ftm_eakses": fields[2],
        "no_panel_eakses": fields[3],
        "no_port_eakses": int(fields[4]) if fields[4].isdigit() else fields[4],
        "nama_lemari_ftm_oakses": fields[5],
        "no_panel_oakses": fields[6],
        "no_port_oakses": int(fields[7]) if fields[7].isdigit() else fields[7],
        "no_core_feeder": int(fields[8]) if fields[8].isdigit() else fields[8],
        "nama_segmen_feeder_utama": fields[9],
        "status_oa": fields[10],
        "kapasitas_kabel_feeder_utama": fields[11],
        "nama_ocd": fields[12],
    }
    success, message = await post_data(payload)

    await update.message.reply_text(
        message
    )
    ConversationHandler.END

async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Perintah dibatalkan."
    )
    ConversationHandler.END