class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def iterate(current,nums,total):
            if len(current) == total:
                ans.append(current)
            if len(current) < total:
                for i in range(0,len(nums)):
                    if len(current) == 0:
                        iterate(current+[nums[i]],nums,total)
                    if len(current) > 0:
                        if current[-1] < nums[i]:
                            iterate(current +[nums[i]],nums,total)
                        else:
                            pass
        ans = []
        iterate([],list(range(1,n+1)),k)
        return ans