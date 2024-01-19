class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 
        right = len(s)-1
        while left <= right:
            # left < right for the even sized length 
            # left <= right for the odd sized length
            temp = s[right]
            s[right] = s[left]
            s[left] = temp 
            left +=1 
            right -=1 

        
