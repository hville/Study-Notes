# pylint: disable=E0401, C0103, C0325
"""
Created on Wed Aug 10 2017
@author: hugov

SOURCES VARIABLES
  oilperperson - 2010 mt/person/year
  relectricperperson - kWh/person/year
  urbanrate - %
  incomeperperson
"""

import numpy
import pandas
pandas.set_option('display.float_format', lambda x: '%f'%x) # bug fix for display formats

data = pandas.read_csv('../data/gapminder.csv', low_memory=False)
size = len(data.country)

# convert values to float, ignoring empty values
for key in ['oilperperson', 'relectricperperson', 'urbanrate', 'incomeperperson']:
  data[key] = data[key].apply(lambda x: float(x) if x != ' ' else numpy.nan)
  nanCountries = [val for idx, val in enumerate(data.country) if numpy.isnan(data[key][idx])]
  print()
  print(key, 'missing fields changed to NaN:', str(len(nanCountries)), '/', str(size))
  print(nanCountries)

# new combined variables
data['kgoilperincome'] = 1000 * data['oilperperson'] / data['incomeperperson']
data['relectricperincome'] = data['relectricperperson'] / data['incomeperperson']
data['relectricperoil'] = data['relectricperperson'] / data['oilperperson']

#examining frequency distributions for age
print('\nCross-tab analysis\n')
fields = ['incomeperperson', 'relectricperperson', 'oilperperson',
          'relectricperoil', 'relectricperincome', 'kgoilperincome'
         ]
labels = ['Q1', 'Q2', 'Q3', 'Q4']
urbanrateQs = pandas.qcut(data.urbanrate, 4, labels)
for field in fields:
  print(pandas.crosstab(urbanrateQs, pandas.qcut(data[field], 4, labels)), '\n')
