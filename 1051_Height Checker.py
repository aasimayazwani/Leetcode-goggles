class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        counter = 0 
        for i in range(0,len(heights)):
            if heights[i]== new_heights[i]:
                pass
            else:
                counter+=1
        return counter