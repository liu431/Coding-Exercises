## Date and Time

### datetime
```python
import datetime
```

#### Display the current date
```python
datetime.datetime.now()
```

#### Datae objects
```python
# Create a date object
x = datetime.datetime(2021, 1, 2)
# Format date objects into readable strings
x.strftime("%B") # January
x.strftime("%m") # 01
x.strftime("%Y") # 2021
x.strftime("%d") # 02


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


## Pandas
```python
# Import packages
import numpy as np
import pandas as pd
# Load data
df = pd.read_csv(file)
```
### Dataframe
#### [df.to_numpy](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html)
```python
# Convert the DataFrame to a NumPy array
df.to_numpy()
```

#### [df.is_null](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)
#### [df.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)

```python
# Detect and fill missing values with 0
na_values = df.is_null().to_numpy().sum()
if na_values > 0:
    df = df.fillna(0)
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
df.sort_values(by=['Date'], ascending=False) # Sort by Date in descending order
```

#### [df.iterrows](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
```python
# Iterate over df rows as (index, series) pairs
for index, row in df.iterrows():
    print(row['Name], row['Date])
```
