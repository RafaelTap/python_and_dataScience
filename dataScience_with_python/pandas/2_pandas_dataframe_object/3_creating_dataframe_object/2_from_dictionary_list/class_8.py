import pandas as pd

#any dictionary list can be created in a dataframe
#simple list comprehension to create some data

data = ({'a': i, 'b': 2 * i}
        for i in range(3))

print_data = pd.DataFrame(data)
print(print_data, '\n')

#if we don't have some dictionary keys, Pandas fills with the values "NaN" (not a number)

data_2 = pd.DataFrame([{'a':1, 'b':2}, {'b':3, 'c':4}])
print(data_2)
