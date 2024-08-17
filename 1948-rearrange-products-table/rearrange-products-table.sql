select * from 
(select product_id, "store1" as "store" , store1 as "price" from products UNION 
ALL
select product_id, "store2" as "store" , store2 as "price" from products UNION ALL
select product_id, "store3" as "store" , store3 as "price" from products ) as t1 
where price is not Null ; 