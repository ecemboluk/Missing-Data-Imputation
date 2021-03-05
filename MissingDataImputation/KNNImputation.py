import pandas as pd
import data

from sklearn.neighbors import KNeighborsClassifier

df = data.data

df_na = df.dropna(axis=0)
# we use k=3 for knn
# By weights = 'distance', we weight points by the inverse of their distance giving closer neighbors great influences
knn = KNeighborsClassifier(3, weights='distance')

# We use the data with compate data analysis for training KNN
model = knn.fit(df_na.loc[:, ['total_bill', 'tip']], df_na.loc[:, 'size'])

# Find the missing values in size
missing_size = df['size'].isnull()

# Extract the tips of observations with total_bill missing
df_missing_size = pd.DataFrame(df[['total_bill', 'tip']][missing_size])

# Used trained k = 3 KNN to predict missing size
imputed_size = model.predict(df_missing_size)

# print(imputed_size)
