import pandas as pd
import os
from data.biochemical_nutrients_weights_data import biochemical_nutrients_weights

biochemical_nutrients_weights_df = pd.DataFrame(biochemical_nutrients_weights).T
biochemical_nutrients_weights_df = biochemical_nutrients_weights_df.reset_index()
biochemical_nutrients_weights_df = biochemical_nutrients_weights_df.rename(columns={'index': 'name'})

biochemical_nutrients_weights_df.to_csv(os.path.join("csv", "biochemical_nutrients_weights.csv"), index=False)
