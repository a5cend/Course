import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 4, 1, 6],
    'arr_time': [834, 4561, 4813, 564],
    'dep_time': [840, 4570, 4880, 590]}).set_index('id')

print(data, '\n')

# index = 2
# print(data.loc[[index], 'dep_time'])
# month = 1
# print(data[data.month == month])

diff = data.loc[:, 'dep_time'].values - data.loc[:, 'arr_time'].values
print(diff)
data['diff'] = diff
print(data)
