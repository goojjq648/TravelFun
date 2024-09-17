from django.urls import path, include
from . import views
from .views import custom_logout_view 

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('logout/', custom_logout_view, name='logout'),
    path('food/', include('food_app.urls')),
    
]
