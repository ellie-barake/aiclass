import pandas as pd

data_set=pd.read_csv("titanic.csv")
print("first 5 rows of the data_set")
print(data_set.head())
print(data_set.info())
print(data_set.describe())