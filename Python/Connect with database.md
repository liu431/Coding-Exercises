## Connect with SQL database to get data

```python
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, inspect
server = ''
database = ''
username = ''
password = ''
driver= '{ODBC Driver 17 for SQL Server}'
conn = f"""Driver={driver};Server={server},1433;Database={database};Uid={username};Pwd={password};Network=DBMSSOCN;Connection Timeout=30;"""
params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
engine = create_engine(conn_str, echo=False)
```

### Get query results
```python
def GetTable():
    '''Return query results as a pandas dataframe'''
    query = """
            SELECT * FROM TABLE
            """
    with engine.connect() as con:
        result = con.execute(query)
        df = pd.DataFrame((tuple(t) for t in result.fetchall()), columns = result.keys())
        con.close()

    return df
    
GetTable()
```

### Update table columns
```python
def UpdateTable(age, name):
    '''Update information in the table'''
    query = """
            UPDATE TABLE
            SET
            Age = ?
            WHERE Name = ?
            """
    with engine.connect() as con:
        con.execute(query, (age, name))
        con.close()

    return df
    
UpdateTable(age=25, name='Ben')
```
