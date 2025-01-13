with cte as
    (select *, row_number() over (order by topping_name asc ) as "numbering"
        from
        (select * from toppings 
        order by topping_name asc ) as t1 )

select 
concat(t1.topping_name,",",t2.topping_name,",",t3.topping_name) as "pizza", 
t1.cost+t2.cost+t3.cost as "total_cost"
from cte as t1, cte as t2, cte as t3
where 
t1.numbering < t2.numbering and 
t2.numbering < t3.numbering and 
t1.numbering < t3.numbering 
order by total_cost desc, pizza asc ;  