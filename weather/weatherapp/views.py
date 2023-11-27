from django.shortcuts import render,HttpResponse
import json
import requests


# Create your views here.

def weatherapi(request):
    city='varanasi'

    if request.GET:
        city=request.GET["Cityname"]
    appid="852aabe2b9fa456630d55d0f7035f26a"
    url="https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(city,appid)
    response=requests.get(url)
    data=json.loads(response.text)
    temp=data["main"]["temp"]
    feel=data["main"]["feels_like"]
    temp_min=data["main"]["temp_min"]

    print(data)

    return render(request,"weather.html",{"City":city,"temp_min":temp_min,"city":city,"data":data,"temp":temp,"feel":feel})

    if city not in data:
        return HttpResponse("Opps")