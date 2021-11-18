from django.contrib import admin
from django.db import models
from Seller.models import Company,Employee

# Register your models here.
@admin.register(Company,Employee)
class CompanyModelAdmin(admin.ModelAdmin):
    pass


class EmployeeModelAdmin(admin.ModelAdmin):
    pass
