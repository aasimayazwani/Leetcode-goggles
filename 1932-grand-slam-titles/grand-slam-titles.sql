# Write your MySQL query statement below
with cte as 
(select Wimbledon as "titles" from Championships 
UNION ALL 
select Fr_open as "titles" from Championships 
UNION ALL 
select US_open as "titles" from Championships 
UNION ALL
select Au_open as "titles" from Championships )

select t2.player_id, t2.player_name, t1.grand_slams_count from
(select titles as "player_id",
        count(titles) as "grand_slams_count"

        from cte 
        group by titles) as t1 
inner join players as t2 
on t1.player_id = t2.player_id 
; 