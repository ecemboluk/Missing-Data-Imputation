import data

df = data.data

# print(df.head())
# print(pd.isnull(df).sum())

# Remove missing value
df_re = df.dropna(axis=0)

# Change missing value with 0
df["total_bill"] = df["total_bill"].fillna(0)
df["size"] = df["size"].fillna(0)

# print(df)