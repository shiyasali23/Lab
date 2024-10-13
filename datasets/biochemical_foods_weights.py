import pandas as pd
import os
from data.biochemical_foods_weights_data import biochemical_foods_weights

biochemical_foods_weights_df = pd.DataFrame(biochemical_foods_weights).T
biochemical_foods_weights_df = biochemical_foods_weights_df.reset_index()
biochemical_foods_weights_df = biochemical_foods_weights_df.rename(columns={'index': 'name'})

biochemical_foods_weights_df.to_csv(os.path.join('csv', 'biochemical_foods_weights.csv'), index=False)
