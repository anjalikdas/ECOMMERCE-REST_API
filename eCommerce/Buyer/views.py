from django.db.models.aggregates import Count
from django.http import response
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import customer
from django.contrib.auth.models import User
from .serializers import UserSerializer, customerSerializer,CustomerCountSerializer
import json

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer   

    
class CustomerViewset(viewsets.ModelViewSet):
       
    def get_serializer_class(self):
        return customerSerializer

    def get_queryset(self):
        return customer.objects.all()




class StateList(APIView):

    def get(self,request):
        output_list =[]
        
    
        all_state_list=set(customer.objects.values_list('address__state',flat=True))
        
    
        for state in all_state_list:
         output={}
         all_state_customer=customer.objects.filter(address__state=state)
         data=json.dumps((customerSerializer((all_state_customer),many=True,context={'request': request}).data),indent=4)
         output['customers'] =json.loads(data)
         output['state']=state 
         output['count']=all_state_customer.count()
         output_list.append(output)
                
        serializer=CustomerCountSerializer(output_list,many=True)
        return Response(serializer.data)
