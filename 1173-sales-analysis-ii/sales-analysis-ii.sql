# Write your MySQL query statement below
with cte as (select t2.buyer_id, t1.product_name from product as t1 
inner join
sales as t2 on 
 t1.product_id = t2.product_id )


select distinct buyer_id from cte where 
cte.product_name = "S8" 
and cte.buyer_id not in (select buyer_id from cte where 
cte.product_name = "iPhone" )