import numpy as np

a = np.array([4, 9, 16, 25], float)
print(type(a))

print(a[:2])
print(a[3])

a[0] = 10.1
print(a)

b = np.full(10, 1)
print(b)

b = a[::-1]
print(b)

print(np.zeros(10))
print(np.ones(10))
print(np.arange(10, 20))

print(b.min())
print(b.max())
print(b.mean())

print(np.sqrt(a))
