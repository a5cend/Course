import numpy as np
import random


def matrix0(x, y):
    dim = x * y
    m = np.full(dim, random.random())
    return m.reshape(x, y)
    # return np.array([np.full(x, random.random()), np.full(y, random.random())])


def matrix1(x, y):
    result = np.random.random((x, y))
    return result.min(), result.max()
    # return np.array([np.full(x, random.random()), np.full(y, random.random())])


def matrix(x, y):
    return np.random.randint(low=0, high=10, size=(x, y))


print(matrix(2, 3))
