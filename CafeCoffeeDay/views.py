"""
This module contains the views for the Cafe Coffee Day application.

These views handle requests from the user and return HTML templates responses.
"""
from django.shortcuts import render, redirect
from .models import CafeCoffeeDay,MenuItem


# Create your views here.
def index(request):
    """ Render the index page of the website."""
    cafeshop = CafeCoffeeDay.objects.all()
    menuitem = MenuItem.objects.all()
    context = {
        'cafeshop': cafeshop,
         'menuitem': menuitem,
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
        
def delete(request,id):
    """Render the delete page of the website return the home
    """
    cafeshop = CafeCoffeeDay.objects.filter(id=id)
    cafeshop.delete()
    return redirect('home')
    
def view_menu(request):
    """ Render the index page of the website."""
    menuitem = MenuItem.objects.all()
    context = {
        'menuitem': menuitem,
    }
    return render(request, 'index.html', context)
    
    
def addMenu(request):
    """Render the view menu page of the website. """
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_price = request.POST.get('item_price')
        item_ingredients = request.POST.get('item_ingredients')
        item_category = request.POST.get('item_category')
        menuitem = MenuItem(
            item_name=item_name,
            item_description=item_description,
            item_price=item_price,
            item_ingredients=item_ingredients,
            item_category=item_category
            )
        menuitem.save()
    return redirect('view_menu')