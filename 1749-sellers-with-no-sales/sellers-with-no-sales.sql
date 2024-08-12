# Write your MySQL query statement below
select seller_name from seller 
where seller_id not in
(select distinct seller_id from orders 
where 
date_format(sale_date,"%Y") = "2020")
order by seller_name asc ; 