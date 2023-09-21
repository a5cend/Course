import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a[0, 1])
print(a[1, 2])

print(a.shape)
print(a.dtype)
b = np.array(range(10), float)
b_reshape = b.reshape((2, 5))
print(b_reshape)

print(b.tolist())
print(list(b))

