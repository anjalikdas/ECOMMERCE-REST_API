from django.contrib import admin
from .models import Payment,sucessfull_transaction,unsucessfull_transaction
# Register your models here.


admin.site.register(Payment)


admin.site.register(sucessfull_transaction)

admin.site.register(unsucessfull_transaction)
