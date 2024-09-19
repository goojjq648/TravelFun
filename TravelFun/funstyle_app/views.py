from django.shortcuts import render

# Create your views here.
def funstyle_mainPage(request):
    return render(request, 'funstyle_app/funstyle_mainPage.html')