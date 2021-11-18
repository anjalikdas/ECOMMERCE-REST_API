from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    address = models.JSONField()
    email = models.EmailField(max_length=70, unique=True)
    Phone_no = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ["company_name"]   


class Employee(models.Model):
    DEPARTMENT = (
        ('BA','Business Analysts'),
        ('CSR','Customer Service Representative'),
        ('OC','Order Clerks'),
        ('DD','Delivery driver'),
        ('PM','Product Manager'),
        ('MM','Marketing manager'))
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35,blank=True,null=True)
    address = models.JSONField()
    email = models.EmailField(max_length=70, unique=True)
    Phone_no = models.CharField(max_length=10,null=True)
    department = models.CharField(choices = DEPARTMENT,null=True,default='PM',max_length=20)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='employee')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name+" "+ self.last_name

    class Meta:
        ordering = ["first_name"]      
