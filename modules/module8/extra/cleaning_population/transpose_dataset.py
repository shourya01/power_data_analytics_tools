import pandas as pd

pd.read_csv('combined_csv.csv', header=None).T.to_csv('rotated_csv.csv', header=False, index=False)
