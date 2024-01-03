with cte as 
(select user_id, gender, 1 as "ordering",
row_number() over (order by user_id) as "row_numbering" from genders 
where gender = "female"
UNION ALL
select user_id, gender, 3 as "ordering",
row_number() over (order by user_id) as "row_numbering" from genders 
where gender = "male"
UNION ALL
select user_id, gender, 2 as "ordering",
row_number() over (order by user_id) as "row_numbering" from genders 
where gender = "other")

select user_id, gender from cte 
order by row_numbering asc , ordering asc   ; 