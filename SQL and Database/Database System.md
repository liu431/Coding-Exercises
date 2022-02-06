## Notes

[GaTech CS 6400: Database Systems Concepts and Design](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design)

[Book - Elmasri & Navathe: Fundamentals of Database Systems. 7 Edition. Pearson 2016.](https://www.amazon.com/Fundamentals-Database-Systems-Ramez-Elmasri/dp/0133970779)

### Fundamentals Of Databases
* Database: a collection of related data that represents some aspect of teh real world
* Database management system (DBMS): computerized system that enables users to create and maintain a databse
* Program-data independence: the structure of data files is stored in the DBMS catelog separately from the access programs
* Operations: 1. interface (operation name and the data types of its argument/parameters); 2. implementation (sepecified separately and can be changed without affecting the interface)
* Data abstraction: program-data independence and program-operation independence; suppression of details of data organization and storage and the highlighting of the essential features for an improved understanding of data
* Transaction: an executing program or process that includes one or more database accesses, such as reading or updating of databse records
* Data normalization: a database deisgn that stores each logical data item in only one place in the database
* Denormalization: don't have to search multiple files to collect this data by placing all the data together
* Advantages of using DBMS
  * Control redundancy: avoid storing the same data multiple times
  * Restrict unauthorized access: security and authorization subsystem to specify account restrictions
  * Provide persistent storage for program objects and data structures
  * Provide storage structures and search techniques for efficient query processing
  * Provide backup and recovery
  * Provide multiple user interfaces (GUIs)
  * Represent complex relationships among data
  * Enforce integrity constraints and business rules
  * Permit inferencing and actions using rules and triggers; stored procedures
  * Potential for enforcing standards
  * Reduced application development time
  * Flexibility to change the structure as requirements change
  * Availability of up-to-date information
  * Economies of scale by reducing overall costs of operation and management 
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
* State/Snapshot/Current set of occurences or instances: data in teh database at a particular moment in timw
* 3-schema architecture
  * Internal level: has internal schema that describes the physical storage structure of the database
    * Physical data independence: capacity to change the internal schema without having to change the conceptual schema 
  * Conceptual level: has conceptual schema that describes the structure of the whole database for a community of users
    * Logical data independence: capacity to change the conceptual schema without having to change the external schema 
  * Exernal or view level: describes the part that a particular use group is interested in and hides the rest
 * Languages
   * Data definition language (DDL): define the conceptual and internal schemas
   * Storage definition language(SDL): specify the internal schema
   * View definition language (VDL): specify user views and their mappings to the conceptual schema
   * Data manipulation language (DML): retrieval, insertion, deletion , and modification of the database
     * Low level / procedural: record-at-a-time, embedded in a general-purpose language
     * High level (such as SQL): set-at-a-time, declarative (which data to retrieve rather than how to retrieve it)   
*  Utilities
   * Loading: load existing data files
   * Backup: create a backup copy of the database to restore in case of catastrophic disk failure
   * Storage reorganziation: create new access paths to improve performance
   * Performance monitoring: provide statistics to DBA for making decisions
* Client/Server
  * Client: a user machine that provides user interface capabilities and local processing
  * Server: system containing both hardware and software that can provide services to the client machines
  * 3-tier: GUI/Web Interface (Presentation Layer) <-> Application Programs/Web pages (Business Logic Layer) <-> DBMS (Database Services Layer) 
 
 
### Entity Relationship Model

* Entity (rectangular box in ERD): reprsent object or concept in the real world
  * Entity type: define a collection of entities that have the same attribute
  * Entity set/collection: collection of all entities of a particular entity type in the database at any point in time 

* Attributes (ovals in ERD): particular properties that describe the entity; key attribute to identify each entity uniquely (underlined in ERD)
  * Single-valued: things that name other things, types could be lexical, visable, audible; associated with value sets 
  * Multi-valued (double ovals in ERD): one entity links with multiple properties 
  * Composite (double ovals in ERD): combine properties (Ex. Address; could be divided into smaller subparts)
  * Derived (dotted line in ERD): determined from the stored attributed (Ex. age from birth_date)
  * NULL: 1. missing values; 2. not known whether the attribute values exists
  
* Relationship types (diamond-shaped box in ERD)
  * Degree
    * Binary: 2 participating entity types
    * Tenary: 3 participating entity types
  * Types 
    * 1-1: partial function; names of multiple relationship types between the same two entity types must be unique
    * 1-N: partial function; Ex. employer with many employees 
    * Mandatory 1-N: total function; Ex. each employee must be linked to one employer
    * N-M: many to many
    * N-ary: need multple attributes to uniquely identify one instance
    * Many: cannot be reduced to a conjunction of binary relationship types
    * Recursive/self-referencing: model hierarchy structure; same entity type name participates more than once in different roles

  * Structural constraints
    * Total participation / existing dependency (double line in ERD): every entity in the total set of employee entities must be related to a department entity via WORKS_FOR
    * Partital participation (single line in ERD): some of the set of employee entities are related to some department entity via MANAGES, but not necessarily all.
  * Attributes
    * 1:1: determined by either side
    * 1:N: can be migrated only to the entity tpe on the N-side
    * M:N: determined by the combination of participating entities in a relationship instance 
  * Weak entity types (surrounded with double lines in ERD): entity types that don't have key attributes of their own
    * When the primary key of one of the related entities does not contain a primary key component of the other related entities
    * Have a partial key that can uniquely identify weak entities that are related to the same owner entity
    * Strong entity types: have a key attribute
    * Identifying relationships (double diamond in ERD): when the primary key of the related entity contains the primary key of the “parent”; at most one instance of the identified entity; each entity is uniquely referenced

### Enhanced Entity-Relationship Model (EER)
* Class/subclass relationship (circle in ERD)
  * Every entity that is a member of one of the _Subtype / Subclass_ is alao of the _superclass/supertype_ entity type 
  * Inheritance: subtypes inherit properties from supertypes
* Specialization and Generalization
  * Specialization: process of defining a set of subclass of an entity type; subclasses could have specific attributes
    * Attribute-defined (arc in ERD): all subclasses in a specialization have their membership condition on the same attribute of the superclass
    * Disjointness (d in ERD): subclasses of the specialization must be disjoint sets
    * Overlapping (o in ERD): same entity may be a member of 1+ subclasses of the specialization
    * Completness
      * Total (double line in ERD): every entity in the superclass must be a member of at least one subclass
      * Partial (single line in ERD): allow an entity not to belong to any of the subclasses  
  * Generalization: suppress the differences among several entity types, identify common features, and generalize them into a single superclass

* Union entity types: subclass represents a collection of objects that is a subset of the UNION of distinct entity types


### Relational model
  * Data structures, Constraints, Operations, Algebra Calculus (tuple calculus-SQL, domain calculus-QBE) 
  * The value of a relation is independent of attribute order and tuple order.

### EER Relational Mapping


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


### Metadata







### Methodology
#### I: ANALYSIS
* Assumptions: known business processes, documents, tasks, system boundary; one database schema unifying all views can be designed 
* Software process: Business process redesign -> __Analysis__(information flow diagram) -> __Specification__(tasks, ER diagram) -> __Design__ (abstract code with SQL, relational schema) -> __Implementation__(PHP code with SQL, MySQL relational platform) -> Testing
* Information flow diagram 
  * Soild line for potential flow; dashed line for system boundary 
  * never connect two documents or two tasks
* Requirements of the social network app example
  * Uniquely identify user by email address and password combination (input document)
  * For new user registration, information will be written into the database (input document)
  * Edit User profile contains Sex, Birthdate, CurrentCity, Hometown, Interests, Education, Professional (input & output document)
  * View profile screen (output document)
  * Friend requests (input & output document)
  * Search for friends (output document)
  * Friends list (output document)
  * Users must be either regular users or admin users (with last login); inherit properties for supertype User
  * List of schools with graduation date; same school could appear multipel times; each school must have a schooltype 
  * List of employers with name and titles; same employer appear multiple times with different titles
  * Friend request (1-N)




#### II: SPECIFICATION
* Output: EER diagram, data formats, constrainst, task decomposition
* Observation on what goes into and comes out of the database
  * Everything in the database must come from somewhere
  * Everything on the input documents must go somewhere
  * Everything in the database must be used for something
  * Everything on the output documents must come from somewhere
* Use attribute names from the document in the EER
* Data formats:  __beg, steal, borrow__ best practices
* Constraints
  * DateConnected is NULL until request is accepted
  * Cannot be friend with yourself
  * Can only comment on status of friends 
* Task decomposition
  * Considerations 
    * Lookup vs. insert, delete, and update (different locks)
    * How many schema constraints are involved? (many locks)
    * Are enabling conditions consistent across tasks? (let run what can run)
    * Are frequencies consistent across tasks? (index only what must be indexed)
    * Is consistency essential? (ACID transaction properties)
    * Is mother task needed or not?
  * Decomposition
    * View profile (all 3 sections are read-only and have same frequency)
      * Subtasks: view profile, view education, view professional
    * Edit profile (read, insert, delete, and update)
      * Subtasks: view profile, update personal, add/del school, add/del job 
    * Friend requests
      * Subtasks: view requests, accept/reject/cancel, request friend  





#### III: DESIGN

#### IV: Implementation
