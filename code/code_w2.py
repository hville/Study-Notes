# pylint: disable=E0401, C0103, C0325
"""
Created on Wed Aug  9 10:05:11 2017
@author: hugov

VARIABLES
    oilperperson - 2010 mt/person/year
    relectricperperson - kWh/person/year
    urbanrate - %
"""

import numpy
import pandas
pandas.set_option('display.float_format', lambda x: '%f'%x) # bug fix for display formats

data = pandas.read_csv('../data/gapminder.csv', low_memory=False)
names = ['oilperperson', 'relectricperperson', 'urbanrate']

print ('Frequency Tables:')
for key in names:
    print(key)
    data[key] = pandas.to_numeric(data[key], errors='coerce') #strings --> numeric
    count = data[key].value_counts(sort=False) #(sort=False, normalize=True))
    print(count)

print ('Row counts for ' + str(len(names)) + '/' + str(len(data.columns)) + ' columns')
for key in names:
    print('\t' + key + ':' + str(len(data)))

print ('Outliers')
for key in names:
    print ('\t' + key)
    for idx, val in enumerate(data[key]):
        if val == 0 or val == 100:
            print('\t\t' + data['country'][idx] + ': ' + str(val))
