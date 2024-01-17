class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        import string
        from string import ascii_lowercase

        distance_map = {}
        positions = {}

        for i in range(0,len(ascii_lowercase)):
            distance_map[ascii_lowercase[i]]= distance[i] +1

        for i in range(0,len(s)):
            if s[i] in positions:
                positions[s[i]].append(i)
            else:
                positions[s[i]] = [i]
                
        for key in positions.keys():
            if distance_map[key] != abs(positions[key][0]-positions[key][1]):
                return False 
            else:
                pass 
        return True