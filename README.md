# Study Notes

*purpose: sharing your work & insight*
*github.com/hville/study-notes*

## 1. Data Management and Visualization

*Coursera Data Analysis and Interpretation Specialization*

### Week 1

* population vs sample
* representative sample > exploratory data analysis > inference (knowledge about population)
* unit of observation > variables
* individuals x variables
* categorical(dummy codes) vs quantitative vs unique identifier
* DATASETS
  * Adolescent Health (Add Health) school-based survey
    * social, economic, psychological, and physical wellbeing of adolescents.
  * Mars Crater Study.
    * characteristics of >350,000 craters
  * NESARC
    * mental health and substance use disorders
  * [gap minder](gapminder.org)
    * numerous measures from 195 countries
* code book : how the data are arranged in the computer file
* [**week-1 task**](data-visualization-w1.md)

### Week 2

* Exploratory Data Analysis
  * organize, sumarize, patterns, deviations
  * examine distribution
* python
  * [www.continuum.io](https://www.continuum.io/)
* [**week-2 task**](data-visualization-w2.md)
* [**week-2 code**](./code/code_w2.py)

### Week 3

* Data Management: decisions about data
  * tools: code book, frequency distribution
  * trim missing Data (NaN for python)
  * rescale/normalise variables (same units)
  * reverse scaling (recoding frequency vs time)
  * secondary variables (combination of variables)
  * categorical --> quantitative
  * quantitative --> categorical
* [**week-3 task**](data-visualization-w3.md)
* [**week-3 code**](./code/code_w3.py)

### Week 4

* new plotting python functions
  * `.groupby(...)`, `.astype(...)`, `.countplot(...)`
  * `.xlabel(...)`, `.title(...)`
  * qualitative: `.distplot(...).dropna()`
* distribution shape
  * histogram (count per intervals)
  * shape
    * centering, symetry, skeyness
    * peakness | modality
  * center
    * mode(frequency), average(expected), median(half point)
  * spread
    * spread | range | min&max | standard deviation
    * variance `1/(N-1) * ∑(x-E)`
  * `.groupby(...).describe()`
* role of variables
  * X: explanatory, independent, predictor
  * Y: response, dependent, outcome
* plot
  * C->C: bar chart (`seaborn.factorplot`)
    * 2 cat response variable: eg 0:No, 1:Yes
  * Q->Q: scatterplot (`seaborn.regplot`)
    * or C=bin(Q): barchart
  * Q->C: bin Q in 2 cat (eg 0:No, 1:Yes)
  * C->Q: C->E(Q) barchart
* [**week-3 task**](data-visualization-w3.md)
* [**week-3 code**](./code/code_w3.py)
