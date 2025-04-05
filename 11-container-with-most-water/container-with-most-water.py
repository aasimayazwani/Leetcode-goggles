class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = -1
        left, right = 0, len(height)-1
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            ans = max(min_height*width,ans)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return ans