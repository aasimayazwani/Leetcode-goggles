class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1
        left, right = 0, len(height)-1
        while left < right:
            current_height = min(height[left],height[right])
            width = right - left
            area = max(area,current_height*width)
            if height[left] <= height[right]:
                left +=1 
            else:
                right -=1 
        return area 