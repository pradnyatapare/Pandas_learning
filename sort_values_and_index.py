import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Arya", "Pradnya", "Aditya", "Neha"],
    "Age": [23, 21, 25, 22],
    "Score": [88, 92, 85, 90]
}

df = pd.DataFrame(data)

print(df)
print("-" * 40)

# Sort by column values (Age - ascending)
df_sorted_age = df.sort_values(by="Age")
print("Sorted by Age (Ascending):")
print(df_sorted_age)
print("-" * 40)

# Sort by column values (Score - descending)
df_sorted_score = df.sort_values(by="Score", ascending=False)
print("Sorted by Score (Descending):")
print(df_sorted_score)
print("-" * 40)

# Sort by multiple columns
df_sorted_multi = df.sort_values(
    by=["Age", "Score"],
    ascending=[True, False]
)
print("Sorted by Age (Asc) and Score (Desc):")
print(df_sorted_multi)
print("-" * 40)

# Sort by index (ascending)
df_sorted_index = df.sort_index()
print("Sorted by Index (Ascending):")
print(df_sorted_index)
print("-" * 40)

# Sort by index (descending)
df_sorted_index_desc = df.sort_index(ascending=False)
print("Sorted by Index (Descending):")
print(df_sorted_index_desc)
print("-" * 40)

# Set Name as index and sort index
df_indexed = df.set_index("Name")
print("DataFrame with Name as Index:")
print(df_indexed)
print("-" * 40)

df_sorted_name_index = df_indexed.sort_index()
print("Sorted by Name Index:")
print(df_sorted_name_index)
