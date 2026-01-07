import pandas as pd

# Step 1: Create sample data
data = {
    'Name': ['Amit', 'Neha', 'Amit', 'Ravi', None],
    'Age': [22, None, 22, 25, 30],
    'Score': [65, 45, 65, None, 90]
}

df = pd.DataFrame(data)

print(df)
print("-" * 10)

# Step 2: Count missing values
print("Missing values count:")
print(df.isna().sum())
print("-" * 10)

# Step 3: Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())
df['Name'] = df['Name'].fillna("Unknown")

# Step 4: Remove duplicate rows based on Name and Age
df_cleaned = df.drop_duplicates(subset=['Name', 'Age'])
print(df_cleaned)
