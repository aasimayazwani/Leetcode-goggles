class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mapping = [set(item) for item in words]
        counting = 0
        for i in range(0,len(mapping)):
            for j in range(i,len(mapping)):
                if i != j:
                    if mapping[i] == mapping[j]:
                        counting +=1 
        return counting 