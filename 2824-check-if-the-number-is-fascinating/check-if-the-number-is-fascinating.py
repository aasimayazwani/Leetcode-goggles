class Solution:
    def isFascinating(self, n: int) -> bool:
        from collections import Counter
        n = str(n) + str(2*n) + str(3*n)
        mapping = Counter([int(item) for item in n])
        current = Counter(list(range(1,10)))
        print(current)
        return mapping == current 

        #return len([item for item in list(set(n)) if item != 0]) == 9