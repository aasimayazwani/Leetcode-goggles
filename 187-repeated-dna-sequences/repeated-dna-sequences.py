class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {}
        current = s
        cur = current[0:9]
        for i in range(9,len(current)):
            cur = cur + current[i]
            if cur in mapping:
                mapping[cur] +=1
            if cur not in mapping:
                mapping[cur] =1 
            cur = cur[1:]
        print(mapping)
        return [item[0] for item in mapping.items() if item[1] > 1]