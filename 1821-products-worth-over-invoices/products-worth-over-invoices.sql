# Write your MySQL query statement below
with cte as
    (select product_id, sum(rest) as "rest", 
                sum(paid) as "paid", 
                sum(canceled) as "canceled", 
                sum(refunded) as "refunded"
                from invoice
            group by product_id)

select  
p2.name, 
ifnull(p1.rest,0) as "rest", 
ifnull(p1.paid,0) as "paid", 
ifnull(p1.canceled,0) as "canceled", 
ifnull(p1.refunded,0) as "refunded"
from product as p2
left join 
cte as p1 
on 
p1.product_id = p2.product_id 
order by p2.name asc ;