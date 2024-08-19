# Write your MySQL query statement below
# Algorithm: 
    ## for each player identify the earliest login date 
    ## identify those player_id where the event_date 
with cte as
    (select *, dense_rank() over (partition by player_id order by event_date asc) as "ranking" from activity
    ),

table1 as
(select distinct t1.player_id from cte as t1, cte as t2 
where t1.player_id = t2.player_id and 
t1.ranking = 1 and t2.ranking = 2 and 
abs(datediff(t2.event_date,t1.event_date)) = 1) 

select round(count(player_id)/(select count(distinct player_id) from cte),2) as "fraction" from table1 