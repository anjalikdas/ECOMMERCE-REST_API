from django.core.management.base import BaseCommand,CommandError
from Order.models import Order
from datetime import timedelta, datetime
from django.utils.timezone import utc



def now():
    return datetime.utcnow().replace(tzinfo=utc)


class Command(BaseCommand):
    help='total no of items ordered today'

    def handle(self,*args,**options):
     
     order_list=Order.objects.filter(ordered_date=now())
     if order_list.exists():
      self.stdout.write('no of items ordered today')   
      self.stdout.write(self.style.SUCCESS(order_list.count()))
     else:
        self.stdout.write(self.style.SUCCESS("There are no orders "))   
     return 
