from django.urls import path
from . import views
app_name='travel'
urlpatterns = [
    path('', views.travel_main, name='travel'),
    path('register/', views.register, name='register'),
   
    path('preview/<int:id>', views.preview, name='preview'),

    #資料crud
    path('register01/', views.register01, name='register01'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit01/<int:id>', views.edit01, name='edit01'),
    path('delete/<int:id>', views.delete, name='delete'),
  
    #顯示讀取資料
    path('region/', views.region, name='region'),
    path('town/<str:region_name>', views.town),
    path('show/<str:town_name>', views.show),
  

    #確認資料
    path('travelName/', views.travelName, name='travelName'),
    path('travelTel/', views.travelTel, name='travelTel'),
    path('travelAddress/', views.travelAddress, name='travelAddress'),
    path('travelRegion/', views.travelRegion, name='travelRegion'),
    path('travelTown/', views.travelTown, name='travelTown'),
]



