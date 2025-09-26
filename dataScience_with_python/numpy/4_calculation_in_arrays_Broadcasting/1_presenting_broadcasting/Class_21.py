import numpy as np

#broadcast in practice

#a frequent use is to subtract a values mean calculated by lines from array.

rng = np.random.default_rng(seed=1701)
x = rng.random((10, 3))

Xmean = x.mean(0)
print(Xmean)

#centralizing the array x subtracting the mean (it's a broadcast operation)
# within the machine precision, the mean of array is 0.
X_centered = x - Xmean
print(X_centered.mean(0))
