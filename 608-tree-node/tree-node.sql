# Write your MySQL query statement below
# pseudo code and logic
# CASE 1 : if the parent_id is null then i's a root node 
# if the parent_id id not null then its either an inner node or a leaf node
    ## CASE 2 if the node happens to be a inner node it will be a parent to some other node 
    ## CASE 3 if the node happends to be an inner node it cannot be parent node to any other node. 
select id, 
case when p_id is null then "Root"
    when id in (select distinct p_id from tree where p_id is not null) then "Inner"
    when id not in (select distinct p_id from tree where p_id is not null) then "Leaf"
    end as "type"
from tree 