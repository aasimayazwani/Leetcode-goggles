class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = [0]*len(heights)
        stack = []
        for i in range(0,len(heights)):
            counter = 0
            while len(stack) > 0 and heights[i] >= heights[stack[-1]] :
                counter +=1
                result[stack[-1]] = counter
                stack.pop()
            stack.append(i)
        answer = []
        for i in range(0,len(result)):
            if result[i] == 0:
                answer.append(i)
        return answer       
