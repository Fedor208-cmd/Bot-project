async def help(update, context):
    await update.message.reply_text("Список команд:\n"
                                    "/start - я с тобой поздороваюсь)))\n"
                                    "/registration - зарегистрироваться;\n"
                                    "/check - пройтись по всем вопросам;\n"
                                    "/add - добавить новый вопрос;\n"
                                    "/delete - удалить любой вопрос.\n")