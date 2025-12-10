import numpy as np

#accessing subarrays
#to access a part of array are used the format: x1[start:step:stop]

rng = np.random.default_rng(seed= 1701)

x1 = rng.integers(10, size=21)
print("array", x1)

print("subarray: ", x1[:5])
print("subarray after index 5", x1[5:])
print("subarray in the middle of array: ", x1[3:9])
print("each second element of the array: ", x1[::2])
print("each second element of the array from index number 4: ", x1[4::2])
print("accessing array from de last item (inverted array)")
print("all elements in inverted order: ", x1[::-1])
print("each second element of the array in inverted order from index number 5: ", x1[5::-2])

print("-------------------------------------------------------------")

x2 = rng.integers(10, size=(6, 6))

print("array:\n", x2)
print("first two lines from third column", x2[:2, :3])
print("first four lines and each second columns ", x2[:4,::2])
print("all lines and columns in inverted order", x2[::-1,::-1])
print("first column of the array: ", x2[:,0])
print("first line of the array: ", x2[0, :])
print("only first line - clean synthax: ", x2[0])

sub_array = x2[:3, :3]
print("subarray 3x3:\n", sub_array)

sub_array[2,1] = 8 # modify this array, modify the original array too
print(x2)

print("copying subarray and changing some value ")
sub_array_2 = x2[:3, :3].copy()
print(sub_array_2)

sub_array_2 [2,2] = 3

print("element 2x2 changed\n",sub_array_2, "\n", "original array\n", x2)
