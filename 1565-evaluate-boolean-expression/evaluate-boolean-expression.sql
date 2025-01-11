# Write your MySQL query statement below
with cte as
    (select 
    t2.left_operand, 
    t2.operator, 
    t2.right_operand, 
    t1.value as "left_val"
    from variables as t1 
    inner join 
    expressions as t2 
    on 
    t1.name = t2.left_operand), 

cte2 as
    (select 
    *, p1.value as "right_val" 
    from variables as p1 
    inner join 
    cte as p2 
    on 
    p1.name = p2.right_operand)

select left_operand, operator, right_operand, 
    case 
        when operator = "=" and left_val = right_val then "true" 
        when operator = ">" and left_val > right_val then "true" 
        when operator = "<" and left_val < right_val then "true" 
        else "false"
    end as "value"
from cte2 