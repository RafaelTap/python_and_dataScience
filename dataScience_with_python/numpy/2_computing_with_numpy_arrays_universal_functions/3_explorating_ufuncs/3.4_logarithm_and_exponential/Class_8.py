import numpy as np

#common operations available in ufuncs (logarithm)

x = np.array([1, 2, 4, 10])
print(x)
print(np.log(x))
print(np.log2(x)) #logarithm of base 2
print(np.log10(x))#logarithm of base 10


#special versions widely used to keep the value entrance precision of very small values

y = [0, 0.01, 0.002, 0.1]

print("\n", y)
print(np.expm1(y))
print(np.log1p(y))

