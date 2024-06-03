import pandas as pd

series_data = [10,15,20,25]
ser = pd.Series(series_data)

# print(ser)
dataframe_data = ([
    [100, "a", True],
    [200, "b", False],
    [150, "d", False],
    [550, "c", True]
])

df = pd.DataFrame(dataframe_data)
df.index=["01","02","03","04"]
df.columns=["A","B","C"]

print(df[['A', 'B']])
