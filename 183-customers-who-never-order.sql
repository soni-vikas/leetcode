# Write your MySQL query statement below

select c.name Customers from Customers c LEFT JOIN Orders o ON c.id = o.customerID where o.customerID IS NULL