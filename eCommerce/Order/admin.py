from django.contrib import admin
from .models import Order,ProductCart
# Register your models here.

@admin.register(Order,ProductCart)

class OrderModelAdmin(admin.ModelAdmin):
    pass

class ProductOrderModelAdmin(admin.ModelAdmin):
    pass

