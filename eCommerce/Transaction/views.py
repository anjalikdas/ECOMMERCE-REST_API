from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Payment,sucessfull_transaction,unsucessfull_transaction
from .serializers import PaymentSerializer,sucessfull_transactionSerializer,unsucessfull_transactionSerializer,Customer_spendingSerializer
from django.db.models.aggregates import Sum
from django.db.models import Func
from django.db import models
from .serializers import Customer
from rest_framework.response import Response
from Buyer.models import customer
from Buyer.serializers import customerSerializer
import json

# Create your views here.
class PaymentViewset(viewsets.ModelViewSet):
       def get_serializer_class(self):
        return  PaymentSerializer

       def get_queryset(self):
           return Payment.objects.all()
    


class Successfull_transactionViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return sucessfull_transactionSerializer 

    def get_queryset(self):
           return sucessfull_transaction.objects.all()


class Unsuccessfull_transactionViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return  unsucessfull_transactionSerializer   

    def get_queryset(self):
           return unsucessfull_transaction.objects.all() 


class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()





class Customer_spending(APIView):
    
    def get(self,request):
        output_list=[]
        all_customer_list=set(Payment.objects.values_list('customer',flat=True))

        
        m=11
               
        for cust in all_customer_list:
            qs=Payment.objects.annotate(month=Month('updated_on')).values('month','amount').filter(customer=cust).filter(month=m)
            output={}

            if qs.exists():
                amount=sum(qs.values_list('amount',flat=True))
                customer_list=customer.objects.filter(id=cust)
                data=json.loads(json.dumps((customerSerializer((customer_list),many=True,context={'request': request}).data),indent=4))
                output['customer']=data 
                output['month']=m 
                output['amount']=amount
                output_list.append(output) 
        serializer=Customer(output_list,many=True)
        return Response(serializer.data)
