# Write your MySQL query statement below
with cte as 
    (select 
        delivery_id, 
        customer_id, 
        order_date, 
        customer_pref_delivery_date
        from
        (select *, 
            dense_rank() over (partition by customer_id order by order_date)
            as "ranking"
            from delivery) as t1
        where ranking =1),

cte2 as
    (select *, 
        case 
            when order_date = customer_pref_delivery_date then 1 
            else 0 
        end as "value"
        from cte)

select round((sum(value)/count(*))*100,2) as "immediate_percentage"  from cte2 ; 
