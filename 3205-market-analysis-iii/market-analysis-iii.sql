with cte as 
(select 
t1.seller_id, 
t1.favorite_brand, 
t2.order_id, 
t2.item_id
from users as t1 
inner join orders as t2 
on t1.seller_id = t2.seller_id)

select seller_id, num_items from
(select *, dense_rank() over (order by num_items desc ) as "ranking"
from
(select seller_id, count(distinct item_id) as "num_items" 
from 
(select 
t4.seller_id, 
t4.favorite_brand, 
t4.order_id, 
t4.item_id,
t5.item_brand
 from cte as t4
inner join 
items as t5 
on t4.item_id = t5.item_id ) as t6 
where favorite_brand != item_brand 
group by seller_id
order by seller_id asc) as t7)
as t8 
where ranking = 1   
