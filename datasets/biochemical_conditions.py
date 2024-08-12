import pandas as pd
from data.biochemicals_conditions_data import biochemicals_conditions

biochemical_units_df = pd.read_csv("csv/biochemical_units.csv")
biochemical_conditions_df = biochemical_units_df[['name']].copy()

# Collect all unique conditions
conditions = set()
for biochemical, data in biochemicals_conditions.items():
    conditions.update(data['hypo_conditions'])
    conditions.update(data['hyper_conditions'])

# Initialize a dictionary to hold the new columns
new_columns = {condition: 0 for condition in conditions}

# Create a DataFrame from the dictionary
conditions_df = pd.DataFrame(new_columns, index=biochemical_conditions_df.index)

# Concatenate the new columns to the original DataFrame
biochemical_conditions_df = pd.concat([biochemical_conditions_df, conditions_df], axis=1)

# Fill in the values for hypo and hyper conditions
for biochemical, data in biochemicals_conditions.items():
    hypo = data['hypo_conditions']
    for nutrient in hypo:
        biochemical_conditions_df.loc[biochemical_conditions_df['name'] == biochemical, nutrient] = -1
    hyper = data['hyper_conditions']
    for nutrient in hyper:
        biochemical_conditions_df.loc[biochemical_conditions_df['name'] == biochemical, nutrient] = 1

biochemical_conditions_df.to_csv("csv/biochemical_conditions.csv", index=False)