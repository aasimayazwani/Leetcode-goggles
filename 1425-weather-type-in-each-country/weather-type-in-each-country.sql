# Write your MySQL query statement below
with cte as
    (select country_id, avg(weather_state) as "temp", value
        from
        (select country_id, weather_state, date_format(day,"%Y-%m") as "value"
        from weather) as t1
        group by country_id, value),

cte2 as
    (select country_id, 
    case 
        when temp <= 15 then "Cold"
        when temp >= 25 then "Hot" 
        else "Warm"
    end as "weather_type"
    from cte 
    where value = "2019-11")

select 
p2.country_name, p1.weather_type
from cte2 as p1 
inner join countries as p2 on 
p1.country_id = p2.country_id