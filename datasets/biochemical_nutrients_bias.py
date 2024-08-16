import pandas as pd
from data.biochemical_nutrients_bias_data import biochemicals_nutrients_bias

biochemical_units_df = pd.read_csv("csv/biochemical_units.csv")
food_nutrients_df = pd.read_csv("csv/food_nutrients.csv")
biochemical_nutrients_bias_df = biochemical_units_df[['name']].copy()

nutrients = food_nutrients_df.columns.difference(['name','category','sub_category', 'nutriscore'])

for nutrient in nutrients:
  biochemical_nutrients_bias_df[nutrient] = 0

for biochemical, data in biochemicals_nutrients_bias.items():
  increasing = data['increasing_nutrients']
  for nutrient in increasing:
      biochemical_nutrients_bias_df.loc[biochemical_nutrients_bias_df['name'] == biochemical, nutrient] = 1
  decreasing = data['decreasing_nutrients']
  for nutrient in decreasing:
      biochemical_nutrients_bias_df.loc[biochemical_nutrients_bias_df['name'] == biochemical, nutrient] = -1


biochemical_nutrients_bias_df.to_csv("csv/biochemical_nutrients_bias.csv", index=False)