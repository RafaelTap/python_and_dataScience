import  numpy as np

#example of broadcast number 1

#if two arrays have a different number of dimensions, the shape of array with the smallest number of dimension is
#filled with number 1 on the left side.
#a.shape become (1,3)

a = np.arange(3)
b = np.ones((2,3))

print(a.shape, " ", b.shape)

#if the shape of two arrays no match in any dimension, the array with the shape equals a 1 in this dimension
#will be extended to match with others.
# b.shape keep (2,3)
# a.shape become (2,3)
sum_ = a + b
print(sum_)