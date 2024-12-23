import numpy as py
import pandas as pd


footballer_data = [
    ["M.S.Dhoni", 36, 75, 5428000],
    ["A.B.D Villers", 38, 74, 3428000],
    ["V.Kohli", 31, 70, 8428000],
    ["S.Smith", 34, 80, 4428000],
    ["C.Gayle", 40, 100, 4528000],
    ["J.Root", 33, 72, 7028000],
    ["K.Peterson", 42, 85, 2528000],
]


df  = pd.DataFrame(footballer_data, columns= ["Name", "Age", "Weight", "Salary"])

# print("FIRST COLUMN", df.iloc[:, 0])
custom = df.set_index("Age")
print(custom.loc[31:40])