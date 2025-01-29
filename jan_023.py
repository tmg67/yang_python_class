import pandas as pd

data1 ={
    "id": [1,2,3],
    "name":["alice", "bob", "charlie"]

}

data2 ={
    "id":[2, 3, 4],
    "Score":[85, 90, 80]

}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
 #merge the two dataframes on the ID column
merged_df = pd.merge(df1, df2, on="id", how="inner")
print("merged dataframe:")
print(merged_df)