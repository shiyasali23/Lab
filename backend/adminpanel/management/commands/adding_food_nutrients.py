# from django.core.management.base import BaseCommand
# import pandas as pd
# from adminpanel.models import Nutrient, Food, FoodNutrient

# class Command(BaseCommand):
#     help = 'Process food nutrients data from a CSV file'

#     def handle(self, *args, **kwargs):
#         try:
#             df = pd.read_csv('/Users/shiyas/Desktop/code-red/Lab/dataset/food_nutrients.csv')
#         except FileNotFoundError:
#             print("The file was not found.")
#             return

#         # Drop unnecessary columns
#         df = df.drop(columns=['Unnamed: 0', 'category', 'sub_category'])

#         flatten_list = []
        
#         # Caching Food and Nutrient objects
#         food_cache = {food.name: food.id for food in Food.objects.all()}
#         nutrient_cache = {nutrient.name: nutrient.id for nutrient in Nutrient.objects.all()}

#         for index, row in df.iterrows():
#             food_name = row['name']
#             if food_name not in food_cache:
#                 print(f"Food with name {food_name} not found.")
#                 continue

#             food_id = food_cache[food_name]
            
#             for nutrient, value in row.drop(['name']).items():
#                 if nutrient not in nutrient_cache:
#                     print(f"Nutrient with name {nutrient} not found.")
#                     continue
                
#                 nutrient_id = nutrient_cache[nutrient]
#                 flatten_list.append({'food_id': food_id, 'nutrient_id': nutrient_id, 'value': value})

#         # Save to FoodNutrient model
#         for entry in flatten_list:
#             FoodNutrient.objects.create(
#                 food_id=entry['food_id'],
#                 nutrient_id=entry['nutrient_id'],
#                 value=entry['value']
#             )
        
#         print("Data has been successfully saved.")
