from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('token/refresh/', views.refresh_token, name='refresh_token'),
    path('logout/', views.logout, name='logout'),
]
