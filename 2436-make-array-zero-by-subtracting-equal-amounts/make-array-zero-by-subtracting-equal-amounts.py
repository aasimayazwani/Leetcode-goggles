class Solution:
    def minimumOperations(self, nums):
        if list(set(nums)) == [0]:
            return 0
        counting = 0
        while True:
            x = self.get_min(nums)
            nums = self.subtract(nums,x)
            if list(set(nums)) == [0]:
                return counting +1
            else:
                counting +=1


    def get_min(self,nums):
        return min([item for item in nums if item > 0])

    def subtract(self,arr,x):
        for i in range(0,len(arr)):
            if arr[i] == 0:
                pass
            else:
                arr[i] = arr[i] - x
        return arr