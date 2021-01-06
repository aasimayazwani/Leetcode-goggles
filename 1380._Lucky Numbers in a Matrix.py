class Solution:
    def luckyNumbers (self, matrix):
        lucky = [] 
        rows, col = len(matrix[0]),len(matrix)
        for column_index in range(0,col):
            for row_index in range(0,rows):
                if max(self.column_elements(matrix,row_index))==self.row_elements(matrix,column_index):
                    lucky.append(matrix[column_index][row_index])
        return lucky 
        
    def column_elements(self,matrix,index):
        col= []
        for i in range(0,len(matrix)):
            col.append(matrix[i][index])
        return col
    
    def row_elements(self,matrix,index):
        return min(matrix[index])