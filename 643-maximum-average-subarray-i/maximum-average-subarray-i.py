class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # integer array, n elements
        # contiguous array of length k 
        # the order or the sequence of nums is relevant hence can't use hash table or sets
        # clearly a sliding window problem
        mapping = {}
        for i in range(0,len(nums)):
            mapping[i] = nums[i]

        average = -10000
        length = k -1 
        current = nums[0:length]
        total = sum(current)
        for i in range(length,len(nums)):
            total += mapping[i]
            average = max(average,total/k)
            total = total - mapping[i-k+1]
        return average