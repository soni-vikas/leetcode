# Write your MySQL query statement below

select activity_date day, count(distinct user_id) active_users
from Activity
group by activity_date
having activity_date > "2019-06-27" and activity_date <= "2019-07-27"
