Tables
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
