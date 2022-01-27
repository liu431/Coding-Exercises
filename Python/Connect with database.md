## Notes

[Real Python - Introduction to Python SQL Libraries](https://realpython.com/python-sql-libraries/)

### Connect with SQL database to get data

```python
# sqlalchemy: a Python SQL toolkit that provides us flexibility to make connection to various RDBS
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

### Pandas methods 
```python
# Extract data from Source
pd.read_sql_query('select * from Sales',engine)
# Join tables
pd.merge(Sales, SalesPerson, on='SalesPersonID', how='left')
# Write to RDBS
df.to_sql('SalesReport', con=engine, if_exists='replace', index=False)
```

### Get query results as a list
```python
def GetList():
    '''Return query results as a list'''
    query = """
            SELECT * FROM TABLE
            """
    with engine.connect() as con:
        result = con.execute(query)
        res_list = [row[0] for row in result.fetchall()]
        con.close()

    return res_list
    
GetList()
```

### Get query results as a dataframe
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

### Add new records
```python
def AddStudent(age, name):
    '''Add information in the table'''
    query = """
            INSERT INTO TABLE (age, name)
            VALUES = (?, ?)
            """
    with engine.connect() as con:
        con.execute(query, (age, name))
        con.close()
    return None
    
AddStudent(age=30, name='John')
```





