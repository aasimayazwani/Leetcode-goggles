class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for iteration in range(0,len(nums)):
            length = 0
            for current in range(0,len(nums)):
                if nums[current] < nums[iteration] and nums != iteration:
                    length +=1
                else:
                    pass 
            output.append(length)
        return output