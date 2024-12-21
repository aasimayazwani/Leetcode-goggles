# Write your MySQL query statement below
select user_id, max(time_stamp) as "last_stamp"
from
(select user_id, year(time_stamp) as "year", time_stamp
from logins) as t1 
where year = 2020 
group by user_id ; ;