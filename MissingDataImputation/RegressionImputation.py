import pandas as pd
import data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = data.data

# Firstly we let add 0 to missing value.
df_corr = df.dropna(axis=0)

# We let analyze relationship together features
corr = df_corr.corr()
# print(corr)

# create s subset of data where there are no missing values in the tip and total_bill variable
df_bill_tip = df.dropna(axis=0, subset=['total_bill', 'tip'])
df_bill_tip = df_bill_tip.loc[:, ['total_bill', 'tip']]

# find the entries with total_bill missing
missing_bill = df['total_bill'].isnull()
# extract the tips of observations with total bill missing
tip_missbill = pd.DataFrame(df['tip'][missing_bill])

X = df_bill_tip[['tip']]
Y = df_bill_tip[['total_bill']]

# train a linear model regressing total_bill on tip using 80% training 20% testing
X_train, X_text, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# fit a linear model
lm = LinearRegression().fit(X_train, Y_train)

# use fitted model and tip values to predict miisng total_bill
bill_pred = lm.predict(tip_missbill)

print(bill_pred)