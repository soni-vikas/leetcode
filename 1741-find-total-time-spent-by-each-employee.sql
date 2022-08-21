# Write your MySQL query statement below


select event_day day, emp_id, (sum(out_time) - sum(in_time)) total_time
from Employees
group by emp_id, event_day
