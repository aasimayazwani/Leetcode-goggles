class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mapping = {}
        for i in range(1,len(grid)*len(grid) +1):
            mapping[i] = 1 
            
        combined = []
        for i in range(0,len(grid)):
            combined.extend(grid[i])
            
        current = Counter(combined)
        a = [item[0] for item in current.items() if item[1] > 1][0]
        b = [item[0] for item in mapping.items() if item[0] not in list(current.keys())][0]
        return [a,b]