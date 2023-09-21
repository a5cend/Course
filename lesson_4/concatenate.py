import numpy as np

a = np.array([1, 2], float)
b = np.array([3, 4, 5], float)
c = np.array([6, 7], float)

# print(np.concatenate((a, b, c)))

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7, 8]], float)

print(np.concatenate((a, b)))
print('\n')
print(np.concatenate((a, b), axis=0))
print('\n')
print(np.concatenate((a, b), axis=1))
