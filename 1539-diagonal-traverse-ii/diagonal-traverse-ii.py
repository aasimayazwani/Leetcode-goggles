class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums[i])):
                heapq.heappush(arr,(i+j,-i,nums[i][j]))
        ans = []
        while arr:
            position, second, value = heapq.heappop(arr)
            ans.append(value)
        return ans 