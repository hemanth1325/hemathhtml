import numpy as np
import pandas as pd
H = [0, 0, 0, 0, 0, 0]
df = pd.read_csv("finds.csv", sep=",", header=None)
print(df)
attribute = np.array(df)[:, :-1]
print(attribute)
target = np.array(df)[:, -1]
print(target)
for i in range(len(df)):
    for j in range(len(df.columns) - 1):
        if df.iloc[i, -1] == "Yes":
            if H[j] == 0:
                H[j] = df.iloc[i, j]
            elif df.iloc[i, j] != H[j]:
                H[j] = '?'
print(H)