
from rest_framework import serializers


from .models import Product,Category



class ProductSerializer(serializers.ModelSerializer):
   class Meta:
        model = Product
        fields = ('id','product_name','product_code','category','product_dimension','price','stock','is_active','seller','employee')
   
    
              
   
#    def validate_product_dimension(self,value):
#         if value['not_valid']:
#             raise serializers.ValidationError("Not valid")
#         return value  

  



class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model=Category
        fields = ('id','name','description','product')


    def create(self,validated_data):
        product_data=validated_data.pop('product')
        category=Category.objects.create(**validated_data)
        for product in product_data:
            Product.objects.create(category=category,**product)
        return category    

    def update(self, instance, validated_data):
        product_data=validated_data.pop('product')
        instance.stock=validated_data.get("stock",instance.stock)
        instance.save()
        keep_products=[]
        for product in product_data:
            if "id" in product.keys():
                if Product.objects.filter(id=product['id']).exists():
                    p=Product.objects.get(id=product['id'])
                    p.status=product.get('status',p.status)
                    keep_products.append(p.id)
                else:
                    continue
            else:
                p=Product.objects.create(**product,Category=instance) 
                keep_products.append(p.id)       
        for product in instance.product_data:
            if product.id  not in keep_products:
                product.delete()
        return instance        

                
