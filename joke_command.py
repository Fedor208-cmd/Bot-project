from config import url
import requests

async def jokes(update, context):
    response = requests.get(url)
    joke = response.json()
    await update.message.reply_text(f"{joke["setup"]}\n"
                                    f"{joke["punchline"]}")
