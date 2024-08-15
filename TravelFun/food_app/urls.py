from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # http://127.0.0.1:8000/food_app/
    path('', views.food_mainPage, name='food_mainPage'),
]
