import pandas as pd

#dataframe is an object Series collection in dataframe with one column that can be created from an Series object.

population_dict = ({'rio de janeiro': 6098345, 'sao paulo': 34576483, 'vitoria': 34586758, 'belo horizonte': 87940531})
area_dict = ({'rio de janeiro': 60983, 'sao paulo': 34576, 'vitoria': 34586, 'belo horizonte': 87940})

population = pd.Series(population_dict)

pop_column = pd.DataFrame(population, columns=['population'])
print(pop_column)

