import numpy as np
import pandas as pd

df = pd.read_csv("ggds/titanic.csv")


df_shape = df.shape

# classifying the data
categorical_df = [c_df for c_df in df.columns if df[c_df].dtypes == "object"]
numerical_df = [n_df for n_df in df.columns if df[n_df].dtypes != "object"]

# checking for missing values
df1 = df.drop(columns=["Name", "Ticket"])
df_r = df1.shape[0]
is_null = round(df1.isnull().sum() / df_r * 100, 2)
# print(is_null)
# df1.dropna(subset = ["Cabin"], axis=1, inplace=True)
df2 = df1.drop(columns=["Cabin"])
df2.dropna(subset=["Embarked"], axis=0, inplace=True)
# filling the age
df3 = df2.fillna(df2.Age.mean())
# print(df3.isnull().sum())
