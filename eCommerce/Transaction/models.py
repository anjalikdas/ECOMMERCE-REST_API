
from django.db import models
from Buyer.models import customer
from Order.models import Order
from Seller.models import Company


# Create your models here.

class Payment(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True,related_name='payment')
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=9)
    status = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"] 

class sucessfull_transaction(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True,related_name='Sucessful_transaction')
    seller = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"] 

class unsucessfull_transaction(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True)
    seller = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_on"] 

    @property
    def cancelled_by(self):
        if self.customer is not None:
            return "customer:"+str(self.customer.full_name())
        elif self.seller is not None:
            return "seller:"+str(self.seller.company_name)
