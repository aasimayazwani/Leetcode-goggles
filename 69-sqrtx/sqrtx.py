class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, target = 0, x, x
        while left <= right:
            #print([left,right])
            mid = left + (right-left)//2
            product = mid*mid
            if target == product:
                return mid
            elif target < product :
                right = mid -1 
            elif target > product:
                left = mid + 1 
        return right