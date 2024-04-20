class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        answer = []
        current = []
        index = 0 
        while index < len(original):
            current.append(original[index])
            index +=1 
            if index % n == 0:
                answer.append(current)
                current = []
        
        return answer