import numpy as np

rng = np.random.default_rng()

x = rng.integers(0, 10, (3, 4))
print(x, "\n")
print(sum(x), "\n")
print(np.sum(x), "\n")
# the numpy aggregation will be applied in all elements from array
print(x.sum())

# axis = 0 -> colum
#minimals values in each columns
min_columns_values = x.min(axis= 0)
print(min_columns_values, "\n")

#maximals values in each line
max_columns_values = x.max(axis= 0)
print(max_columns_values)

#axis = 1 -> line
#minimals values in each line
min_lines_values = x.min(axis= 1)
print(min_lines_values, "\n")

#maximals values in each lines
max_lines_values = x.max(axis= 1)