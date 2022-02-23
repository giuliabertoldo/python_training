import pandas as pd 

df = pd.read_csv("data/gapminder.csv")
df = df.drop(df.columns[[0]], axis=1)
df.head()