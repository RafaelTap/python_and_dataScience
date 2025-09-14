import numpy as np

x = np.arange(5)
y = np.empty(5)

np.multiply(x, 10, out= y)
print(x)
print(y)

#views of arrays, recording the calculation result into elements from an array
z = np.zeros(10)
np.power(2, x, out=z[::2])
print(z)
