import numpy as np

a = np.random.randint(0, 100, size=(8, 4))
print(a, '\n')

b = np.random.randint(0, 100, size=(4, 2))
print(b, '\n')

print(np.dot(a, b))
