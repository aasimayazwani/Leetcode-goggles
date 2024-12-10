class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # remove min element 
        # remove min element 
        heapq.heapify(nums)
        counter = 0
        ans, temp = [], []
        while nums:
            cur1 = heapq.heappop(nums)
            temp.append(cur1)
            if len(temp) == 2:
                ans.extend(temp[::-1])
                temp = []
        return ans 
