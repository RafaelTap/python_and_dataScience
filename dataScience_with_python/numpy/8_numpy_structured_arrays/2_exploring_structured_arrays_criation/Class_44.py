import numpy as np

#structured array's data type can be specified with dictionary method.

data = np.dtype({'names':('name', 'age', 'weight'),
       'formats':('U10', 'i4', 'f8')})
print(data, '\n')

data_1 = np.dtype({'names':('name', 'age', 'weight'),
       'formats':((np.str_, 10), np.int32, np.float64)})
print(data_1, '\n')

#tuple list
data_2 = np.dtype([('name','S10'),('age', 'i4'),('weight', 'f8')])
print(data_2, '\n')

#if the types names is not important, we can list the data types in only one string separated by
# comma.

data_types = np.dtype('S10, i4, f8')
print(data_types)