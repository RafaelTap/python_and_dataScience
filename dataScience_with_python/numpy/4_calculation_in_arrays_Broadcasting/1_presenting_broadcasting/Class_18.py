import numpy as  np

# in arrays with the same size the operations are made in each element.
x = np.array([0, 1, 2, 3])
y = np.array(range(1,5))

print(x + y)
print(x * y)

sum_result = 5 + x
print(sum_result)

# operation in multidimensional array

m = np.ones((4, 4))
print(m)
#adding a one-dimensional array in multidimensional array
print(f"m + a: {m + x}")

