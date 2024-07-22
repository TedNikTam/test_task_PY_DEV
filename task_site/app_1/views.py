from django.shortcuts import render
from django.http import HttpResponse


#==========================
import requests
from pprint import pprint


open_weather_token = '2231ff65e81ef78deb6df51d6a6e597e'

def get_weather(city, open_weather_token):
    # получаем назвние города и делаем запрос для получения погоды
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        if r.status_code == 200:
            return {'status': 'OK', 'data': r.json()}
        else:
            return {'status': 'FAIL', 'data': r.data}
    except Exception as ex:
        print(ex)
        return {'status': 'FAIL', 'data': ex}
#========================

def index(request):
    return render(request, "index.html")

def city_place(request):
    # получаем из данных запроса POST отправленные через форму данные(название города)
    city = request.POST.get("city", "Undefined")
    data = get_weather(city, open_weather_token)
    if data['status'] == 'OK':
        print(data['data']['main'])
        temp_data = data['data']['main']['temp']
        feels_like_data = data['data']['main']['feels_like']
        temp_max_data = data['data']['main']['temp_max']
        temp_min_data = data['data']['main']['temp_min']
        pressure_data = data['data']['main']['pressure']
        print(f'Город: {city} \nТемпература: {temp_data}°C \nОщущается как: {feels_like_data}°C \nМаксимальная температура: {temp_max_data}°C \nМинимальная температура: {temp_min_data}°C\nДавление: {pressure_data} мм рт. ст.')
        # return HttpResponse(f"<h2> {data['data']['main']} </h2>")
        return HttpResponse(f'''<h2>Город : {city} <br> 
                            Температура: {temp_data}°C <br> 
                            Ощущается как: {feels_like_data}°C <br>
                            Максимальная температура: {temp_max_data}°C <br> 
                            Минимальная температура: {temp_min_data}°C <br> 
                            Давление: {pressure_data} мм рт. ст.</h2>''')
    else:
        return HttpResponse(f"<h2> ERROR: {data['data']} </h2>")