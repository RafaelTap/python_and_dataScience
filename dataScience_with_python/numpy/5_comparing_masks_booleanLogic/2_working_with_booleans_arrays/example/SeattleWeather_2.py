import numpy as np
from vega_datasets import data
import matplotlib.pyplot as plt

# rainy days between 10 and 20 millimeters
rainfall_mm = np.array(data.seattle_weather().set_index('date')['precipitation']['2015'])

raining_day = np.sum((rainfall_mm > 10) & (rainfall_mm < 20)) #parenteses are very important here
                                                              # if remove then an error appear.

plt.style.use("seaborn-v0_8-whitegrid")
plt.hist(raining_day, 40)
plt.show()