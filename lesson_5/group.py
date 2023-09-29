import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'year': [2013, 2013, 2013, 2013],
    'month': [1, 4, 1, 6],
    'arr_time': [834, 4561, 4813, 564],
    'dep_time': [840, 4570, 4880, 590]}).set_index('id')

print(data, '\n')

# количество рейсов по месяцам
print(data.groupby('month')['month'].count())

# добавление столбца
diff = data.loc[:, 'dep_time'].values - data.loc[:, 'arr_time'].values
data['diff'] = diff
print(data, '\n')

# группировка по месяцам и сумма разниц
print(data.groupby('month')['diff'].sum())
