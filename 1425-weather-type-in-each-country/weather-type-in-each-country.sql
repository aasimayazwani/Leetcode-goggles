# Write your MySQL query statement below
with cte as 
    (select country_name, avg(temperature) as "temp" from
        (select country_name, temperature from 
            (select t1.country_name, t2.weather_state as "temperature", date_format(day,"%Y-%m") as "month" 
            from countries as t1 
            inner join 
            weather as t2 
            on 
            t1.country_id = t2.country_id)  as t3 
            where month = "2019-11") as t4 
        group by country_name )

select country_name,
case 
    when temp <= 15 then "Cold"
    when temp >= 25 then "Hot"
    else "Warm"
    end 
    as "weather_type"
from cte