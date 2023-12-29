# Write your MySQL query statement below
with cte as (select seller_id, sum(price) as "total" from sales
group by seller_id )

select seller_id from 
(select *, dense_rank() over (order by total desc) as "ranking"
from cte)  as t3 
where ranking = 1 ;