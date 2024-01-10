# Write your MySQL query statement below
with cte as
(select product_id, new_price, change_date from
    (select *, dense_rank() over (partition by product_id order by change_date desc) as "ranking"
    from
        (select product_id, new_price,change_date
        from products 
        where change_date <= "2019-08-16" ) as t2
    ) as t3 
where ranking = 1) 

select t5.product_id, ifnull(cte.new_price,10) as "price" from 
(select distinct product_id from products) as t5 
left join 
cte 
on t5.product_id = cte.product_id  
