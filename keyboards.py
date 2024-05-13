from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from translations import _

language_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🇺🇸 English'), KeyboardButton(text='🇷🇺 Русский')]
], resize_keyboard=True, input_field_placeholder='Выберите язык')


def main_menu(lang):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('☁ Погода', lang)), KeyboardButton(text=_('⚙ Язык', lang))]
    ], resize_keyboard=True)
    return markup


def weather_keyboard(lang):
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('🏙 Ввести другой город', lang)), KeyboardButton(text=_('⬅ Назад', lang))]
    ], resize_keyboard=True)
