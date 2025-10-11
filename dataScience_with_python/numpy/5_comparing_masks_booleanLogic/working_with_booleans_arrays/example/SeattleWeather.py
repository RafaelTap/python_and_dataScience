import numpy as np
import matplotlib.pyplot as plt
from vega_datasets import data

#use operations from dataframe to extract the precipitation
#as numpy array

rainfall_mm = np.array(data.seattle_weather().set_index('date')['precipitation']['2015'])
print(len(rainfall_mm))

plt.style.use("seaborn-v0_8-whitegrid")
plt.hist(rainfall_mm, 40)
plt.show()

