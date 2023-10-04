import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('emojis.csv')
print(data)


def func(category: str):
    data_categories = data['Category']
    print(data_categories)
    my_cat = data_categories[data_categories == category]
    if len(my_cat) != 0:
        return print(f'{len(my_cat) / len(data_categories) * 100} %')
    else:
        return print('Категория отсутствует')


func('Flags')
