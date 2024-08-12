
import pandas as pd
from data.biochemical_foods_bias_data import biochemicals_fruits, biochemicals_vegetables, biochemicals_seeds, biochemicals_seafoods, biochemicals_diarys, biochemicals_meats, biochemicals_nosh

food_nutrients_df = pd.read_csv("csv/food_nutrients.csv")

import pandas as pd

biochemical_categories = {
    'fruits': biochemicals_fruits,
    'vegetables': biochemicals_vegetables,
    'seeds': biochemicals_seeds,
    'seafoods': biochemicals_seafoods,
    'diarys': biochemicals_diarys,
    'meats': biochemicals_meats,
    'nosh': biochemicals_nosh
}




# Create initial DataFrame with biochemicals as rows and food items as columns
biochemicals_list = list(biochemical_categories['nosh'].keys())  # Assuming 'nosh' contains all biochemicals
food_items_list = food_nutrients_df['name'].tolist()

# Initialize DataFrame with zeros
biochemical_foods_bias_df = pd.DataFrame(0, index=biochemicals_list, columns=food_items_list)

# Function to update DataFrame based on biochemical data
def update_biochemical_data(df, biochemical_data):
    for category, biochemicals in biochemical_data.items():
        for biochemical, data in biochemicals.items():
            increasing = data.get('increasing', [])
            decreasing = data.get('decreasing', [])
            df.loc[biochemical, df.columns.isin(increasing)] = 1
            df.loc[biochemical, df.columns.isin(decreasing)] = -1

# Update DataFrame for all categories
update_biochemical_data(biochemical_foods_bias_df, biochemical_categories)

# Reset index to include biochemicals as a column
biochemical_foods_bias_df.reset_index(inplace=True)
biochemical_foods_bias_df.rename(columns={'index': 'name'}, inplace=True)

biochemical_foods_bias_df.to_csv("csv/biochemical_foods_bias_df.csv", index=False)
