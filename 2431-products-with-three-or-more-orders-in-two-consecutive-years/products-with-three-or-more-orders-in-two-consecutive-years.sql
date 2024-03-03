# Write your MySQL query statement below
with cte as
(select product_id, count(order_id) as "total", years
from
(select *, year(purchase_date) as "years" from orders) as t1 
group by product_id, years)

select distinct t2.product_id from cte as t2, cte as t3 
where t2.product_id = t3.product_id and 
      t2.total >= 3 and 
      t3.total >= 3 and 
      t3.years - t2.years = 1 ;