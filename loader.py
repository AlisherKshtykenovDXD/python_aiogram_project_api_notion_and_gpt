from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyrogram import Client

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
pyro_client = Client(name="my_account", api_id=config.api_id, api_hash=config.api_hash)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
