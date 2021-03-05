import numpy as np
import seaborn as sb

# Preparing Data

tips = sb.load_dataset(("tips"))

# use a subset of the data for demonstration
data = tips.loc[:,["total_bill", "size", "tip"]]

# introduce random NA's in size variable(discrete) and total_bill variable(continuous)
data.loc[0:20, 'size'] = np.nan
data.loc[220:230, "total_bill"] = np.nan

# print(pd.isnull(data).sum())