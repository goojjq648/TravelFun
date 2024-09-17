from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('member_list/', views.member_list, name='member_list'),
    path('member/edit/<int:id>/', views.edit_member, name='edit_member'),  # 編輯會員
    path('member/delete/<int:id>/', views.delete_member, name='delete_member'),  # 刪除會員
    path('no_permission/', views.no_permission, name='no_permission'),
    path('add_member/', views.add_member, name='add_member'),
    path('search_members/', views.search_members, name='search_members')
    
]
