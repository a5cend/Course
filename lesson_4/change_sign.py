import numpy as np

a = np.random.randint(low=0, high=15, size=15, dtype=int)
print(a)

print(np.array(list(map(lambda x: -x if 3 < x < 8 else x, a))))

a[(3 < a) & (a < 8)] *= -1
print(a)
