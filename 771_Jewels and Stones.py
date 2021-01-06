class Solution(object):
    def numJewelsInStones(self, J, S):

        jewelSet = set()
        for jewel in J:
            jewelSet.add(jewel)
        
        jewels = 0
        for stone in S:
            if stone in jewelSet:
                jewels += 1
        
        return jewels