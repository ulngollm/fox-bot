from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters

import requests as req
import os

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

app = Client('bot', API_ID, API_HASH, bot_token=BOT_API_TOKEN)


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

app.run()
