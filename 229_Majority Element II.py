class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from itertools import groupby
        lengths = len(nums)/3
        nums.sort()
        L = [list(v) for k, v in groupby(nums)]
        temp = list(filter(lambda x : len(x) > lengths, L))
        return [temp[i][0] for i in range(0,len(temp))]