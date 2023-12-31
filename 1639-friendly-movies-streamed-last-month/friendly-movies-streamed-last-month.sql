select distinct title from 
(select t2.title,t1.program_date from tvprogram as t1 
left join 
content as t2 
on t1.content_id = t2.content_id 
where t2.kids_content = "Y" and 
t2.content_type = "Movies"
having date_format(t1.program_date,"%Y-%m") = "2020-06")as t3  ; 