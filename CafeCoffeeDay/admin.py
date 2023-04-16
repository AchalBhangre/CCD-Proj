from django.contrib import admin

# Register your models here.
from .models import CafeCoffeeDay,MenuItem


admin.site.register(CafeCoffeeDay)
admin.site.register(MenuItem)
