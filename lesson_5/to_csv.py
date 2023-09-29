import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 4, 1, 6],
    'arr_time': [834, 4561, 4813, 564],
    'dep_time': [840, 4570, 4880, 590]}).set_index('id')

print(data, '\n')

diff = data.loc[:, 'dep_time'].values - data.loc[:, 'arr_time'].values
data['diff'] = diff
data.to_csv('flights.csv', index=False, header=False)

data_new = pd.read_csv('flights.csv')
print(data_new)
