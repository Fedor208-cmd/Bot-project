import json
from check_if_not_registered_func import check_if_not_registered


async def start(update, context):
    if check_if_not_registered(update, context):
        await update.message.reply_text(
            "Привет! Для начала работы необходимо зарегестрироваться. Введи команду /help для списка команд."
        )
    else:
        await update.message.reply_text("Привет! Введи команду /help для списка команд.")


async def registration(update, context):
    if not check_if_not_registered(update, context):
        await update.message.reply_text("Вы уже зарегистрированы!")
    else:
        data = {
            str(update.message.from_user.id): {
            "1": "Вы спали 7-8 часов этой ночью?",
            "2": "Вы ели достаточное количество белка сегодня?",
            "3": "Вы выходили сегодня на свежий воздух?"
            }
        }
        file = open("database_users.json", "w", encoding="utf-8")
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.close()
        await update.message.reply_text("Регистрация прошла успешно!")
