import os
from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer

load_dotenv()

forecast_token = os.getenv('FORECAST_TOKEN')
sms_token = os.getenv('SMS_TOKEN')

town_title = "Курск"

server = SMSServer(sms_token)

new_event = get_new_event(forecast_token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template ='''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''
sms_message = sms_template.format(
    town_title=town_title,
    event_time=event_time,
    event_date=event_date,
    event_area=event_area,
    phenomenon_description=phenomenon_description
)
server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: функция ввыводит только регион и погода
# Вывод: пустые переменные

# Гипотеза 2: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: в переменной town_title есть название города "Курск"
# Вывод: в переменной есть название города

# Гипотеза 3: дать разное название переменным токен 
# Способ проверки: делаем 1 FORECAST_TOKEN, 2 SMS_TOKEN
# Код для проверки: 
# forecast_token = os.getenv('FORECAST_TOKEN')
# sms_token = os.getenv('SMS_TOKEN')
# Установленный факт: теперь токен передает правильные данные
# Вывод: 1 токен заменял второй токен

# Гипотеза 4: переменные с 22 по 26 строку пустые
# Способ проверки: добавить к ним переменные
# Код для проверки:
# town_title=town_title, event_time=event_time, event_date=event_date, event_area=event_area, phenomenon_description=phenomenon_description
# Установленный факт: переменные начали получать данные
# Вывод: переменным нужны были аргументы
