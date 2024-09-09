from django.core.management.base import BaseCommand
from mlmodels.models import MachineLearningModel

class Command(BaseCommand):
    help = 'Delete records from the MachineLearningModel table'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm deletion of all records in the MachineLearningModel table',
        )

    def handle(self, *args, **kwargs):
        confirm = kwargs['confirm']

        if not confirm:
            self.stdout.write(self.style.ERROR('You must confirm the deletion by using --confirm'))
            return

        deleted_count, _ = MachineLearningModel.objects.all().delete()
        if deleted_count:
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} records from MachineLearningModel table'))
        else:
            self.stdout.write(self.style.WARNING('No records found to delete in MachineLearningModel table'))