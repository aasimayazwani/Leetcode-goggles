class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        mapping = {}
        def iterate(arr,nums,k):
            if len(arr) == k:
               mapping[tuple(arr)] = 1
            else:
                for i in range(0,len(nums)):
                    if (len(arr) == 0) or (nums[i] not in arr and (arr[-1] < nums[i])):
                        iterate(arr + [nums[i]],nums,k)
                        
        nums = list(range(1,n+1))
        
        iterate([],nums,k)
        return [list(item) for item in  mapping.keys()]
        #return ans