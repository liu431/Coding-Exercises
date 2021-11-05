
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
