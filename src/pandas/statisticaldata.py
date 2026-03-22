import pandas as pd


vmcloud = pd.read_csv("../../data/ml/vmCloud_data.csv")

#print summary statistics of the dataset
print("Summary statistics of the dataset :")
print(vmcloud.describe())

#print dataset info
print("Info of the dataset :")
print(vmcloud.info())


