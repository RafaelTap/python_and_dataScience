import numpy as np

x = np.array([1,2,3,4,5])
print("less then: ", x<3)
print("greater then: ", x>3)
print("greater or equals", x>=3)
print("less or equals", x<=3)
print("different: ", x!=3)
print("equals: ", x==3)
print(2*x)
print("power: ", 2**x)
print((2*x) == (2**x))