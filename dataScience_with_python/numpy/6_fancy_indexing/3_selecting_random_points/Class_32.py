import numpy as np
import matplotlib.pyplot as plt
#a fancy indexing common use is in selection of sub lines sets of a matrix.
mean = [0,0]
cov = [[1, 2],
       [2, 5]]
rng = np.random.default_rng(seed=1701)
x = rng.multivariate_normal(mean, cov, 100)
print(x.shape, "\n")

# using plotting tools we can see this points as a dispersion chart.
print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')
plt.scatter(x[:, 0], x[:, 1])
plt.show()