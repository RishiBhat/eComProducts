from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),    
    #path('dash',views.dash, name="dash"),    
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('prod/<int:id>', views.prod,name="prod"),
    
    
]
