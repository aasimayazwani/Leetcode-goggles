# Write your MySQL query statement below
select *, 
case 
    when x + y > z and  x + z > y and y + z > x then "Yes"
    when x + y <= z or  x + z <= y or y + z <= x then "No"
end 
    as "triangle"
from Triangle 
     