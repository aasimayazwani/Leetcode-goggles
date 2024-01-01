select city_id, day, degree from 
(select *, dense_rank () over (partition by city_id order by degree desc, day asc ) as "ranking" from weather) as t1 
where ranking = 1 
order by city_id asc ; 
