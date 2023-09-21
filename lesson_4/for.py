import numpy as np

array_for = np.array(range(15), int)
for i in array_for:
    print(i)

array_for_m = array_for.reshape(3, 5)
for i in array_for_m:
    print(i)
