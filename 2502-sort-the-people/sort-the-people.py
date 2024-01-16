class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(0,len(names)):
            mapping[heights[i]] = names[i]
        
        sorted_arr = sorted(mapping.items(), key = lambda x:x[0],reverse = True )
        return [item[1] for item in sorted_arr]