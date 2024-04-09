class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        min_stack = [-a,-b,-c]
        heapify(min_stack)
        score = 0
        popped = []
        while len(min_stack) > 1:
            a = heappop(min_stack) + 1 
            b = heappop(min_stack) + 1 
            score +=1
            if a < 0:
                heappush(min_stack,a)
            if b < 0:
                heappush(min_stack,b)
        return score 

            
            