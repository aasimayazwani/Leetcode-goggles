select distinct t2.title from tvprogram as t1 
inner join content as t2 
on 
t1.content_id = t2.content_id 
where t2.Kids_content = "Y" and t2.content_type = "Movies" and 
date_format(t1.program_date, "%Y-%m") = "2020-06" ;