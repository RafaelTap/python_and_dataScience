import numpy as np

rng = np.random.default_rng(seed= 1701)

x = rng.integers(100, size= 10)
print(x)

#accessing three elements

print(x[0], x[3], x[7])

#an alternative is pass a unique index list
index = [0, 3, 7]
print(x[index]) #array of indexes

print(" ")

#when we use an array of indexes, the format of result will reflect the format of array of indexes not
#the array that is being indexed.
index_2 = [[2,5],
           [7,9]]
print(x[index_2])
print(" ")

#fancy indexing work too with multidimensional arrays.
x = np.arange(12).reshape(3, 4)
print(x)
print(" ")

#first index is the row and the second index is the column.
row = np.array([0,1,2])
col = np.array([2, 1, 3])
print(x[row, col])

# here the value of each line is the vector of each column, exactly as we saw in arithmetic operations broadcasting
row[:, np.newaxis] * col
print(row)


