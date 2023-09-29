import pandas as pd

data = {'day 1': 100, 'day 2': 0, 'day 3': 150, 'day 4': 200}

data_new = pd.Series(data)
print(data_new.index)


# data_new = pd.Series(data)[:3]
# print(data_new[data_new != 0])
#
# allowable_keys = 'day 1', 'day 2', 'day 3'
#
# for key
