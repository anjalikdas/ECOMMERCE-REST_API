from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays count of companies'
    def add_arguments(self, parser):
        parser.add_argument('count',type=int,help='indicate the count')
    
    def handle(self,*args,**kwargs):
        count=kwargs['count']
        print("total_count:",count)