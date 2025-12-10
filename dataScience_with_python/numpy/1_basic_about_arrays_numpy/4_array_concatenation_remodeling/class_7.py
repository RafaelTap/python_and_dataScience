import numpy as np

#concatenating two or more arrays

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9])
z = np.array([10,11])

x_y = np.concatenate([x,y])
x_y_z = np.concatenate([x, y, z])

print(x_y)
print(x_y_z)