import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('emojis.csv')
print(data)

# years = set(data['Year'])
# print(years)
#
# numbers = pd.DataFrame({
#     'years': list(years),
#     'number': np.zeros(len(years), int)}).set_index('years')
#
# for year in years:
#     numbers.loc[year] = len(data[data['Year'] == year])
# print(numbers)
#
# maximum = numbers['number'].idxmax()
# print(max)
# print(numbers.loc[maximum])

print(data.groupby('Year')['Year'].count())

plt.plot(data.groupby('Year')['Year'].count())
plt.savefig('new_emojis per year.png')
