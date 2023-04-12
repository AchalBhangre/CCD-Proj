from django.shortcuts import render,redirect

from .models import CafeCoffeeDay

# Create your views here.
def INDEX(request):
    cafeshop = CafeCoffeeDay.objects.all()
    context={
        'cafeshop': cafeshop,
    }
    return render(request,'index.html',context)
    
def ADD(request):
    if request.method=='POST':
        fName = request.POST.get('fName')
        coffeeName = request.POST.get('coffeeName')
        address = request.POST.get('address')
        price = request.POST.get('price')
        
        cafeshop=CafeCoffeeDay(
             fName = fName,
             coffeeName = coffeeName,
             address = address,
             price = price
             
            )
        cafeshop.save()
    return redirect('home')
    
def EDIT(request):
    cafeshop = CafeCoffeeDay.objects.all()
    context={
        'cafeshop': cafeshop,
    }
    return redirect(request,'index.html',context)
    
def UPDATE(request,id):
    if request.method=='POST':
        fName = request.POST.get('fName')
        coffeeName = request.POST.get('coffeeName')
        address = request.POST.get('address')
        price = request.POST.get('price')
        
        cafeshop=CafeCoffeeDay(
             id=id,
             fName = fName,
             coffeeName = coffeeName,
             address = address,
             price = price
             
            )
        cafeshop.save()
        return redirect('home')
    return redirect(request,'index.html')

def DELETE(request,id):
    cafeshop = CafeCoffeeDay.objects.filter(id = id)
    cafeshop.delete()
    context={
        'cafeshop': cafeshop,
    }
    return redirect('home')
   


    
    
    
    
