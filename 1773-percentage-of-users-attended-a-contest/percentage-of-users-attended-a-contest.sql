# Write your MySQL query statement below
select contest_id, round(percentage,2) as "percentage"
from
(select contest_id, 
((select count(user_id) as "total")*100)/(select count(*) from users) as "percentage" 
from register
group by contest_id 
order by percentage desc, contest_id asc)as t1 
