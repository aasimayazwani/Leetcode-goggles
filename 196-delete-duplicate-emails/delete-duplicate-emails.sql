# Write your MySQL query statement below
delete p2 from person as p1, person as p2 
where p1.email = p2.email and 
p2.id > p1.id ; 