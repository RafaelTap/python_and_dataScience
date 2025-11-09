import numpy as np
from vega_datasets import data

# boolean array with masks
#we can calculate same statistics datas in precipitation Seattle data.
rainfall_mm = np.array(data.seattle_weather().set_index('date')['precipitation']['2015'])

#mask of all rainy days
rainy = (rainfall_mm > 0)

#mask of all summer days, june 21 is the day number 172.
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("median precip on rainy days in 2015 (mm): ", np.median(rainfall_mm[rainy]))
print("median precip on summer days in 2015 (mm):", np.median(rainfall_mm[summer]))
print("maximum precip on summer days in 2015 (mm):", np.maximum(rainfall_mm[summer]))
print("median precip on non-summer days in 2015 (mm):", np.median(rainfall_mm[rainy & ~summer]))

