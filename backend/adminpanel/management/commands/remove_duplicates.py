# adminpanel/management/commands/remove_duplicates.py

from django.core.management.base import BaseCommand
from adminpanel.models import Nutrient
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate Nutrient entries'

    def handle(self, *args, **kwargs):
        duplicates = (Nutrient.objects
                      .values('name')
                      .annotate(name_count=Count('name'))
                      .filter(name_count__gt=1))

        for duplicate in duplicates:
            nutrients = Nutrient.objects.filter(name=duplicate['name'])
            first_nutrient = nutrients.first()
            nutrients.exclude(id=first_nutrient.id).delete()

        self.stdout.write(self.style.SUCCESS('Successfully removed duplicate Nutrient entries'))
