import numpy as np

# we can use fancy indexing to change parts of an array.
# changing the item values of array of indexes
x = np.arange(10)
y = np.array([2, 1, 8, 4])
print(x, "\n", y)

x[y] = 99
print(x, "\n")

#we can any assignment operator
x[y] -= 10
print(x, "\n")

#the .at method applies the specific operator in the specifics indexes(here is i) with specific values(here is 1)
i = [2, 3, 3, 4, 4, 4]
z = np.zeros(10)
np.add.at(z, i, 1)
print(z)

