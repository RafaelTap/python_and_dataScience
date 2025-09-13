import numpy as np
from numpy.core.numeric import newaxis

x1 = np.array([ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(x1)

# line vector
x1.reshape(1,10)
print(x1)

#column vector ??
x1.reshape(10,1)
print(x1)

#using newaxis()
# line vector
x1[np.newaxis, :]
print(x1)

# column vector
x1[:, np.newaxis]
print(x1)

#check substitute function to use, .newaxis() is deprecated