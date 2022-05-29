# Write your MySQL query statement below
# Find the person_name of the last person that can fit on the bus without exceeding the weight limit of 1000 kg.
## Use running total and calculate the total weight after fitting certain person

SELECT person_name
FROM (SELECT person_name, SUM(Weight) OVER (ORDER BY Turn) AS TotalW
    FROM Queue) t
WHERE TotalW <= 1000
ORDER BY TotalW DESC
LIMIT 1
