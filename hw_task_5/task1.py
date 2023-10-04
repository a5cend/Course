import numpy as np
import pandas as pd

matrix = np.random.randint(1, 10, (10, 10), int)
print(pd.DataFrame(matrix))
