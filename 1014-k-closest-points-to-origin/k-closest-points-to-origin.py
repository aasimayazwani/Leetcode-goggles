class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(0,len(points)):
            heapq.heappush(min_heap,(self.calculate(points[i][0],points[i][1]),points[i]))

        result = []
        while k > 0:
            distance, coordinate = heapq.heappop(min_heap)
            k-=1
            result.append(coordinate)
        return result 

    def calculate(self,x,y):
        return math.sqrt((x)**2 + (y)**2)