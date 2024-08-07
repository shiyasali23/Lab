import pandas as pd
from biochemicals_data import biochemicals, biochemicals_nutrients

# Flatten biochemical data into a list of dictionaries
flatten_biochemicals = [
    {
        'name': biochemichals,
        'category': data['category'],
        'unit': data['unit'],
        'female_Min': data['healthy_range_female'][0],
        'female_Max': data['healthy_range_female'][1],
        'male_Min': data['healthy_range_male'][0],
        'male_Max': data['healthy_range_male'][1]
    }
    for biochemichals, data in biochemicals.items()
]

# Create DataFrame from flattened biochemical data
biochemical_units_df = pd.DataFrame(flatten_biochemicals)

# Extract unique nutrients from biochemicals_nutrients
nutrients = {nutrient for data in biochemicals_nutrients.values() for nutrient in data['increasing_nutrients'] + data['decreasing_nutrients']}

# Create initial biochemical_nutrients_df with zeros
biochemical_nutrients_df = pd.DataFrame({'name': list(biochemicals_nutrients.keys())})
for nutrient in nutrients:
    biochemical_nutrients_df[nutrient] = 0

# Function to update biochemical_nutrients_df
def update_nutrients_df(df, biochemical, data):
    for nutrient in data['increasing_nutrients']:
        df.loc[df['name'] == biochemical, nutrient] = 1
    for nutrient in data['decreasing_nutrients']:
        df.loc[df['name'] == biochemical, nutrient] = -1

# Update biochemical_nutrients_df for each biochemical
for biochemical, data in biochemicals_nutrients.items():
    update_nutrients_df(biochemical_nutrients_df, biochemical, data)

# Combine biochemical_units_df and biochemical_nutrients_df
biochemical_units_nutrients_df = pd.concat([biochemical_units_df, biochemical_nutrients_df.drop(columns=['name'])], axis=1)
# biochemical_units_nutrients_df.to_csv('biochemical_units_nutrients.csv')
# biochemical_nutrients_df.to_csv('biochemical_nutrients.csv')