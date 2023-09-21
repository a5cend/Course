import numpy as np


def sorting1(*args):
    # print(np.array(args, dtype=int))
    return np.sort(np.array(args, dtype=int))


def sorting2(*args):
    filt = list(filter(lambda x: type(x) == int, args))
    return np.sort(np.array(filt, dtype=int))


def sorting3(*args):
    s = sorted(list(filter(lambda x: type(x) == int, args)))
    return np.sort(np.array(s, dtype=int))


print(sorting1(1, 2, -3, -5.5))
print(sorting2(1, 2, -3, -5.5))
print(sorting3(1, 2, -3, -5.5))
