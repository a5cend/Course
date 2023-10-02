import numpy as np
import csv
import re
import pandas as pd


class An:
    def __init__(self, path):
        self.path = path
        self.data = None

    def read(self):
        self.data = np.genfromtxt(self.path, dtype=str, delimiter=',', invalid_raise=False,
                                  usecols=(0, 3), skip_header=1, missing_values='', filling_values='us', max_rows=1000)
        # self.data = csv.reader(self.path, delimiter=',')

    def maxViewsCountry(self):
        # return set(self.data[:, 1])
        viewsPerCountry = {}
        countries = self.data[:, 1]
        countries = set(countries[countries != ''])
        for country in countries:
            viewsPerCountry.update({country: len(re.findall(country, str(self.data[:, 1])))})
        return viewsPerCountry


file = An('nlo.csv')
file.read()
print(file.maxViewsCountry())
