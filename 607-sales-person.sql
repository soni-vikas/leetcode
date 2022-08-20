# Write your MySQL query statement below

select s.name
from Salesperson s
left join (
    select o.sales_id, o.order_id
    from Orders o
    join Company c
    on o.com_id = c.com_id
    where c.name = "RED"
) m
on s.sales_id = m.sales_id
where m.order_id is null