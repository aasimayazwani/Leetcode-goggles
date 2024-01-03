# Write your MySQL query statement below
with temp_table as 
(select distinct order_id, 
        avg(quantity) over 
        (partition by order_id) as avg_quantity,
        max(quantity) over 
        (partition by order_id) as max_quantity 
        from OrdersDetails) 
        
select order_id  from temp_table
where max_quantity > (select max(avg_quantity) from temp_table) ;