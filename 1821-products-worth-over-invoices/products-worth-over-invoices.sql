# Write your MySQL query statement below
with cte as 
(select product_id, sum(rest) as "rest", sum(paid)  as "paid", 
sum(canceled) as "canceled",
sum(refunded) as "refunded"
from INVOICE  
group by product_id)

select t1.name, ifnull(t2.rest,0) as "rest",ifnull(t2.paid,0) as "paid", ifnull(t2.canceled,0) as "canceled", ifnull(t2.refunded,0) as "refunded" from product as t1 
left join cte as t2 
on t1.product_id = t2.product_id
order by t1.name asc  ; 