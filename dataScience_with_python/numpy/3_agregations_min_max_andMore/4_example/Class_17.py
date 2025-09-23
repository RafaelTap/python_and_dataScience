import pandas as pd
import numpy as np
data = pd.read_csv("president_height.csv")
heights = np.array([data["height (cm)"]])
print(heights, "\n")

print("standard deviation: ", heights.std())
print("mean height: ", heights.mean())
print("minimum height: ", heights.min())
print("maximum height: ", heights.max())