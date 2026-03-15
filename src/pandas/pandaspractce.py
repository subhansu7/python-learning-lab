import pandas as pd

#basketball = pd.read_csv("../../data/ml/basketball.csv")
basketball = pd.read_csv("../../data/ml/nba_all_seasons.csv")
#print first 5 rows of the dataset
print("First 5 rows of the dataset :")
print(basketball.head())

#print memory location of the dataset
print("Memory location of the dataset :")
print(id(basketball))

#print column names of the dataset
print("Column names of the dataset :")
print(basketball.columns)

#print number of columns in the dataset
print("Number of columns in the dataset :")
print(len(basketball.columns))

#print summary of the dataset
print("Summary of the dataset :")
print(basketball.info())

#print shape of the dataset
print("Shape of the dataset :")
print(basketball.shape)

#check for missing values in the dataset. Count null values in each column.
print("Missing values in the dataset :")
#isnull() function returns a boolean DataFrame where True indicates missing values 
#and False indicates non-missing values.
print(basketball.isnull())
#count number of missing values in each column
print(basketball.isnull().sum())

#check column - college where data is missing
print("Missing values in the column 'college' :")
print(basketball['college'].isnull())

#count number of missing values in the column 'college'
print("Number of missing values in the column 'college' :")
print(basketball['college'].isnull().sum())

#print rows where player_name is Gheorghe Muresan
print("Rows where player_name is Gheorghe Muresan :")
print(basketball[basketball['player_name'] == 'Gheorghe Muresan']['college'])

#isna() function is an alias for isnull() function. It returns a boolean DataFrame where True indicates missing values and False indicates non-missing values.
print("Missing values in the column 'college' using isna() function :") 
print(basketball['college'].isna())
print("Number of missing values in the column 'college' using isna() function :")
print(basketball['college'].isna().sum())

#print summary statistics of the dataset
print("Summary statistics of the dataset :")
print(basketball.describe())