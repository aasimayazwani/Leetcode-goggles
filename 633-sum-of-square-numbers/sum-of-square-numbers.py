class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maximum = self.sqrt(c,"estimation")
        for i in range(0,maximum+1):
            cur = c - i*i
            ans = self.sqrt(cur,"exact")
            if ans != -1:
                return True
        return False


    def sqrt(self,target,search_type):
        left, right = 0, target
        while left <= right:
            #print([left,right])
            mid = left + (right-left)//2
            product = mid*mid 
            if target == product:
                return mid
            elif target > product:
                left = mid + 1 
            elif target < product:
                right = mid -1 
        if search_type == "estimation":
            return right
        if search_type == "exact":
            return -1
    
