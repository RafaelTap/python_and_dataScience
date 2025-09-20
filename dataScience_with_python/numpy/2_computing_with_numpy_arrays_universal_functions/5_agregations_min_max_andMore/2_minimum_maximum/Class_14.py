import numpy as np

# functions min ad max are used to encounter the
# minimum and maximum values.

x = np.array([range(10)])
print(x, "\n")

min_x = np.min(x)
max_x = np.max(x)
sum_x = np.sum(x)
print("maximum value: ", max_x, "\n", "minimum value: ", min_x, "\n", "values sum: ", sum_x)
