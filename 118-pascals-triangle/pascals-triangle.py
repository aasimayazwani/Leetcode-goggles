class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            matrix = [[1],[1,1]]
            iterations = numRows - 2 
            while iterations  > 0 :
                current = matrix[-1]
                ans = []
                for i in range(0,len(current)-1):
                    ans.append(current[i+1]+current[i])
                temp = [1] + ans + [1]
                iterations -=1 
                matrix.append(temp)
        return matrix 
