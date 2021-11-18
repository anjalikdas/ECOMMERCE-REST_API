from django.contrib import admin
from .models import customer
# Register your models here.

@admin.register(customer)

class CustomerModelAdmin(admin.ModelAdmin):
    pass
