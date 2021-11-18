from django.contrib import admin
from .models import ProductPrice
# Register your models here.
@admin.register(ProductPrice)

class ProductPriceModelAdmin(admin.ModelAdmin):
    pass
