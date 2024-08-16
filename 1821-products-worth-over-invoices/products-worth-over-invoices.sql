# Write your MySQL query statement below
with cte as
    (select product_id ,
            sum(rest) as "rest", 
            sum(paid) as "paid", 
            sum(canceled) as "canceled",
            sum(refunded) as  "refunded"
    from invoice 
    group by product_id)

select t2.name, ifnull(t1.rest,0) as "rest",
                ifnull(t1.paid,0) as "paid",
                ifnull(t1.canceled,0) as "canceled",
                ifnull(t1.refunded,0) as "refunded" from product as t2 
left join 
 cte as t1 
on t2.product_id  =  t1.product_id
order by t2.name