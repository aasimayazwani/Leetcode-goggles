class Solution:
    def isPalindrome(self, s: str) -> bool:
        import math
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        filtered_chars = [item.lower() for item in filtered_chars]
        forward = ("".join(filtered_chars))
        backward = forward[::-1]
        length = int(len(forward)/2)
        for left in range(0,length):
            if forward[left] == backward[left]:
                pass 
            else:
                return False
        return True 