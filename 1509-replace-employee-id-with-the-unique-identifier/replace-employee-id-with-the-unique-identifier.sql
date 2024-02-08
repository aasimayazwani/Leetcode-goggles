select ifnull(t2.unique_id,null) as "unique_id", t1.name from
employees as t1 
left join 
EmployeeUNI as t2 
on t1.id =  t2.id 