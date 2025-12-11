import pandas as pd

# a Pandas object Series is one-dimensional array of indexed data.
# can be created from a list or an array
# Series combines a sequence of values with a sequence of indexes that we can
# access with attributes values and index, values are a familiar numpy array, index is an object pd.index
# of array type.

data = pd.Series([0.25,0.5,0.75,1])
values = data.values
index = data.index
print(data, '\n')
print(values, '\n')
print(index, '\n')

# we can access data from associated index using [].
print(data[2], '\n')

print(data[0:2])

#