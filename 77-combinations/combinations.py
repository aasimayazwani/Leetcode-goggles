class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(nums,current,k):
            if len(current) == k:
                ans.append(current)
            if len(current) < k:
                for i in range(0,len(nums)):
                    backtrack(nums[i+1:],current+[nums[i]],k)
        nums = list(range(1,n+1))
        backtrack(nums,[],k)
        return ans 
