class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = -1000000
        for i in range(0,len(accounts)):
            current = sum(accounts[i])
            if max_val < current:
                max_val = current
            else:
                pass 
        return max_val 