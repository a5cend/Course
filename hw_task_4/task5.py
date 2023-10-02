import numpy as np


def func(number: int):
    if type(number) == int:
        for i in range(2, number - 1):
            m = number % i
            if m == 0:
                n = int(number / i)
                print(i, n)
                print(np.random.randint(0, 100, size=(n, i)))
            else:
                print('error')
    else:
        print('type error')


func(8)
