
```python
# Import packages
import numpy as np
import pandas as pd
# Load data
df = pd.read_csv(file)
```

## Pandas
### Dataframe
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
