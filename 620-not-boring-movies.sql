# Write your MySQL query statement below

select *
from Cinema c
where c.description <> "boring" and c.id % 2
order by rating desc