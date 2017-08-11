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
size = len(data.country)

# convert values to float, ignoring empty values
for key in ['oilperperson', 'relectricperperson', 'urbanrate', 'incomeperperson']:
  data[key] = data[key].apply(lambda x: float(x) if x != ' ' else numpy.nan) # to numeric values
  seaborn.distplot(data[key].dropna(), kde=False) # histogram
  #nanCountries = [val for idx, val in enumerate(data.country) if numpy.isnan(data[key][idx])]
  #print()
  #print(key, 'missing fields changed to NaN:', str(len(nanCountries)), '/', str(size))
  #print(nanCountries)

# new combined variables
data.kgoilperincome = 1000 * data.oilperperson / data.incomeperperson
data.relectricperincome = data.relectricperperson / data.incomeperperson
data.relectricperoil = data.relectricperperson / data.oilperperson


# ????

'''
plt.xlabel('Number of Cigarettes per Month')
plt.title('Estimated Number of Cigarettes per Month among Young Adult Smokers in the NESARC Study')

# standard deviation and other descriptive statistics for quantitative variables
print 'describe number of cigarettes smoked per month'
desc1 = sub2['NUMCIGMO_EST'].describe()
print desc1

c1= sub2.groupby('NUMCIGMO_EST').size()
print c1

print 'describe nicotine dependence'
desc2 = sub2['TAB12MDX'].describe()
print desc2

c1= sub2.groupby('TAB12MDX').size()
print c1

print 'mode'
mode1 = sub2['TAB12MDX'].mode()
print mode1

print 'mean'
mean1 = sub2['NUMCIGMO_EST'].mean()
print mean1

print 'std'
std1 = sub2['NUMCIGMO_EST'].std()
print std1

print 'min'
min1 = sub2['NUMCIGMO_EST'].min()
print min1

print 'max'
max1 = sub2['NUMCIGMO_EST'].max()
print max1

print 'median'
median1 = sub2['NUMCIGMO_EST'].median()
print median1

print 'mode'
mode1 = sub2['NUMCIGMO_EST'].mode()
print mode1


c1= sub2.groupby('TAB12MDX').size()
print c1

p1 = sub2.groupby('TAB12MDX').size() * 100 / len(data)
print p1


c2 = sub2.groupby('NUMCIGMO_EST').size()
print c2

p2 = sub2.groupby('NUMCIGMO_EST').size() * 100 / len(data)
print p2

'''

'''
#examining frequency distributions for age
print('\nCross-tab analysis\n')
fields = ['incomeperperson', 'relectricperperson', 'oilperperson',
          'relectricperoil', 'relectricperincome', 'kgoilperincome'
         ]
labels = ['Q1', 'Q2', 'Q3', 'Q4']
urbanrateQs = pandas.qcut(data.urbanrate, 4, labels)
for field in fields:
  print(pandas.crosstab(urbanrateQs, pandas.qcut(data[field], 4, labels)), '\n')
'''
