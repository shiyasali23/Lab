import  pandas as pd
from dataset.user_data import user_1

biochemicals_df = pd.read_csv("dataset/biochemical_units_nutrients.csv")

def scale_biometrics(healthy_min, healthy_max, i):
    optimum_value = (healthy_min + healthy_max) / 2
    if healthy_min <= i <= healthy_max:
        return round(2 * (i - optimum_value) / (healthy_max - healthy_min), 2)
    elif i < healthy_min:
        return round((i - healthy_min) - 1, 2)
    elif i > healthy_max:
        return round((i - healthy_max) + 1, 2)

scaled_user = user_1.copy()

for biom_name, biom_data in scaled_user["biometrics"].items():
    biochemical_info = biochemicals_df[biochemicals_df["name"] == biom_name]
    if not biochemical_info.empty:
        healthy_min = biochemical_info[f"{scaled_user['gender']}_Min"].values[0]
        healthy_max = biochemical_info[f"{scaled_user['gender']}_Max"].values[0]
        scaled_value = scale_biometrics(healthy_min, healthy_max, biom_data["value"])
        scaled_user["biometrics"][biom_name]["scaled_value"] = scaled_value

# Sort biometrics by scaled_value
scaled_user['biometrics'] = dict(sorted(scaled_user['biometrics'].items(), key=lambda item: item[1]['scaled_value']))
hypo_biochemicals = [i for i, j in scaled_user["biometrics"].items() if j["scaled_value"] < 0]
hyper_biochemicals = [i for i, j in scaled_user["biometrics"].items() if j["scaled_value"] > 0]

biochemical_nutrients_df = pd.read_csv("dataset/biochemical_nutrients.csv")
def picking_increasing_decreasing(user_data, biochemicals, df):
    increasing_list = []
    decreasing_list = []

    for biochemical in biochemicals:
        pos_list = df.columns[df.loc[df['name'] == biochemical].eq(1).any()].tolist()
        neg_list = df.columns[df.loc[df['name'] == biochemical].eq(-1).any()].tolist()

        for nutrient in pos_list:
            increasing_list.append({nutrient: user_data['biometrics'][biochemical]['scaled_value']  * -1})

        for nutrient in neg_list:
            decreasing_list.append({nutrient: user_data['biometrics'][biochemical]['scaled_value']})

    return increasing_list, decreasing_list

hypo_increasing_nutrients, hypo_decreasing_nutrients = picking_increasing_decreasing(user_1,
    hypo_biochemicals, biochemical_nutrients_df
)
hyper_increasing_nutrients, hyper_decreasing_nutrients = picking_increasing_decreasing(user_1,
    hyper_biochemicals, biochemical_nutrients_df
)

def add_nutrients(nutrients_list):
    result = {}
    for item in nutrients_list:
        for key, value in item.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
combined_nutrients = hypo_increasing_nutrients + hypo_decreasing_nutrients + hyper_increasing_nutrients + hyper_decreasing_nutrients
def combine_values(combined_nutrients):
    weighted_combined_nutrients = {}

    for nutrient_dict in combined_nutrients:
        for nutrient, value in nutrient_dict.items():
            if nutrient in weighted_combined_nutrients:
                weighted_combined_nutrients[nutrient] += value
            else:
                weighted_combined_nutrients[nutrient] = value

    return weighted_combined_nutrients
weighted_combined_nutrients = combine_values(combined_nutrients)
biochemical_food_df = pd.read_csv("dataset/food_biochemicals.csv")
def get_increasing_decreasing_foods(biochemicals, biochemical_food_df, user_biometrics):
    increasing_foods = []
    decreasing_foods = []

    for biochemical in biochemicals:
        foods_increase = biochemical_food_df[biochemical_food_df[biochemical] == 1]["name"].tolist()
        for food in foods_increase:
            increasing_foods.append({food: user_biometrics[biochemical]['scaled_value'] * -1 })


        foods_decrease = biochemical_food_df[biochemical_food_df[biochemical] == -1]["name"].tolist()
        for food in foods_decrease:
            decreasing_foods.append({food: user_biometrics[biochemical]['scaled_value']})

    return increasing_foods, decreasing_foods

hyper_increasing_foods, hyper_decreasing_foods = get_increasing_decreasing_foods(
    hyper_biochemicals, biochemical_food_df, user_1['biometrics']
)

hypo_increasing_foods, hypo_decreasing_foods = get_increasing_decreasing_foods(
    hypo_biochemicals, biochemical_food_df, user_1['biometrics']
)
combined_foods = hypo_increasing_foods + hypo_decreasing_foods + hyper_increasing_foods + hyper_decreasing_foods
weighted_combined_foods = combine_values(combined_foods)

food_nutrients_df = pd.read_csv("dataset/food_nutrients.csv")

# Initialize an empty list to store the results
food_score = []

# Get the keys of the weighted_combined_nutrients
weighted_combined_nutrients_keys = list(weighted_combined_nutrients.keys())

# Iterate through each row in the DataFrame
for index, row in food_nutrients_df.iterrows():
    food_name = row['name']
    food_bias = weighted_combined_foods.get(food_name, 0)  # Get the food bias score or default to zero
    nutrient_weights = {}

    # Retain Id, Category, and Sub_Category
    nutrient_weights['category'] = row['category']
    nutrient_weights['sub_category'] = row['sub_category']
    nutrient_weights['name'] = food_name

    nutrient_sum = 0

    for nutrient, value in row.drop(['category', 'sub_category', 'name']).items():
        if nutrient in weighted_combined_nutrients_keys:
            weight = value * weighted_combined_nutrients[nutrient]
        else:
            weight = 0  # Set weight to 0 if nutrient is not in the keys
        nutrient_weights[nutrient] = weight
        nutrient_sum += weight

    # Calculate the total score by summing the nutrient weights and adding the food bias
    total_score = nutrient_sum + food_bias

    # Append the food bias and total score to the nutrient weights
    nutrient_weights['bias'] = food_bias
    nutrient_weights['score'] = total_score

    # Append the nutrient weights dictionary to the list
    food_score.append(nutrient_weights)

# Convert the list to a DataFrame
food_score_df = pd.DataFrame(food_score)
food_score_df = food_score_df.sort_values(by='score')

# food_score_df.to_csv('dataset/user_1_food_score.csv')

sorted_scaled_biometrics = sorted(scaled_user['biometrics'].items(), key=lambda x: x[1]['scaled_value'])
x = food_nutrients_df['name'].to_list()
print(x)