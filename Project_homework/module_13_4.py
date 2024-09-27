from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = ""
bot = Bot(token=api)
dsp = Dispatcher(bot, storage=MemoryStorage())


@dsp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dsp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст, пожалуйста')
    await UserState.age.set()


@dsp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост, пожалуйста')
    await UserState.growth.set()


@dsp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес, пожалуйста')
    await UserState.weight.set()


@dsp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await state.finish()
    calories = calc_calories(**data)
    await message.answer(f'Для вас норма {calories} килокалорий в сутки')
    await message.answer('конец')


@dsp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


def calc_calories(age, growth, weight):
    if isinstance(age, str):
        age = float(age)
    if isinstance(growth, str):
        growth = float(growth)
    if isinstance(weight, str):
        weight = float(weight)
    result = 10 * weight + 6.25 * growth - 5 * age + 5
    return result


if __name__ == "__main__":
    executor.start_polling(dsp, skip_updates=True)
