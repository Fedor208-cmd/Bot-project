import json
from telegram.ext import ConversationHandler
from check_if_not_registered_func import check_if_not_registered

counter_yes = 0
counter_questions = 1
name = ""

async def check(update, context):
    global counter_questions, name
    if check_if_not_registered(update, context):
        await update.message.reply_text("Вы не зарегистрированы!")
        return ConversationHandler.END
    file = open("database_users.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    name = data[str(update.message.from_user.id)]["name"]
    await update.message.reply_text(f"{name}, {data[str(update.message.from_user.id)][str(counter_questions)]}")
    counter_questions += 1
    return 2


async def check_continuation(update, context):
    global counter_questions, counter_yes, name
    file = open("database_users.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    answer = update.message.text.lower()
    if answer != "да" and answer != "нет":
        await update.message.reply_text("Ошибка, ответ должен быть да или нет\n "
                                        f"{data[str(update.message.from_user.id)][str(counter_questions - 1)]}")
        return 2
    if answer == "да":
        counter_yes += 1
    if counter_questions > len(data[str(update.message.from_user.id)]) - 2:
        await update.message.reply_text(
            f"{int((counter_yes / (len(data[str(update.message.from_user.id)]) - 2)) * 100)}% выполнено!")
        counter_yes = 0
        counter_questions = 1
        return ConversationHandler.END
    await update.message.reply_text(f"{name}, {data[str(update.message.from_user.id)][str(counter_questions)]}")
    counter_questions += 1
    return 2
