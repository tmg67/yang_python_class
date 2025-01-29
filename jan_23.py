import pandas as pd
import numpy as np

data ={
    "Name":["alice", "bob", "charlie","david"],
    "Age": [25,np.nan,30,35],
    "City": ["New york", "Los angeles", "Chicago", None]
}
df = pd.DataFrame(data)
print("original dataframe:")
print(df)
#filling missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("unknown", inplace=True)
print("\ndataframe after filling missing values:")
print(df)

#drops raws with missing values
df = df.dropna()
print("\n dataframe after droppping rows with missing values:")
print(df)

