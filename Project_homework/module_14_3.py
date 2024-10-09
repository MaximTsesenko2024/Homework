from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

product_list = [
    {'filename': 'Image/C.jpg', 'name': 'Витамин С', 'text': 'Витамин С'},
    {'filename': 'Image/D3.jpg', 'name': 'Витамин D3', 'text': 'Витамин D3'},
    {'filename': 'Image/B_g.jpg', 'name': 'Витамины B', 'text': 'Витамины группы B'},
    {'filename': 'Image/Se+Zn.jpg', 'name': 'Se+Zn', 'text': 'Витамины с добавлением силена и цинка'},
]

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ],
    resize_keyboard=True)

calories_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ])
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=product_list[0]['name'], callback_data='product_buying'),
            InlineKeyboardButton(text=product_list[1]['name'], callback_data='product_buying'),
            InlineKeyboardButton(text=product_list[2]['name'], callback_data='product_buying'),
            InlineKeyboardButton(text=product_list[3]['name'], callback_data='product_buying'),
        ]
    ])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = "7284490976:AAEOor2Wg8N-7i29K9X9MXf4GK_cQPF25cc"
bot = Bot(token=api)
dsp = Dispatcher(bot, storage=MemoryStorage())


@dsp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=main_kb)


@dsp.message_handler(text='Купить')
async def get_buying_list(massage: types.Message):
    for i in range(len(product_list)):
        with open(product_list[i]['filename'], 'rb') as img:
            await massage.answer_photo(img, 'Название: {} | Описание: {} | Цена: {}'.format(product_list[i]['name'],
                                                                                            product_list[i][
                                                                                                'text'],
                                                                                            str((i + 1) * 100)))
    await massage.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)


@dsp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dsp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию', reply_markup=calories_kb)


@dsp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Упрощённая формула Миффлина-Сан Жеора для мужчин:\n '
                              '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dsp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст, пожалуйста')
    await UserState.age.set()
    await call.answer()


@dsp.message_handler(text='Информация')
async def information(massage: types.Message):
    await massage.answer('Расчет суточной нормы калорий для мужчин по упрощённой формуле Миффлина-Сан Жеора.')


@dsp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост, пожалуйста')
    await UserState.growth.set()


@dsp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес, пожалуйста')
    await UserState.weight.set()


@dsp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await state.finish()
    calories = calc_calories(**data)
    await message.answer(f'Для вас норма {calories} килокалорий в сутки')
    await message.answer('конец')


@dsp.message_handler()
async def all_massages(message: types.Message):
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
