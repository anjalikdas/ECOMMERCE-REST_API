import csv
from django.core.management.base import BaseCommand, CommandError
from Buyer.models import customer
from django.contrib.auth.models import User
from Order.models import ProductCart
from Product.models import Product



class Command(BaseCommand):
    help = ("import data from a csv file to model")


    def add_arguments(self, parser):
        parser.add_argument('model',nargs=1,type=str,help='Model name to export like Seller.Employee')
        parser.add_argument('path',nargs=1,type=str,help='path')


    def handle(self, *app_labels, **options):
        from django.apps import apps
        app_name, model_name = options['model'][0].split('.')
        model = apps.get_model(app_name, model_name)
        file_path=options['path']

        productorder= []
        with open(options['path'][0], 'r') as file:
            csvreader = csv.DictReader(file)    
            for row in csvreader:
                
                q= model(customer=customer.objects.get(user=User.objects.get(first_name=(row['customer']))),
                          address=row['address'],
                          address_second=row['address_second'],
                          postal_code=row['postal_code'],
                          country=row['country'],
                          state=row['state'],
                          status=row['status']
                          )
                q.save()
            
                product=ProductCart.objects.filter(product=Product.objects.get(product_name=row['product']),customer=customer.objects.get(user=User.objects.get(first_name=(row['customer']))))
                print(product)
                for p in product:
                    q.product.add(p)
            
                productorder.append(q)
            # print(productorder)
            model.objects.bulk_create(productorder)