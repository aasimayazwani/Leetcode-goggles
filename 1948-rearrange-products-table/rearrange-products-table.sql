# Write your MySQL query statement below
with cte as 
(select product_id,"store1" as store, store1 as "price" from products
uNION ALL
select product_id,"store2" as store, store2 as "price" from products 
uNION ALL
select product_id,"store3" as store, store3 as "price" from products )

select * from cte 
where price is not null ; 