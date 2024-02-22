class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        ans = []
        def iterate(arr,nums,target):
            if len(arr) == k and target == 0:
                #arr = sorted(arr)
                if arr not in ans:
                    ans.append(arr)
            else:
                for j in range(0,len(nums)):
                    if len(arr) == 0 or nums[j] < arr[-1]:
                        iterate(arr+[nums[j]],nums,target - nums[j])

        iterate([],nums,n)
        return ans