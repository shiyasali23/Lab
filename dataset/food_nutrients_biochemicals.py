import pandas as pd
from foods_data import fruit, vegetable, seed, seafood, meat, dairy, nosh,biochemichals_fruits, biochemichals_vegetables, biochemicals_seeds, biochemicals_seafoods, biochemicals_meats, biochemicals_diarys, biochemicals_nosh

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
nutrient_columns = food_nutrients_df.columns.difference(['name', 'category', 'sub_category'])
food_nutrients_df[nutrient_columns] = food_nutrients_df[nutrient_columns].astype('float16')
# food_nutrients_df.to_csv('food_nutrients.csv')

#---------------------------------------------------------------

biochemical_categories = {
    'fruits': biochemichals_fruits,
    'vegetables': biochemichals_vegetables,
    'seeds': biochemicals_seeds,
    'seafoods': biochemicals_seafoods,
    'diarys': biochemicals_diarys,
    'meats': biochemicals_meats,
    'nosh': biochemicals_nosh
}

# Create initial DataFrame
names_list = food_nutrients_df[['name']].values.tolist()
biochemicals_list = list(biochemicals_nosh.keys())
food_biochemicals_df = pd.DataFrame(names_list, columns=['name'])

# Initialize columns with zeros
for biochemical in biochemicals_list:
    food_biochemicals_df[biochemical] = 0


# Function to update DataFrame based on biochemical data
def update_biochemical_data(df, biochemical_data):
    for category, biochemicals in biochemical_data.items():
        for biochemical, data in biochemicals.items():
            increasing = data.get('increasing', [])
            decreasing = data.get('decreasing', [])

            df.loc[df['name'].isin(increasing), biochemical] = 1
            df.loc[df['name'].isin(decreasing), biochemical] = -1


# Update DataFrame for all categories
update_biochemical_data(food_biochemicals_df, biochemical_categories)

food_biochemicals_df.to_csv('food_biochemicals.csv')
