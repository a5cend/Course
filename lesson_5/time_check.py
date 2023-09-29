import pandas as pd

apple = pd.DataFrame({
    'date': ['2017-02-03', '2017-01-09', '2016-12-21'],
    'Open': [128.3, 117.9, 116.8],
    'Close': [129.8, 118.98, 117]}).set_index('date')

print(apple)

print(apple.loc['date'])
