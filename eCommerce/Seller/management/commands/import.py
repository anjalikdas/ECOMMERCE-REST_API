import csv
from django.core.management.base import BaseCommand, CommandError
from Seller.models import Company



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
        employee = []
        with open(options['path'][0], 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                employee.append(

                        model(first_name=row['first_name'],
                        last_name=row['last_name'],
                        address=row['address'],
                        email=row['email'],
                        Phone_no=row['Phone_no'],
                        department=row['department'],
                        Company=Company.objects.get(company_name=row['Company'])
                        )
                    
                )
            print(employee)
            model.objects.bulk_create(employee)