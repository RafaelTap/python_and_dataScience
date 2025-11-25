import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# noinspection PyTypeChecker
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                                 'formats':((np.str_, 10), np.int32, np.float64)})
print(data, data.dtype, '\n')

print(data['age'])

data_rec = data.view(np.recarray)
age_ = data_rec.age

#check code