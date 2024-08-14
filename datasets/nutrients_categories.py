import pandas as pd 
from data.food_nutrients_data import fruit

flattened_nutrients = []
seen_nutrients = set()  # Initialize a set to keep track of unique nutrient entries

for food_category, data in fruit.items():
    for food_name, nutrients_dict in data.items():
        for nutrient_category, nutrient_info in nutrients_dict.items():
            for nutrient_name, nutrient_value in nutrient_info.items():
                # Create a tuple of (name, category) for uniqueness check
                nutrient_entry = (nutrient_name, nutrient_category)

                # Check if the nutrient entry is already in the set
                if nutrient_entry not in seen_nutrients:
                    # If not seen before, add it to the set and the list
                    seen_nutrients.add(nutrient_entry)
                    flattened_nutrients.append(
                        {
                            'name': nutrient_name,
                            'category': nutrient_category
                        }
                    )

# Convert the list to a DataFrame
nutrients_categories_df = pd.DataFrame(flattened_nutrients)
nutrients_categories_df.to_csv('csv/nutrients_categories.csv', index=False)