import numpy as np

#reduce the array to unic object, using some operation
x = [1, 2, 3, 4, 5]
x1 = np.add.reduce(x)
print(x1, "\n")

y = np.arange(1, 7)
y1 = np.multiply.reduce(y)
print(y1, "\n")

#storing all intermediate values
y2 = np.add.accumulate(y)
y3 = np.multiply.accumulate(y)
print(y2, "\n")
print(y3)
