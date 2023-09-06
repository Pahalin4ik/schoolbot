from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from database import Database

db = Database(
    os.getenv('db_name'),
    os.getenv('user'),
    os.getenv('password'),
    os.getenv('host'),
    os.getenv('port')
)
storage = MemoryStorage()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot, storage=storage)
