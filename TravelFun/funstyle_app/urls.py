from django.urls import path
from . import views

app_name = 'funstyle'

urlpatterns = [
    # http://127.0.0.1:8000/funstyle_app/
    path('', views.funstyle_mainPage, name='funstyle_mainPage'),
]
