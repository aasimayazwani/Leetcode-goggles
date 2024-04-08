class SmallestInfiniteSet:

    def __init__(self):
        self.arr = list(range(1,1001))
        heapq.heapify(self.arr)
        self.mapping = {}
        for i in range(1,1001):
            self.mapping[i] = 1 
        

    def popSmallest(self) -> int:
        cur = heapq.heappop(self.arr)
        del self.mapping[cur]
        return cur 

    def addBack(self, num: int) -> None:
        if num in self.mapping :
            pass
        if num not in self.mapping:
            heapq.heappush(self.arr,num)
            self.mapping[num]= 1 

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)