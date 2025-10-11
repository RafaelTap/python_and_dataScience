import numpy as np

rng = np.random.default_rng(seed= 1701)

x = rng.integers(10, size= (3, 4))
print(x)

print("counting entrances")
#how many values < 6 (true)
print("values < 6: ", np.count_nonzero(x<6))
print("values < 0 ?", np.any(x<0))
print("all values < 10", np.all(x<10))
print("all values == 6", np.all(x==6))




