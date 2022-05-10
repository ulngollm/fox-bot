import random

from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters

import os

from ApiClient import DogApiClient, RandomFoxApiClient, FoxrudorApiClient

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

app = Client('bot', API_ID, API_HASH, bot_token=BOT_API_TOKEN)


async def send_fox(client, message):
    src = (RandomFoxApiClient, FoxrudorApiClient)
    image = random.choice(src)().random()
    await message.reply(image)


async def refund(client, message):
    await app.delete_messages(message.chat.id, [message.id, message.reply_to_message_id])


async def send_dog(client, message):
    api = DogApiClient()
    image = api.random()
    await message.reply(image)


app.add_handler(MessageHandler(send_fox, filters.command('fox')))
app.add_handler(MessageHandler(send_dog, filters.command('dog')))
app.add_handler(MessageHandler(refund, filters.command('refund')))

app.run()
