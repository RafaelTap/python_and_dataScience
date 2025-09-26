import numpy as np
import matplotlib as plt

#ploting a two-dimensional function

#x and y have 50 paces from 0 to 50
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50) [:, np.newaxis]

#f(x, y)
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

plt.imshow(z, origin= 'lower', extent= [0, 5, 0, 5])
plt.colorbar()
