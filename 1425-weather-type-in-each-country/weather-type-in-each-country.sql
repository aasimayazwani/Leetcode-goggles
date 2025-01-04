# Write your MySQL query statement below
with cte as
(select country_id, temp
    from
    (select country_id, 
            avg(weather_state) as "temp",
            date_format(day,"%Y-%m") as "val"
            from weather
            group by country_id, val) as t1 
    where 
    val = "2019-11"),

cte2 as
(select country_id, 
        case 
            when temp <= 15 then "Cold"
            when temp >= 25 then "Hot"
            else "Warm"
        end as "weather_type"
        from cte)

select p2.country_name, p1.weather_type from 
    cte2 as p1 
    inner join 
    countries as p2 
    on 
    p1.country_id = p2.country_id ; 