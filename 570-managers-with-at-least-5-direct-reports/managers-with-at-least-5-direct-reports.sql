select e1.name from employee e1 inner join (
select id, name, count(*) as total, managerId from employee 
group by managerId 
having total >= 5) as t 
on e1.id = t.managerid 