select distinct author_id as "id"
from
(select author_id 
from views 
where author_id = viewer_id) as t1 
order by id asc; 