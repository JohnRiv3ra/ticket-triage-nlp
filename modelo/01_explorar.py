#pandas
import pandas as pd

df = pd.read_csv('data/tickets_raw.csv')

print(df.shape)
print(df.columns)
print(df.head(10))
print(df["language"].value_counts())
print(df["priority"].value_counts())
print(df["queue"].value_counts())