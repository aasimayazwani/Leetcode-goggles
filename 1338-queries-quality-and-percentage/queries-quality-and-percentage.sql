# Write your MySQL query statement below
select * from 
(select query_name, round(avg(rating/position),2) as "quality",
round(sum(rating<3)*100/count(*),2) as poor_query_percentage
from queries
group by query_name ) as t1 
where query_name is not null ; 