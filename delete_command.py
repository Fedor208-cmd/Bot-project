from telegram.ext import ConversationHandler
import json
from check_if_not_registered_func import check_if_not_registered


async def delete(update, context):
    if check_if_not_registered(update, context):
        await update.message.reply_text("Вы не зарегистрированы!")
        return ConversationHandler.END
    file = open("database_users.json", "r", encoding="utf-8")
    all_questions = json.load(file)
    questions = all_questions[str(update.message.from_user.id)]
    file.close()
    line = ""
    for i in range (1, len(questions) + 1):
        line += f"{i}: {questions[str(i)]}\n"
    await update.message.reply_text("Какой вопрос вы бы хотели убрать? Введите номер вопроса.\n"
                                    f"{line}")
    return 2

async def delete_complete(update, context):
    key = update.message.text
    file = open("database_users.json", "r", encoding="utf-8")
    all_questions = json.load(file)
    questions = all_questions[str(update.message.from_user.id)]
    file.close()
    del questions[key]
    new_questions = dict()
    new_key = 1
    for question in questions.values():
        new_questions[new_key] = question
        new_key += 1
    all_questions[str(update.message.from_user.id)] = new_questions
    file = open("database_users.json", "w", encoding="utf-8")
    json.dump(all_questions, file,  indent=4, ensure_ascii=False)
    file.close()
    await update.message.reply_text("Вопрос удалён.")
    return ConversationHandler.END
