from itertools import groupby 

class Solution:
    def repeatedNTimes(self, A):
        from itertools import groupby
        A.sort()
        L = [list(v) for k, v in groupby(A)]
        temp = list(filter(lambda x : len(x) > 1, L))
        return temp[0][0]