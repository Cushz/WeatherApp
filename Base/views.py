from django.shortcuts import render
import requests
from .models import *
from .forms import *
# Create your views here.
def indexView(request):
    # to get data
    cities=City.objects.all()
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form  = CityForm()        
    data=[]
    for city in cities:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=035f6c42a1b7250a8ec77b71f0a7c7f1")
        weather = response.json()
        data_of_city = {
        'city': city,
        'temperature': weather["main"]["temp"],
        'description': weather["weather"][0]["description"],
        'icon': weather["weather"][0]["icon"],
        }
        data.append(data_of_city)
    context = {'data': data,"form":form}
    
    print(context)
    return render(request, "index.html",context)