# Write your MySQL query statement below
## Get number list from each continent
## Use ROW_NUMBER() AS the key to join list
WITH 
Ame AS (SELECT ROW_NUMBER() OVER () id, name AS America
FROM Student WHERE continent = 'America'
ORDER BY name),
Asi AS (SELECT ROW_NUMBER() OVER () id, name AS Asia
FROM Student WHERE continent = 'Asia'
ORDER BY name),
Eur AS (SELECT ROW_NUMBER() OVER () id, name AS Europe
FROM Student WHERE continent = 'Europe'
ORDER BY name)

## Combine the lists
SELECT America, Asia, Europe
FROM Ame
LEFT JOIN Asi USING(id)
LEFT JOIN Eur USING (id)

# Follow up: If it is unknown which continent has the most students, could you write a query to generate the student report?

## MAX ignores any null values. MAX returns NULL when there is no row to select.
SELECT
    MAX(CASE WHEN continent = 'America' THEN name END)AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END)AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END)AS Europe  
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS id FROM student) AS t
GROUP BY id
