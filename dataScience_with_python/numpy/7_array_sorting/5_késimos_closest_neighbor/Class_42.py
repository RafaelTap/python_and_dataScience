import numpy as np
import matplotlib.pyplot as plt

# let's see how use the function argsort() in multiples axes to found the closest neighbor
# at a certain point in a set.
rng = np.random.default_rng(seed=42)
x = rng.random((10,2))

# now we calculate the distance between each pair of point.
dist_sq = np.sum((x[:, np.newaxis] - x[np.newaxis, :]) ** 2, axis= -1)

k=2
nearest_partition = np.argpartition(dist_sq, k + 1, axis= 1)

plt.scatter(x[:,0], x[:,1], s=100)

for i in range(x.shape[0]):
    for j in nearest_partition[i, :k + 1]:
        plt.plot(*zip(x[j], x[i]), color= 'black')
        plt.show()

""" CHECK THE CODE """

