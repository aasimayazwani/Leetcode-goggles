class Solution:
    def fillCups(self, amount: List[int]) -> int:
        if list(set(amount)) == [0]:
            return 0 
        
        amount = [-int(item) for item in amount]
        heapify(amount)
        seconds = 0
        
        while len(amount) > 1:
            #print(amount)
            a = heappop(amount) + 1 
            b = heappop(amount) + 1 
            seconds +=1 
            if a < 0:
                heappush(amount,a)
            if b < 0:
                heappush(amount,b)
        if len(amount) > 0:
            return seconds + -(amount[0])
        if len(amount) == 0:
            return seconds