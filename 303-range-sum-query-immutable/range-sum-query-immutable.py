class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.current = [0]
        for i in range(0,len(nums)):
            self.current.append(self.current[-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        #print(self.current)
        return self.current[right+1] - self.current[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)