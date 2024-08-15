from django.shortcuts import render

# Create your views here.


def food_mainPage(request):
    return render(request, 'food_app/food_mainPage.html')
