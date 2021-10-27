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
    
    
    path('form/', views.form,name="form"),
    path('prod/', views.prod,name="prod"),
    path('update/<int:id>', views.update,name="update"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('prolist/<int:id>', views.prolist,name="prolist"),
    
    
    
    
]
