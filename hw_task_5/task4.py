import numpy as np
import pandas as pd

data = pd.read_csv('emojis.csv')
print(data)
subcategories = set(data['Subcategory'])
print(subcategories)

numbers = pd.DataFrame({
    'subcategories': list(subcategories),
    'number': np.zeros(len(subcategories), int)}).set_index('subcategories')
print(numbers)

for cat in subcategories:
    numbers.loc[cat] = len(data[data['Subcategory'] == cat])
print(numbers)

maximum = numbers['number'].idxmax()
print(max)
print(numbers.loc[maximum])

# print(data.groupby('Subcategory')['Subcategory'].count())