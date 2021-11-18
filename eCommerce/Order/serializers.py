from rest_framework import serializers
from .models import Order,ProductCart





class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCart
        fields = ('id','customer','product','quantity','url')

       

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = ('id','customer','product','address','address_second','postal_code','country','state','ordered_date','status','url')


class ProductDetailSerializer(serializers.ModelSerializer):
    count=serializers.ReadOnlyField()
    class Meta:
        model=Order
        fields=('customer','product','count')
        depth=1
        


class OrderDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('customer','product','ordered_date')
        depth=1
                 
class ProductDetailSerializer(serializers.ModelSerializer):
    customer=serializers.ReadOnlyField()
    product_list=serializers.ReadOnlyField()
    total_no_of_products_ordered=serializers.StringRelatedField()
    class Meta:
        model=Order
        fields=('customer','product_list','total_no_of_products_ordered')
        
class DateSerializer(serializers.ModelSerializer):
    customer=serializers.ReadOnlyField()
    products=serializers.ReadOnlyField()
    ordered_date=serializers.StringRelatedField()
    class Meta:
        model=Order
        fields=('customer','products','ordered_date')                