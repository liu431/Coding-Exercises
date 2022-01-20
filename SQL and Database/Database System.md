## Notes

[GaTech CS 6400: Database Systems Concepts and Design](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design)

[Book - Elmasri & Navathe: Fundamentals of Database Systems. 7 Edition. Pearson 2016.](https://www.amazon.com/Fundamentals-Database-Systems-Ramez-Elmasri/dp/0133970779)

### Fundamentals Of Databases
* Models: represent a perception of structures of reality; helpful to examine or manage part of the real world
  * only emphasizes selecetd aspects
  * is described in some language
  * can be erroneous
  * may have featues that are not exist in reality
  * When to use: data intebnsive apps; persistent storage of data; centralized control of data; control of redundancy; control of consistency and integrity; multiple use support; data sharing; documentation; independence; control of access abndsecurity; backup and recovery

* Data modeling: fix a perception of structures of reality and represent this perception
* Process modeling: may be represented by 1. embedded in program code; 2. executed ad-hoc
* Data models: data structures; integrity constraints; operations
  * Entity-relationship model
  * Relational model: tables (schema: table name, data type, rows/columns); constraints (rules that cannot be expressed by the data structures alone);
  * Hierarchical model
* Keys: uniqueness constraints
* Surrogate: system-generated, unqiue, internal identifiers; represent an entity of the real world inside the database; immutable by the application programs
* Integrity: database reflects reality well; Consistency: database doesn't have internal conflicts
* ANSI/SPARC 3-level DB architecture: separate schema and data
  * External schema: use of data; describe parts of the information in the conceptual schema in a form convenient to a particular user group's view; derived from the ceonceptual schema; `view` virtual table
  * Conceptual schema: meaning of data; describe all conceptually relevant, general, time-invariant structural aspects of reality; exclude aspects of data representation and physical organization, and access
  * Internal schema: storage of data; describe how the information described in the ceonceptual schema is physically represented to provide the overall best performance 
* Physical data independence: a measure of how much the internal schema can change without affecting the application programs
* Logical data independence: a measure of how much the conceptual schema can change without affecting the application programs
* Metadata 
  * System metadata: critical in a DBMS
  * Business metadata: critical in a data warehouse  











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
 
