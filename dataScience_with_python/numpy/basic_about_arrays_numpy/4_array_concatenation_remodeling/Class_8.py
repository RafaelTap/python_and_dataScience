import numpy as np

# concatenating two-dimensional arrays

x = np.array([1,2,3])
y = np.array([[4],
             [7]])
grid = np.array([[1,2,3],
             [4,5,6]])

# concatenate along the first axis
x1 = np.concatenate([grid, grid])
print(x1, "\n")

#concatenated along the second axis, indexed from 0
x2 = np.concatenate([grid, grid], axis= 1)
print(x2, "\n")

x2 = np.concatenate([grid, grid], axis= 0) # he same: x1 = np.concatenate([grid, grid])
print(x2, "\n")

# array with mixed dimension
#using .vstack() - vertical - and .hstack() - horizontal

x3 = np.vstack([x, grid])
print(x3, "\n")

x4 = np.hstack([grid, y])
print(x4, "\n")
