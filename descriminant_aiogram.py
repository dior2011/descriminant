import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram import types
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ContentType, File, Message
from descriminant_states import Form
from descriminant import descriminant

TOKEN = "6796185877:AAE7DFikiOA-RW2YvKTnExVHuYqcMVPEAwc"
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def start_command(message:Message,state:FSMContext):
    await state.set_state(Form.a)
    await message.answer(text="Assalomu alaykum! Diskriminant topish uchun a,b,c kerak bo'ladi! a ni kiriting!")

@dp.message(F.text,Form.a)
async def a_ni_olish(message: Message,state:FSMContext):
    try:
        await state.update_data(a=int(message.text))
        await state.set_state(Form.b)

        await message.answer(text="b ni kiriting!")
    except:
        await message.answer(text="Iltimos, son kiriting!")

@dp.message(F.text,Form.b)
async def b_ni_olish(message: Message,state:FSMContext):
    try:
        await state.update_data(b=int(message.text))
        await state.set_state(Form.c)

        await message.answer(text="c ni kiriting!")
    except:
        await message.answer(text="Iltimos, son kiriting!")

@dp.message(F.text,Form.c)
async def c_ni_olish(message: Message,state:FSMContext):
    try:
        await state.update_data(c=int(message.text))
        data = await state.get_data()
        a = data.get("a")
        b = data.get("b")
        c = data.get("c")
        text = descriminant(a,b,c)
        await message.answer(text=text)
        
    except:
        await message.answer(text="Iltimos, son kiriting!")

    
    
async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

