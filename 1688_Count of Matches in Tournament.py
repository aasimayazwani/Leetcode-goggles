class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.some(n)
        
    def some(self,n):
        count = 0 
        matches = 0 
        while int(n/2) > 0:
            next_round_teams = n%2 + int(n/2) 
            matches = int(n/2)
            #print(matches)
            prev = matches
            count += matches
            n = next_round_teams
        return count