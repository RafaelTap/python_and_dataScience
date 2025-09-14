import numpy as np

x = np.array(range(1, 4))

y = np.array([1, 2, 3])

# common operations available in ufuncs (exponential)
print(x, "\n")
print(y, "\n")
print(x, "\n")
print("e^x = ", np.exp(x), "\n")
print("2^x = ", np.exp2(x), "\n")
print("3^x = ",np.power(3., x), "\n")