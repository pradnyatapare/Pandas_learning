import pandas as pd

data = {
    'Name': ['Amit', 'Neha', 'Ravi', 'Priya', 'Kiran'],
    'Age': [22, 17, 25, 19, 30],
    'Score': [65, 45, 80, 55, 90],
    'City': ['Pune', 'Mumbai', 'Pune', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)

print("-------")
result = df[df['Age']>18]
print(result)
print("-------")

result2 = df[df['Score']>60]
print(result2)
print("-------")

result3 = df[df['City']== 'Pune']
print(result3)
print("-------")

result4 = df.loc[df['Age']<20 , 'Name']
print(result4)
print("-------")

result5 = (df['Score']>= 50).sum()
print(result5)

stud = df[(df['Age']>18) & (df['Score']>60)]
print(stud)

stud1 = df[(df['City']=='Pune') | (df['City']=='Mumbai') ]
print(stud1)

stud3 = df.loc[df['Score']>=70 , ['Name','Score']]
print(stud3)

op = df.loc[df['City']=='Mumbai']
print(op)

df.loc[df['Score']<50, 'Score' ]=50
print(df)

df.loc[df['City'] == 'Pune', 'City'] = 'Nagpur'
print(df)


op4 = df.loc[df['Age']>20 , ['Name','Age']]
print(op4)