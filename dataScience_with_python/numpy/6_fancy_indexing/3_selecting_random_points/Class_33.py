import numpy as np
import matplotlib.pyplot as plt

#a fancy indexing common use is in selection of sublines sets of a matrix.
mean = [0,0]
cov = [[1, 2],
       [2, 5]]
rng = np.random.default_rng(seed=1701)
x = rng.multivariate_normal(mean, cov, 100)
print(x.shape, "\n")

# we'll use fancy indexing to select 20 random points. First, we choose 20 random indexes, no repetition and then,
# we use this indexes to select a part of original array.

indexes = np.random.choice(x.shape[0], 20, replace=False)
print(indexes, "\n")

selection = x[indexes] #fancy indexing
print(selection.shape, "\n")

# now we can see the selected points
plt.scatter(x[:, 0], x[:, 1], alpha= 0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolors='none', edgecolors='black', s=200)
plt.show()

