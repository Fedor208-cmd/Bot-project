from telegram.ext import ConversationHandler
from check_if_not_registered_func import check_if_not_registered
import json


async def add(update, context):
    if check_if_not_registered(update, context):
        await update.message.reply_text("Вы не зарегистрированы!")
        return ConversationHandler.END
    file = open("database_users.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    name = data[str(update.message.from_user.id)]["name"]
    await update.message.reply_text(f"{name}, какой вопрос Вы бы хотели добавить?")
    return 2

async def add_complete(update, context):
    usr = str(update.message.from_user.id)
    task = update.message.text
    file = open("database_users.json", "r", encoding="utf-8")
    ctrl = json.load(file)
    file.close()
    file = open("database_users.json", "w", encoding="utf-8")
    if task not in ctrl[usr].values():
        ctrl[usr][str(len(ctrl[usr]) - 1)] = task
        json.dump(ctrl, file, indent=4, ensure_ascii=False)
        file.close()
        await update.message.reply_text("Вопрос добавлен.")
    else:
        await update.message.reply_text("Вопрос уже существует.")
    return ConversationHandler.END
