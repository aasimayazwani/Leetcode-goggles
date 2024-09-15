class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        k = len(matrix[0])
        for i in range(0,k):
            matrix.append([item[i] for item in matrix[0:k]][::-1][0:k])
            #print(current)
            #matrix.append(current[0:k])

        
        while k > 0:
            matrix.pop(0)
            k-=1
        