with cte as
(select t2.buyer_id, 
        t1.product_name 
        from product as t1 
        inner join 
        sales as t2 
        on t1.product_id = t2.product_id )

select distinct t4.buyer_id from cte as t4 , cte as t5 
where t4.buyer_id = t5.buyer_id and 
t4.product_name = "S8" and t5.product_name != "iPhone" and 
        t4.buyer_id not in (select t4.buyer_id from cte as t4 , cte as t5 
        where t4.buyer_id = t5.buyer_id and 
        t4.product_name = "S8" and t5.product_name = "iPhone")