from django.test import TestCase

# Create your tests here.

# biochemicals = {
#     {
#         name : 'x',
#         id : 1,
#     },
#     {
#         name : 'w',
#         id : 2,
#     },
#     {
#         name : 'z',
#         id : 3,
#     },
# }


# here in biometrics w and x are registered and z not so biometrics should look like this

# biometrics = {
#     {
#         'biochemical':{
#             'name': 'x',
#             'id': 1,
#         }
#         'value' :34,
#         'scaled_value' : 0.34
#     },
#     {
#         biochemical :{
#             'name': 'w',
#             'id': 2,
#         }
#         'value' :4,
#         'scaled_value' : 0.4
#     },
#     {
#         biochemical : {
#         'name': 'z',
#         'id': 3,
#         }
#         'value' : null,
#         'scaled_value' :  null,
#     },
# }

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
