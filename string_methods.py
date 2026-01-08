import pandas as pd

data = {
    "Name": [" Arya ", "pradnya", "ADITYA", None],
    "City": ["Pune", "Mumbai", "Delhi", "Pune"],
    "Score": ["85", " 90 ", "78", None]   # score as string
}

df = pd.DataFrame(data)

# Convert name to uppercase
df["Name_upper"] = df["Name"].str.upper()

# Convert name to lowercase
df["Name_lower"] = df["Name"].str.lower()

# Remove extra spaces
df["Name_stripped"] = df["Name"].str.strip()

# Length of name strings
df["Name_length"] = df["Name"].str.len()

# Strip score and convert to integer
df["Score_clean"] = df["Score"].str.strip()
df["Score_int"] = pd.to_numeric(df["Score_clean"], errors="coerce")

# Check if city starts with 'P'
df["City_starts_P"] = df["City"].str.startswith("P")

# First character of name
df["First_char"] = df["Name"].str.strip().str[0]
print(df)