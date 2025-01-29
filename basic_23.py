import pandas as pd

data = {
    "name":["alice", "bob", "hari", "david"],
    "score":[85, 92, 88, 75]

}

df = pd.DataFrame(data)

#sort by score in descending order
sorted_df = df.sort_values(by='score', ascending=False)
print("dataframe sorted by score")
print(sorted_df)

#add a rank column
df["rank"]=df["score"].rank(ascending=False)
print("\ndataframe with rank:")
print(df)
