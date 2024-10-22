import pandas as pd

df = pd.read_csv("username.csv")

print(df.to_string())

print(df.head(2))

print(df.tail(1))