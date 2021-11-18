
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProductCart,Order
from Buyer.serializers import customerSerializer
from Buyer.models import customer
from .serializers import ProductCartSerializer,OrderSerializer,ProductDetailSerializer,OrderDateSerializer,DateSerializer
from rest_framework.filters import SearchFilter
from Product.serializers import ProductSerializer
from Product.models import Product
import json
# Create your views here.

class ProductCartViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return  ProductCartSerializer

    def get_queryset(self):
        return ProductCart.objects.all()

class OrderViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return OrderSerializer 

    def get_queryset(self):
        return Order.objects.all() 

   

class ProductDetail(APIView):
     
     def get(self,request):
        output_list=[]
        all_customer_list=set(Order.objects.values_list('customer',flat=True))
        
        for cust in all_customer_list:
            output={}
            product_list=Order.objects.values_list('product',flat=True).filter(customer=cust).filter(ordered_date__range=['2021-10-15', '2021-10-25'])
            product= Product.objects.filter(id__in=product_list)
            
            if product.exists():
                customers=customer.objects.filter(id=cust)
                output['customer']=json.loads(json.dumps((customerSerializer((customers),many=True,context={'request': request}).data),indent=4))
                output['product_list']=json.loads(json.dumps((ProductSerializer((product),many=True).data),indent=4))

                output['total_no_of_products_ordered']=product_list.count()
                output_list.append(output)  
              
        serializer=ProductDetailSerializer(output_list,many=True)
        return Response(serializer.data)
     
    
   
class OrdereddateViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderDateSerializer
    filter_backends = [SearchFilter]
    search_fields = ('ordered_date',)


class OrderedDateView(APIView):

     def get(self,request):
        output_list=[]
        all_customer_list=set(Order.objects.values_list('customer',flat=True))
        
        
        m='2021-10-04'
               
        for cust in all_customer_list:
            product_list=Order.objects.values_list('product',flat=True).filter(customer=cust).filter(ordered_date=m)
            
            output={}
            product= Product.objects.filter(id__in=product_list)

            if product.exists():
                customers=customer.objects.filter(id=cust)
                output['customer']=json.loads(json.dumps((customerSerializer((customers),many=True,context={'request': request}).data),indent=4))
                output['products']=json.loads(json.dumps((ProductSerializer((product),many=True).data),indent=4))
                output['ordered_date']=m
                output_list.append(output) 
        serializer=DateSerializer(output_list,many=True)
        return Response(serializer.data)
