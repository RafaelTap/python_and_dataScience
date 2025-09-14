import numpy as np

# array of angles
x = np.array([34, 50, 96])
sin_ = np.sin(x)
cos_ = np.cos(x)
tan_ = np.tan(x)

print("sin(x): ", sin_)
print("cos(x): ", cos_)
print("tan(x): ", tan_)

# inverse trigonometric functions

print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))