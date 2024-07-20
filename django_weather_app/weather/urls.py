from django.urls import path, include
from .views import landing_page, WeatherDataListCreate, update_weather, create_weather

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('api/weather/', WeatherDataListCreate.as_view(), name='weather-list-create'),
    path('update-weather/<int:id>/', update_weather, name='update-weather'),
    path('create-weather/', create_weather, name='create-weather'),
]