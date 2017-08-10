<!-- markdownlint-disable MD029 -->
# Data Visualization - Week 3

## Code

```python
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
          'relectricperincome', 'relectricperincome', 'kgoilperincome'
         ]
labels = ['Q1', 'Q2', 'Q3', 'Q4']
urbanrateQs = pandas.qcut(data.urbanrate, 4, labels)
for field in fields:
  print(pandas.crosstab(urbanrateQs, pandas.qcut(data[field], 4, labels)), '\n')
```

Full code in [this file](./code/code_w3.py)

## Results and Observations

### Selected Source Variables

* `oilperperson`: metric tons of oil / year / person
* `relectricperperson`: residential electric consumption kWh / year / person
* `urbanrate`: Urban population %
* `incomeperperson`: $ / person

### Source Data Treatment

Missing values in the CSV files (empty strings `' '`) were converted to `NaN`
* `oilperperson`: 150 / 213
* `relectricperperson`: 77 / 213
* `urbanrate`: 10 / 213
* `incomeperperson`: 23 / 213

### Source Data Cross-tab Analysis

The full frequency tables are not shown here because the values for each 213 countries are mostly unique for each country (i.e. frequency == 1, probability == 1/213). Exceptions are empty values that were converted to `NaN` as listed above

Instead, each variable was grouped into quartiles and compared to the `urbanrate`, the urban population ratio

```text
incomeperperson  Q1  Q2  Q3  Q4
urbanrate
Q1               30  11   4   3
Q2               16  19  12   1
Q3                2  14  19  11
Q4                0   2  12  33

relectricperperson  Q1  Q2  Q3  Q4
urbanrate
Q1                  14   5   0   1
Q2                  14  12   7   2
Q3                   4  11  17   9
Q4                   1   6  10  21

oilperperson  Q1  Q2  Q3  Q4
urbanrate
Q1             4   1   0   0
Q2             5   2   1   0
Q3             6   9   7   3
Q4             1   4   7  12
```

### Composit Variables

The oil and electric power consumption both tend to rize with the urban population ratio but so is the income per person. Since income is very likely to cause increased energy consumption, 3 new composite variables were created:
* `kgoilperincome`: 1000 * `oilperperson` / `incomeperperson`
* `relectricperincome`: `relectricperperson` / `incomeperperson`
* `relectricperoil`: `relectricperperson` / `oilperperson`

### Composit Variables Cross-tab Analysis

```text
relectricperoil  Q1  Q2  Q3  Q4
urbanrate
Q1                1   1   2   1
Q2                2   4   1   1
Q3                4   7   8   6
Q4                9   3   4   8

relectricperincome  Q1  Q2  Q3  Q4
urbanrate
Q1                   4   3   5   7
Q2                   6   9   7  13
Q3                  10   9  12   9
Q4                  13  11   8   4

kgoilperincome  Q1  Q2  Q3  Q4
urbanrate
Q1               1   0   3   1
Q2               0   1   3   4
Q3               7   8   4   6
Q4               8   6   5   4
```

The composit variables with the income portion removed paint a more nuanced picture and is not clear at this level of granularity what are the relationships, if any.
