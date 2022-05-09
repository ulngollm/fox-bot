from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters

import requests as req
import os
import asyncio

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

app = Client('bot', API_ID, API_HASH, bot_token=BOT_API_TOKEN)

# todo deploy heroku https://devcenter.heroku.com/articles/getting-started-with-python#introduction
# todo run using asyncio
async def my_handler(client, message):
    print(f"message from {message.from_user.username}: {message.text}")
    if not message.from_user.is_bot:
        await message.reply(input('response'))


async def send_fox(client, message):
    url = 'https://randomfox.ca/floof/'
    result = req.get(url)
    image = result.json().get('image')
    await message.reply(image)


async def refund(client, message):
    await app.delete_messages(message.chat.id, [message.id, message.reply_to_message_id])
    await send_fox(client, message)


app.add_handler(MessageHandler(send_fox, filters.command('fox')))
app.add_handler(MessageHandler(refund, filters.command('refund')))
app.add_handler(MessageHandler(my_handler))

app.run()
