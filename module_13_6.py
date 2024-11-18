from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()
kb = InlineKeyboardMarkup()
button =InlineKeyboardButton(text="Рассчитать", callback_data="rasschet")
kb_rasschet = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Рассчитать норму калорий",  callback_data="calories")
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")

kb.add(button)
kb_rasschet.add(button1)
kb_rasschet.add(button2)


@dp.message_handler(commands = 'start')
async def start(message):
    await message.answer(text="Привет, я помогу рассчитать каллории",reply_markup=kb)

@dp.callback_query_handler(text = 'rasschet')
async def main_menu(call):
    await call.message.answer("Выберите опцию",reply_markup=kb_rasschet)
    await call.answer()

@dp.callback_query_handler(text = "formulas")
async def get_formulas(call):
    await call.message.answer("Формула для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

@dp.callback_query_handler(text ="calories" )
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
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