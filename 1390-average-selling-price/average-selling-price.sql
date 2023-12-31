select t1.product_id, ifnull(round(sum(t2.units*t1.price)/sum(t2.units),2),0) as "average_price"
from prices as t1  
left join unitssold as t2  
on t1.product_id = t2.product_id and 
t2.purchase_date between t1.start_date and t1.end_date
group by t1.product_id  ; 