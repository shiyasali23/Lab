# from django.core.management.base import BaseCommand
# import pandas as pd
# from adminpanel.models import Biochemical, Nutrient, Weight

# class Command(BaseCommand):
#     help = 'Process nutrient biochemicals data from a CSV file'

#     def handle(self, *args, **kwargs):
#         try:
#             df = pd.read_csv('/Users/shiyas/Desktop/code-red/Lab/dataset/biochemical_nutrients.csv')
#         except FileNotFoundError:
#             print("The file was not found.")
#             return

#         # Drop unnecessary columns
#         df = df.drop(columns=['Unnamed: 0'])

#         flatten_list = []

#         # Caching nutrient and Biochemical objects
#         nutrient_cache = {nutrient.name: nutrient.id for nutrient in Nutrient.objects.all()}
#         biochemical_cache = {biochemical.name: biochemical.id for biochemical in Biochemical.objects.all()}

#         for nutrient_name, nutrient_id in nutrient_cache.items():
#             # Filter DataFrame for the specific nutrient
#             filtered_df = df[df['name'] == nutrient_name]

#             # If no data for the specific nutrient, skip
#             if filtered_df.empty:
#                 continue

#             # Iterate over biochemical columns
#             for biochemical_name, biochemical_id in biochemical_cache.items():
#                 if biochemical_name in filtered_df.columns:
#                     value = filtered_df[biochemical_name].values[0]
#                     flatten_list.append({
#                         'nutrient_id': nutrient_id,
#                         'biochemical_id': biochemical_id,
#                         'value': value
#                     })
        
#         # Now create and save Weight instances
#         for item in flatten_list:
#             try:
#                 Weight.objects.create(
#                     nutrient_id=item['nutrient_id'],
#                     biochemical_id=item['biochemical_id'],
#                     weight=item['value']
#                 )
#             except Exception as e:
#                 print(f"Failed to create Weight instance: {e}")

#         print(f"Created {len(flatten_list)} Weight instances.")
