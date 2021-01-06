class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:    
        discounted = []
        #prices = [8,4,6,2,3]
        for i in range(0,len(prices)-1):
            usable = prices[i+1:]
            discount = self.minimum_index(usable,prices[i])
            if discount != None:
                print(True)
                s = [prices[i]-discount]
                discounted.extend(s)
            else:
                discounted.append(prices[i])
        discounted.append(prices[-1])
        return discounted
        
        
    def minimum_index(self,array,match):
        for i in range(0,len(array)):
            try:
                if array[i] <= match:
                    return array[i]
            except:
                return 0 