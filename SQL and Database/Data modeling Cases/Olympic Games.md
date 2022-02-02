Table
- OlympicGames (ID, SeqID, HostingCity, HostingCountry, Year, StartDate, EndDate)
- Teams (ID, Name, Country, OlympicGames)
- Athelete (ID, Name, TeamsID, Country, BirthDate)
- Sports (ID, Sport)
- Results (ID, OlympicGamesID, Sport, TeamID, Rank, Score)

##### Who is the young athelete from U.S.A when they won the medal?
```sql
SELECT A.Name, YEAR(O.Year) - YEAR(A.BirthDate) AS ageWhenWonMedal
FROM Results R
LEFT JOIN  OlympicGames O ON O.ID = R.OlympicGamesID
LEFT JOIN Teams T ON T.ID = R.TeamID
LEFT JOIN Athelete A ON A.TeamsID = T.TeamsID
LEFT JOIN Sports S USING (Sport)
WHERE Rank <= 3 and A.Country = 'U.S.A'
ORDER BY YEAR(O.Year) - YEAR(A.BirthDate) DESC
LIMIT 1
```

##### Which country won the most medal in 2021?

```sql
SELECT Country
FROM Results R
LEFT JOIN  OlympicGames O ON O.ID = R.OlympicGamesID
LEFT JOIN Teams T ON T.ID = R.TeamID
LEFT JOIN Sports S USING (Sport)
WHERE Rank <= 3 and O.year = 2020
GROUP BY Country
ORDER BY COUNT(TeamID)) DESC
LIMIT 1
```




