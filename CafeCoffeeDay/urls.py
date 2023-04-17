"""
adding urls of the all the action
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('home', views.index, name='home'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='update'),
    path('add_menu', views.add_menu, name='add_menu'),
    
]
