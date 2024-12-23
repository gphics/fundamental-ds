import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ggds/titanic.csv")
# df = pd.read_csv("./titanic.csv")
cat_data = [cat for cat in df.columns if df[cat].dtype == "object"]
num_data = [num for num in df.columns if df[num].dtype != "object"]
# print(cat_data)
# print(num_data)

df1 = df.drop(columns=["Name", "Ticket"])
x = round(df1.isnull().sum() * 100 / df1.shape[0])
df2 = df1.drop(columns=["Cabin"])
df3 = df2.fillna(df2.Age.mean())
y = round(df3.isnull().sum() * 100 / df3.shape[0])
# print(y)

# plt.boxplot(df3["Age"], vert=False)
# plt.ylabel("Variable")
# plt.xlabel("Age")
# plt.title("Age Box Plot")
# plt.show()

age_mean = df3["Age"].mean()
age_std = df3["Age"].std()

print(
    f"""
      
      MEAN: {age_mean}
      STD: {age_std}
      """
)
age_lb = age_mean - age_std * 2
age_ub = age_mean + age_std * 2
print(
    f"""
      
      LB: {age_lb}
      UB: {age_ub}
      """
)
