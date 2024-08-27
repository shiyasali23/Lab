# from django.test import TestCase



# [
#     {"biochemical_id": 1, "value": 105},
#     {"biochemical_id": 2, "value": 6.0},
#     {"biochemical_id": 3, "value": 16.0},
#     {"biochemical_id": 4, "value": 210},
#     {"biochemical_id": 5, "value": 135},
#     {"biochemical_id": 6, "value": 60},
#     {"biochemical_id": 7, "value": 155},
#     {"biochemical_id": 8, "value": 165},
#     {"biochemical_id": 9, "value": 115},
#     {"biochemical_id": 10, "value": 19},
#     {"biochemical_id": 11, "value": 8.5},
#     {"biochemical_id": 12, "value": 1.6},
#     {"biochemical_id": 13, "value": 32},
#     {"biochemical_id": 14, "value": 125},
#     {"biochemical_id": 15, "value": 22},
#     {"biochemical_id": 16, "value": 27},
#     {"biochemical_id": 17, "value": 520},
#     {"biochemical_id": 18, "value": 620},
#     {"biochemical_id": 19, "value": 3.2},
#     {"biochemical_id": 20, "value": 230},
#     {"biochemical_id": 21, "value": 47},
#     {"biochemical_id": 22, "value": 1.0},
#     {"biochemical_id": 23, "value": 5.5},
#     {"biochemical_id": 24, "value": 19},
#     {"biochemical_id": 25, "value": 0.9},
#     {"biochemical_id": 26, "value": 145},
#     {"biochemical_id": 27, "value": 4.5},
#     {"biochemical_id": 28, "value": 10},
#     {"biochemical_id": 29, "value": 2.0},
#     {"biochemical_id": 30, "value": 3.8},
#     {"biochemical_id": 31, "value": 104},
#     {"biochemical_id": 32, "value": 27},
#     {"biochemical_id": 33, "value": 62},
#     {"biochemical_id": 34, "value": 3.0},
#     {"biochemical_id": 35, "value": 4.5},
#     {"biochemical_id": 36, "value": 7.5},
#     {"biochemical_id": 37, "value": 1.6},
#     {"biochemical_id": 38, "value": 2.7},
#     {"biochemical_id": 39, "value": 125},
#     {"biochemical_id": 40, "value": 290},
#     {"biochemical_id": 41, "value": 2.7},
#     {"biochemical_id": 42, "value": 42},
#     {"biochemical_id": 43, "value": 47},
#     {"biochemical_id": 44, "value": 0.6},
#     {"biochemical_id": 45, "value": 22},
#     {"biochemical_id": 46, "value": 11},
#     {"biochemical_id": 47, "value": 4.0},
#     {"biochemical_id": 48, "value": 1.3},
#     {"biochemical_id": 49, "value": 3.5},
#     {"biochemical_id": 50, "value": 30},
#     {"biochemical_id": 51, "value": 32},
#     {"biochemical_id": 52, "value": 85},
#     {"biochemical_id": 53, "value": 27},
#     {"biochemical_id": 54, "value": 0.9},
#     {"biochemical_id": 55, "value": 210},
#     {"biochemical_id": 56, "value": 13},
#     {"biochemical_id": 57, "value": 32},
#     {"biochemical_id": 58, "value": 310}
# ]






# # Create your tests here.

# # biochemicals = {
# #     {
# #         name : 'x',
# #         id : 1,
# #     },
# #     {
# #         name : 'w',
# #         id : 2,
# #     },
# #     {
# #         name : 'z',
# #         id : 3,
# #     },
# # }


# # here in biometrics w and x are registered and z not so biometrics should look like this

# # biometrics = {
# #     {
# #         'biochemical':{
# #             'name': 'x',
# #             'id': 1,
# #         }
# #         'value' :34,
# #         'scaled_value' : 0.34
# #     },
# #     {
# #         biochemical :{
# #             'name': 'w',
# #             'id': 2,
# #         }
# #         'value' :4,
# #         'scaled_value' : 0.4
# #     },
# #     {
# #         biochemical : {
# #         'name': 'z',
# #         'id': 3,
# #         }
# #         'value' : null,
# #         'scaled_value' :  null,
# #     },
# # }

# [
#     {"biochemical_id": 1, "value": 103},
#     {"biochemical_id": 2, "value": 5.7},
#     {"biochemical_id": 3, "value": 15.5},
#     {"biochemical_id": 4, "value": 204},
#     {"biochemical_id": 5, "value": 130},
#     {"biochemical_id": 6, "value": 55},
#     {"biochemical_id": 7, "value": 150},
#     {"biochemical_id": 8, "value": 160},
#     {"biochemical_id": 9, "value": 110},
#     {"biochemical_id": 10, "value": 18},
#     {"biochemical_id": 11, "value": 8},
#     {"biochemical_id": 12, "value": 1.5},
#     {"biochemical_id": 13, "value": 30},
#     {"biochemical_id": 14, "value": 120},
#     {"biochemical_id": 15, "value": 20},
#     {"biochemical_id": 16, "value": 25},
#     {"biochemical_id": 17, "value": 500},
#     {"biochemical_id": 18, "value": 600},
#     {"biochemical_id": 19, "value": 3.0},
#     {"biochemical_id": 20, "value": 220},
#     {"biochemical_id": 21, "value": 45},
#     {"biochemical_id": 22, "value": 0.9},
#     {"biochemical_id": 23, "value": 5.0},
#     {"biochemical_id": 24, "value": 18},
#     {"biochemical_id": 25, "value": 0.85},
#     {"biochemical_id": 26, "value": 140},
#     {"biochemical_id": 27, "value": 4.2},
#     {"biochemical_id": 28, "value": 9.5},
#     {"biochemical_id": 29, "value": 1.9},
#     {"biochemical_id": 30, "value": 3.5},
#     {"biochemical_id": 31, "value": 102},
#     {"biochemical_id": 32, "value": 26},
#     {"biochemical_id": 33, "value": 60},
#     {"biochemical_id": 34, "value": 2.8},
#     {"biochemical_id": 35, "value": 4.2},
#     {"biochemical_id": 36, "value": 7.0},
#     {"biochemical_id": 37, "value": 1.5},
#     {"biochemical_id": 38, "value": 2.5},
#     {"biochemical_id": 39, "value": 120},
#     {"biochemical_id": 40, "value": 280},
#     {"biochemical_id": 41, "value": 2.5},
#     {"biochemical_id": 42, "value": 40},
#     {"biochemical_id": 43, "value": 45},
#     {"biochemical_id": 44, "value": 0.5},
#     {"biochemical_id": 45, "value": 20},
#     {"biochemical_id": 46, "value": 10},
#     {"biochemical_id": 47, "value": 3.8},
#     {"biochemical_id": 48, "value": 1.2},
#     {"biochemical_id": 49, "value": 3.2},
#     {"biochemical_id": 50, "value": 28},
#     {"biochemical_id": 51, "value": 30},
#     {"biochemical_id": 52, "value": 80},
#     {"biochemical_id": 53, "value": 25},
#     {"biochemical_id": 54, "value": 0.8},
#     {"biochemical_id": 55, "value": 200},
#     {"biochemical_id": 56, "value": 12},
#     {"biochemical_id": 57, "value": 30},
#     {"biochemical_id": 58, "value": 300}
# ]


# class BiometricsEntrySerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     biometrics = serializers.ListField(child=serializers.DictField(), write_only=True)

#     class Meta:
#         model = BiometricsEntry
#         fields = ['id', 'user', 'health_score', 'created', 'biometrics']

#     def create(self, validated_data):
#         user = self.context['user']
#         biometrics_data = validated_data.pop('biometrics')
        
#         with transaction.atomic():
#             biometrics_entry = BiometricsEntry.objects.create(user=user, **validated_data)
            
#             for data in biometrics_data:
#                 biochemical = Biochemical.objects.get(id=data['biochemical_id'])
#                 Biometrics.objects.create(
#                     biochemical=biochemical,
#                     biometricsentry=biometrics_entry,
#                     value=data['value']
#                 )
        
#         self.update_health_score(biometrics_entry)
#         return biometrics_entry
    
#     def update_health_score(self, biometrics_entry):
#         try:
#             current_time = timezone.now()

#             # Get distinct biochemicals across all biometrics for this user
#             unique_biochemicals = (
#                 Biometrics.objects.filter(biometricsentry__user=biometrics_entry.user)
#                 .values_list('biochemical', flat=True)
#                 .distinct()
#             )            

#             # Retrieve all biometrics for the unique biochemicals
#             biometrics_queryset = (
#                 Biometrics.objects.filter(
#                     biochemical__in=unique_biochemicals,
#                     biometricsentry__user=biometrics_entry.user,
#                     expired_date__gt=current_time
#                 )
#                 .order_by('biochemical', '-created')
#             )

#             # Keep track of the latest biometrics for each biochemical
#             latest_biometrics = {}
#             for bio in biometrics_queryset:
#                 if bio.biochemical not in latest_biometrics:
#                     latest_biometrics[bio.biochemical] = bio.scaled_value

#             # Calculate total score
#             total_score = sum(latest_biometrics.values())

#             # Update the health score
#             biometrics_entry.health_score = total_score
#             self.update_food_score(latest_biometrics)
#             biometrics_entry.save()
#         except Exception as e:
#             print(e)
                
#     def update_food_score(self, latest_biometrics):
#         food_bias_weights = []
#         nutrient_bias_weights = []        
#         food_weights_obj = FoodWeight.objects.all()
#         nutrient_weights_obj = NutrientWeight.objects.all()
        
#         try:
#             # Process biochemicals and their corresponding weights and biases
#             for biochemical, scaled_value in latest_biometrics.items():
#                 # Retrieve all FoodWeights related to the biochemical
#                 food_weights = food_weights_obj.filter(biochemical=biochemical)
#                 for food_weight in food_weights:
#                     food_bias_weights.append({food_weight.food: (food_weight.weight * scaled_value) * -1})
#                     food_bias_weights.append({food_weight.food: (food_weight.bias * scaled_value) * -1})

#                 # Retrieve all NutrientWeights related to the biochemical
#                 nutrient_weights = nutrient_weights_obj.filter(biochemical=biochemical)
#                 for nutrient_weight in nutrient_weights:
#                     nutrient_bias_weights.append({nutrient_weight.nutrient: (nutrient_weight.bias * scaled_value) * -1})
#                     nutrient_bias_weights.append({nutrient_weight.nutrient: (nutrient_weight.weight * scaled_value) * -1})

#             # Calculate total bias weights
#             total_food_bias_weights = self.add_values(food_bias_weights)
#             total_nutrients_bias_weights = self.add_values(nutrient_bias_weights)
            
#             # Calculate food nutrient sums
#             food_nutrients_obj = FoodNutrient.objects.all()
#             food_nutrient_sum = {}
#             for food in total_food_bias_weights.keys():
#                 food_nutrient_sum[food] = 0
#                 food_nutrients = food_nutrients_obj.filter(food=food)
#                 for food_nutrient in food_nutrients:
#                     nutrient = food_nutrient.nutrient
#                     food_nutrient_sum[food] += food_nutrient.normalized_value * total_nutrients_bias_weights.get(nutrient)

#             # Normalize the nutrient sum and total food bias weights
#             scaled_nutrient_sum = self.normalize_columns(food_nutrient_sum)
#             scaled_total_food_bias_weights = self.normalize_columns(total_food_bias_weights)
            
#             # Normalize the `normalized_nutriscore` for all foods
#             foods = Food.objects.all()
#             normalized_nutriscore = {food: food.normalized_nutriscore for food in foods}
            

#             food_score = {}

#             for food in foods:
#                 food_key = food  
#                 food_score[food_key] = (
#                     scaled_total_food_bias_weights.get(food_key, 0) + 
#                     scaled_nutrient_sum.get(food_key, 0)
#                 ) + normalized_nutriscore.get(food_key, 0)
        
#         except Exception as e:
#             print(f"An error occurred: {e}")

 

#     def add_values(self, data):
#         # Use a dictionary to accumulate values
#         merged_dict = {}
#         for item in data:
#             for key, value in item.items():
#                 merged_dict[key] = merged_dict.get(key, 0) + value
        
#         return merged_dict
    
#     def normalize_columns(self, data_dict):
#         min_val = min(data_dict.values())
#         max_val = max(data_dict.values())
#         normalized_dict = {k: (v - min_val) / (max_val - min_val) for k, v in data_dict.items()}
#         return normalized_dict
