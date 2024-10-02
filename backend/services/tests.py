# from django.test import TestCase

# def fetch_user_data(user):
#     try:
#         biometrics_entries = BiometricsEntry.objects.filter(user=user)
        
#         if not biometrics_entries.exists():
#             return None, 'No biometrics entries found for the user.'
        
#         latest_entry = biometrics_entries.latest('created')
#         biometrics = Biometrics.objects.filter(biometricsentry__user=user)
#         food_scores = FoodScore.objects.filter(biometricsentry=latest_entry)
        
        
        
#         biometrics_data_dict = {}
        
#         for biometric in biometrics:
#             bio_name = biometric.biochemical.name
            
#             if bio_name not in biometrics_data_dict:
#                 biometrics_data_dict[bio_name] = {
#                     'values': [],
#                     'healthy_min': (
#                         biometric.biochemical.female_min if user.gender == 'female'
#                         else biometric.biochemical.male_min
#                     ),
#                     'healthy_max': (
#                         biometric.biochemical.female_max if user.gender == 'female'
#                         else biometric.biochemical.male_max
#                     ),
#                     'category': biometric.biochemical.category.name,
#                 }
            
#             biometrics_data_dict[bio_name]['values'].append({
#                 'value': biometric.value,
#                 'scaled_value': biometric.scaled_value,
#                 'expired_date': biometric.expired_date,
#                 'created': biometric.biometricsentry.created
#             })

#         # Convert the dictionary to the desired list format
#         biometrics_data_list = [{name: data} for name, data in biometrics_data_dict.items()]
        
      
        
#         # Process health scores data
#         health_scores_data = [
#             {
#                 'id': entry.id,
#                 'health_score': entry.health_score,
#                 'created': entry.created,
#             }
#             for entry in biometrics_entries
#         ]

#         biochemicals = Biochemical.objects.prefetch_related(
#             Prefetch(
#                 'biometrics',
#                 queryset=Biometrics.objects.filter(biometricsentry__user=user).order_by('biochemical_id', 'created'),
#                 to_attr='user_biometrics'
#             )
#         )

        
#         latest_biometrics_data = []
#         conditions = set()
#         time_now = timezone.now()
#         for biochemical in biochemicals:
#             if biochemical.user_biometrics:
#                 latest_biometric = biochemical.user_biometrics[-1]  
#                 latest_biometrics_data.append({
#                     'biochemical': {
#                         'name': biochemical.name,
#                         'id': biochemical.id,
#                         'category': biochemical.category.name,
#                     },
#                     'value': latest_biometric.value,
#                     'scaled_value': latest_biometric.scaled_value,
#                     'expired_date': latest_biometric.expired_date,
#                 })
                
#                 if latest_biometric.expired_date > time_now:
#                     if latest_biometric.scaled_value < -1:
#                         conditions.update(
#                             BiochemicalCondition.objects.filter(
#                                 biochemical=biochemical,
#                                 is_hyper=False
#                             ).values_list('condition__name', flat=True)
#                         )
#                     elif latest_biometric.scaled_value > 1:
#                         conditions.update(
#                             BiochemicalCondition.objects.filter(
#                                 biochemical=biochemical,
#                                 is_hyper=True
#                             ).values_list('condition__name', flat=True)
#                         )
#             else:
#                 latest_biometrics_data.append({
#                     'biochemical': {
#                         'name': biochemical.name,
#                         'id': biochemical.id,
#                         'category': biochemical.category.name,
#                     },
#                     'value': None,
#                     'scaled_value': None,
#                     'expired_date': None,
#                 })
        
#         return {
#             'user': UserSerializer(user).data,
#             'biometrics': biometrics_data_list,
#             'latest_biometrics': latest_biometrics_data,
#             'food_scores': FoodScoreSerializer(food_scores, many=True).data,
#             'health_score': health_scores_data,
#             'conditions': list(conditions)
#         }, None

#     except Exception as exc:
#         logger.exception(f"Error fetching user biometrics entry details: {exc}")
#         return None, 'Error fetching user biometrics entry details.'


# {
#     "e688ccc2-e824-4779-a8f3-8abf76be6e8a": 92,
#     "18e86132-bc91-4e9d-9f61-16211748456e": 5.2,
#     "4c928c60-3f2d-4ab5-b988-3d7b884dd213": 14.5,
#     "92577cc9-a183-44a3-9360-d3bf9a9676f2": 215,
#     "fdba59e8-fbe8-4046-b085-826d85d3a6f7": 130,
#     "ae125f69-ac7a-434d-bf70-12d36d19d1a9": 55,
#     "2d506c51-4236-47b9-b76c-153bdda92878": 165,
#     "3a38d8c5-2437-43fc-8fc7-8bafb453c9b2": 180,
#     "51dc1d42-5b21-464a-995f-625ef0d70af8": 95,
#     "2de8368f-7173-45e2-9213-6b8aba4ceced": 18,
#     "26af4f7c-9325-4319-9936-35dd8acaab82": 12,
#     "5e1dc5d0-c952-4390-9048-1a89842ff17a": 1.8,
#     "e5acb0b2-1b66-4bf7-9c68-3d1a16975867": 30,
#     "6a7f5c17-03ad-48f3-b080-ba986d6d48eb": 135,
#     "e7bc258f-c313-462b-9fcc-58a05f443b22": 22,
#     "fb0b6ca3-9899-4e1a-a857-8e35c2ee8c1f": 28,
#     "6dcd1df2-83ac-454c-8d6e-b60af77ff36a": 550,
#     "3ad9a810-64a7-4637-be15-b95a0046cd50": 650,
#     "b7bc20d7-dc48-4c2a-a241-93eb5b531c49": 10,
#     "964308da-b544-42f3-84e1-87295006caee": 450,
#     "e151ec7d-78f4-4f7c-94df-fa3969d30a73": 48,
#     "9e883b1b-762d-4118-8513-53c648c0fd26": 0.8,
#     "aa4d71c3-1800-482e-8761-9a55dcee5ee5": 4.5,
#     "bae689f6-961e-435a-b422-48aecbc2cf4b": 15,
#     "69732240-22a1-45cb-a5ef-705e36866fb0": 0.75,
#     "55b031e1-2bb4-4848-81b3-2a50607ba4c9": 142,
#     "f016039b-9715-4d13-bd2d-8b2c3631aa00": 4.2,
#     "66e51ff0-3249-43ec-a3d1-119def4d0bf8": 9.5,
#     "ecefcf3d-b9b6-4c85-a0c1-7f35942bc6e4": 2.0,
#     "aeb1b7bf-1578-4965-a4fb-0813aa558054": 3.5,
#     "ea10602e-aa51-410f-bb11-35a813908f69": 102,
#     "a0885ab5-21a3-4c34-889a-9bbfc9ee8c9d": 26,
#     "2cfae71e-9493-4e1f-9e5f-6dd23bb7e79d": 35,
#     "3c1a5fbe-4aa9-4883-bf5c-ed1373d27461": 2.8,
#     "68a6627d-aa68-4044-b70a-265a3269c50e": 4.2,
#     "b8d4549f-6bd1-4c0d-84a3-949b8a23fc46": 7.0,
#     "87ccff8f-7bc1-43af-8004-c9ae5bb584c9": 1.5,
#     "e64550b5-8f66-47ff-b406-6dab801fc054": 4.5,
#     "9b1450f5-ff2d-4910-b40a-e141a0a7ef8c": 120,
#     "8ae36c0d-a0c3-4b81-b21a-3b21b0fa3a8a": 280,
#     "182aa161-62d8-4796-a8c4-6e45ab3620f9": 2.5,
#     "c3e7e245-b6e6-48d1-a0d8-1dd01f1c9fc1": 42,
#     "53c6f4a6-a5f7-4d96-8bfd-13af545b59aa": 180,
#     "cbf25f52-0eee-4b01-a1ea-a2273d390a9f": 12,
#     "14afc68d-a231-481a-a15b-0a970296cdd8": 15,
#     "fd0703cf-d0ae-41c8-9318-4acf1edcac1d": 9,
#     "6e9005ea-769f-4a39-8f40-f7f13240b034": 2.8,
#     "7e1eaf27-19fa-4374-a43f-e8f1ab35a289": 1.3,
#     "5f526fc3-091f-4451-9f12-ef0f714e9aab": 3.5,
#     "779d083f-49a3-4014-9ef8-d8d0c3a427d6": 25,
#     "79463132-f07f-4186-9d8d-f76d307ea131": 22,
#     "188a6d12-7679-4587-a71a-16aa0c60af56": 75,
#     "7ecc9010-1ed6-4101-b4b8-0a337f69836d": 20,
#     "57178a78-3dea-4aad-be8b-1a67db563c7e": 0.8,
#     "2449bc09-60fe-460d-a5ac-ba55e1cb2116": 210,
#     "be04edb2-7649-4274-9680-a53a6f5fe853": 12.5,
#     "74b1287b-84f1-4783-bd0c-e3a7c52a9d8c": 30,
#     "9450eeb7-696b-4b32-91e9-af9b62272b71": 300
# }