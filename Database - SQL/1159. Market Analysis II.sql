# Write your MySQL query statement below
# Find for each user whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no. It is guaranteed that no seller sold more than one item on a day.
## CTE: use rank() to find the orders that users sold as the second item
## Use case when to classify whether it matches with their favorite brand

WITH order_rank_tbl AS (
    SELECT seller_id, item_brand
    FROM
        (SELECT seller_id, item_brand, RANK() OVER(PARTITION BY seller_id ORDER BY order_date) AS ord_rank
        FROM Orders
        LEFT JOIN Items USING (item_id)) t
    WHERE ord_rank = 2)

SELECT user_id as seller_id,
       CASE WHEN favorite_brand = item_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand 
FROM Users
LEFT JOIN order_rank_tbl ON order_rank_tbl.seller_id = Users.user_id

