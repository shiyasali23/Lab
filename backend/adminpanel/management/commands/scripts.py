from services.models import Biometrics
from adminpanel.models import Weight
from django.core.management.base import BaseCommand
from decimal import Decimal

class Command(BaseCommand):
    help = 'Calculate and print food scores for a given user'

    def handle(self, *args, **kwargs):
        def calculate_food_scores(user_id=6):
            
            # Fetch biometrics for the user
            biometrics = Biometrics.objects.filter(user_id=user_id).values('biochemical__name', 'scaled_value')
            weighted_nutrients = []

            for bio in biometrics:
                biochemical_name = bio['biochemical__name']
                scaled_value = Decimal(bio['scaled_value'])  
                
                
                weights = Weight.objects.filter(biochemical__name=biochemical_name, nutrient__isnull=False)
                
                for weight in weights:
                    weight_value = Decimal(weight.weight)  # Ensure weight is a Decimal
                    nutrient_score = weight_value * scaled_value
                    weighted_nutrients.append({weight.nutrient.name: nutrient_score})
                    
            def combine_values(combined_list):
                weighted_combined_list = {}

                for nutrient_dict in combined_list:
                    for nutrient, value in nutrient_dict.items():
                        if nutrient in weighted_combined_list:
                            weighted_combined_list[nutrient] += value
                        else:
                            weighted_combined_list[nutrient] = value

                return weighted_combined_list
            
            combined_weighted_nutrients = combine_values(weighted_nutrients)
            
            print(weighted_nutrients)
            
        calculate_food_scores(6)
