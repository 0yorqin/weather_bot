import requests
from translations import _

params = {
    'appid': '5ae5392a86c025d5aa26489e3ae72334',
    'units': 'metric'
}


def get_current_weather(city, lang):
    params['lang'] = lang
    params['q'] = city
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params).json()
    try:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        current_weather = f'''{_('☁ <b>Текущая погода:</b>', lang)}
    
{_('🌡 Температура:', lang)} {temperature}С
{_('☁ На улице:', lang)} {description}
{_('💧 Влажность:', lang)} {humidity}
{_('🔵 Давление:', lang)} {pressure}
{_('🍃 Скорость ветра:', lang)} {wind_speed}
'''

    #/////////////////////////////////////////////////////////////////////////////24 hours

        lat, lon = data["coord"]["lat"], data["coord"]["lon"]
        params['lat'], params['lon'] = data["coord"]["lat"], data["coord"]["lon"]
        forecast = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=params).json()
        temp = 0.0
        descr = {}
        count = 0
        for i in forecast["list"][:8]:
            temp += i["main"]["temp"]
            count += 1
            if 'weather' in i and i['weather']:
                description = i['weather'][0]['description']
                if description in descr:
                    descr[description] += 1
                else:
                    descr[description] = 1

        temp24h = temp / count
        max_count = 0
        descr24h = None
        for d, c in descr.items():
            if count > max_count:
                descr24h = d

        current_weather += f'''
{_('☁ <b>Ближайшие 24 часа</b>', lang)}:
    
{_('🌡 Температура:', lang)} {round(temp24h, 2)}C
{_('☁ На улице:', lang)} {descr24h}
'''
    #///////////////////////////////////////////////////////////////////////////////////////////////3 days

        temp = 0.0
        descr = {}
        count = 0
        for i in forecast["list"][:24]:
            temp += i["main"]["temp"]
            count += 1
            if 'weather' in i and i['weather']:
                description = i['weather'][0]['description']
                if description in descr:
                    descr[description] += 1
                else:
                    descr[description] = 1

        temp72h = temp / count
        max_count = 0
        descr72h = None
        for d, c in descr.items():
            if count > max_count:
                descr72h = d

        current_weather += f'''
{_('☁ <b>Ближайшие 3 дня</b>', lang)}:
    
{_('🌡 Температура:', lang)} {round(temp72h, 2)}C
{_('☁ На улице:', lang)} {descr72h}
'''
    except:
        current_weather = _('''⁉ Название города введен неправильно, либо такой город не существует!
        
😊 Попробуйте ввести другое название''', lang)

    return current_weather
