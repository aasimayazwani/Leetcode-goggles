class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        return self.bs(num)
        
    def bs(self,num):
        left = 0 
        right = num - 1
        while left <= right:
            mid = left + (right -left)//2
            squared = mid*mid
            if squared == num:
                return True
            if squared < num:
                left = mid + 1 
            if squared > num:
                right = mid - 1
        return False