# Write your MySQL query statement below
select players.player_id, players.player_name, q.grand_slams_count from players inner join 
(select sum(total) as grand_slams_count, contest as player_id from 
(select count(*) as total,Wimbledon as  contest from championships group by Wimbledon 
union all
select count(*) as total, Fr_open as contest from championships group by Fr_open  
union all
select count(*) as total,US_open as  contest from championships group by US_open 
union all
select count(*) as total,Au_open as contest from championships group by Au_open  ) as t 
group by contest) as q on 
players.player_id = q.player_id 
; 