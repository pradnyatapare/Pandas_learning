import pandas as pd
import numpy as np
#creating emty dataframe
df = pd.DataFrame()
print(pd)

#creating  Dataframe form List
list = ["pradnya","Ashmit","Anushka","Hitesh"]
df2 = pd.DataFrame(list) 
print(df2)

#creating Dataframe from NumPy Array
#This argument explicitly provides a list of labels for the columns in the resulting DataFrame
arr = np.array([["Anushka",67],["Ashmit",90],["pradnya",89]])
df3 = pd.DataFrame(arr, columns=['Name','Score'])
print(df3)

#creating Dataframe from List of Dictionaries
dict = {
    'Name' : ["pradnya","Hitesh","Anuradha"],
    'Section' : ['A','B','c'],
    'Score' : [98,89,87]
}
df4 = pd.DataFrame(dict)
print(df4)
