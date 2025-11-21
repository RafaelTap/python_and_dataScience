import numpy as np

#each element has an array or a value matrix.
#here, a data type with 'mat' component consisting of a 3x3 float dot matrix.

tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3,3))])
x = np.zeros(1, dtype=tp)
print(x[0], '\n')
print(x['mat'][0], '\n')
print(x)