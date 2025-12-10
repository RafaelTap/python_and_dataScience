import numpy as np

#operation between two arrays

#arrays unidimensional
x = np.arange(5)
y = np.arange(1, 6)

result = x/y
print(x)
print(y)
print(result, "\n")

#multidimensional arrays
z = np.arange(9).reshape(3, 3)
result_1 = 2 ** z
print(result_1)
