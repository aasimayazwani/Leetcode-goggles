class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(0,len(matrix)):
            arr.extend(matrix[i])
        return self.bs(arr,target)
        
    def bs(self,nums,target):
        left = 0 
        right  =len(nums)-1
        while left <= right:
            middle = left + (right - left)//2
            if target == nums[middle]:
                return True
            if target > nums[middle]:
                left = middle +1 
            if target < nums[middle]:
                right = middle - 1
        return False
