select max(total)-min(total) as "difference_in_score"
from
    (select assignment1+assignment2+assignment3 as "total"
    from scores) as t1 