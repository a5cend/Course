import numpy as np

a = np.array([1, 2, 3], float)
b = np.array([4, 5, 6], float)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print('\n')

m1 = np.array([[1, 2], [3, 4], [5, 6]], int)
m2 = np.array([-1, 3], float)
print(m1 + m2)

print('\n')
print(np.dot(m1, m2))
