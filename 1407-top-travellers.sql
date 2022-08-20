# Write your MySQL query statement below
select u.name name, ifnull(sum(r.distance), 0) travelled_distance
from users u
left join Rides r
on u.id = r.user_id
group by u.id
order by travelled_distance desc, name asc