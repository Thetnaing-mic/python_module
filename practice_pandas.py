import pandas as pd

# series_data = [10,15,20,25]
# ser = pd.Series(series_data)

# # print(ser)
# dataframe_data = ([
#     [100, "a", True],
#     [200, "b", False],
#     [150, "d", False],
#     [550, "c", True]
# ])

# df = pd.DataFrame(dataframe_data)
# df.index=["01","02","03","04"]
# df.columns=["A","B","C"]

df = pd.read_csv("./titanic.csv")

# print(df[["Age", "Name"]])
# print(df[0:10])
# print(df.loc[2:5])

# print(df["Age"]>=30) 
# print(df[df["Age"].isin([20,30,40])])
# sorted_df = df.sort_values("PassengerId", ascending=False)

# 問題
# 1
# print(df["Age"], ["Gender"], ["Pclass"], ["Fare"], ["Survived"])
# print(df.loc[[Age], [Gender], [Pclass], [Fare], [Survived]])

# 2
# df = df.dropna(how="any")
# print(df)

# # 3
# print(df["Fare"].max())
# print(df["Fare"].min())

# # 4
print(len(df[df["Age"] < 30]))

# # 5
# print(df.sort_values("Pclass", ascending=False))

# # 6
# print(df[df["Survived"] == 1].groupby("Gender").count())

# # 7
# print(df.groupby("Gender")["Age"].mean())

