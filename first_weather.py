from pyowm import OWM


try:
    city = input('Введите насеенный пункт: ')

    owm = OWM('30b3e480af39c5c8a31c53584f1bdd67')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    bt = w.detailed_status
    temperature = w.temperature('celsius')['temp']
    t = w.temperature('celsius')['feels_like']
    print("В месте под названием " + str(city) + " сейчас " + str(bt) + " и " + str(temperature) + " градус/градусов по цельсию," + " ощущается как " + str(t) + " градус/градусов")
except :
    print('Город не найден')