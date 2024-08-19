with cte as 
(select order_id, product_id, 
        avg(quantity) over (partition by order_id) as "avg_quantity", 
        max(quantity) over (partition by order_id) as "max_quantity"
        from 
        ordersdetails)

select distinct order_id  from cte
where max_quantity > (select max(avg_quantity) from cte) ;