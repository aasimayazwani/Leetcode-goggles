select distinct viewer_id  as "id" from
(select viewer_id, count(distinct article_id) as "unique_views" from views 
group by view_date, viewer_id
having unique_views > 1) as t1 
order by viewer_id asc ; 