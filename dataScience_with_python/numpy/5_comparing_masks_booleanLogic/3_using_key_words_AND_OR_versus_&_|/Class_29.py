import numpy as np

# in python all whole number are considered true
print(bool(42), bool(0))
print(bool(42 and 0))
print(bool(43 or 0))
print(" ")

# when we use &, | the expression operate on element bitwise representation, applying and/or on the bits tha form the
#number
print(bin(42))
print(bin(59))
print(bin(42 & 59))
print(bin(42 | 59))
print(" ")

a = np.array([1,0,1,0,1,0], dtype=bool)
b = np.array([1,1,1,0,1,1], dtype=bool)
print(a | b)
print(" ")
#evaluate an expression of an array, we must use the operators &/| in the place of and/or.
x = np.arange(10)
print(x)
print((x > 4) & (x < 8))
#masking the values
print(x[(x > 4) & (x < 8)])