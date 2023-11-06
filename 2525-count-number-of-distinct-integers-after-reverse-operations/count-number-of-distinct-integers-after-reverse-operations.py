class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = []
        for i in range(0,len(nums)):
            arr.append(self.reverse_int(nums[i]))
        print(arr)
        nums = arr + nums
        nums = list(set(nums))
        return len(nums)

    def reverse_int(self,item):
        return int(str(item)[::-1])