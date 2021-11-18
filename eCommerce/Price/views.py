from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductPrice
from .serializers import ProductPriceSerializer
# Create your views here.

class ProductPriceViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return  ProductPriceSerializer

    def get_queryset(self):
        return ProductPrice.objects.all()