# Write your MySQL query statement below
select distinct email from 
(select email, count(email) over (partition by email) as "counting"
from person ) as t1 
where counting > 1 ; 