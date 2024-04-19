class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = self.get(matrix)
        return results

    def get(self,mat):
        answer = []
        while len(mat) > 0:
            answer.extend(mat[0])
            del mat[0]
            cur = []
            if (len(mat) > 0) and (len(mat[0]) > 0):
                for i in range(0,len(mat)):
                    cur.append(mat[i][-1])
                    del mat[i][-1]
                answer.extend(cur)
            if len(mat)> 0:
                answer.extend(mat[-1][::-1])
                del mat[-1]
            left = []
            if (len(mat)>0) and (len(mat[0]) > 0):
                for i in range(0,len(mat)):
                    left.append(mat[i][0])
                    del mat[i][0]
            answer.extend(left[::-1])
        return answer