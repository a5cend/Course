import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('BCT-USD.csv').set_index('Date')
# print(data['Open'])


def func(date_min, date_max):
    print(data['Open'][date_min: date_max])

    plt.plot(data['Open'][date_min: date_max])
    plt.plot(data['Close'][date_min: date_max])
    plt.show()
    plt.savefig('BCT-USD.png')


func('2021-10-21', '2021-11-29')
