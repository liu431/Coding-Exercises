# Write your MySQL query statement below
WITH cte AS 
(SELECT 
    id, 
    drink, 
    ROW_NUMBER() OVER () AS nb 
 FROM CoffeeShop),

cte2 AS 
(SELECT 
    id,
    drink,
    nb, 
    ISNULL(drink),
    SUM(1-ISNULL(drink)) OVER (ORDER BY nb) AS group_id 
 FROM cte) 
 
 SELECT 
    id,
    FIRST_VALUE(drink) OVER (PARTITION BY group_id) AS drink
FROM cte2
