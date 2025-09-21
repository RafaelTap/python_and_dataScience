import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# UNITED STATES OF AMERICA PRESIDENTS HEIGHT AVERAGE

data = pd.read_csv("president_height.csv")
heights = np.array(data["height (cm)"])
print(heights)

#using matplotlib
plt.style.use("seaborn-v0_8-whitegrid" )

plt.hist(heights)
plt.title("Height distribution of US President")
plt.xlabel("height (cm)")
plt.ylabel("number")
plt.show()
