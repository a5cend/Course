import numpy as np


def dot(a, b):
    if a[1] == b[0]:
        m1 = np.ones(a[0] * a[1]).reshape((a[0], a[1]))
        print(m1)
        m2 = np.ones(b[0] * b[1]).reshape((b[0], b[1]))
        print(m2)
        print(np.dot(m1, m2))
    else:
        print('error')


dot((2, 3), (3, 5))
dot((2, 3), (4, 5))
