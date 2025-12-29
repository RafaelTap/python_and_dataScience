import pandas as pd

# every series object is a version of : Series(data, index=index).
# data is one of many entities
# index is optional argument

# data is a list or a numPy array and index is a sequence of int
x = pd.Series([1, 2, 3, 4])
print(x)

# data is scalable, repeated to fill the specifical index
y = pd.Series(4, index=[10, 20, 30])
print(y)

# data is a dictionary and index has the dictionary keys as standard.
z = pd.Series({2:'a', 4:'b', 6:'c'})
print(z)

# data in each case the index is defined to control the order or used keys subset
w = pd.Series({1:'a', 2:'b', 3:'c'}, index= [2, 3])
print(w)