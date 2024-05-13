translations = {
    'en': {
        'Приветствую! Чем могу помочь?': 'Greetings! How can I help you?',
        '☁ Погода': '☁ Weather',
        '⚙ Язык': '⚙ Language',
        '☁ <b>Текущая погода:</b>': '☁ <b>Current weather:</b>',
        '🌡 Температура:': '🌡 Temperature:',
        '☁ На улице:': '☁ Description:',
        '💧 Влажность:': '💧 Humidity:',
        '🔵 Давление:': '🔵 Pressure:',
        '🍃 Скорость ветра:': '🍃 Wind speed:',
        '☁ <b>Ближайшие 24 часа</b>': '☁ <b>Next 24 hours</b>',
        '☁ <b>Ближайшие 3 дня</b>': '☁ <b>Next 3 days</b>',
        'Введите город': 'Type a city',
        '🏙 Ввести другой город': '🏙 Type another city',
        '⬅ Назад': '⬅ Back',
        'Вернуться в главное меню': 'Back to main menu',
        'Выберите язык': 'Choose language',
        '''⁉ Название города введен неправильно, либо такой город не существует!
        
😊 Попробуйте ввести другое название''': '''⁉ Incorrect city name or city does not exist!

😊 Try typing another city'''
    }
}


def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text
