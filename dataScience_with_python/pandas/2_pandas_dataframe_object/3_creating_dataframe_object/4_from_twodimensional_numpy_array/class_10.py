import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.rand(3,2),
                    columns=['foo', 'bar'],
                    index= ['a', 'b', 'c']) # we can choose not to use explicit indexes
print(data, '\n')

rng = np.random.default_rng(seed=1702)
matrix = rng.random((3,2))
data_2 = pd.DataFrame(matrix,
                      columns=['f1', 'f2'])
print(data_2)

