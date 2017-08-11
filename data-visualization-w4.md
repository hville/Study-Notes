<!-- markdownlint-disable MD029 -->
# Data Visualization - Week 3

## Code

```python
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
```

Full code in [this file](./code/code_w4.py)


## Selected Source Variables

* `oilperperson`: metric tons of oil / year / person
* `relectricperperson`: residential electric consumption kWh / year / person
* `urbanrate`: Urban population %
* `incomeperperson`: $ / person


## Distribution of Source Variables

![Source Variables](/w4-source-dist.png)

From the unimodal distibution plot of these 4 source variables:
* `oilperperson`: unimodal @0, right skew
  * count   63.000000
  * mean     1.484085
  * std      1.825090
  * min      0.032281
  * max     12.228645
* `relectricperperson`: unimodal @0, right skew
  * count     136.000000
  * mean     1173.178995
  * std      1681.440173
  * min         0.000000
  * max     11154.755033
* `urbanrate`: bimodal, left skew
  * count   203.000000
  * mean     56.769360
  * std      23.844933
  * min      10.400000
  * max     100.000000
* `incomeperperson`: unimodal @0, right skew
  * count      190.000000
  * mean      8740.966076
  * std      14262.809083
  * min        103.775857
  * max     105147.437697


## Selected Composit Variables

The oil and electric power consumption both tend to rize with the urban population ratio but so is the income per person. Since income is very likely to cause increased energy consumption, 2 new composite variables were created:
* `kgoilperincome = 1000 * oilperperson / incomeperperson`
* `relectricperincome = relectricperperson / incomeperperson`


## Distribution of Composit Variables

![Composit Variables](/w4-calc-dist.png)

From the unimodal distibution plot of these 4 source variables:
* `kgoilperincome`: unimodal @0, right skew
  * count   61.000000
  * mean     0.156447
  * std      0.119273
  * min      0.039493
  * max      0.538605
* `relectricperincome`: unimodal @~0.2, right skew
  * count   130.000000
  * mean      0.206968
  * std       0.217425
  * min       0.000000
  * max       1.453452


## Scatterplot and interpretation

![Composit Variables](/w4-urbanrate-oilperincome-scatter.png)
![Composit Variables](/w4-urbanrate-relectricperincome-scatter.png)
￼
Although the oil and electrical consumption per person both increases with income, the consumption of both these energy measures per income decreases with the urban population ratio. This suggest that urbanization might be a driver in reducing energy consumption for a given income level.
