from django.db import models
from django.db.models.deletion import CASCADE
from Product.models import Product
# Create your models here.


class ProductPrice(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.Product.product_name+"   "+self.Product.price


    class Meta:
        verbose_name_plural = "Product price details"
