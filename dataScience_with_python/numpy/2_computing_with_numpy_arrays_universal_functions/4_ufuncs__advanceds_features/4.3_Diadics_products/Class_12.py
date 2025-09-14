import numpy as np

# any ufuncs can calculate the output of all pairs of two different entries with the method outer()
#creating a table
x = np.arange(1, 6)
x1 = np.multiply.outer(x, x)
print(x1)