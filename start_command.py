from check_if_not_registered_func import check_if_not_registered


async def start(update, context):
    if check_if_not_registered(update, context):
        await update.message.reply_text(
            "Привет! Для начала работы необходимо зарегистрироваться. Введи команду /help для списка команд."
        )
    else:
        await update.message.reply_text("Привет! Введи команду /help для списка команд.")

