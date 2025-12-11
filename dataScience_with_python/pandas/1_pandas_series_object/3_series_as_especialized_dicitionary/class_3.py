import pandas as pd

population_dict = {'sao paulo': 11_904_961,
                   'rio de janeiro': 6_730_729,
                   'belo horizonte': 2_415_872,
                   'curitiba': 1_830_795,
                   'vitoria': 343_378}

population = pd.Series(population_dict)
print(population,'\n')

# typical item
print(population['vitoria'])

#slicing
print(population['rio de janeiro':'curitiba'])

#