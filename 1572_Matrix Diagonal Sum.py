class Solution:
    def diagonalSum(self, mat):
        summ = 0 
        summ += self.value_iter(mat)
        mat2 = self.revw(mat)
        summ += self.value_iter(mat2)
        return summ - self.remove_common(mat)

    def remove_common(self,mat):
        if len(mat)%2 != 0:
            val = len(mat)//2
            return mat[val][val]
        if len(mat)%2 == 0:
            val = 0
            return val
        

    def revw(self,mat):
        new = []
        for i in range(0,len(mat)):
            new.append(list(reversed(mat[i])))
        return new

    def value_iter(self,mat):
        summ = 0 
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if i == j:
                    summ +=mat[i][j]
                else:
                    pass
        return summ