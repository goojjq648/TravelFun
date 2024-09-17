from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main_app/home.html')

def food(request):
    return render(request, 'main_app/food.html')

def custom_logout_view(request):
    auth_logout(request)
    return render(request, 'main_app/logout.html')