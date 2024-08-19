# first orders of customers that are also delievred in the 
# same day as the order was placed
with cte as
(select customer_id, 
case 
    when order_date = customer_pref_delivery_date then 1 
    else 0 
    end 
    as "status", 
    dense_rank() over (partition by customer_id order by order_date asc)
    as "ranking"
    from delivery)

select round(100*(sum(status)/count(*)),2) as "immediate_percentage" from cte 
where ranking = 1 ; 