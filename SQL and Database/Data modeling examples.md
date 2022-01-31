### Data Models

##### Ex. Movie
- Movies (MovieID, Name, Year, BoxResults, Star Ratings)
- Cast (MovieID, ActorID, ActorRole)
- Actor (ActorID, Name, Gender)

a. Top 10 grossing movie last year?
```sql
SELECT MovieID, Name
FROM Movies
WHERE Year = YEAR(NOW()) - 1
ORDER BY BoxResults DESC
LIMIT 10
```
b. All movies which starred Brad Pitt.
```sql
SELECT DISTINCT Movies.Name
FROM Cast 
LEFT JOIN Actor USING (ActorID)
LEFT JOIN Movies USING (MovieID)
WHERE Actor.Name = 'Brad Pitt'
```
c. Every actor which Brad Pitt has worked with.
```sql

```

##### Ex. College/University
- Faculty (ID, Name, Title, Department, JoinDate)
- Student (ID, Name, Major, StartDate)
- Course (ID, Name, Term, Faculty, Department, Credit Hours)
- Course Registration (ID, StudentID, CourseID, RegistrationDate)


##### Ex. Sales 
- Sales (date, salesid, marketid, region, salesamount)

a. Total sales of each region in the past one month
```sql
SELECT region, SUM(salesamount) AS totalsales
FROM Sales
WHERE DATEDIFF(NOW(), date) <= 30
```

b. List of marketids that have above-average salesamount in each region
```sql
WITH avgsales_tbl AS (SELECT region, AVG(salesamount) AS avgsales
FROM Sales
GROUP BY 1)
SELECT DISTINCT Sales.region, Sales.marketid
FROM Sales
LEFT JOIN avgsales_tbl USING (REGION)
WHERE salesamount > avgsales
```
  
#### Food delivery App (Grubhub/Seamless)
- Restaurant (ID, Contact, )
- Customers (ID, Name, )
- Orders (ID, CustomerID, RestaurantID, PaymentID, DateTime)
- Payment (ID, Method, Status, Amount, DateTime)


















