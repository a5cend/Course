import pandas as pd

my_series = pd.Series([2, 4, 6])

print(my_series)
print(my_series[1])

my_series1 = pd.Series([2, 4, 6], index=['a', 'b', 'c'])
print(my_series1)
print(my_series1['a'])      # 2

my_series2 = pd.Series([2, 4, 6], index=[3, 2, 1])
print(my_series2)
print(my_series2[3])        # 2

my_series3 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(my_series3)
print(my_series3['b'])      # 2
print(my_series3[my_series3 > 2])      # c 3

my_series3[['a', 'b', 'c']] = 10
print(my_series3)
print(my_series3.values)
print(my_series3.index)
print(my_series3.name)

my_series3.index = ['d', 'e', 'asd']
print(my_series3)
print(my_series3['d', 'e', 'asd'], '\n')

