class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]
        for i in range(0,len(gain)):
            prefix_sum.append(prefix_sum[-1] + gain[i])
        return max(prefix_sum)