import pandas as pd


indexes = pd.Index([1, 2, 3, 4, 5])
print(indexes[1], '\n')
print(indexes[4], '\n')
print(indexes[:2], '\n')
print(indexes[::2], '\n')

#like arrays numpy attributes
print(indexes.shape, indexes.size, indexes.ndim, indexes.dtype)

#Index does not support mutable operations
try:
    ind = indexes[3] = 1
    print(ind)
except Exception as err:
    print(err)
