class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        total = items1 + items2 
        mapping = {}
        for i in range(0,len(total)):
            if total[i][0] in mapping:
                mapping[total[i][0]] += total[i][1]
            if total[i][0] not in mapping:
                mapping[total[i][0]] = total[i][1]
        
        answers = sorted(mapping.items(), key = lambda x:x[0])
        return answers 