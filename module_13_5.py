from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()
kb = ReplyKeyboardMarkup(resize_keyboard = True)
button = KeyboardButton(text="Рассчитать")
button1 = KeyboardButton(text="Информация")
kb.add(button)
kb.add(button1)

@dp.message_handler(commands = 'start')
async def start(message):
    await message.answer(text="Привет, я помогу рассчитать каллории", reply_markup=kb)

@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(year = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(metr = message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(kilo = message.text)
    data = await state.get_data()
    # norma_cal = 10*data['kilo']+6.25*data['metr']-5*data['year']-161
    norma_cal = (10*int(data['kilo'])+6.25*int(data['metr'])-5*int(data['year']))-161

    await message.answer(f"Ваша норма калорий {norma_cal}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
