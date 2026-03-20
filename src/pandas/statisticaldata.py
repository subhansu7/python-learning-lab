import pandas as pd

#basketball = pd.read_csv("../../data/ml/basketball.csv")
basketball = pd.read_csv("../../data/ml/nba_all_seasons.csv")

#print summary statistics of the dataset
print("Summary statistics of the dataset :")
print(basketball.describe())