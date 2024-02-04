class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(0,length):
            current = [item[i] for item in matrix[0:length]]
            matrix.append(current[::-1])

        while length > 0:
            matrix.pop(0)
            length -=1
        
        