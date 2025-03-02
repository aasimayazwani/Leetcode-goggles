# Write your MySQL query statement below
select actor_id, director_id
    from
    (select actor_id, director_id, count(*) as "counting"
    from actordirector
    group by actor_id, director_id) as t1 
    where counting >= 3; 