class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        counting = 0
        current = num[0:k-1]
        for i in range(k-1,len(num)):
            current = current + num[i]
            #print(current)
            if (int(current) != 0) and (int(num)%int(current) == 0):
                counting +=1 
            current = current[1:]
        return counting 