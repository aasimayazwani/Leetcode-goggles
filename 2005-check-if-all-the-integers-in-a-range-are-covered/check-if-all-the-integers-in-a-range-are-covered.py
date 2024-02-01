class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        total = []
        for i in range(0,len(ranges)):
            total.extend(list(range(ranges[i][0],ranges[i][1]+1)))
        new = set(list(range(left,right+1)))
        return new.issubset(set(total))