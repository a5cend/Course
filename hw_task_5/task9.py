import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('BCT-USD.csv')#.set_index('Date')
# print(data['Open'])

# изменение типа данных
index_of_min = data['Volume'].idxmin()
data['Date'] = data['Date'].astype('datetime64[ns]')
data['Year Month'] = data['Date'].dt.to_period('M')
# print(data)

# print(data.groupby('Year Month')['Volume'].sum())
# print(data.groupby('Year Month')['Volume'].first())
# print(data.groupby('Year Month')['Volume'].last())

new_data = data.groupby('Year Month')['Year Month'].nunique()
diff = data.groupby('Year Month')['Open'].first() - data.groupby('Year Month')['Close'].last()
print(diff[diff < 0])

# new_data['Open'] = data.groupby('Year Month')['Open'].first()
# print(new_data)
# new_data = pd.DataFrame({
#     'Year Month': ,
#     'Year Month Open': data.groupby('Year Month')['Open'].first(),
#     'Year Month Close': data.groupby('Year Month')['Close'].last()})
# print(new_data)
# print(data.groupby('Year Month')['Year Month'][data.groupby('Year Month')['Open'].first() > data.groupby('Year Month')['Close'].last()])
