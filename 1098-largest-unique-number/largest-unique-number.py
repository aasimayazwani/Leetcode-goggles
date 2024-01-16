class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        ht = {}
        for number in A:
            if number not in ht:
                ht[number] = 1
            else:
                ht[number] += 1
        
        for key in sorted(ht.keys())[::-1]:
            if ht[key] == 1:
                return key
        return -1
        