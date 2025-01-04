# Write your MySQL query statement below
select minute as "interval_no", sum(order_count) as "total_orders"
    from
    (select
        ceil(minute/6)  as "minute", order_count
        from orders ) as t1
    group by minute 
    order by interval_no asc ; 