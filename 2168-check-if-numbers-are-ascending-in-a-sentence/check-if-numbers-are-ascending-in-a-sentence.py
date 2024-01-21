class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = [int(item) for item in s.split(" ") if item.isdigit()]
        for i in range(0,len(s)-1):
            if s[i] >= s[i+1]:
                return False
        return True 
            