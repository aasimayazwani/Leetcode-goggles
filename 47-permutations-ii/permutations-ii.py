class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def iterate(current,nums,length):
            if len(current) == length:
                if current not in ans:
                    ans.append(current)
            if len(current) < length:
                for i in range(0,len(nums)):
                    iterate(current + [nums[i]],nums[0:i] + nums[i+1:],length)
        ans = []
        iterate([],nums,len(nums))
        return ans