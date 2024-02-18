class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # follow operatios until empty
            # find the largest element in rows from each row.                                                      
        length = len(nums)
        for i in range(0,length):
            nums.append(sorted(nums[i],reverse=True))
        del nums[0:length]
        total = 0 
        initial = 0
        while initial < len(nums[0]):
            total += max([item[initial] for item in nums])
            initial +=1 
        return total 