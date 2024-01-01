# Write your MySQL query statement below
with cte as
(select * from 
(select *, dense_rank() over (partition by product_id order by year asc )
as "ranking"
 from sales) as t1 
 where ranking = 1 )

 select cte.product_id, cte.year as "first_year",
 cte.quantity, cte.price
  from cte 
 inner join product as t2 
 on cte.product_id = t2.product_id ; 