class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(0,len(matrix)):
            arr += matrix[i]
        
        left, right = 0, len(arr)-1

        while left <= right :
            middle = left + (right - left)//2
            if target < arr[middle]:
                right = middle -1 
            elif target > arr[middle]:
                left = middle + 1 
            elif target == arr[middle]:
                return True 
        return False 