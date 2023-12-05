class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0 
        else:
            heapq.heapify(nums)
            # Pop elements from the heap to get them in sorted order
            sorted_nums = []
            max_diff = -10000 
            while nums:
                sorted_nums.append(heapq.heappop(nums))
            
            current_element = sorted_nums[0]
            for i in range(1,len(sorted_nums)):
                current_diff = sorted_nums[i] - current_element
                current_element = sorted_nums[i]
                if current_diff > max_diff:
                    max_diff = current_diff 
                else:
                    pass 
            return max_diff 