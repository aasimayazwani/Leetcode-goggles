class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        temp = []
        for i in range(0,n):
            summ = start + 2*i
            temp.append(summ)
        result = 0 
        for i in range(0,len(temp)):
            result ^= temp[i]
        return result 