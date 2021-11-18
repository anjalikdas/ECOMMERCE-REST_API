from django.shortcuts import render
from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return  CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        return Product.objects.all()
    
    
    def get_serializer_class(self):
        return  ProductSerializer 

 

    

    
