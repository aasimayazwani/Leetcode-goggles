# Write your MySQL query statement below
select 
t1.firstName , 
t1.lastName, 
ifnull(t2.city,Null) as "city",
ifnull(t2.state,Null) as "state" 
from person as t1 
left join 
address as t2 
on 
t1.personid = t2.personid  ; 