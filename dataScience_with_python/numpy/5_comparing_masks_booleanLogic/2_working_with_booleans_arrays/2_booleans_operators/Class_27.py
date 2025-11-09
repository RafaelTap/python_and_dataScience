import numpy as np
from vega_datasets import data

rainfall_mm = np.array(data.seattle_weather().set_index('date')['precipitation']['2015'])

print("rainy days without rain: ", rainfall_mm == 0)
print("number of days with rain: ", rainfall_mm != 0)
print("days with more than 10 mm: ", rainfall_mm > 10)
print("rainy days with less 5 mm: ", ((rainfall_mm > 0) & (rainfall_mm < 5)))
