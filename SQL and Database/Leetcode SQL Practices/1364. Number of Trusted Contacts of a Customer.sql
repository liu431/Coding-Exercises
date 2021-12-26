# Write your MySQL query statement below
# Find the following for each invoice_id: customer_name, price, contacts_cnt, trust_contacts_cnt
## Group Contacts to get contacts_cnt and trust_contacts_cnt
## Join new Contacts with Invoice
WITH contacts_tbl AS 
(SELECT user_id, COUNT(*) AS contacts_cnt, 
SUM(CASE WHEN Customers.customer_name IS NOT NULL THEN 1 ELSE 0 END) AS trusted_contacts_cnt
FROM Contacts
LEFT JOIN Customers ON Contacts.contact_name = Customers.customer_name
GROUP BY user_id)

SELECT invoice_id, customer_name, price, IFNULL(contacts_cnt, 0) AS contacts_cnt, IFNULL(trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices 
LEFT JOIN contacts_tbl USING (user_id)
LEFT JOIN Customers ON Customers.customer_id = Invoices.user_id
ORDER BY invoice_id
