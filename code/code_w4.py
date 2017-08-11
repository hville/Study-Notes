# pylint: disable=E0401, C0103, C0325
"""
Created on Wed Aug 11 2017
@author: hugov
"""
# BOILETPLATE
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt
#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)
# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# PROGRAM
data = pandas.read_csv('../data/gapminder.csv', low_memory=False)

# convert values to float, ignoring empty values
print('Source Variables')
axs = plt.subplots(ncols=4, nrows=1)
for i, key in enumerate(['oilperperson', 'relectricperperson', 'urbanrate', 'incomeperperson']):
  # to numeric values
  data[key] = data[key].apply(lambda x: float(x) if x != ' ' else numpy.nan)
  # histogram
  seaborn.distplot(data[key].dropna(), kde=False, ax=axs[1][i])
  print(data[key].describe())

# new combined variables
print('Derived Variables')
data['kgoilperincome'] = 1000 * data.oilperperson / data.incomeperperson
data['relectricperincome'] = data.relectricperperson / data.incomeperperson

# histogram
axs = plt.subplots(ncols=2, nrows=1)
for i, key in enumerate(['kgoilperincome', 'relectricperincome']):
  seaborn.distplot(data[key].dropna(), kde=False, ax=axs[1][i])
  print(data[key].describe())

# Scatterplots
for i, key in enumerate(['oilperperson', 'relectricperperson', 'incomeperperson']):
    axs = plt.subplots(ncols=1, nrows=1)
    seaborn.regplot(x="urbanrate", y=key, data=data)

for i, key in enumerate(['kgoilperincome', 'relectricperincome']):
    axs = plt.subplots(ncols=1, nrows=1)
    seaborn.regplot(x="urbanrate", y=key, data=data)
