from aiogram import types
import utils
from dispatcher import dp, db


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(
        "Раді вас вітати(ага, аякже)", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton("Розклад")
            )
        )


@dp.message_handler(text="Розклад")
async def timetable(msg: types.Message):
    lessons = db.get_timetable(msg.from_id)
    if lessons is None:
        await msg.answer("Тебе нема в системі")
        return
    lessons = utils.lessons_to_text(lessons)
    await msg.answer(text=lessons)
