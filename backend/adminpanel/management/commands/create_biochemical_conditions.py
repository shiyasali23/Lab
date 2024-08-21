from django.core.management.base import BaseCommand
import pandas as pd
from django.db import transaction
from adminpanel.models import Biochemical, Condition, BiochemicalCondition

class Command(BaseCommand):
    help = 'Create biochemical conditions from CSV file'

    def handle(self, *args, **kwargs):
        csv_path = '/Users/shiyas/Desktop/code-red/Lab/datasets/csv/biochemical_conditions.csv'
        
        try:
            data = pd.read_csv(csv_path)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error reading CSV file: {e}"))
            return

        with transaction.atomic():
            for index, row in data.iterrows():
                biochemical_name = row['name']
                
                try:
                    biochemical = Biochemical.objects.get(name=biochemical_name)
                except Biochemical.DoesNotExist:
                    self.stderr.write(self.style.ERROR(f"Biochemical {biochemical_name} not found"))
                    continue

                for condition_name in data.columns[1:]:
                    value = row[condition_name]
                    
                    if value == 0:
                        continue

                    is_hyper = True if value == 1 else False

                    try:
                        condition, _ = Condition.objects.get_or_create(name=condition_name)
                        BiochemicalCondition.objects.create(
                            biochemical=biochemical,
                            condition=condition,
                            is_hyper=is_hyper
                        )
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error processing row {index} for condition {condition_name}: {e}"))
                        raise  

        self.stdout.write(self.style.SUCCESS("Biochemical conditions import completed successfully."))
