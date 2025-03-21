# Write your MySQL query statement below
select 
sum(ifnull(t1.apple_count,0)
+ifnull(t2.apple_count,0)) as "apple_count",
sum(ifnull(t1.orange_count,0) +ifnull(t2.orange_count,0)) as "orange_count"
from boxes as t1 
left join 
chests as t2 
on 
t1.chest_id = t2.chest_id
