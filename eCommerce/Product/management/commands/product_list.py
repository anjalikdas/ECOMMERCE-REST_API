from django.core.management.base import BaseCommand, CommandError
from Product.models import Product

class Command(BaseCommand):
    help = 'Prints all product names'

    def handle(self,*args,**options):
        try:
            products = Product.objects.all()
            for p in products:
                 self.stdout.write(self.style.SUCCESS(p.product_name))
        except:
            self.stdout.write(self.style.ERROR('Field "product_name" does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully printed all Product names'))
        return