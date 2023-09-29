import pandas as pd

data = pd.DataFrame({
    'product': ['tomato', 'potato', 'cucumber', 'apple'],
    'day_1': [7293, 5781, 5782, 7482],
    'day_2': [5728, 1209, 5795, 1345],
    'day_3': [5648, 4561, 4813, 564]}, index=['A', 'B', 'C', 'D']).set_index('product')

print(data)
# print(data['A'])

# data.reset_index()
# print(data['A'])      # error

data_cut = data.drop('cucumber')
data_cut = data_cut.drop('day_1', axis=1)
print(data_cut)
