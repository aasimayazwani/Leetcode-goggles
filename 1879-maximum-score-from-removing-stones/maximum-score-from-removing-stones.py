class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a,b,c]
        arr = [-item for item in arr]
        heapq.heapify(arr)
        # pick 2 non zero entries 
        counting = 0
        while len(arr) > 1:
            x, y = heapq.heappop(arr), heapq.heappop(arr)
            x, y = -1*(x), -1*(y)
            counting +=1 
            if x-1 > 0:
                heapq.heappush(arr,-1*(x-1))
            if y-1>0:
                heapq.heappush(arr,-1*(y-1))
        return counting 