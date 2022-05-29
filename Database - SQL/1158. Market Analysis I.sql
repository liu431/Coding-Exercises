# Write your MySQL query statement below
# Find for each user, the join date and the number of orders they made as a buyer in 2019
## id and join date are in Users table
## Get order numbers fro Orders
WITH ordercts AS 
    (SELECT buyer_id, COUNT(*) AS Cts 
     FROM Orders 
     WHERE YEAR(order_date) = 2019
     GROUP BY buyer_id 
     )
SELECT user_id as buyer_id, join_date, IFNULL(Cts, 0) AS orders_in_2019 
FROM Users
LEFT JOIN ordercts
ON ordercts.buyer_id = Users.user_id

