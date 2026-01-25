from telegram.ext import *
from config import BOT_TOKEN
from start_and_registration_commands import start, registration
from add_command import add, add_complete
from delete_command import delete, delete_complete
from check_command import check, check_continuation
from help_command import help


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("registration", registration))
    application.add_handler(CommandHandler("start", start))

    conv_handler_add = ConversationHandler(
        entry_points=[CommandHandler("add", add)],
        states={
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_complete)]
        },
        fallbacks=[]
    )

    conv_handler_delete = ConversationHandler(
        entry_points=[CommandHandler("delete", delete)],
        states={
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, delete_complete)]
        },
        fallbacks=[]
    )

    conv_handler_check = ConversationHandler(
        entry_points=[CommandHandler("check", check)],
        states={
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_continuation)]
        },
        fallbacks=[]
    )

    application.add_handler(conv_handler_check)
    application.add_handler(conv_handler_delete)
    application.add_handler(conv_handler_add)
    application.run_polling()

if __name__ == "__main__":
    main()