<!-- markdownlint-disable MD029 -->
# Data Visualization - Week 2

## Code

```python
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
```

Full code in [this file](./code/code_w2.py)

## Observations

### Selected Variables
* *oilperperson*: metric tons of oil / year / person
* *relectricperperson*: residential electric consumption kWh / year / person
* *urbanrate*: Urban population %

### Frequency Tables

The full frequency tables are not shown here because the values for each 213 countries are mostly unique for each country (i.e. frequency == 1, probability == 1/213)

### Observations and Outliers

* Countries with 100% urban population
  * Bermuda: 100.0
  * Cayman Islands: 100.0
  * Hong Kong, China: 100.0
  * Macao, China: 100.0
  * Monaco: 100.0
  * Singapore: 100.0

* Countries with missing electrical consumption
  * Gibraltar
  * Iraq
  * Korea, Dem. Rep.
  * Namibia
  * Netherlands Antilles
