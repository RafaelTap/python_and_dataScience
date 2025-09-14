import numpy as np

x = np.array([-1, -2, -3, -4, -5])

abs_1 = abs(x)
print(abs_1, "\n")

# correspondent ufunc under the alias np.abs()
abs_2= np.absolute(x)
print(abs_2, "\n")

# complex data returns the magnitude

y = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
abs_3 = np.abs(y)
print(abs_3)