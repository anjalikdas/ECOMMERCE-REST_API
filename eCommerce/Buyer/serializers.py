from django.db.models import fields
from rest_framework import serializers
from .models import customer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id','first_name','last_name','email','username')

  


class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model=customer
        fields = ('id','customer_name','user','address','ph_no',)

    def validate_Phone_no(self, data): 
        if customer.objects.filter(ph_no=data).exists():
            raise serializers.ValidationError("There is already a user with this phone number,please enter difference value") 
        return data    

class CustomerCountSerializer(serializers.ModelSerializer):
     customers=serializers.ReadOnlyField()
     state=serializers.ReadOnlyField()
     count=serializers.ReadOnlyField()
     class Meta:
         model=customer
         fields=('customers','state','count')        

    
    
   
       