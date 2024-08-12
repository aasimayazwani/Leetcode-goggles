# Write your MySQL query statement below
select city from
(select city, avg(price) as "city_price"
from listings
group by city) as t1 
where city_price > (select avg(price) from listings)
order by city 