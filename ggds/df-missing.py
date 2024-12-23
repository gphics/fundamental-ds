import numpy as np
import pandas as pd

semester_result = [
    ["Surgery", 70],
    ["Anatomy", np.nan],
    ["Biochemistry", 90],
    ["Physiology", np.nan],
    ["Bacteriology", np.nan],
    ["Immunology", 60],
]

df = pd.DataFrame(semester_result, columns=["Course", "Score"])
x = df.dropna(axis=1)
print(x)
