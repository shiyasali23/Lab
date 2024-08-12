from data.biochemical_units_data import biochemicals_units
import pandas as pd

flatten_data = []

for biochemichals, data in biochemicals_units.items():
  row = {}
  row['name'] = biochemichals
  row['category'] = data['category']
  row['unit'] = data['unit']
  row['female_Min'] = data['healthy_range_female'][0]
  row['female_Max'] = data['healthy_range_female'][1]
  row['male_Min'] = data['healthy_range_male'][0]
  row['male_Max'] = data['healthy_range_male'][1]
  flatten_data.append(row)

biochemical_units_df = pd.DataFrame(flatten_data)
biochemical_units_df.to_csv("csv/biochemical_units.csv", index=False)