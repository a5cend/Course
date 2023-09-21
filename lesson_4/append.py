import numpy as np

a = np.array(range(10), int)
print(a)
a = np.append(a, 10)
print(a)

m = np.array([[1, 2], [3, 4]], int)
print(m)
m = np.append(m, np.array([[10, 11]]), axis=0)
print(m)
m = np.append(m, np.array([[10, 11]]))
print(m)
