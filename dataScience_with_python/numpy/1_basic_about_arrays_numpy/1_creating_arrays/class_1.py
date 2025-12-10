import numpy as np

#zero
array_1 = np.zeros(3, dtype='int')
print(array_1)

print("-----")

#one
array_2 = np.ones((5,5), dtype='float')
print(array_2)

print("-----")

#matrix 4x4 fulled with 3.5
array_3 = np.full((4,4), 3.5)
print(array_3)

print("-----")

#
array_4  = np.arange(0,30, 2)
print(array_4)

print("-----")

array_5 = np.array([range(i, i +4) for i in [2, 4, 6, 8]])
print(array_5)

print("-----")

#create an array with 20 values equality distributed between 0 and 1.
array_6 = np.linspace(0, 1, 20)
print(array_6)

print("-----")

array_7 = np.random.random((4,4))
print(array_7)

print("-----")

array_8 = np.random.normal(0, 1, (5,5))
print(array_8)

print("-----")

array_9 = np.random.randint(0, 15, (8,8))
print(array_9)

print("-----")

array_10 = np.eye(5)
print(array_10)

print("-----")

array_11 = np.empty(5)
print(array_11)

