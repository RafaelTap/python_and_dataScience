import numpy as np

#separating array
x = np.array([range(1, 21)])
print(x)
y = np.array([1,2,3,99,99,3,2,1])
z = np.array([range(1,9)])

y1, y2, y3 = np.split(y, [3, 5])
print(y1, y2, y3)

z1, z2, z3 = np.split(y, [3, 5])
print(z1, z2, z3, "\n")

#multidimensional array

grid = np.arange(16).reshape((4, 4))
print(grid, "\n")

upper, lower = np.vsplit(grid, [2])
print(upper, "\n", lower, "\n")

left, right = np.hsplit(grid, [2])
print(left, "\n", right)

#from third axis use function -> np.dsplit()


