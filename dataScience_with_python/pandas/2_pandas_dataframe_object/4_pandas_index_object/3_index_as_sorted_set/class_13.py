import pandas as pd

indA = pd.Index([1, 2, 3, 5, 7, 9, 11, 13, 15])
indB =pd.Index([1, 3, 4, 5, 7, 9, 10, 15, 16])

intersection = indA.intersection(indB)
print(intersection, '\n')

union = indA.union(indB)
print(union, '\n')

sym_diff = indA.symmetric_difference(indB)
print(sym_diff)