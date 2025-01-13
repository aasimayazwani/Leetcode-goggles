# Write your MySQL query statement below
with cte as
    (select month, order_id, customer_id, invoice
        from
        (select 
        order_id, date_format(order_date,"%Y-%m") as "month", 
            customer_id, invoice
            from orders) as t1 
        where invoice > 20)

select month, count(distinct order_id) as "order_count", 
            count(distinct customer_id) as "customer_count"
            from cte 
        group by month 