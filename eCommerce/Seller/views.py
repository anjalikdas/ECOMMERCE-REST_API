from django.db.models import query
from django.db.models.aggregates import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework import response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer,DepartmentSerializer
from rest_framework.filters import SearchFilter
from rest_framework_extensions.mixins import NestedViewSetMixin
import json




# Create your views here.
class CompanyViewset(NestedViewSetMixin,viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ('company_name',)
    
    def get_serializer_class(self):
        return  CompanySerializer
     
        

    def get_queryset(self):
        return Company.objects.all()
       

  
class EmployeeViewset(NestedViewSetMixin,viewsets.ModelViewSet):
    # filter_backends = [SearchFilter]
    # search_fields = ('department',)
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer

    # def get_serializer_class(self):
    #     return  EmployeeSerializer

    # def get_queryset(self):
    #     return Employee.objects.all()
       

class EmployeeDetailViewset(NestedViewSetMixin,viewsets.ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class=EmployeeSerializer
        
        filter_backends = [SearchFilter]
        search_fields = ('Company__company_name',)



class DepartmentList(APIView):

    def get(self,request):
        output_list =[]
        
    
        all_dept_list=set(Employee.objects.values_list('department',flat=True))
        
    
        for dept in all_dept_list:
         output={}
         all_dept_employess=Employee.objects.filter(department=dept)
    
       
         data=json.dumps((EmployeeSerializer((all_dept_employess),many=True,context={'request': request}).data),indent=4)
        
         output['employess'] =json.loads(data)
         output['department']=dept 
         output['count']=all_dept_employess.count()
         output_list.append(output)
               
        serializer=DepartmentSerializer(output_list,many=True)
        return Response((serializer.data))
 
