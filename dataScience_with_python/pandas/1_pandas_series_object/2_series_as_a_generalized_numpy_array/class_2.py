import pandas as pd

# explicit index definition
data = pd.Series((2.3, 2.5, 2.7, 2.9, 3.1, 3.3), ('a', 'b', 'c', 'd', 'e', 'f'))
print(data, '\n')
print(data['d'], '\n')
print(data['b':'d'])
print('<<<<<>>>>>')

#discontinued indexes
data_2 = pd.Series((2, 4, 6, 8, 10),(2, 5, 8, 10 , 11))
print(data_2)
print(data_2[10])
print(data_2[11])