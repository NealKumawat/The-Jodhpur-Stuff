import pandas as pd
df = pd.read_csv("Naive_Bayes_Theorem/data.csv")
# print(df)
x = df.drop("Pass", axis = 1)
y = df["Pass"]
print(x.shape)
print(y.shape)