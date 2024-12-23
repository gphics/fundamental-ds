import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.weightstats import ztest

x = pd.read_csv("data.csv")
y = ttest_1samp(x["releaseYear"], 1991.8, alternative="two-sided")
print("T-TEST", y)

z = ztest(x["releaseYear"], value=1991.8)
print("Z-TEST", z)
