# Write your MySQL query statement belows
select distinct t1.seat_id from cinema as t1, cinema as t2 
where t1.free = 1 and t2.free = 1 and 
abs(t1.seat_id - t2.seat_id) = 1
order by t1.seat_id asc  ; 