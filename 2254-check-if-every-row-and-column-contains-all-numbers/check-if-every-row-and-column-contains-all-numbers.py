class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        total = len(matrix)   
        for i in range(0,len(matrix)):
            if len(set(matrix[i])) != total:
                return False 
            else:
                pass 
        for i in range(0,len(matrix)):
            current = [item[i] for item in matrix ]
            if len(set(current)) != total:
                return False 
            else:
                pass 
        return True 
        