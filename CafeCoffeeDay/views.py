"""
This module contains the views for the Cafe Coffee Day application.

These views handle requests from the user and return HTML templates responses.
"""
from django.shortcuts import render, redirect
from .models import CafeCoffeeDay


# Create your views here.
def index(request):
    """ Render the index page of the website."""
    cafeshop = CafeCoffeeDay.objects.all()
    context = {
        'cafeshop': cafeshop,
    }
    return render(request, 'index.html', context)
def add(request):
    """Render the add page of the website. """
    if request.method == 'POST':
        fName = request.POST.get('fName')
        coffeeName = request.POST.get('coffeeName')
        address = request.POST.get('address')
        price = request.POST.get('price')
        cafeshop = CafeCoffeeDay(
            fName=fName,
            coffeeName=coffeeName,
            address=address,
            price=price
            )
        cafeshop.save()
    return redirect('home')
def edit(request):
    """ Render edit add page of the website.
    """
    cafeshop = CafeCoffeeDay.objects.all()
    context = {
        'cafeshop': cafeshop,
    }
    return redirect(request, 'index.html', context)
def update(request, id):
    """ Render the update page of the website.
     return home page
     """
    if request.method == 'POST':
        fName = request.POST.get('fName')
        coffeeName = request.POST.get('coffeeName')
        address = request.POST.get('address')
        price = request.POST.get('price')
        cafeshop = CafeCoffeeDay(
            id=id,
            fName=fName,
            coffeeName=coffeeName,
            address=address,
            price=price
            )
        cafeshop.save()
        return redirect('home')
def delete(id):
    """Render the delete page of the website return the home
    """
    cafeshop = CafeCoffeeDay.objects.filter(id=id)
    cafeshop.delete()
    return redirect('home')
    