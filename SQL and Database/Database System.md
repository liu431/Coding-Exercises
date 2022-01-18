## Notes

[GaTech CS 6400: Database Systems Concepts and Design](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design)

[Book - Elmasri & Navathe: Fundamentals of Database Systems. 7 Edition. Pearson 2016.](https://www.amazon.com/Fundamentals-Database-Systems-Ramez-Elmasri/dp/0133970779)

### Fundamentals Of Databases

### Methodology I: ANALYSIS

### Extended-Entity Relationship Model

### Methodology II: SPECIFICATION

### EER Relational Mapping

### Methodology III: DESIGN

### Normalization

### Methodology III: Design (SQL Statements)

### Relational Algebra And Calculus

### SQL (Structural Query Language)
* Based on relational tuple calculus and some algebra
* Insert, Delete, Update

```sql
# Insert
INSERT INTO Students(Email, StudentName, StartYear)
  VALUES('abc@gt.edu', 'Harry', 2022)
  
# Delete
DELETE FROM Students
WHERE StartYear = 2021

# Update
UPDATE Students
SET StudentName = 'Ben'
WHERE Email = 'abc@gt.edu'
```

* Syntax
  - use * wildcard for all columns); specify needed columns for projections
  - DISTINCT() to only keep distinct values
  - If there are no same-named attributes, teh NATURAL JOIN defaults to Cartesian product
  - String matching
    - % matches any string, including the empty string, Ex: LIKE 'San%'
    - _matches any single character, Ex: LIKE 'A____'
  - Set operations
    - UINION: values that show up in eithor of sets without duplicates; UNION ALL: with duplicates
    - INTERSECT: values that show up in both of sets without duplicates; INTERSECT ALL: with duplicates
    - EXCEPT: values that show up in Set A and not in B without duplicates; EXCEPT ALL: with duplicates
  - Build-in functions - count, sum, avg, min, max
  - HAVING: condition on the group
  - Nested queries 
    - IN / NOT IN
    - =, <>, <=, >=, <, >, {ALL | ANY | SOME}
  - Correalted: WHERE NOT EXISTS 
    - Think of it as a sub-query evaulates once for each row of the outer query 

```sql
SELECT column1, column2, ...
FROM table1, table 2, ...
WHERE condition (AND, OR, NOT)
```






### Efficiency

### Methodology IV: Implementation

### Metadata
 
