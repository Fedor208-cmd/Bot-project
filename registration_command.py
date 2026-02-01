import json
from telegram.ext import ConversationHandler
from check_if_not_registered_func import check_if_not_registered

name = ""

async def registration_begin(update, context):
    if not check_if_not_registered(update, context):
        await update.message.reply_text("Вы уже зарегистрированы!")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Как к вам обращаться?")
        return 2

async def registration_continuation(update, context):
    global name
    name = update.message.text
    await update.message.reply_text("Сколько вам лет?")
    return 3

async def registration_finish(update, context):
    global name
    age = update.message.text
    if age.isdigit():
        user = str(update.message.from_user.id)
        file = open("database_users.json", "r", encoding="utf-8")
        data = json.load(file)
        file.close()

        data[user] = {
            "1": "Вы спали 7-8 часов этой ночью?",
            "2": "Вы ели достаточное количество белка сегодня?",
            "3": "Вы выходили сегодня на свежий воздух?",
            "age": str(age),
            "name": str(name)
        }
        name = ""
        file = open("database_users.json", "w", encoding="utf-8")
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.close()

        await update.message.reply_text("Регистрация прошла успешно!")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Ошибка, введёные данные должны быть числом. Сколько вам лет?")
        return 3