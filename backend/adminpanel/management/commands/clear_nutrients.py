# adminpanel/management/commands/clear_nutrients.py

from django.core.management.base import BaseCommand
from adminpanel.models import Nutrient

class Command(BaseCommand):
    help = 'Delete all Nutrient entries'

    def handle(self, *args, **kwargs):
        # Count the number of entries to be deleted
        count = Nutrient.objects.count()
        
        # Delete all entries
        Nutrient.objects.all().delete()

        # Output the result
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Nutrient entries'))
