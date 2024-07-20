from django.shortcuts import render, get_object_or_404, redirect
from .models import WeatherData
from rest_framework import generics
from .serializers import WeatherDataSerializer
from .forms import WeatherDataForm

# Create your views here.

def create_weather(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
    else:
        form = WeatherDataForm()
    return render(request, 'weather/create_weather.html', {'form': form})


def update_weather(request, id):
    weather_data = get_object_or_404(WeatherData, id=id)
    if request.method == 'POST':
        form = WeatherDataForm(request.POST, instance=weather_data)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
    else:
        form = WeatherDataForm(instance=weather_data)
    return render(request, 'weather/update_weather.html', {'form': form})


def landing_page(request):
    search_cidade = request.GET.get('search')
    if search_cidade:
        weather_data = WeatherData.objects.filter(cidade__icontains=search_cidade)
    else:
        weather_data = WeatherData.objects.all()
    return render(request, 'weather/landing_page.html', {'weather_data': weather_data})

class WeatherDataListCreate(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
