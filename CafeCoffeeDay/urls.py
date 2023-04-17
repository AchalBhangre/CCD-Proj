"""
adding urls of the all the action
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='update'),
    path('add_menu', views.add_menu, name='add_menu'),
]
