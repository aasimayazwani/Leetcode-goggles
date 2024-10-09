class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices.copy()
        for i in range(0,len(prices)):
            while len(stack) > 0 and prices[i] <= prices[stack[-1]]:
                result[stack[-1]] = abs(prices[i] - prices[stack[-1]])
                stack.pop()
            stack.append(i)
        return result 
