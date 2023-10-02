import re
import numpy as np


class AnFile:
    def __init__(self, path):
        self.path = path
        self.array = None

    def read(self):
        self.array = np.genfromtxt(self.path, dtype=str)

    def search_pattern(self):
        matched = []
        for s in self.array:
            if re.match(r'\w+', s)[0]:
                matched.append(re.match(r'\w+', s)[0])
        return matched


csv = AnFile('array.csv')
csv.read()
print(csv.array)

print(csv.search_pattern())
