#pandas 
#data manipulation and analysis
#series (one dimensional) liek list or column in a spread sheet
#dataframe (two dimensional) numpy pandas ma use gari rako nai hunxa
#key features( handling missing data, filtering,sorting and grouping data)
#commanly used  functions
#pd.read_csv: 
import pandas as pd

#create a dataframe from dictionary
data ={
    "Name":["alice", "bob", "charlie"],
    "Age": [25,30,35],
    "City": ["New york", "Los angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("dataframe:")
print(df)

#read data from a CSV file
#(assume 'data.csv) exists in the current directory)
#df = pd.read_csv("data.csv")

#display the first few rows ogf the data frame
print("\nFirst 2 rows:")
print(df.head(2))

#filter rows where age>25
filtered_df = df[df["Age"]>25]
print("\nFiltered adtaframe:")
print(filtered_df)

#add anew columnn
df["score"] = [85, 90, 88]
print("\ndataframe with new column:")
print(df)

#save the dataframe
df.to_csv("output.csv", index=False)
print("\n data savedo output.csv")