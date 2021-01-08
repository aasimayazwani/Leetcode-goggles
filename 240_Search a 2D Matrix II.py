class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(matrix)):
            if self.BinarySearch(matrix[i],target) == True :
                return True 
        return False 
        
        
    def BinarySearch(self,nums,target):
        initial, final = 0 , len(nums) -1 
        while initial <= final :
            middle_element = (initial+final)//2
            if nums[middle_element] > target:
                final = middle_element-1
            if nums[middle_element] < target:
                initial = middle_element +1
            if nums[middle_element] == target:
                return True 
        return False 