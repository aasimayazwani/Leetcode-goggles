# Write your MySQL query statement below
select distinct customer_id from
    (select customer_id, count(distinct product_key) as "counting"
    from customer
    group by customer_id) as t1 
    where counting = (select count(*) from product)