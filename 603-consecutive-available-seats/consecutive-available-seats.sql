# Write your MySQL query statement below
with cte 
as
(select 
t1.seat_id as "seat1",t2.seat_id as "seat2"
from cinema as t1, cinema as t2 
where 
t2.seat_id - t1.seat_id = 1 and 
t1.free = 1 and 
t2.free = 1) 

select distinct seat_id
from
    (select seat1 as "seat_id" from cte
    union all
    select seat2 as "seat_id" from cte)
    as t1 
order by seat_id asc ; 