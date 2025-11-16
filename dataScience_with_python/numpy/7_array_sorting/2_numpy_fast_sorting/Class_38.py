import numpy as np

# the function np.sort is analogous to the function 'sorted' and will return any efficient sorted copy
# of any array.

x = np.array([1, 34, 22, 56, 77, 9])
print(x, '\n')

sorted_x = np.sort(x)
print(sorted_x, '\n')

# we can use the method .sort() to sort the list without a copy.
x.sort()
print(x, '\n')

# .argsort() return the index of sorted elements.

i = x.argsort()
print(i, '\n')

#fancy indexing
fi = x[i]
print(fi)
