class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        greatest =max(candies)
        temp = []
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=greatest:
                temp.append(True)
            else:
                temp.append(False)
        return temp 