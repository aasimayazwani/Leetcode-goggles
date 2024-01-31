class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        values = []
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[0])):
                if matrix[row][col] == 0:
                    values.append([col,row])

        zero_columns = [item[0] for item in values]
        zero_rows = [item[1] for item in values]

        for j in range(0,len(matrix)):
            for i in range(0,len(zero_columns)):
                matrix[j][zero_columns[i]] = 0
        
        for k in range(0,len(zero_rows)):
            matrix[zero_rows[k]] = [0]*len(matrix[0])

        


        
    