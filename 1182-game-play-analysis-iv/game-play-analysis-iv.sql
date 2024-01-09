# Write your MySQL query statement below
# Algorithm: 
    ## for each player identify the earliest login date 
    ## identify those player_id where the event_date 

select round(fraction,2) as "fraction" from 
(select count(distinct player_id)/(select count(distinct player_id) from activity)
as "fraction" from 
(select *, min(event_date) over (partition by player_id) as "earliest"
from activity ) 
as t1 
where datediff(event_date,earliest) = 1 ) as t2 
;