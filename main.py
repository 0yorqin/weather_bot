import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from config import TOKEN
import keyboards as kb
from database import DataBase
from translations import _
from states import Weather
from weather import get_current_weather

bot = Bot(TOKEN)
dp = Dispatcher()
db = DataBase()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    chat_id = message.chat.id
    db.create_users_table()
    user = db.get_user_by_chat_id(chat_id)
    if user:
        lang = db.get_lang(chat_id)
        await message.answer(_('Приветствую! Чем могу помочь?', lang[0]), reply_markup=kb.main_menu(lang[0]))
    else:
        db.register_user(chat_id)
        await message.answer('Выберите язык', reply_markup=kb.language_kb)


@dp.message(F.text.in_(["🇺🇸 English", "🇷🇺 Русский"]))
async def set_language(message: Message):
    chat_id = message.chat.id
    if message.text == '🇺🇸 English':
        lang = 'en'
        db.set_lang(chat_id, lang)
        await message.answer('Language set to English!', reply_markup=ReplyKeyboardRemove())
        await cmd_start(message)
    elif message.text == '🇷🇺 Русский':
        lang = 'ru'
        db.set_lang(chat_id, lang)
        await message.answer('Выбран Русский язык!', reply_markup=ReplyKeyboardRemove())
        await cmd_start(message)


@dp.message(F.text.in_(['☁ Погода', '☁ Weather']))
async def weather_menu(message: Message, state: FSMContext):
    chat_id = message.chat.id
    lang = db.get_lang(chat_id)[0]
    await state.set_state(Weather.city)
    await message.answer(_('Введите город', lang), reply_markup=ReplyKeyboardRemove())


@dp.message(Weather.city)
async def get_weather(message: Message, state: FSMContext):
    chat_id = message.chat.id
    lang = db.get_lang(chat_id)[0]
    await state.update_data(city=message.text)
    data = await state.get_data()
    await message.answer(get_current_weather(data['city'], lang), parse_mode='HTML',
                         reply_markup=kb.weather_keyboard(lang))
    await state.clear()


@dp.message(F.text.in_(['🏙 Ввести другой город', '🏙 Type another city']))
async def another_city(message: Message, state: FSMContext):
    await weather_menu(message, state)


@dp.message(F.text.in_(['⬅ Назад', '⬅ Back']))
async def back(message: Message):
    chat_id = message.chat.id
    lang = db.get_lang(chat_id)[0]
    await message.answer(_('Вернуться в главное меню', lang), reply_markup=kb.main_menu(lang))


@dp.message(F.text.in_(['⚙ Язык', '⚙ Language']))
async def language_menu(message: Message):
    await message.answer('Выберите язык', reply_markup=kb.language_kb)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
