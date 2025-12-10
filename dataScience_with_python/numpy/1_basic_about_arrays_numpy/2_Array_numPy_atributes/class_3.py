import numpy as np

#arrays index: accessing individual elements

rng = np.random.default_rng(seed=1701)

x1 = rng.integers(10, size=8) #one-dimensional array
x2 = rng.integers(10, size=(4,7)) #two-dimensional array
x3 = rng.integers(10, size=(4,5,6)) #three-dimensional array
x4 = rng.integers(10, size =(4,5,6,7)) #four-dimensional array

print("one-dimensional array: ", x1)
print("first element: ", x1[0])
print("second element: ", x1[1])
print("fifth element: ", x1[4])
print("last element: ", x1[-1])

print("---------------------")

print(x2)
print("line one, sixth element",x2[1, 5])
print("second line, fourth element", x2[2, 3])
print(x2[3, 4])
x2[3, 4] = 1
print(x2)

