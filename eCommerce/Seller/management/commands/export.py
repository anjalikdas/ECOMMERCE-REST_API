"""
 Prints CSV of all fields of a model.
"""

import csv
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = ("Output the specified model as CSV")


    def add_arguments(self, parser):
        parser.add_argument('model',nargs=1,type=str,help='Model name to export like Seller.Employee')
        parser.add_argument('outfile',nargs=1,type=str,help='Save path, Seller/employee_export')


    def handle(self, *app_labels, **options):
        from django.apps import apps
        app_name, model_name = options['model'][0].split('.')
        model = apps.get_model(app_name, model_name)
        field_names = [f.name for f in model._meta.fields]
        writer = csv.writer(open(options['outfile'][0], 'w'), quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerow(field_names)
        for instance in model.objects.all().order_by('id'):
            writer.writerow([str(getattr(instance, f)) for f in field_names])