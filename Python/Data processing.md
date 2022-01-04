## Date and Time

### datetime
```python
import datetime
```

#### Display the current date
```python
datetime.datetime.now()
```

#### Data objects
```python
# Create a date object
x = datetime.datetime(2021, 1, 2)
# Format date objects into readable strings
x.strftime("%B") # January
x.strftime("%m") # 01
x.strftime("%Y") # 2021
x.strftime("%d") # 02
```

#### Waiting week days
```python
from datetime import datetime
def WeekDays(Days):
    '''Calculate the waiting week days by excluding the weekends'''
    if Days >= 5:
        Days = Days - 2 * (Days // 5)
    else:
        # When time clock starts from late last week or during the weekend
        if Days > datetime.today().weekday():
            if Days >= 2:
                Days -= 2
            else:
                Days = 0
    return Days
WeekDays(1) # Work done by last Sunday -> 0
WeekDays(2) # Work done by last Saturday -> 0
WeekDays(3) # Work done by last Friday -> 1
WeekDays(4) # Work done by last Thursday -> 2
WeekDays(5) # Work done by last Wednesday -> 3
```

#### Convert between month name and month number
```python
# abbreviated month name
month_name = "Jan"
month_number = datetime.datetime.strptime(month_name, "%b").month # 1

# full month names
month_name = "January"
month_number = datetime.datetime.strptime(month_name, "%B").month # 1
```

## List, Arrays
#### List comprehension
```python
# Remove empty string form list
list(filter(None, ['', 'abc', ''])) # ['abc']

# Create new lists with range of values
a = np.arange(1,11)
# Create list with odd values
b = [i for i in a if i%2 == 1]
# Create list with values from a but not in b
c = [i for i in a if i not in b]
```

## Numpy
#### [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
```python
# Recode gender
genderList = np.array(['Male', 'Female', 'Male'])
np.where(genderList == 'Male', 1, 0) # array([1, 0, 1])
```

#### Export data
```python
np.savetxt('output.csv', df, delimiter=',', fmt='%1.3f')
```

## Pandas
```python
# Import packages
import numpy as np
import pandas as pd
# Load data
df = pd.read_csv(file)
```
### Dataframe
#### [pd.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
```python
listA = [1,2]
listB = [3, 4]
df = pd.DataFrame({'A': listA, 'B': listB})
```

#### [df.to_numpy](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html), [df.is_null](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html), [df.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)

```python
# Detect and fill missing values with 0
na_values = df.is_null().to_numpy().sum()
if na_values > 0:
    df = df.fillna(0)
```

#### [df.sum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)
```python
df.sum(axis = 0) # Sum over the index
df.sum(axis = 1) # Sum over the columns
df['A'].sum() # Sum of one column

```

#### [df.apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
```python
# Get the last name from the Name column
df['Name'].apply(lambda i : i.split(' ')[-1])
```

#### [df.str.contains](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html)
```python
# Return rows where Name column contains/doesn't contain certain strings; Fill False value for missing values
df[df['Name'].str.contains('Ben', na=False)]
df[~df['Name'].str.contains('Ben', na=False)]
```

#### [df.drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
```python
# Return df with duplicated rows of same name removed
df.drop_duplicates([subset=['Name']])
```

#### [df.sort_values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
```python
# Return sorted df by certain values along certain axis
## Sort in place
df.sort_values(by=['Date'], ascending=False) # Sort by Date in descending order
## Store sorted object and replace the existing object
df = df.sort_values(by=['Date'])
```

#### [df.iterrows](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
```python
# Iterate over df rows as (index, series) pairs
for index, row in df.iterrows():
    print(row['Name], row['Date])
```

#### Set one column as index
```python
def column2Index(df, colname='ID'):
    '''Set index column as the dataframe index'''
    df.index = df[colname]
    df.drop([colname], axis=1, inplace=True)
    return df
```

### Summary of commands
![](https://media-exp1.licdn.com/dms/image/C4E22AQGEBF8Ihm81ng/feedshare-shrink_800/0/1640185264820?e=1643241600&v=beta&t=6TQHBPZPpuRpL5ue0hQNNk6hNUo_J91sgIaGlt9dlms)
