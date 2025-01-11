# Write your MySQL query statement below
with cte as
    (select *
        from
        (select *, 
            dense_rank() over (partition by customer_id order by order_date) as "ranking", 
            case 
                when order_date =customer_pref_delivery_date then 1 
                else 0 
                end as "status"
            from delivery) as t1 
        where ranking = 1)

select round(100*(sum(status)/count(*)),2) as "immediate_percentage" from cte 