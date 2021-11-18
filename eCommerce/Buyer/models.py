from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.JSONField()
    ph_no = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
         return str(self.user.first_name+" "+self.user.last_name)

    class Meta:
        verbose_name_plural = "Customer Details"     

    @property
    def customer_name(self):
       return "%s %s" % (self.user.first_name, self.user.last_name)    
