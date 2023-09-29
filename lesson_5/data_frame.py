import pandas as pd

data = pd.DataFrame({
    'product': ['tomato', 'potato', 'cucumber', 'apple'],
    'day_1': [7293, 5781, 5782, 7482],
    'day_2': [5728, 1209, 5795, 1345],
    'day_3': [5648, 4561, 4813, 564]}, index=['A', 'B', 'C', 'D'])

print(data, '\n')
print(data.loc['A'], '\n')
print(data.iloc[0], '\n')


print(data.day_1)
# print(data['day_1'])
