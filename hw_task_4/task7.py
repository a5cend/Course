import numpy as np


def func(a: np.array, s: int, last=False):
    x = len(a)
    print(a)
    b = np.random.randint(0, 100, (x, s))
    print(b)
    c = np.dot(a, b)
    print(c)
    if not last:
        c = np.sin(c)
    else:
        c = np.maximum(c, 0)
    return c, b


c1 = func(a=np.array([4, 5, 1, 7, 9]), s=10)[0]
print('\n')
c2 = func(a=c1, s=10)[0]
print('\n')
c3 = func(a=c2, s=5, last=True)[0]
print('\n')

print(c3)
print(c3 * 100)
