from aiogram import executor
import handlers
from dispatcher import dp, db
import logging


logging.basicConfig(level=logging.INFO)
executor.start_polling(dp)
