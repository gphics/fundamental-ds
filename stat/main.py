from scipy.stats import norm, chi2_contingency
import numpy as np
from sklearn.datasets import load_diabetes
import pandas as pd
# mean = 78
# std  =25
# total_pop = 100
# target_score = 60

# z_score = (target_score - mean) / std

# prob = norm.cdf(z_score)

# percent = prob*100


# Pearson's Chi Square Test
# data = [[207, 282, 241], [234, 242, 232]]

# stat, p, x,y = chi2_contingency(data)
# print(p)


# Correlation coeficient
# x = np.array([1, 3, 5, 7, 8, 9, 10, 15])
# y = np.array([10, 20, 30, 40, 50, 60, 70, 80])


# cor = np.corrcoef(x,y)
# print(cor)

df = load_diabetes(as_frame=True)

df = df.frame
cor = np.corrcoef(df["age"], df["bp"])
print(cor)