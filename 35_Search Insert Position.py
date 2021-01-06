class Solution:
    def searchInsert(self,List, target):
        position = 0
        for i in range(0,len(List)):
            if List[i] == target:
                return i 
        for j in range(0,len(List)):
            if target > List[j]:
                position = position + 1
                j = j +1
        return position