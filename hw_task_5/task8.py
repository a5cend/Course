import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('BCT-USD.csv')#.set_index('Date')
# print(data['Open'])

# изменение типа данных
index_of_min = data['Volume'].idxmin()
data['Date'] = data['Date'].astype('datetime64[ns]')
data['Year Month'] = data['Date'].dt.to_period('M')
print(data)
print('month ', data['Year Month'].loc[index_of_min])


