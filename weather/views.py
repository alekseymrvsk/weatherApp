from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'dc6e607a6b3706b5eeaf4d74b47f2338'
    url = 'https://api.openweathermap.org/data/2.5/' \
          'weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
