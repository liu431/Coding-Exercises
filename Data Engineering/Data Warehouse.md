## Notes 

Taken from [Udemy class Data Warehouse Fundamentals for Begineers](https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/)

[Tutorialspoint Data Warehousing Tutorial](https://www.tutorialspoint.com/dwh/index.htm)

### Data Warehousing Concepts
#### Value
Data warehousing is the fundemental underpinning of modern data-driven decision making (past, present, future, the unknown).

Bill Inmon (1990): a data warehouse is a subject oriented, integrated, time-variant, and non-volatile collection of data

#### Terminologies
* Metadata: data that are used to represent other data
* Metadata Repository: contains the following metadata (Business, Operational, Data for mapping from operational environment to data warehouse, The algorithms for summarization)
* Data Cube: represent data in multiple dimensions; defined by dimensions and facts
* Data Mart: subset of organization-wide data that is valuable to specific groups of people in an organization
 
#### Process Flow 
* Extract and load the data.
* Cleaning and transforming the data.
* Backup and archive the data.
* Managing queries and directing them to the appropriate data sources.

#### What is a data warehouse

* A warehouse filled with data
* Build on top of some types of databases
* Data are copied from external sources
* Integrated, subject oriented, __time variant__, __non volatile__

#### Compare with other tools
* Data lake is built on top of big data sources.
* Data virtualization is read-only DDBMS (distributed database management system).

### Data Warehousing Architecture

#### Business Analysis Framework
* Top-down view: allows the selection of relevant information needed for a data warehouse.
* Data source view: presents the information being captured, stored, and managed by the operational system.
* Data warehouse view: includes the fact tables and dimension tables. It represents the information stored inside the data warehouse.
* Business query view : view of the data from the viewpoint of the end-user

#### Three-Tier Architecture
* Bottom Tier − the data warehouse database server. It is the relational database system. We use the back end tools and utilities to feed data into the bottom tier by performing the Extract, Clean, Load, and refresh functions.

* Middle Tier − the OLAP Server that can be implemented in either of the following ways.
  - By Relational OLAP (ROLAP): an extended relational database management system; maps the operations on multidimensional data to standard relational operations.
  - By Multidimensional OLAP (MOLAP) model: directly implements the multidimensional data and operations.
* Top-Tier - the front-end client layer; holds the query tools and reporting tools, analysis tools and data mining tools.

#### Online Analytical Processing Server (OLAP) 

* Relational OLAP (ROLAP): uses relational or extended-relational DBMS
List of OLAP operations
  - Roll-up: performs aggregation on a data cube by climbing up a concept hierarchy for a dimension or dimension reduction
  - Drill-down: one or more dimensions from the data cube are added
  - Slice: select one particular dimension from a given cube and provides a new sub-cube
  - Dice: selects two or more dimensions from a given cube and provides a new sub-cube
  - Pivot (rotate): rotates the data axes in view in order to provide an alternative presentation of data
   
* Multidimensional OLAP (MOLAP): uses array-based multidimensional storage engines for multidimensional views of data
* Hybrid OLAP (HOLAP): offers higher scalability of ROLAP and faster computation of MOLAP
* Specialized SQL Servers: provides advanced query language and query processing support for SQL queries over star and snowflake schemas in a read-only environment

#### Centralized Data Warehouse
* Use single database; One stop shopping for data to support business decisions
* Hostorical challenges: technology, work processes
* Today's challenge: organizational & human factors

#### Data Mart
* Smaller scale, narrowly-focused data warehouse
* Two types: dependent and independent (whether it draws data from warehouse or sources)
* Data warehouse vs independent data mart: warehouse has data from many sources; data marts has one or some sources
* Analogy: data marks as retailers; warehouse as wholesaler

#### Component-Based Data Warehouse
* Multiple decomposited components operating together for the data warehouse environment
* Disadv: inconsistent data; difficult to cross-integrate

#### Cube = Multidimentional database (MDBMS)
* Not a relational database
* Specialized "dim-aware" database
* Alterntaive for smaller-scale data warehouse and data marts
* Fast uery response time for "modest" data volumes
* Less flexible data structures than RDBMS

#### ODS (Operational Data Store)
* Integrate current operational data from multiple sources
* Often real-time source -> ODS data feeds -> "What is happening now?"
* Superseded by big data (velocity needs)

#### Staging Layer
* Important part in Extraction as landing zone
* Pull the data as quickly as possible from data sources
* Persistent vs Non-persistent: whether or not delete dat athat are already moved to user layer

### Bring Data Into Data Warehouse - ETL: Extract, Transform, Load
* Extract: quickly pull raw data from source applications; traditionally done in "batches"; land in data warehouse staging layer
* Transform: prepare for __uniform__ data in user access layer
* Load: store uniform data in user access layer

#### ELT
* Load the data before transformation
* "Blast" data into big data environment, such as Hadoop HDFS, AWS S3, etc
* Likely used when building data lake

[Comparison](https://www.xplenty.com/blog/etl-vs-elt/#comparison)

#### Initial loading ETL
* Normally one time only
* Before data warehouse goes live
* All __relevant__ data definitely/probably needed for BI and analytics; not all possible source data

#### Incremental ETL
* Incrementally "refreshes" the data warehouse
* Bring in new and modified data
* Special handling for deleted data
* Keep DW up to data
* 4 patterns
  - Append
  - In-place update
  - Complete replacement
  - Rolling append

#### Data Transformation
* Goal: "Apple to Apple" comparison -> uniformity, restructuring
* Models: 
  - Data value unification of value, type, size
  - De-duplication of same record from different systems
  - Dropping columns (vertical slicing) of unnecessary information
  - Value-based row filtering (horizontal slicing)
  - Correcting known errors

#### Mix-and-Match Incremental ETL
* Frequency of ETL feeds: Daily, Daily, Hourly, Weekly...
* Types of ETL feeds: Append, Replace, Rolling Append...

### Data Warehousing Design: Building Blocks

* BI Category drives data model
  - Basic reporting -> Dimensional
  - Online analytical processing (OLAP) -> Dimensional
  - Predictive analytics -> Data minig/specialized
  - Exploratory analytics -> Data minig/specialized

* Dimensionality (what does the data column measure)
  - One or more measurements (quantifiable; such as average annual salary, max time )
  - Dimensional context of each measurement (__By__(sliced and grouped), __For__(one or more specific values))
 
* Facts, Fact Tables, Dimensions, and Dimension Tables
  - Facts: numeric and quantifiable, measurement/metric
  - Fact table: store facts
  - Dimensions: context of a fact (Ex. department, major, student, employee, building)
  - Dimension Tables: store dimensions

* Additivity in Facts
  - Facts that could be aggregated. Ex. employees' salary, students' credit hours
  - Non-additive facts
    - Ex. GPA, margins, percentages, ratios
    - Possibly store them for individual row easy access 
    - Calculate aggregate averages, ratios, percentages, etc   
  - Semi-additive facts
    - Sometimes could be added; sometimes not  
    - Typically used in periodic snapshot fact tables

* Star Schema vs. Snowflake Schema

| Star | Snowflake |
| --- | ----------- |
| All dimensions along a given hierarchy in one dim table | Each dim/dimensional level in its own table |
| Only one level away from fact table along each hierarchy | One or more levels away from fact table along each hierarchy |
| With one fact table visually resembles a star | With one fact table visually resembles a snowflake |
| Overall fewer database joins for drilling up/down | Overall more databases joins for drilling up/down |
| Database primary -> foreign key relationships straightforward | Database primary-> foreign key relationships more complex|
| Typically more database storage needed for dim data | Typically less database storage needed for dim data |
|"Denormalized" dimension table data | "Normalized" dimension table data |

* Database Keys 
  - Primary  vs. foreign keys
    - Primary: unique identifier for each row in a table; could be a column (field)
    - Foreign: some other tables' primary key; used to indicate logical relationship; help improve query performance 
  - Natural vs. surrogant keys
    - Natural: might be "cryptic" or "understandable"; travel from source systems with the rest of the data; keep as "secondary keys"
    - Surrogate (preferred to be used as primary key): no business meaning; generated by the database itself or a supplemental system

### Dimensional Modeling (Design Facts, Fact Tables, Dimensions, and Dimension Tables)
* Design Dim Tables
  - Name: Suffix with _DIM, Ex Faculty_DIM
  - Snowflake scheme PK-FK rules
    - 1 table for each level of a hierarchy
    - Every non-terminal dimension has 1. primary/surrogate key; 2. the next highest level's primary/surrogate key as a foreign key

* Fact Tables

Primary key: combination of all foreign keys (surrogare) relating back to dim tables

  - Transaction: record facts (measurements) from transactions
    - Rule 1: facts available at some grain (level of detail)
    - Rule 2: facts occur simultaneously; such as whether they are same business processes
 
  - Periodic snapshot: track a given measurement at regular intervals -> easier and more direct access for certain types of business qns
    -  Type 1: aggregated result of "regular" transactions
    -  Type 2: levels that are not related to "regular" transactions; no transactions from which the levels are built
  - Accumulating snapshot: track the process of a business process through formally defined stages
    -  Measure elapsed time spent in each phase
    -  Include both completed and in-progress phases
    -  Could also track other measures as process proceeds
    -  Introduce concept of multiple relationships from fact table back to a single dim table
    - Ex. Student financial aid applications (multiple processes)
      - Dim: Student, Time, Employees responsible for each phase
      - FinAid_Accumul_Snapshot: Student_Key (PK, FK), Day_Submitted_Key (PK, FK), Day_Screening_Key (PK, FK), Day_Prelim_Key (PK, FK), Day_Final_key (PK, FK), Day_Payment_Key (PK, FK), Emp_Screen_Key (PK, FK), Emp_Prelim_Key (PK, FK), Emp_Final_Key (PK, FK), Emp_Payment_Key (PK, FK), Days_Screening, Days_Prelim_Decision, Days_Final_Decision, Days_Decision_to_Pmt
  - Factless (measure the occurrence)
    - Record occurrence of a transaction that has no measurements
      - Use cases: track an occured event but nothing significant to meausre
      - Tracking fact, value = 1; SUM() rather than COUNT()
      - Ex. Registration of a webinar
        - Track: which student registered, for each webinars, dates
        - Webinar_Reg_Fact (factless): Student_Key (PK, FK), Date_Reg_Key (PK, FK), Date_Sched_Key (PK, FK), Webinar_Key (PK, FK)
        - Webinar_Attend_fact (transaction): Student_Key (PK, FK), Date_Held_Key (PK, FK), Webinar_Key (PK, FK), Attend_Duration
        - Could count rows with/without filters

    - Record coverage or eligibility relationships or association among multiple parties
      - Typically between a starting and ending date or time
      - Ex. Academic advisors assigned to students
        - Advisor_Assign_fact: Student_Key (PK, FK), Advisor_Key (PK, FK), Date_Begin_Key (PK, FK), Date_End_Key (PK, FK)

* SQL for Dim and Fact Tables
  - Star schema dim tables
    ```sql
    CREATE TABLE FACULTY_DIM (
    Faculty_Key    INT NOT NULL,
    Faculty_ID     VARCHAR(10) NOT NULL,
    Year_Joined    INT,
    ...
    Dept_ID        VARCHAR(10) NOT NULL,
    ...
    College_ID     VARCHAR(10) NOT NULL,
    ...
    PRIMARY KEY(Faculty_Key)
    );
    ```
    
   - Snowflake schema 
     - Non-terminal dim tables
     ```sql
     CREATE TABLE FACULTY_DIM (
     Faculty_Key    INT NOT NULL,
     Faculty_ID     VARCHAR(10) NOT NULL,
     Year_Joined    INT,
     Department_Key INT NOT NULL,
     PRIMARY KEY(Faculty_Key),
     FOREIGN KEY (Department_Key) REFERENCES Department_DIM (Department_Key)
     );
     ```

     - Terminal dim tables (no foreign key to references other tables)
     ```sql
     CREATE TABLE College_DIM (
     Faculty_Key    INT NOT NULL,
     Faculty_ID     VARCHAR(10) NOT NULL,
     Year_Joined    INT,
     PRIMARY KEY(College_Key),
     );
     ```

   - Transaction-grained fact table
     ```sql
     CREATE TABLE Tuition_Bill_Fact (
     Student_Key       INT NOT NULL,
     Date_Key          INT NOT NULL,
     Tuition_Bill_Amt  DECIMAL(8,2) NOT NULL,
     PRIMARY KEY (Student_Key, Date_Key),
     FOREIGN KEY (Student_Key) REFERENCES Student_DIM (Student_Key),
     FOREIGN KEY (Date_Key) REFERENCES Date_DIM (Date_Key)
     );
     ```   

   - Periodic snapshot fact table
     ```sql
     CREATE TABLE Meal_Card_Pmt_Fact (
     Student_Key        INT NOT NULL,
     Date_Key           INT NOT NULL,
     Campus_Food_Key    INT NOT NULL,
     Meal-Card_Balance  DECIMAL(8,2) NOT NULL,
     PRIMARY KEY (Student_Key, Date_Key, Campus_Food_Key),
     FOREIGN KEY (Student_Key) REFERENCES Student_DIM (Student_Key),
     FOREIGN KEY (Date_Key) REFERENCES Date_DIM (Date_Key),
     FOREIGN KEY (Campus_Food_Key) REFERENCES Date_DIM (Campus_Food_Key)
     );




### Slowly Changing Dimensions
* Techniques to manage history within data warehouse
* Enables warehouse to appropriately manage history regardless of policies in transactional applications
* 3 main policies for historical data
  - (Always retain original value -> Type 0)
  - Overwrite old date; no history retention -> Type 1
  - __Maintain unlimited history with new row -> Type 2__
  - Maintain limited history with new column -> Type 3

* Compare 3 main SCD types

| SCD Type | Techniques | Implications |
| -------- | ---------- | ----------- |
| Type 1 | "In-Place Update" ETL pattern | Simpliest, but no history maintained
| Type 2 | Create new dim table row for each new history version | Most architecturally complex, but robust representation of history |
| Type 3 | Smallest number of dim table columns for multiple history versions | Easily switch back and forth between "as-is" and "as-was" reporting, but limited use cases |

* Design a Type 1 SCD
  - Replace old value with new value at same place; common for correct errors
  - UPDATE statement

| Adv | Disadv | 
| -------- | ---------- |
| Simpliest and most straightforward | Might still want hostory of errors for auditing purposes|
| Data warehouse content errors are purged forever | Reporting before and after Type 1 change could vary |
| best for error correction and any other "don't need any history" situations | Tendency to overuse Type 1 changes since much simpler than Type 2 |


* Design a Type 2 SCD
  - Existing row remains as-is; common for new/update attribute value
  - New row added to the dim table
  - New role reflects current state of all attributes
  - Complications with reporting and analytics
  - Best handled through careful "multi-step" SQL between dim tables and fact tables
  - Indicate order of versions
    - Use Current_Flag 
    - Use effective/expiration dates
    - Kimball (DW Toolkit): use both flag and effective/expiration dates
 
 * Design a Type 3 SCD
   - Add new column rather than new row to reflect changes
   - "Old value" column and "new value" column
   - For flexible reporting
   - Use case where every row in a dim table is changed at the same time, such as reorganization
   - Could have 3 or 4 columns

### Design ETL
* Factors for design: ETL architecture, Dim & Fact table models, Star & Snowflake schemas, Slowly changing dim
* Limit amount of incoming data to be processes; use "change data capture" (use transactional data timestamps to process only new data)
* Process dim tables before fact tables as dimension table surrogate keys are needed for fact tables
* Opportunities for parallel processing
* ETL for Dim table with star scheme
  - Step 1: prepare data; significant smallest amount of data subset
  - Step 2: transform data
  - Step 3: process new dim rows
    - For each row:
      - If new: add to DIM table
      - If not new: process any Type 1 and Type 2 changes
  - Step 4: process SCD Type 1 changes
    - Basic in-place update
    - Might need to apply any given Type 1 change to more than 1 row; Look for all dim table rows for that natural key 
  - Step 5: process SCD Type 2 changes
    - Basic append with new surrogate key
    - Use natural key as the guide

* ETL for fact tables
  - Transactional systems provide natural keys
  - Recommend using combination of both flag and effective/expiration dates


### Environment
#### Cloud vs. On-premise
* Adv to cloud-based DH
  - Offload routine syste, maintenance and upgrades
  - Lower initial platform investment
  - Diaster recovery
  - Data lake/big data synergies

* Disadv to clou-based DH
  - Security
  - Migrate existing DWs from on-premises to cloud
  - Cloud-to-cloud data transport
  - Expensive for data egress

* Trend
  - Shift to cloud
  - Dake lakes alongside or succeed DH

Think dimensional (at least for user-facing BI)!























