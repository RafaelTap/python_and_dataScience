import pandas as pd

# dataframe is a two-dimensional array with explicit lines and columns indexes

population_dict = ({'rio de janeiro': 6098345, 'sao paulo': 34576483, 'vitoria': 34586758, 'belo horizonte': 87940531})
area_dict = ({'rio de janeiro': 60983, 'sao paulo': 34576, 'vitoria': 34586, 'belo horizonte': 87940})

population = pd.Series(population_dict)
print(population, '\n')
area = pd.Series(area_dict)
print(area)

state = pd.DataFrame({'population': population, 'area': area})
print(state, '\n')
print(state.index)
