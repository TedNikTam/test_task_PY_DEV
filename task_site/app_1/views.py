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

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные(имя и возраст)
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")

def city_place(request):
    # получаем из данных запроса POST отправленные через форму данные(название города)
    city = request.POST.get("city", "Undefined")
    data = get_weather(city, open_weather_token)
    if data['status'] == 'OK':
        return HttpResponse(f"<h2> {data['data']} </h2>")
    else:
        return HttpResponse(f"<h2> ERROR: {data['data']} </h2>")