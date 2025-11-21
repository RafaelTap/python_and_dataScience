import numpy as np

# this class shows the use of structured arrays and arrays of register that provide a storage for compounds and
# heterogeneous data.
# imagine that we have many data categories about many people, and we would like to save those values to use
# in a Python program. We can save in tree different arrays.
# but, # this way to store the values don't guarantee that the arrays are related.

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

#simple array
x = np.zeros(4, dtype=int)
print(x, type(x), '\n')

#now we can create a structured array using a specification of compound data type.
# noinspection PyTypeChecker
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                                 'formats':('U10', 'i4', 'f8')})
print(data.dtype, '\n')

#U10 -> string Unicode with maximum length = 10
#i4 -> 4 bytes int (32 bits)
#f8 -> 8 bytes flot (64 bits)

#data is an empty container array, and now we can fill with the values lists.
#now, data are organized in a structured array.

data ['name'] = name
data ['age'] = age
data ['weight'] = weight
print(data, '\n')

# we can refer to the values by index or name.

#getting all the names, ages and weights
all_names = data['name']
all_ages = data['age']
all_weights = data['weight']
print(all_names, '\n', all_ages, '\n', all_weights, '\n')

#getting the lines of data

#first line
first_line = data[0]
#second line
second_line = data[1]
#third line
third_line = data[2]
print(first_line, '\n', second_line, '\n', third_line, '\n')

#getting the last line
last_line = data[-1]
print(last_line, '\n')

#getting the name of last line
name_last_line = data[-1]['name']
print(name_last_line, '\n')

#getting the name of second to last line
name_ = data[-2]['name']
print(name_, '\n')

#using boolean masking to filter ages.

age = data[data['age'] < 30]['name']
print(age)

# to make advanced operations we must consider the package Pandas, it has an object 'dataframe'.

