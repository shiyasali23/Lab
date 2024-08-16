from django.core.management.base import BaseCommand
from adminpanel.models import NutrientWeight

class Command(BaseCommand):
    help = 'Delete all entries in the NutrientWeight table'

    def handle(self, *args, **kwargs):
        # Confirm action with the user
        if input("Are you sure you want to delete all records from NutrientWeight table? Type 'yes' to confirm: ") != 'yes':
            self.stdout.write(self.style.WARNING('Operation canceled.'))
            return

        # Delete all records from NutrientWeight table
        deleted_count, _ = NutrientWeight.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} records from NutrientWeight table.'))
