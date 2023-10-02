import numpy as np

size = 8
indexes = range(0, size)
a = np.zeros((size, size), int)
print(a, '\n')


for i, line in enumerate(a):
    if i % 2 == 0:
        a[i] = np.array(list(map(lambda x, index: 0 if index % 2 else 1, line, indexes)))
    else:
        a[i] = np.array(list(map(lambda x, index: 1 if index % 2 else 0, line, indexes)))

print(a)
