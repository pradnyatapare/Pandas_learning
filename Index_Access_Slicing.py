import pandas as pd
data = {
    'Name' : ["Arya","Pradnya","Aditya"],
    'Age' : [34,56,78],
    'Score' : [34,56,78]
}
df = pd.DataFrame(data)
print(df)
print("-------------")
#acces coloum
col = df["Name"]
print(col)
print("-------------")
#use set_index() to set custom index
df2 = df.set_index("Name")
print(df2)
print("-------------")
#use reset_index to reset index
df3 = df.reset_index()
print(df3)
print("-------------")
#use loc[] to access rows and colowms using their lables
column = df.loc[1]
print(column)
print("-------------")
row = df.loc[1,"Name"]
print(row)
print("-------------")
#iloc[] is used to access using position
column1 = df.iloc[1]
print(column1)
print("-------------")
row2 = df.iloc[1,2]
print(row2)
print("-------------")
#slicing using loc[] and iloc[]
slice1 = df.loc[0:1 ,["Name","Age"]]#stop included
print(slice1)
print("-------------")
slice2 = df.iloc[0:1,0:1]#stop excluded
print(slice2)
print("-------------")




