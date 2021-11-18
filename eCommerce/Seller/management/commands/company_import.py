import csv
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = ("import data from a csv file to model")


    def add_arguments(self, parser):
        parser.add_argument('model',nargs=1,type=str,help='Model name ')
        parser.add_argument('path',nargs=1,type=str,help=' path')


    def handle(self, *app_labels, **options):
        from django.apps import apps
        app_name, model_name = options['model'][0].split('.')
        model = apps.get_model(app_name, model_name)
        file_path=options['path']
        rows = []
        with open(options['path'][0], 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                model.objects.create(company_name=row[0],address=row[1],email=row[2],Phone_no=row[3])