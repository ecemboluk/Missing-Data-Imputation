import numpy as np
import data

df = data.data

# Dataframe for mean, median and mod
df_mean =df
df_median = df
df_mod = df

# For mean
df_mean["total_bill"] = df_mean["total_bill"].fillna(np.mean(df_mean["total_bill"]))
df_mean["size"] = df_mean["size"].fillna(np.mean(df_mean["size"]))

# For median
df_median["total_bill"] = df_median["total_bill"].fillna(np.median(df_median["total_bill"]))
df_median["size"] = df_median["size"].fillna(np.median(df_median["size"]))

# For Mode
mode_total_bill = df["total_bill"].mode()
mode_size = df["size"].mode()

df_mod["total_bill"] = df_mod["total_bill"].fillna(mode_total_bill[0])
df_mod["size"] = df_mod["size"].fillna(mode_size[0])

print(df_mod)
