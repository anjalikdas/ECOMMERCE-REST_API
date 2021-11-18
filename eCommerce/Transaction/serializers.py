from rest_framework import serializers
from .models import Payment,sucessfull_transaction,unsucessfull_transaction




class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields = ('customer','order','amount','status')



class sucessfull_transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=sucessfull_transaction
        fields = ('id','customer','seller','order','payment')   


class unsucessfull_transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=unsucessfull_transaction
        fields = ('id','customer','seller','order','payment',)  
     


    
class Customer_spendingSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField()
    total_amount = serializers.ReadOnlyField()
    month = serializers.ReadOnlyField()
    class Meta:
        model = Payment
        fields = ('customer','month','total_amount',)  


class Customer(serializers.ModelSerializer):
    customer=serializers.ReadOnlyField()
    amount = serializers.ReadOnlyField()
    month = serializers.ReadOnlyField()
    class Meta:
        model = Payment
        fields =('customer','amount','month')

        

            
    