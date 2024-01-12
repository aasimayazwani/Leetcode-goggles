select distinct viewer_id as "id" 
from 
(select viewer_id, view_date, count(distinct Article_id) as "counting"
from views
group by viewer_id, view_date) as t1 
where counting > 1 
order by viewer_id asc ; 
