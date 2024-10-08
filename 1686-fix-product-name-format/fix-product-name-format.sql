# Write your MySQL query statement below
select product_name, sale_date, count(*) as "total" from
    (select lower(trim(product_name)) as "product_name",
            date_format(sale_date,"%Y-%m") as "sale_date"
            from sales ) as t1 
    group by product_name, sale_date     
    order by product_name asc, sale_date asc ; 