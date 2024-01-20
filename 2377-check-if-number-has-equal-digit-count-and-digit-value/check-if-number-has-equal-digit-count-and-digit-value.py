class Solution:
    def digitCount(self, num: str) -> bool:
        # the string consists of only digits
        #  
        from collections import Counter
        num = [int(item) for item in num]
        mapping = Counter(num)
        for i in range(0,len(num)):
            if int(num[i]) != mapping[int(i)]:
                return False
            else:
                pass
        return True 