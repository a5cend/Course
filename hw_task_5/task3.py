import numpy as np
import pandas as pd

matrix = np.random.randint(1, 10, (10, 10), int)

data = pd.DataFrame(matrix, index=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'g', 'k'))
print(data, '\n')
# print(data.iloc[0], '\n')
# print(sum(data.loc['a']))
# print(data.loc[:])

print(data.index)
print(data.columns.values)
print(np.mean(data.to_numpy()))
data.to_csv('random_matrix.csv')
