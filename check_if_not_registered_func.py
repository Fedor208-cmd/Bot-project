import json

def check_if_not_registered(update, context):
    usr = str(update.message.from_user.id)
    file = open("database_users.json", "r", encoding="utf-8")
    ctrl = json.load(file)
    file.close()
    return bool(usr not in ctrl.keys())
