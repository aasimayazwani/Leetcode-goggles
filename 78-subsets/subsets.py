class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def iterate(nums,current):
            if len(nums) == 0:
                result.append(current)
            else:
                if len(current) > 0:
                    result.append(current)
                for i in range(0,len(nums)):
                    iterate(nums[i+1:],current+[nums[i]])
        iterate(nums,[])
        return result