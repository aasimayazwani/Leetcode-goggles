# Write your MySQL query statement below
with cte as
(select t1.invoice_id, t1.price, t1.user_id, t2.contact_email, t2.trusting from invoices as t1 
left join 
(select * ,
case 
    when contact_name in (select customer_name from customers) then 1 
    else 0 
    end 
    as "trusting"
from contacts) as t2 
on t2.user_id = t1.user_id )


select invoice_id, customer_name, price, contacts_cnt, ifnull(trusted_contacts_cnt,0) as "trusted_contacts_cnt"
from 
(select  
cte.invoice_id, 
customers.customer_name,
cte.price, 
cte.trusting, 
sum(trusting) as "trusted_contacts_cnt",
count(trusting) as "contacts_cnt"
from customers
inner join cte 
on customers.customer_id = cte.user_id
group by cte.invoice_id) as t5
order by invoice_id asc  ;