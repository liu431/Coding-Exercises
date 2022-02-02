Table
- OlympicGames (ID, SeqID, HostingCity, HostingCountry, Year, StartDate, EndDate)
- Teams (ID, Name, Country, OlympicGames)
- Athelete (ID, Name, TeamsID, BirthDate)
- Sports (ID, Sport)
- Results (ID, OlympicGamesID, Sport, TeamID, Rank, Score)

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




