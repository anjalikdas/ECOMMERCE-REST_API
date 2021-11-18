from django.db import models
from Seller.models import Company,Employee

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"    


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_code = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,related_name='product')
    product_dimension = models.JSONField()
    price = models.DecimalField(decimal_places=2,max_digits=9)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('product_code','employee')
        ordering = ["product_code"]

    def __str__(self):
        return self.product_name
   

    
