from data.food_nutrients_data import fruit, vegetable, seed, seafood, meat, dairy, nosh
from data.food_nutriscore_data import food_nutriscore

import os
import pandas as pd

food_nutrients_dict = {
    'fruit': fruit,
    'vegetable': vegetable,
    'seed': seed,
    'seafood': seafood,
    'meat': meat,
    'dairy': dairy,
    'nosh': nosh
}

flattened_foods = []
for category_name, data in food_nutrients_dict.items():
    for sub_category, food in data.items():
        for name, nutrients_dict in food.items():
            row = {
                'name': name,
                'category': category_name,
                'sub_category': sub_category
            }
            for nutrient_subcategory, nutrient_info in nutrients_dict.items():
                for nutrient, nutrient_value in nutrient_info.items():
                    nutrient_key = nutrient
                    row[nutrient_key] = nutrient_value['value']

            flattened_foods.append(row)

food_nutrients_df = pd.DataFrame(flattened_foods)

food_nutrients_df['nutriscore'] = food_nutrients_df.name.map(food_nutriscore)


nutrient_columns = food_nutrients_df.columns.difference(['name', 'category', 'sub_category'])
food_nutrients_df[nutrient_columns] = food_nutrients_df[nutrient_columns].astype('float16')

food_nutrients_df.to_csv(os.path.join("csv", "food_nutrients.csv"), index=False)