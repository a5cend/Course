import numpy as np
import pandas as pd

matrix = np.random.randint(1, 10, (10, 10), int)

data = pd.DataFrame(matrix, index=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'g', 'k'))
print(data, '\n')
print(data.iloc[0], '\n')
data['sum'] = data.sum(axis=1)
print(data, '\n')
print(data[data['sum'] >= 60], '\n')

# print(list(filter(lambda x: x > 5, data.loc[:])))
